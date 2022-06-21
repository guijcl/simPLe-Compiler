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
		t[0] = {'nt': 'var_declared'} | t[3] | t[1] | {'e': t[5]}

def p_function_declaration(t):
	""" function_declaration : function_heading body 
	| identifier COLON type LPAREN parameter_list RPAREN SEMICOLON """
	if len(t) == 3:
		t[0] = {'nt': 'function_defined'} | t[1] | t[2]
	if len(t) != 3:
		if t[5] == None:
			t[0] = {'nt': 'function_declared'} | t[1] | t[3]
		else:
			t[0] = {'nt': 'function_declared'} | t[1] | t[3] | {'parameters': t[5]}


def p_function_heading(t):
	""" function_heading : identifier COLON type LPAREN parameter_list RPAREN """
	if t[5] == None:
		t[0] = t[1] | t[3]
	else:
		t[0] = t[1] | t[3] | {'parameters': t[5]}

def p_parameter_list(t):
	""" parameter_list : parameter COMMA parameter_list
	| parameter 
	| """
	if len(t) == 2:
		t[0] = [t[1]]
	elif len(t) > 2:
		t[0] = [t[1]] + t[3]

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
	 | local_variable_declaration
	 | assignment_statement
	 | array_def
	 | if_statement
	 | while_statement
	 | return_statement
     | expression SEMICOLON
	 | """
	if len(t) > 1:
		t[0] = t[1]

def p_body(t):
	""" body : statement """
	t[0] = {'body': t[1]}

def p_param_list(t):
	""" param_list : param COMMA param_list
	 | param 
	 | """
	if len(t) == 2:
		t[0] = [t[1]]
	elif len(t) > 2:
		t[0] = [t[1]] + t[3]

def p_param(t):
	""" param : expression """
	t[0] = t[1]

def p_local_variable_declaration(t):
	""" local_variable_declaration : identifier COLON type ASSIGNMENT expression SEMICOLON """
	t[0] = {'nt': 'var_declared'} | t[3] | t[1] | {'e': t[5]}

def p_assignment_statement(t):
	""" assignment_statement : identifier ASSIGNMENT expression SEMICOLON 
	| identifier LBRACKET_S expression RBRACKET_S ASSIGNMENT expression SEMICOLON """
	if len(t) == 5:
		t[0] = {'nt': 'var_assignment'} | t[1] | {'e': t[3]}
	else:
		t[0] = {'nt': 'array_assignment'} | t[1] | {'index': t[3], 'e': t[6]}

def p_array_def(t):
	""" array_def : identifier COLON type SEMICOLON """
	t[0] = {'nt': 'var_defined'} | t[1] | t[3]

def p_if_statement(t):
	""" if_statement : IF expression body ELSE body
	| IF expression body """
	if len(t) == 6:
		t[0] = {'nt': 'if_else', 'cond': t[2], 'if': t[3], 'else': t[5]}
	else:
		t[0] = {'nt': 'if', 'cond': t[2]} | t[3]

def p_while_statement(t):
	""" while_statement : WHILE expression body """
	t[0] = {'nt': 'while', 'cond': t[2]} | t[3]

def p_return_statement(t):
	""" return_statement : RETURN expression SEMICOLON """
	t[0] = {'nt': 'return', 'ret_e': t[2]}

def p_expression(t):
	""" expression : expression_m
	| expression and_or expression_m """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = t[0] = {'nt': 'expr'} | t[2] | {'left': t[1]} | {'right': t[3]}

def p_expression_m(t):
	""" expression_m : expression_e
	| expression_m sign expression_e """
	if len(t) == 2:
		t[0] = t[1]
	else:
		t[0] = {'nt': 'expr'} | t[2] | {'left': t[1]} | {'right': t[3]}

def p_and_or(t):
	""" and_or : AND
	| OR """
	t[0] = {'and_or': t[1]}

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

def p_expression_e(t):
	""" expression_e : identifier
	| integer
	| float
	| string
	| bool
	| array
	| LPAREN expression RPAREN 
	| NOT expression
    | function_call 
	| array_call """
	if len(t) == 3:
		t[0] = {'nt': 'not', 'e': t[2]}
	elif len(t) == 2:
		t[0] = {'nt': 'expr_e', 'e': t[1]}
	else:
		t[0] = {'nt': 'expr_e', 'e': t[2]}

def p_function_call(t):
	""" function_call : identifier LPAREN param_list RPAREN """
	if t[3] == None:
		t[0] = {'nt': 'function_call'} | t[1]
	else:
		t[0] = {'nt': 'function_call'} | t[1] | {'parameters': t[3]}

def p_array_call(t):
	""" array_call : identifier LBRACKET_S expression RBRACKET_S """
	t[0] = {'nt': 'array_call'} | t[1] | {'index': t[3]}

def p_identifier(t):
    """ identifier : IDENTIFIER """
    try:
        t[0] = {'identifier': str(t[1]).lower()}
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
	""" array : LBRACKET_S expression RBRACKET_S """
	t[0] = {'array': t[2]}

def p_type(t):
	""" type : TINTEGER
	| TFLOAT
	| TSTRING 
	| TBOOL 
	| LBRACKET_S type RBRACKET_S """
	if len(t) == 2:
		t[0] = {'type': t[1].lower()}
	else:
		t[0] = {'value_types': t[2]}

def p_error(t):
    print("Syntax error at " + str(t.value) + " in line " + str(t.lineno))
    sys.exit()