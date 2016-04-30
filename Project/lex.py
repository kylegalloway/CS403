from lexeme import Lexeme

class Lexer():

    def __init__(self, file):
        self.lineNumber = 1
        self.file = file
        self.pending = None

    def lex(self):
        self.skipWhiteSpace()
        ch = self.getCharacter()

        if (ch == ""): return Lexeme("END_OF_INPUT")
        if (ch == ';'): return Lexeme("SEMI", ";")
        if (ch == ','): return Lexeme("COMMA", ",")
        if (ch == '('): return Lexeme("OPAREN", "(")
        if (ch == ')'): return Lexeme("CPAREN", ")")
        if (ch == '{'): return Lexeme("OBRACE", "{")
        if (ch == '}'): return Lexeme("CBRACE", "}")
        if (ch == '['): return Lexeme("OBRACKET", "[")
        if (ch == ']'): return Lexeme("CBRACKET", "]")
        if (ch == '+'): return Lexeme("PLUS", "+")
        if (ch == '*'): return Lexeme("MULTIPLY", "*")
        if (ch == '/'): return Lexeme("DIVIDE", "/")
        if (ch == '%'): return Lexeme("MODULO", "%")
        if (ch == '^'): return Lexeme("POWER", "^")
        if (ch == '&'): return Lexeme("AND", "&")
        if (ch == '.'): return Lexeme("PERIOD", ".")
        if (ch == '|'): return Lexeme("OR", "|")

        if (ch == '-'): return self.lexMinus(ch)
        if (ch in ['<', '>', '=', '!']): return self.lexOp(ch)
        if (ch == '\"'): return self.lexString()
        if (ch == '\''): return self.lexString()
        if (ch.isdigit()): return self.lexNumber(ch)
        if (ch.isalpha()): return self.lexWord(ch)

        self.fatal("Bad Character", ch)

    def lexOp(self, ch):
        buff = "" + ch
        ch = self.getCharacter()
        if (buff == ">"):
            if (ch == "="):
                return Lexeme("GREATEREQUAL", ">=")
            else:
                self.pushbackCharacter()
                return Lexeme("GREATER", ">")
        elif (buff == "<"):
            if (ch == "="):
                return Lexeme("LESSEQUAL", "<=")
            else:
                self.pushbackCharacter()
                return Lexeme("LESS", "<")
        elif (buff == "="):
            if (ch == "="):
                return Lexeme("DOUBLEEQUAL", "==")
            else:
                self.pushbackCharacter()
                return Lexeme("EQUAL", "=")
        elif (buff == "!"):
            if (ch == "="):
                return Lexeme("NOTEQUAL", "!=")
            else:
                self.pushbackCharacter()
                return Lexeme("NOT", "!")

    def lexMinus(self, ch):
        buff = "" + ch
        ch = self.getCharacter()
        if (not(ch.isdigit())):
            self.pushbackCharacter()
            return Lexeme("MINUS", "-")
        else:
            while (ch.isdigit()):
                buff += ch
                ch = self.getCharacter()
            self.pushbackCharacter()
            return Lexeme("INTEGER", buff)


    def skipComment(self):
        ch = self.getCharacter()
        if (ch == '#'):
            self.skipLine()
        elif (ch == '{'):
            while (ch != '#'):
                if (ch == '\n'):
                    self.lineNumber += 1
                ch = self.getCharacter()
            ch = self.getCharacter()
            if (ch != '}'):
                self.fatal("Badly formed comment.", " Line: " + str(self.lineNumber))
        elif (ch == '$'):
            self.skipFile()
        else:
            self.fatal("Badly formed comment.", " Line: " + str(self.lineNumber))

    def lexString(self):
        buff = ""
        ch = self.getCharacter()
        while (ch != '\"'):
            if (ch == '\\'): ch = self.getCharacter()
            buff += ch
            ch = self.getCharacter()

        return Lexeme("STRING", "\"" + buff + "\"")

    def lexNumber(self, ch):
        buff = "" + ch
        ch = self.getCharacter()
        while (ch.isdigit()):
            buff += ch
            ch = self.getCharacter()
        self.pushbackCharacter()

        return Lexeme("INTEGER", buff)

    def lexWord(self, ch):
        buff = "" + ch
        ch = self.getCharacter()
        while (ch.isalnum() or ch == "_" or ch == "?"):
            buff += ch
            ch = self.getCharacter()
        self.pushbackCharacter()

        if (buff == "func"): return Lexeme("FUNCTION", "func")
        if (buff == "var"): return Lexeme("VAR", "var")
        if (buff == "while"): return Lexeme("WHILE", "while")
        if (buff == "if"): return Lexeme("IF", "if")
        if (buff == "else"): return Lexeme("ELSE", "else")
        if (buff == "return"): return Lexeme("RETURN", "return")
        if (buff == "lambda"): return Lexeme("LAMBDA", "lambda")
        if (buff == "nil"): return Lexeme("NIL", "nil")
        if (buff == "true"): return Lexeme("BOOLEAN", True)
        if (buff == "false"): return Lexeme("BOOLEAN", False)
        if (buff == "print"): return Lexeme("PRINT", "print")
        if (buff == "append"): return Lexeme("APPEND", "append")
        if (buff == "insert"): return Lexeme("INSERT", "insert")
        if (buff == "remove"): return Lexeme("REMOVE", "remove")
        if (buff == "set"): return Lexeme("SET", "set")
        if (buff == "length"): return Lexeme("LENGTH", "length")

        return Lexeme("ID", buff)


    def getCharacter(self):
        return self.file.read(1)

    def pushbackCharacter(self):
        self.file.seek(self.file.tell() - 1, 0)

    def skipWhiteSpace(self):
        ch = self.getCharacter()
        while (ch.isspace() or ch == "#"):
            if (ch == '\n'):
                self.lineNumber += 1
            if (ch == "#"):
                self.skipComment()
            ch = self.getCharacter()
        if (ch != ""):
            self.pushbackCharacter()

    def skipLine(self):
        ch = self.getCharacter()
        while((ch != '\n')):
            ch = self.getCharacter()
        self.lineNumber += 1

    def skipFile(self):
        self.file.seek(0, 2)

    def fatal(self, *args):
        for x in args:
            print(x)
        exit(1)
