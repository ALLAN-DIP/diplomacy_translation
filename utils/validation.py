from daidepp import create_daide_grammar, daide_visitor

daide = 'YES (PRP (ALY (ITA AUS) VSS (TUR)))'
grammar = create_daide_grammar(level=130, string_type='all')
parse_tree = grammar.parse(daide)
output = daide_visitor.visit(parse_tree)
print(output)