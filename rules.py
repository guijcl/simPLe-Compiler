import sys

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV', 'MOD'),
    ('left', 'EQUAL', 'NEQUAL', 'LTE','LT','GT','GTE'),
    ('left', 'AND', 'OR'),
)

def p_definition_sequence(t):
	""" definition_sequence : definition definition_sequence
	| definition """
	t[0] = {'definition_list':t[1]}

def p_definition(t):
	""" definition : function_declaration
	| variable_declaration """
	t[0] = {'definition':t[1]}

def p_variable_declaration(t):
	""" variable_declaration : identifier COLON type SEMICOLON
	| identifier COLON type ASSIGNMENT element SEMICOLON """
	if len(t) == 5:
		t[0] = {'var':[t[1],t[3]]}
	else:
		t[0] = {'var':[t[1],t[3],t[5]]}

def p_function_declaration(t):
	""" function_declaration : function_heading statement """
	t[0] = {'function':[t[1],t[2]]}

def p_function_heading(t):
	""" function_heading : identifier COLON type LPAREN parameter_list RPAREN """
	t[0] = {'function_head':[t[1],t[3],t[5]]}

def p_parameter_list(t):
	""" parameter_list : parameter COMMA parameter_list
	| parameter """
	if len(t) == 4:
		t[0] = {'parameter_list':[t[1],t[3]]}
	else:
		t[0] = t[1]

def p_parameter(t):
	""" parameter : identifier COLON type """
	t[0] = {'parameter':[t[1],t[3]]}
	
def p_statement_part(t):
	""" statement_part : LBRACKET statement_sequence RBRACKET """
	t[0] = t[2]
	
def p_statement_sequence(t):
	""" statement_sequence : statement statement_sequence
	| statement """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'statement_list':[t[1],t[2]]}

def p_statement(t):
	""" statement : statement_part
	 | assignment_statement
	 | if_statement
	 | while_statement
	 | return_statement
	 | """
	if len(t) > 1:
		t[0] = t[1]

def p_assignment_statement(t):
	""" assignment_statement : identifier COLON type ASSIGNMENT element SEMICOLON """
	t[0] = {'assign':[t[1],t[3],t[5]]}

def p_if_statement(t):
	""" if_statement : IF expression statement ELSE statement
	| IF expression statement """
	if len(t) == 6:
		t[0] = {'if':[t[2],t[3], t[5]]}
	else:
		t[0] = {'if':[t[2],t[3]]}

def p_while_statement(t):
	""" while_statement : WHILE expression statement """
	t[0] = {'while':[t[2],t[3]]}

def p_return_statement(t):
	""" return_statement : RETURN element SEMICOLON """
	t[0] = {'return': t[2]}

def p_expression(t):
	""" expression : expression and_or expression_m
	| expression_m """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'op':[t[2],t[1],t[3]]}

def p_expression_m(t):
	""" expression_m : expression_s
	| expression_m sign expression_s """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'op':[t[2],t[1],t[3]]}

def p_expression_s(t):
	""" expression_s : element 
	| expression_s psign element """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'op':[t[2],t[1],t[3]]}

def p_and_or(t):
	""" and_or : AND
	| OR """
	t[0] = {'and_or':t[1]}

def p_psign(t):
	""" psign : TIMES 
	| DIV """
	t[0] = {'sign':t[1]}

def p_sign(t):
	""" sign : PLUS
	| MINUS
	| MOD
	| EQUAL
	| NEQUAL
	| LT
	| LTE
	| GT
	| GTE """
	t[0] = {'sign':t[1]}

def p_element(t):
	""" element : identifier
	| integer
	| string
	| LPAREN expression RPAREN """
	if len(t) == 2:
		t[0] = {'element':t[1]}
	else:
		t[0] = {'element':t[2]}

def p_identifier(t):
    """ identifier : IDENTIFIER """
    try:
        t[0] = {'identifier':[str(t[1]).lower()]}
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_integer(t):
    """ integer : INTEGER """
    t[0] = {'integer':t[1]}

def p_str(t):
	""" string : STRING """
	t[0] = {'string':t[1]}

def p_type(t):
	""" type : TINTEGER
	| TSTRING """
	t[0] = {'type':[t[1]]}

def p_error(t):
    print("Syntax error at " + str(t.value) + " in line " + str(t.lineno))
    sys.exit()