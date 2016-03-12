class Lexeme():
    def __init__(self, t = None, v = None):
        self.ltype = t
        self.lvalue = v

    def __str__(self):
        if (self.ltype != None):
            if (self.lvalue != None):
                return ("Type: " + self.ltype + " Value: " + self.lvalue)
            else:
                return ("Type: " + self.ltype + " Value: NONE")
        else:
            if (self.lvalue != None):
                return ("Type: NONE Value: " + self.lvalue)
            else:
                return ("Type: NONE Value: NONE")