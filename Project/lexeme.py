class Lexeme():
    def __init__(self, t = None, v = None):
        self.ltype = t
        self.lvalue = v

    def __str__(self):
        if (self.ltype != None):
            if (self.lvalue != None):
                return (self.ltype + " : " + self.lvalue)
            else:
                return (self.ltype)
        else:
            if (self.lvalue != None):
                return ("INVALID")
            else:
                return ("INVALID")