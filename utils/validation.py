from translation.translation import toEnglish
import json
from time import sleep

all_generated = []
count = 0
total = 312

with open ('data/annotated_daide.json', 'r') as f:
    data = json.load(f)

    for entry in data:
        msg = entry['msg']
        daide = entry['daide']
        count += 1
        
        generated = toEnglish(daide)
        all_generated.append({'msg': msg, 'daide': daide, 'translation': generated})
        print(f'{count}/{total}')
        sleep(5)
        
    f.close()

with open ('data/daide_to_english.json', 'x') as f:
    json.dump(all_generated, f, indent=4)
    f.close()