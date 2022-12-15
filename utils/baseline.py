import json

all = []

with open('data/annotated_daide.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    for entry in data:
        msg = entry['msg']
        daide = entry['daide']
        
        if 'PRP' not in daide:
            all.append({'msg': msg, 'daide': daide})

    f.close()

with open('data/annotated_daide_no_prp.json', 'x', encoding='utf-8') as f:
    json.dump(all, f, ensure_ascii=False, indent=4)
    f.close()