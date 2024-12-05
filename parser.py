import sys, os

from ply import yacc,lex

from tokenizer import *
from rules import *

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
	yacc.yacc(debug = logger, errorlog = logger )
	
	data = get_input("./tests/" + filename)

	ast = yacc.parse(data, lexer = lex.lex(nowarn = 1))

	#print(ast)
	return ast

if __name__ == '__main__':
	main()