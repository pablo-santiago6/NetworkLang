#
#   networkyacc.py
#
import ply.yacc as yacc
from networklex import tokens
import Icode


precedence = (
	('left','ID', 'STR'),
	('left','CREATE'),
    ('left','SEND'),
    ('left','CLOSE'),
    ('left','IP')
	)



def p_program(p):
    '''
    program : statement
            | empty
    '''
    # print(p[1])

def p_statement1(p):
	'''statement : CREATE ID IP EXCLAM'''
	global cl
	cl = Icode.server(p[3])
	# p[0] = p[2]


def p_statement2(p):
	'''statement : SEND STR EXCLAM'''
	# print(cl)
	Icode.send(cl, p[2][1:len(p[2])-1])
	# p[0] = p[4]

def p_statement3(p):
    '''statement : CLOSE EXCLAM'''
    Icode.close(cl)
    # p[0] = p[2]

def p_empty(p):
	'''empty :'''
	p[0] = None

def p_error(p):
	print("syntax error ", p)

parser = yacc.yacc()
