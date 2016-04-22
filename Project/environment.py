from lexeme import Lexeme

class Environment():

    def __init__(self):
        self.environment = self.create()

    def cons(self, value, left, right):
        return Lexeme(value, value, left, right)

    def create(self):
        ids = Lexeme("IDS", "IDS", None, None)
        vals = Lexeme("VALS", "VALS", None, None)
        return self.cons("ENV", ids, self.cons("JOIN", vals, None))

    def lookup(self, variable):
        currEnv = self
        while(currEnv != None):
            ids = self.environment.left
            vals = self.environment.right.left
            if(ids.left != None):
                while(ids != None):
                    if(variable.lvalue == ids.left.lvalue):
                        return vals.left
                    ids = ids.right
                    vals = vals.right
            currEnv = currEnv.environment.right.right
        print("Variable ",variable.lvalue," is undefined.");

    def update(self, variable, value):
        currEnv = self
        while(currEnv != None):
            ids = self.environment.left
            vals = self.environment.right.left
            if(ids.left != None):
                while(ids != None):
                    if(variable.lvalue == ids.left.lvalue):
                        vals.left = value
                        return value
                    ids = ids.right
                    vals = vals.right
            currEnv = currEnv.environment.right.right
        print("Variable ",variable.lvalue," is undefined.");


    def insert(self, variable, value):
        if(self.environment.left.left != None):
            self.environment.left.ltype = "JOIN"
            self.environment.left.lvalue = "JOIN"
            self.environment.left = Lexeme("IDS", "IDS", variable, self.environment.left)
            self.environment.right.left.ltype = "JOIN"
            self.environment.right.left.lvalue = "JOIN"
            self.environment.right.left = Lexeme("VALS", "VALS", value, self.environment.right.left)
        else:
            self.environment.left.left = variable
            self.environment.right.left.left = value
        return value

    def extend(self, variables, values, env):
        return self.cons("ENV", variables, self.cons("JOIN", values, env))

    def __str__(self):
        return "ENV"

