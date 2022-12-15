import json
from daidepp import create_daide_grammar, daide_visitor

all = []

def validate(daide):
    try:
        grammar = create_daide_grammar(level=130, string_type='all')
        parse_tree = grammar.parse(daide)
        daide_visitor.visit(parse_tree)
        return True
    except:
        return False

with open('data/annotated_daide.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    for entry in data:
        msg = entry['msg']
        daide = entry['daide']
        
        if not validate(daide):
            print(msg)

    f.close()