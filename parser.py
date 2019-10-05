#!/usr/bin/python3

from enum import Enum

class Node_Types(Enum):
	TYPE = 1
	OPTION = 2
	FILENAME = 3
	COMMENT = 4		

tokens = ('WORD','NUMBER','NEWLINE')
literals = ['[',']','=',"-",'#']

t_WORD = r'[a-zA-Z_\./][a-zA-Z0-9_\.\-/]*'
t_ignore = " \t"

def t_NUMBER(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Interget value too large %d", t.value)
		t.value = 0
	return t


def t_NEWLINE(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")
	return t


def t_error(t):
	print("Illegal character '%s'" % t.value[0])


import ply.lex as lex
lexer = lex.lex()

#with open("test.gpj") as file:
#	data = file.read()
#	lexer.input(data)


#while True:
#	tok = lexer.token()
#	if not tok:
#		break
#	print(tok)



#def p_expression(p):
#	'expressions : expression NEWLINE'
#	p[0] = (p[1])

#def p_expressions(p):
#	'expressions : expressions expression '#NEWLINE'
#	p[0] = p[1] + p[2]

def p_expressions(p):
	'''expressions : expression NEWLINE'''
	p[0] = [p[1]]

def p_expressions_list(p):
	'''expressions : expressions expression NEWLINE'''
	p[0] = p[1] + [p[2]]

def p_expression(p):
	'''expression : filename
		       | type
		       | option
		       | comment'''
	p[0] = p[1]


#def p_expression_error(p):
#	'expressions : expression error NEWLINE'
#	print("Bad expression -> %s" % p[0])

def p_filename(p):
	'filename : WORD'
	p[0] = [Node_Types.FILENAME, p[1]]

#def p_filename_1(p):
#	'filename : "/" WORD'
#	p[0] = ['FILENAME', p[2]]


def p_filename_2(p):
	'filename : filename WORD'
	p[0] = p[1] = [p[2]]

#def p_path(p):
#	'path : "/"'
#	p[0] = ['PATH', p[1]]

 
#def p_path_word(p):
#        'path : path WORD'
#        p[0] = p[1].append(p[2])


#def p_path_fslash(p):
#	'path : path "/"'
#	p[0] = p[1].append(p[2])


def p_type(p):
	'type : "[" WORD "]"'
	p[0] = [Node_Types.TYPE, p[2]]


def p_option(p):
	'''option : '-' WORD'''
	p[0] = [Node_Types.OPTION, p[2]]


def p_option_dash(p):
	'option : "-" "-" WORD'
	p[0] = [Node_Types.OPTION, p[3]]


def p_option_word(p):
	'option : option WORD'
	p[0] = p[1] + [p[2]]


def p_option_equals(p):
	'option : option "="'
	p[0] = p[1]


def p_option_number(p):
	'option : option NUMBER'
	p[0] = p[1] + [p[2]]


def p_comment(p):
	'comment : "#"'
	p[0] = [Node_Types.COMMENT, '']


def p_comment_word(p):
	'comment : comment WORD'
	p[0] = p[1] + [p[2]]


def p_error(p):
	print("Illegal parse '%s'" % p)


import ply.yacc as yacc
parser = yacc.yacc()

if __name__ == '__main__':
	with open("test.gpj") as file:
		data = file.read()
	print(parser.parse(data, debug=False))

