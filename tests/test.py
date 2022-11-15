from translation.translation import toDAIDE, toEnglish

# print(toDAIDE("Can your army in Warsaw support my army in Ukraine?"))

# the following code is used to extract all DAIDE from https://github.com/isi-nlp/DiplomacyAMR/blob/main/annotations/dip-all-amr-daide-smosher-20221031.txt

""" 
arr = []

with open("translations.txt", encoding='utf-8') as myfile:
    data = myfile.read().split("\n\n")
    for amr in data:
        lines = amr.split("\n")
        if lines[-1].startswith('DAIDE: '):
            str = ''
            for line in lines:
                if line.startswith('# ::snt'):
                    str += line[8:] + '\n'
                if line.startswith('DAIDE: '):
                    str += line[7:] + '\n'
            arr.append(str)
            

for amr in arr:
    with open('filtered_translations.txt', 'a', encoding='utf-8') as f:
        f.write(amr)
        f.write("\n")
"""

# the following code is using openai api to translate DAIDE to English
'''
from translation.translation import toEnglish
import random, time

responses = []

with open("data/eng_daide.txt") as f:
    lines = f.read().split("\n\n")
    for entry in lines:
        eng, daide = entry.split("\n")
        translation = toEnglish(daide, temperature=random.random())
        time.sleep(4)
        result = f"English: {eng}\nDAIDE: {daide}\nTranslation: {translation}\n"
        responses.append(result)

with open("data/generated_eng.txt", "a") as f:
    f.write("\n".join(responses))
'''