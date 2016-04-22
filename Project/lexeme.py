class Lexeme():
    def __init__(self, t = None, v = None, left = None, right = None):
        self.ltype = t
        self.lvalue = v
        self.left = left
        self.right = right

    # def __eq__(self, other):
    #     return self.lvalue == other.lvalue

    def __str__(self):
        if (self.lvalue == None):
            val = self.ltype
        else:
            val = self.lvalue

        if (self.right != None):
            if (self.left != None):
                ret = val + " => Left: " + str(self.left) + " Right: " + str(self.right)
            else:
                ret = val + " => Left: None Right: " + str(self.right)
        else:
            if (self.left != None):
                ret = val + " => Left: " + str(self.left)
            else:
                ret = val + " => Left: None Right: None"

        return (ret + "\n")
