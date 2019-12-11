#
#   networklex.py
#
import ply.lex as lex
import re
import os
import codecs

reserved = {
   'create' : 'CREATE', #listen
   'send' : 'SEND',
   'close' : 'CLOSE'
}

tokens = [
    'STR',
    'COMMENT',
    'ID',
    #'TILDE',
    'IP'
]

tokens += reserved.values()

t_ignore = ' \t'

#t_TILDE = '\~'

t_IP = r'\d+\.\d+\.\d+\.\d+'

t_STR = r'\~\s*[a-zA-Z_0-9\!\@\#\$\%\^\&\*\(\)\"\'\.\,]+\s*\~'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:    # Check for reserved words
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_COMMENT(t):
    r';.*'
    pass
    # No return value. Token discarded

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Invalid Token:", t.value[0])
    t.lexer.skip( 1 )

lexer = lex.lex()

"""
def findFile(dir): # Tests the lexer output
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

directory = os.path.curdir + '\\test\\'
file = findFile(directory)
test = directory+file
fp = open(test,'r')
c = fp.read()
print(c+'\n')
print('--------------------')
print('-- lexer results --')
print('--------------------\n')
fp.close()

#lexer.input(c)

while 1:
    tok = lexer.token()
    if not tok : break
    print(tok)
"""
