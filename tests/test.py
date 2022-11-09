from translation.translation import toDAIDE, toEnglish

print(toDAIDE("Can your army in Warsaw support my army in Ukraine?"))

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