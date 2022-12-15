import json
from daidepp import create_daide_grammar, daide_visitor

def validate(daide):
    try:
        grammar = create_daide_grammar(level=130, string_type='all')
        parse_tree = grammar.parse(daide)
        daide_visitor.visit(parse_tree)
        return True
    except:
        return False

valid = 0
total = 0

with open('data/eng_to_daide_clean.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    for entry in data:
        msg = entry['msg']
        daide = entry['daide']
        translation = entry['translation']
        
        if validate(translation):
            valid += 1
        total += 1

    f.close()

print(f'Valid: {valid}/{total} ({valid/total*100:.2f}%)')