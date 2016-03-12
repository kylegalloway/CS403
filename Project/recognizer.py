from lex import Lexer
from lexeme import Lexeme

global pending

def main(filename):
    pass
#     pending = None
#     with open(filename) as file:
#         parse(file)

def parse(file):
    pass
    # lexer = Lexer(file)
    # pending = lexer.lex()
    # while (pending.ltype != "END_OF_INPUT"):
    #     print(pending)
    #     pending = lexer.lex()
    # program()
    # match("END_OF_INPUT")

# def list():
#     item()
#     if (check(COMMA)):
#         match(COMMA);
#         list();

# def block():
#     match(OBRACE)
#     optStatementList()
#     match(CBRACE)

# def optStatementList():
#     if (statementListPending()):
#         statementList()

# def statementPending():
#     return (exprPending() or variableDefinitionPending() or check(IF) or check(FUNCTION) or check(WHILE) or check(IF))

def check(t):
    return (t == pending.ltype)

def advance():
    old = pending
    pending = lex(file)
    return old

def match(t):
    if (check(t)):
        return advance()
    else:
        print("syntaxError")
    # throw(syntaxError)
    # useful because we can tell type received and expected type
    # make more useful with line number

main("program.txt")