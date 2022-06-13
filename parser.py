import sys, os

from ply import yacc,lex

from tokens import *
from rules import *

'''code = """
		check:bool (b:bool);
		(*
		min:Int (a:Int, b:Int) {
			return a + b;
		}
		*)
		max:Int (a:Int, b:Int) {
			while f(a, b) > arr[b(a)] {
				return 5 + a;
			}
			f();
			c:Int = 5;
			arr[b];
			arr2[5];
			if !a {
				return 2;
			} else {
				return 5;
			}
			return b + 10;
		}
		pi:bool = false;
	   """'''

code = """
		min:Int (a:Int, b:Int);
		teste:Int () {
			return 5;
		}
		max:Int (a:Int, b:Int) {
			if a > teste() {
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
	yacc.yacc(debug = logger, errorlog = logger )
	
	#data = get_input(filename)
	data = code

	ast = yacc.parse(data, lexer = lex.lex(nowarn = 1))

	#print(ast)
	return ast

if __name__ == '__main__':
	main()