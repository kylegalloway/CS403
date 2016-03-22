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

# main("program.txt")
main("no_coms_program.txt")