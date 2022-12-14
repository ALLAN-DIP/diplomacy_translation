from daidepp import create_daide_grammar, daide_visitor

grammar = create_daide_grammar(level=130, string_type='all')
message = 'YES (PRP (AND (ALY (ENG FRA) VSS (GER)) (DMZ (ENG FRA) (ECH))))'
parse_tree = grammar.parse(message)
output = daide_visitor.visit(parse_tree)
print(output)