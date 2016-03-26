class Lexeme():
    def __init__(self, t = None, v = None):
        self.ltype = t
        self.lvalue = v

    def __str__(self):
        return (str(self.left) + " : " + str(self.right))