import sys
from types import NoneType

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV', 'MOD'),
    ('left', 'EQUAL', 'NEQUAL', 'LTE','LT','GT','GTE'),
    ('left', 'AND', 'OR'),
)

def p_definition_sequence(t):
	""" definition_sequence : definition definition_sequence
	| definition """
	if len(t) == 2:
		t[0] = [t[1]]
	else:
		t[0] = [t[1]] + t[2]

def p_definition(t):
	""" definition : function_declaration
	| variable_declaration """
	t[0] = t[1]

def p_variable_declaration(t):
	""" variable_declaration : identifier COLON type SEMICOLON
	| identifier COLON type ASSIGNMENT expression SEMICOLON """
	if len(t) == 5:
		t[0] = {'nt': 'var_defined'} | t[1] | t[3]
	else:
		t[0] = {'nt': 'var_declared', 'value': t[5]} | t[1] | t[3]

def p_function_declaration(t):
	""" function_declaration : function_heading body 
	| identifier COLON type LPAREN parameter_list RPAREN SEMICOLON """
	if len(t) == 3:
		t[0] = {'nt': 'function_defined'} | t[1] | t[2]
	else:
		t[0] = {'nt': 'function_declared'} | t[1] | t[3] | t[5]

def p_function_heading(t):
	""" function_heading : identifier COLON type LPAREN parameter_list RPAREN """
	t[0] = t[1] | t[3] | t[5]

def p_parameter_list(t):
	""" parameter_list : parameter COMMA parameter_list
	| parameter """
	if len(t) == 4:
		t[0] = {'parameters': [t[1], t[3]]}
	else:
		t[0] = t[1]

def p_parameter(t):
	""" parameter : identifier COLON type """
	t[0] = t[1] | t[3]
	
def p_statement_part(t):
	""" statement_part : LBRACKET statement_sequence RBRACKET """
	t[0] = t[2]
	
def p_statement_sequence(t):
	""" statement_sequence : statement statement_sequence
	| statement """
	if len(t) == 2:
		t[0] = [t[1]]
	else:
		t[0] = [t[1]] + t[2]

def p_statement(t):
	""" statement : statement_part
	 | assignment_statement
	 | if_statement
	 | while_statement
	 | return_statement
	 | function_call
     | expression
	 | """
	if len(t) > 1:
		t[0] = t[1]

def p_body(t):
	""" body : statement """
	t[0] = {'body': t[1]}

def p_function_call(t):
	""" function_call : identifier LPAREN param_list RPAREN SEMICOLON
	| identifier LPAREN RPAREN SEMICOLON """
	if len(t) == 5:
		t[0] = {'nt': 'function_call'} | t[1]
	else:
		t[0] = {'nt': 'function_call'} | t[1] | t[3]

def p_param_list(t):
	""" param_list : param_list COMMA param
	 | param 
	 | """
	if len(t) == 2:
		t[0] = t[1]
	elif len(t) > 2:
		t[0] = {'parameters': [t[1], t[3]]}

def p_param(t):
	""" param : expression """
	t[0] = t[1]

def p_assignment_statement(t):
	""" assignment_statement : identifier COLON type ASSIGNMENT element SEMICOLON """
	t[0] = {'nt': 'assign'} | t[1] | t[3] | t[5]

def p_if_statement(t):
	""" if_statement : IF expression body ELSE body
	| IF expression body """
	if len(t) == 6:
		t[0] = {'nt': 'if'} | t[2] | t[3] | t[5]
	else:
		t[0] = {'nt': 'if'} | t[2] | t[3]

def p_while_statement(t):
	""" while_statement : WHILE expression body """
	t[0] = {'nt': 'while'} | t[2] | t[3]

def p_return_statement(t):
	""" return_statement : RETURN expression SEMICOLON """
	t[0] = {'nt': 'return', 'value': t[2]}

def p_expression(t):
	""" expression : expression_c
	| expression and_or expression_c """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'expression': t[2] | {'left':t[1]} | {'right':t[3]}}

def p_expression_c(t):
	""" expression_c : expression_e
	| expression_c sign expression_e """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'expression': t[2] | {'left': t[1]} | {'right': t[3]}}

def p_and_or(t):
	""" and_or : AND
	| OR """
	t[0] = {'and_or': t[1]}

def p_expression_e(t):
	""" expression_e : identifier
    | array
	| integer
	| float
	| string
	| bool
	| LPAREN expression RPAREN 
	| NOT element 
    | function_call_inline """
	if len(t) == 2:
		t[0] = t[1]
	elif len(t) == 3:
		t[0] = {'not': t[1]}
	else:
		t[0] = t[1]

def p_sign(t):
	""" sign : TIMES
	| DIV
	| PLUS
	| MINUS
	| MOD
	| EQUAL
	| NEQUAL
	| LT
	| LTE
	| GT
	| GTE """
	t[0] = {'sign': t[1]}

'''def p_expression_s(t):
	""" expression_s : expression_e 
	| expression_s psign expression_e """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'op': t[2] | {'left': t[1]} | {'right': t[3]}}'''

'''def p_psign(t):
	""" psign : TIMES 
	| DIV """
	t[0] = {'sign': t[1]}'''

def p_function_call_inline(t):
	""" function_call_inline : identifier LPAREN param_list RPAREN """
	if type(t[3]) != NoneType:
		t[0] = {'nt': 'function_call_inline'} | t[1] | t[3]
	else:
		t[0] = {'nt': 'function_call_inline'} | t[1]

def p_identifier(t):
    """ identifier : IDENTIFIER """
    try:
        t[0] = {'name': str(t[1]).lower()}
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_integer(t):
    """ integer : INTEGER """
    t[0] = {'integer': t[1]}

def p_float(t):
    """ float : FLOAT """
    t[0] = {'float': t[1]}

def p_str(t):
	""" string : STRING """
	t[0] = {'string': t[1]}

def p_bool(t):
	""" bool : BOOL """
	t[0] = {'bool': t[1]}

def p_array(t):
	""" array : identifier LBRACKET_S element RBRACKET_S
    | identifier LBRACKET_S element RBRACKET_S SEMICOLON """
	t[0] = {'array': t[1] | {'index': t[3]}}

def p_type(t):
	""" type : TINTEGER
	| TFLOAT
	| TSTRING 
	| TBOOL 
	| TARRAY """
	t[0] = {'type': t[1].lower()}

def p_error(t):
    print("Syntax error at " + str(t.value) + " in line " + str(t.lineno))
    sys.exit()