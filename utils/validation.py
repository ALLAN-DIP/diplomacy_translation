from daidepp import create_daide_grammar, daide_visitor

grammar = create_daide_grammar(level=130, string_type='all')
message = 'PRP (AND (XDO ((RUS AMY LVN) MTO PRU)) (XDO ((RUS AMY SEV) MTO UKR)) (XDO ((RUS FLT (STP NCS)) MTO BAR)) (XDO ((RUS FLT SWE) HLD)) (XDO ((RUS AMY WAR) MTO GAL)))'
parse_tree = grammar.parse(message)
output = daide_visitor.visit(parse_tree)
print(output)