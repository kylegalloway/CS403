from parser2 import Parser
from environment import Environment

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    env = Environment()
    print(env)
    # print(evaluate(parse_tree, env))

def evaluate(tree, env):
    # print(tree.ltype)
    if(tree.ltype == "PARSE"):
        return evalPARSE(tree, env)
    elif (tree.ltype == "PROGRAM"):
        return evalPROGRAM(tree, env)
    elif (tree.ltype == "DEFINITION"):
        return evalDEFINITION(tree, env)
    elif (tree.ltype == "VARDEF"):
        return evalVARDEF(tree, env)
    elif (tree.ltype == "FUNCDEF"):
        return evalFUNCDEF(tree, env)
    elif (tree.ltype == "IDDEF"):
        return evalIDDEF(tree, env)
    elif (tree.ltype == "OPTPARAMLIST"):
        return evalOPTPARAMLIST(tree, env)
    elif (tree.ltype == "PARAMLIST"):
        return evalPARAMLIST(tree, env)
    elif (tree.ltype == "OPTEXPRLIST"):
        return evalOPTEXPRLIST(tree, env)
    elif (tree.ltype == "EXPRLIST"):
        return evalEXPRLIST(tree, env)
    elif (tree.ltype == "EXPR"):
        return evalEXPR(tree, env)
    elif (tree.ltype == "PRIMARY"):
        return evalPRIMARY(tree, env)
    elif (tree.ltype == "BLOCK"):
        return evalBLOCK(tree, env)
    elif (tree.ltype == "OPTSTATEMENTLIST"):
        return evalOPTSTATEMENTLIST(tree, env)
    elif (tree.ltype == "STATEMENTLIST"):
        return evalSTATEMENTLIST(tree, env)
    elif (tree.ltype == "STATEMENT"):
        return evalSTATEMENT(tree, env)
    elif (tree.ltype == "WHILELOOP"):
        return evalWHILELOOP(tree, env)
    elif (tree.ltype == "IFSTATEMENT"):
        return evalIFSTATEMENT(tree, env)
    elif (tree.ltype == "OPTELSESTATEMENT"):
        return evalOPTELSESTATEMENT(tree, env)
    elif (tree.ltype == "ELSESTATEMENT"):
        return evalELSESTATEMENT(tree, env)
    elif (tree.ltype == "LAMBDA"):
        return evalLAMBDA(tree, env)
    elif (tree.ltype == "JOIN"):
        return evalJOIN(tree, env)
    elif (tree.ltype == "STRING"):
        return evalSTRING(tree, env)
    elif (tree.ltype == "INTEGER"):
        return evalINTEGER(tree, env)
    elif (tree.ltype == "FUNCTION"):
        return evalFUNCTION(tree, env)
    elif (tree.ltype == "VAR"):
        return evalVAR(tree, env)
    elif (tree.ltype == "WHILE"):
        return evalWHILE(tree, env)
    elif (tree.ltype == "IF"):
        return evalIF(tree, env)
    elif (tree.ltype == "ELSE"):
        return evalELSE(tree, env)
    elif (tree.ltype == "RETURN"):
        return evalRETURN(tree, env)
    elif (tree.ltype == "INCLUDE"):
        return evalINCLUDE(tree, env)
    elif (tree.ltype == "ID"):
        return evalID(tree, env)
    else:
        return "ERROR: "+tree.ltype+" : "+tree.lvalue

def evalPARSE(tree, env):
    return evaluate(tree.left, env)

def evalPROGRAM(tree, env):
    while(tree.right != None):
        evaluate(tree.left, env)
        tree = tree.right.left
    if(tree.right == None):
        evaluate(tree.left, env)

def evalDEFINITION(tree, env):
    if(tree.left != None):
        evaluate(tree.left, env)

def evalVARDEF(tree, env):
    if(tree.right.left.ltype == "ID"):
        variable = tree.right.left.lvalue
        value = evaluate(tree.right.right.right.left, env)
        return env.insert(variable, value, env)

def evalFUNCDEF(tree, env):
    pass

def evalIDDEF(tree, env):
    pass

def evalOPTPARAMLIST(tree, env):
    pass

def evalPARAMLIST(tree, env):
    pass

def evalOPTEXPRLIST(tree, env):
    pass

def evalEXPRLIST(tree, env):
    pass

def evalEXPR(tree, env):
    if(tree.right != None):
        # leftprim = evaluate(tree.left, env)
        # op = evaluate(tree.right.left)
        # rightprim = evaluate(tree.right.right.left, env)
        # return (rightprim op leftprim)
        pass
    else:
        evaluate(tree.left, env)

def evalPRIMARY(tree, env):
    if(tree.right != None):
        pass
    else:
        return evaluate(tree.left, env)

def OPERATOR(tree, env):
    pass

def evalBLOCK(tree, env):
    pass

def evalOPTSTATEMENTLIST(tree, env):
    pass

def evalSTATEMENTLIST(tree, env):
    pass

def evalSTATEMENT(tree, env):
    pass

def evalWHILELOOP(tree, env):
    pass

def evalIFSTATEMENT(tree, env):
    pass

def evalOPTELSESTATEMENT(tree, env):
    pass

def evalELSESTATEMENT(tree, env):
    pass

def evalLAMBDA(tree, env):
    pass

def evalJOIN(tree, env):
    pass

def evalSTRING(tree,env):
    pass

def evalINTEGER(tree,env):
    return tree.lvalue

def evalFUNCTION(tree,env):
    pass

def evalVAR(tree,env):
    pass

def evalWHILE(tree,env):
    pass

def evalIF(tree,env):
    pass

def evalELSE(tree,env):
    pass

def evalRETURN(tree,env):
    pass

def evalINCLUDE(tree,env):
    pass

def evalID(tree,env):
    pass




import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/simple.rwall"
main(filename)
