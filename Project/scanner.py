from lex import Lexer

def main(filename):
    pending = None
    with open(filename) as file:
        scanner(file)

def scanner(file):
    lexer = Lexer(file)
    pending = lexer.lex()
    while (pending.ltype != "END_OF_INPUT"):
        print(pending)
        pending = lexer.lex()

import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/program.rwall"
main(filename)