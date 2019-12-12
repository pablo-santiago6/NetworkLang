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
    'IP',
    'EXCLAM'
]

tokens += reserved.values()

t_ignore = ' \t'
t_EXCLAM = r'\!'
#t_TILDE = '\~'

t_IP = r'\d+\.\d+\.\d+\.\d+'

t_STR = r'\~(.+?)\~'


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
