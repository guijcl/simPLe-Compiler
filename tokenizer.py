tokens = (
	'IDENTIFIER',
	'ASSIGNMENT',
	'SEMICOLON',
	'COLON',
	'COMMA',

	'COMMENT',

	'RETURN',

	'IF',
	'ELSE',
	'WHILE',

	'AND',
	'OR',
	'NOT',

	'EQUAL',
	'NEQUAL',
	'LT',
	'GT',
	'LTE',
	'GTE',

	'PLUS',
	'MINUS',
	'TIMES',
	'DIV',
	'MOD',

	'LBRACKET',
	'RBRACKET',
	'LPAREN',
	'RPAREN',
	'LBRACKET_S',
	'RBRACKET_S',

	'VOID',
	'BOOL',
	'INTEGER',
	'FLOAT',
	'ARRAY',
	'STRING',

	'TVOID',
	'TBOOL',
	'TINTEGER',
	'TFLOAT',
	'TSTRING',
)

t_ASSIGNMENT 	= r"\="
t_SEMICOLON  	= r"\;"
t_COLON      	= r"\:"
t_COMMA			= r"\,"

t_AND 			= r"\&\&"
t_OR 			= r"\|\|"
t_NOT			= r"\!"
t_EQUAL 		= r"\=\="
t_NEQUAL 		= r"\!\="
t_LT			= r"\<"
t_GT			= r"\>"
t_LTE			= r"\<\="
t_GTE			= r"\>\="

t_PLUS			= r"\+"
t_MINUS			= r"\-"
t_TIMES			= r"\*"
t_DIV			= r"/"
t_MOD 			= r"\%"

t_LBRACKET		= r"\{"
t_RBRACKET		= r"\}"
t_LBRACKET_S	= r"\["
t_RBRACKET_S	= r"\]"
t_LPAREN		= r"\("
t_RPAREN		= r"\)"

t_INTEGER		= r"(\-)*[0-9]+"
t_FLOAT			= r"[+-]?([0-9]*[.])[0-9]+"
t_BOOL 			= r"true|false"

reserved_keywords = {	
	'return':	'RETURN',

	'if':		'IF',
	'else':		'ELSE',
	'while':	'WHILE',

	'true':		'BOOL',
	'false':	'BOOL',

	'void':		'TVOID',
	'bool':		'TBOOL',	
	'int':		'TINTEGER',
	'float':	'TFLOAT',
	'string':	'TSTRING',
}

def t_IDENTIFIER(t):
	r"[a-zA-Z]([a-zA-Z0-9])*"
	if t.value.lower() in reserved_keywords:
		t.type = reserved_keywords[t.value.lower()]
	return t

def t_STRING(t): 
    r"(\"([^\\\"]|(\\.))*\")|(\'([^\\\']|(\\.))*\')"
    escaped = 0 
    str = t.value[1:-1] 
    new_str = "" 
    for i in range(0, len(str)): 
        c = str[i] 
        if escaped: 
            if c == "n": 
                c = "\n" 
            elif c == "t": 
                c = "\t" 
            new_str += c 
            escaped = 0 
        else: 
            if c == "\\": 
                escaped = 1 
            else: 
                new_str += c 
    t.value = new_str 
    return t

def t_COMMENT(t):
	r"\(\*[\s\S]*\*\)"

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)