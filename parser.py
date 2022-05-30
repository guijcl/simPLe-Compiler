import sys, os

from ply import yacc,lex

from tokens import *
from rules import *

code = """
		min:Int (a:Int, b:Int);
		max:Int (a:Int, b:Int) {
			if a > b {
				return a;
			}
			return b;
		}
		pi:Int = 3;
	   """

'''code = """pi:Int = 3;"""'''

def get_input(file=False):
	if file:
		f = open(file,"r")
		data = f.read()
		f.close()
	else:
		data = ""
		while True:
			try:
				data += input() + "\n"
			except:
				break
	return data

def main(filename=False):
	logger = yacc.NullLogger()
	yacc.yacc(debug = logger, errorlog= logger )
	
	#data = get_input(filename)
	data = code

	ast = yacc.parse(data, lexer = lex.lex(nowarn=1))

	print(ast)

if __name__ == '__main__':
	main()