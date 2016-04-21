from parser import Parser
from environment import Environment
from lexeme import Lexeme

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    env = Environment()
    print(evaluate(parse_tree, env))

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
    elif (tree.ltype == "NIL"):
        return evalNIL(tree, env)
    elif (tree.ltype == "TRUE"):
        return evalTRUE(tree, env)
    elif (tree.ltype == "FALSE"):
        return evalFALSE(tree, env)
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
    evaluate(tree.left, env)

def evalVARDEF(tree, env):
    variable = tree.right.left
    value = evaluate(tree.right.right.right.left, env)
    return env.insert(variable, value)

def evalFUNCDEF(tree, env):
    variable = tree.right.left
    params = tree.right.right.right.left
    body = tree.right.right.right.right.right.left
    right = Lexeme("JOIN", "JOIN", body, env)
    close = Lexeme("CLOSURE", "CLOSURE", params, right)
    return env.insert(variable, close)

def evalIDDEF(tree, env):
    pass

def evalOPTPARAMLIST(tree, env):
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalPARAMLIST(tree, env):
    if(tree.right == None):
        return evaluate(tree.left, env)
    else:
        pass

def evalOPTEXPRLIST(tree, env):
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalEXPRLIST(tree, env):
    if(tree.right == None):
        return evaluate(tree.left, env)
    else:
        pass

def evalEXPR(tree, env):
    if(tree.right == None):
        return evaluate(tree.left, env)
    else:
        pass

def evalPRIMARY(tree, env):
    if(tree.right == None):
        return evaluate(tree.left, env)
    else:
        pass

def OPERATOR(tree, env):
    return evaluate(tree.left, env)

def evalBLOCK(tree, env):
    return evaluate(tree.right.left, env)

def evalOPTSTATEMENTLIST(tree, env):
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalSTATEMENTLIST(tree, env):
    if(tree.right == None):
        return evaluate(tree.left, env)
    else:
        pass

def evalSTATEMENT(tree, env):
    if(tree.right == None):
        return evaluate(tree.left, env)
    elif(tree.left.ltype == "EXPR"):
        return evaluate(tree.left, env)
    elif(tree.left.ltype == "RETURN"):
        return evaluate(tree.right.left, env)

def evalWHILELOOP(tree, env):
    pass

def evalIFSTATEMENT(tree, env):
    pass

def evalOPTELSESTATEMENT(tree, env):
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalELSESTATEMENT(tree, env):
    pass

def evalLAMBDA(tree, env):
    variable = Lexeme("ID", " ", None, None)
    params = tree.right.right.left
    body = tree.right.right.right.right.left
    right = Lexeme("JOIN", "JOIN", body, env)
    close = Lexeme("CLOSURE", "CLOSURE", params, right)
    return env.insert(variable, close)

# def evalJOIN(tree, env):
#     pass

def evalSTRING(tree,env):
    return tree

def evalINTEGER(tree,env):
    return tree

# def evalFUNCTION(tree,env):
#     pass

# def evalVAR(tree,env):
#     pass

# def evalWHILE(tree,env):
#     pass

# def evalIF(tree,env):
#     pass

# def evalELSE(tree,env):
#     pass

# def evalRETURN(tree,env):
#     pass

# def evalID(tree,env):
#     pass

# def evalNIL(tree, env):
#     pass

# def evalTRUE(tree, env):
#     pass

# def evalFALSE(tree, env):
#     pass





import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/simple.rwall"
main(filename)
