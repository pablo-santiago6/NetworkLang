import ply.yacc as yacc
from networklex import tokens
import os
import re
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
    '''
    run(p[1])

def p_statement1(p):
	'''statement : CREATE ID IP statement'''
	# global cl
	# cl = Icode.server(p[3])
	p[0] = (p[1], p[3])


def p_statement2(p):
	'''statement : SEND STR statement'''
	# print(cl)
	# Icode.send(cl, p[2])
	p[0] = (p[1],p[2])

def p_statement3(p):
    '''statement : CLOSE statement'''
    # Icode.close(cl)
    p[0] = p[1]

def p_emptState(p):
    '''statement : empty'''
    p[0] = None

def p_empty(p):
	'''empty :'''
	p[0] = None

def p_error(p):
	print("syntax error ", p)

parser = yacc.yacc()

def run(p):
    if type(p) == tuple:
        if p[0] == "CREATE":
            global cl
            cl = Icode.server(p[1])
        elif p[0] == "SEND":
            try:
                Icode.send(cl, p[1][1:len(p[1])])
            except:
                pass
    if p == "CLOSE":
        try:
            Icode.close(cl)
        except:
            pass

def findFileY(dir):
    listfil = []
    filnum = ''
    ans = False
    count = 1
    for base, dirs, files in os.walk(dir):
        listfil.append(files)
    for file in files:
        print(str(count) + '. ' +file)
        count = count+1
    while not ans:
        filnum = input('\nNumber of test: ')
        for file in files:
            if file == files[int(filnum)-1]:
                ans = True
                break
    print('chose', files[int(filnum)-1])
    print('printing contents of file\n')
    return files[int(filnum)-1]
if __name__ == '__main__':
    directory = os.path.curdir + '\\test\\'
    file = findFileY(directory)
    test = directory+file
    fp = open(test,'r')
    c = fp.read()
    print(c+'\n')
    print('--------------------')
    print('-- syntax results --')
    print('--------------------\n')
    fp.close()
# global parser
    result = parser.parse(c)
    print(result)

"""
while(True):
    try:
        s = input('')
        if s == "quit":
            break
    except EOFError:
        break
    parser.parse(s)
"""
