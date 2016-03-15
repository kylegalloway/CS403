from lexeme import Lexeme

class Lexer():

    def __init__(self, file):
        self.lineNumber = 1
        self.file = file
        self.pending = None

    def lex(self):
        self.skipWhiteSpace()
        ch = self.getCharacter()

        if (self.endOfFile(ch)): return Lexeme("END_OF_INPUT")
        if (ch == ';'): return Lexeme("SEMI")
        if (ch == ','): return Lexeme("COMMA")
        if (ch == '('): return Lexeme("OPAREN")
        if (ch == ')'): return Lexeme("CPAREN")
        if (ch == '{'): return Lexeme("OBRACE")
        if (ch == '}'): return Lexeme("CBRACE")
        if (ch == '['): return Lexeme("OBRACKET")
        if (ch == ']'): return Lexeme("CBRACKET")
        if (ch == '='): return Lexeme("EQUALS")
        if (ch == '+'): return Lexeme("PLUS")
        if (ch == '-'): return Lexeme("MINUS")
        if (ch == '*'): return Lexeme("TIMES")
        if (ch == '/'): return Lexeme("DIVIDE")
        if (ch == '!'): return Lexeme("NOT")
        if (ch == '%'): return Lexeme("MODULO")
        if (ch == '^'): return Lexeme("EXPONENT")
        if (ch == '&'): return Lexeme("AMPERSAND")
        if (ch == '.'): return Lexeme("PERIOD")
        if (ch == '|'): return Lexeme("BAR")

        if (ch == '<' or ch == '>'): return self.lexOp(ch)
        if (ch == '#'): return self.lexComment()
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
                return Lexeme("GREATEREQUAL")
            else:
                self.pushbackCharacter()
                return Lexeme("GREATER")
        elif (buff == "<"):
            if (ch == "="):
                return Lexeme("LESSEQUAL")
            else:
                self.pushbackCharacter()
                return Lexeme("LESS")


    def lexComment(self):
        ch = self.getCharacter()
        if (ch == '#'):
            self.lineNumber += 1
            self.skipLine()
            return Lexeme("COMMENT")
        elif (ch == '{'):
            while (ch != '#'):
                if (ch == '\n'):
                    self.lineNumber += 1
                ch = self.getCharacter()
            ch = self.getCharacter()
            if (ch == '}'):
                return Lexeme("COMMENT")
            else:
                self.fatal("Badly formed comment.", " Line: " + self.lineNumber)
        elif (ch == '$'):
            self.skipFile()
            return Lexeme("END_OF_INPUT")
        else:
            self.fatal("Badly formed comment.", " Line: " + self.lineNumber)

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
        while (ch.isalnum() or ch == "_"):
            buff += ch
            ch = self.getCharacter()
        self.pushbackCharacter()

        if (buff == "func"): return Lexeme("FUNCTION")
        if (buff == "while"): return Lexeme("WHILE")
        if (buff == "if"): return Lexeme("IF")
        if (buff == "else"): return Lexeme("ELSE")
        if (buff == "return"): return Lexeme("RETURN")
        if (buff == "include"): return Lexeme("INCLUDE")

        return Lexeme("ID", buff)


    def getCharacter(self):
        return self.file.read(1)

    def pushbackCharacter(self):
        self.file.seek(self.file.tell() - 1, 0)

    def skipWhiteSpace(self):
        ch = self.getCharacter()
        while (ch.isspace()):
            if (ch == '\n'):
                self.lineNumber += 1
            ch = self.getCharacter()
        self.pushbackCharacter()

    def endOfFile(self, ch):
        return ch == None

    def skipLine(self):
        ch = self.getCharacter()
        while(ch != '\n'):
            ch = self.getCharacter()
        self.lineNumber += 1

    def skipFile(self):
        self.file.seek(0, 2)

    def fatal(self, *args):
        for x in args:
            print(x)
        exit(1)