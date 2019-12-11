import ply.yacc as yacc
from networklex import tokens
import os
import re
import Icode
import networkyacc

while(True):
    try:
        s = input('')
        if s == "quit":
            break
    except EOFError:
        break
    networkyacc.parser.parse(s)
