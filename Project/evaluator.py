from parser import Parser
from environment import Environment
from lexeme import Lexeme

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    env = Environment()
    print(evaluate(parse_tree, env))
    # evaluate(parse_tree, env)

def evaluate(tree, env):
    # print("In evaluate")
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
    elif (tree.ltype == "ARRAYACCESS"):
        return evalARRAYACCESS(tree, env)
    elif (tree.ltype == "FUNCCALL"):
        return evalFUNCCALL(tree, env)
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
    elif (tree.ltype == "OPERATOR"):
        return evalOPERATOR(tree, env)
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
    elif (tree.ltype == "PRINT"):
        return evalPRINT(tree, env)
    elif (tree.ltype == "CLOSURE"):
        return evalCLOSURE(tree, env)
    elif (tree.ltype == "EQUAL"):
        return evalEQUAL(tree, env)
    elif (tree.ltype == "NOTEQUAL"):
        return evalNOTEQUAL(tree, env)
    elif (tree.ltype == "GREATER"):
        return evalGREATER(tree, env)
    elif (tree.ltype == "LESS"):
        return evalLESS(tree, env)
    elif (tree.ltype == "GREATEREQUAL"):
        return evalGREATEREQUAL(tree, env)
    elif (tree.ltype == "LESSEQUAL"):
        return evalLESSEQUAL(tree, env)
    elif (tree.ltype == "PLUS"):
        return evalPLUS(tree, env)
    elif (tree.ltype == "MINUS"):
        return evalMINUS(tree, env)
    elif (tree.ltype == "MULTIPLY"):
        return evalMULTIPLY(tree, env)
    elif (tree.ltype == "DIVIDE"):
        return evalDIVIDE(tree, env)
    elif (tree.ltype == "POWER"):
        return evalPOWER(tree, env)
    elif (tree.ltype == "AND"):
        return evalAND(tree, env)
    elif (tree.ltype == "OR"):
        return evalOR(tree, env)
    elif (tree.ltype == "ASSIGN"):
        return evalASSIGN(tree, env)
    elif (tree.ltype == "DOUBLEEQUAL"):
        return evalDOUBLEEQUAL(tree, env)
    else:
        return "ERROR: "+tree.ltype+" : "+tree.lvalue

def evalPARSE(tree, env):
    # print("In evalPARSE")
    return evaluate(tree.left, env)

def evalPROGRAM(tree, env):
    # print("In evalPROGRAM")
    while(tree.right != None):
        evaluate(tree.left, env)
        tree = tree.right.left
    if(tree.right == None):
        evaluate(tree.left, env)

def evalDEFINITION(tree, env):
    # print("In evalDEFINITION")
    evaluate(tree.left, env)

def evalVARDEF(tree, env):
    # print("In evalVARDEF")
    variable = tree.right.left
    value = evaluate(tree.right.right.right.left, env)
    return env.insert(variable, value)

def evalFUNCDEF(tree, env):
    # print("In evalFUNCDEF")
    variable = tree.right.left
    params = tree.right.right.right.left
    body = tree.right.right.right.right.right.left
    right = Lexeme("JOIN", "JOIN", body, env)
    close = Lexeme("CLOSURE", "CLOSURE", params, right)
    return env.insert(variable, close)

def evalIDDEF(tree, env):
    # print("In evalIDDEF")
    return evaluate(tree.left, env)

def evalARRAYACCESS(tree, env):
    # print("In evalARRAYACCESS")
    pass

def evalFUNCCALL(tree, env):
    # print("In evalFUNCCALL")
    # Get the args for the function call
    args = getArgs(tree)
    # Get the function def from the ID
    f = getFunction(tree)
    # Eval the function def to get the entire closure
    closure = evaluate(f, env)

    if(closure.ltype != "CLOSURE"):
        return "ERROR: Tried to call "+closure.lvalue+" as function."

    # This gets the defining environment from the closure
    denv = getEnv(closure)
    # This gets the function body from the closure
    body = getBody(closure)
    # This gets the formal parameters from the closure
    params = getParams(closure)

    # This evaluates the arguments in the calling environment
    eargs = evalOPTEXPRLIST(args, env)
    # This builds the new table and attaches it to the denv
    xenv = env.extend(params, eargs, denv)

    # This evaluates the function in the new extended environment
    # ev = es
    return evaluate(body, xenv)

def getArgs(tree):
    return tree.right.right.left

def getFunction(tree):
    return tree.left

def getEnv(tree):
    return tree.right.right

def getBody(tree):
    return tree.right.left

def getParams(tree):
    return tree.left

def evalOPTPARAMLIST(tree, env):
    # print("In evalOPTPARAMLIST")
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalPARAMLIST(tree, env):
    # print("In evalPARAMLIST")
    r = None
    if(tree.right == None):
        return Lexeme("MINPARAMLIST", "MINPARAMLIST", tree.left, None)
    if(tree.right.right.left != None):
        r = evaluate(tree.right.right.left, env)
    new = Lexeme("MINPARAMLIST", "MINPARAMLIST", tree.left, r)
    return new

def evalOPTEXPRLIST(tree, env):
    # print("In evalOPTEXPRLIST")
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalEXPRLIST(tree, env):
    # print("In evalEXPRLIST")
    r = None
    if(tree.right == None):
        return Lexeme("MINEXPRLIST", "MINEXPRLIST", tree.left, None)
    if(tree.right.right.left != None):
        r = evaluate(tree.right.right.left, env)
    new = Lexeme("MINEXPRLIST", "MINEXPRLIST", tree.left, r)
    return new

def evalEXPR(tree, env):
    # print("In evalEXPR")
    if(tree.right == None):
        return evaluate(tree.left, env)
    else:
        return evaluate(tree.right, env)
        # l = evaluate(tree.left, env)
        # op = evaluate(tree.right.left, env)
        # r = evaluate(tree.right.right.left, env)
        # op = tree.right.left

def evalPRIMARY(tree, env):
    # print("In evalPRIMARY")
    if(tree.right == None):
        return evaluate(tree.left, env)
    elif(tree.left == "OPAREN"):
        return evaluate(tree.right.left, env)
    elif(tree.left == "OBRACKET"):
        return evaluate(Lexeme("ARRAY", evaluate(tree.right.left, env), None, None), env)

def evalOPERATOR(tree, env):
    l = eval(tree.right.left.left.lvalue)
    r = eval(tree.right.right.left.left.lvalue)
    op = tree.left.left
    if (op.ltype == "EQUAL"):
        return (l == r)
    elif (op.ltype == "NOTEQUAL"):
        return (l != r)
    elif (op.ltype == "GREATER"):
        return (l > r)
    elif (op.ltype == "LESS"):
        return (l < r)
    elif (op.ltype == "GREATEREQUAL"):
        return (l >= r)
    elif (op.ltype == "LESSEQUAL"):
        return (l <= r)
    elif (op.ltype == "PLUS"):
        return (l + r)
    elif (op.ltype == "MINUS"):
        return (l - r)
    elif (op.ltype == "MULTIPLY"):
        return (l * r)
    elif (op.ltype == "DIVIDE"):
        return (l / r)
    elif (op.ltype == "POWER"):
        return (l ** r)
    elif (op.ltype == "AND"):
        return (l and r)
    elif (op.ltype == "OR"):
        return (l or r)
    elif (op.ltype == "DOUBLEEQUAL"):
        return (l == r)

def evalBLOCK(tree, env):
    # print("In evalBLOCK")
    return evaluate(tree.right.left, env)

def evalOPTSTATEMENTLIST(tree, env):
    # print("In evalOPTSTATEMENTLIST")
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalSTATEMENTLIST(tree, env):
    # print("In evalSTATEMENTLIST")
    r = None
    if(tree.right == None):
        return Lexeme("MINSTATEMENTLIST", "MINSTATEMENTLIST", tree.left, None)
    if(tree.right.right.left != None):
        r = evaluate(tree.right.left, env)
    new = Lexeme("MINSTATEMENTLIST", "MINSTATEMENTLIST", tree.left, r)
    return new

def evalSTATEMENT(tree, env):
    # print("In evalSTATEMENT")
    if(tree.right == None):
        return evaluate(tree.left, env)
    elif(tree.left.ltype == "EXPR"):
        return evaluate(tree.left, env)
    elif(tree.left.ltype == "RETURN"):
        return evaluate(tree.right.left, env)

def evalWHILELOOP(tree, env):
    # print("In evalWHILELOOP")
    conditional = tree.right.right.left
    block = tree.right.right.right.right.left
    while(evaluate(conditional, env) == True):
        evaluate(block, env)

def evalIFSTATEMENT(tree, env):
    # print("In evalIFSTATEMENT")
    conditional = tree.right.right.left
    block = tree.right.right.right.right.left
    optElse = tree.right.right.right.right.right.left
    if(evaluate(conditional, env) == True):
        evaluate(block, env)
    else:
        evaluate(optElse, env)

def evalOPTELSESTATEMENT(tree, env):
    # print("In evalOPTELSESTATEMENT")
    if(tree.left != None):
        return evaluate(tree.left, env)
    return None

def evalELSESTATEMENT(tree, env):
    # print("In evalELSESTATEMENT")
    return evaluate(tree.right.left, env)

def evalLAMBDA(tree, env):
    # print("In evalLAMBDA")
    params = tree.right.right.left
    body = tree.right.right.right.right.left
    right = Lexeme("JOIN", "JOIN", body, env)
    close = Lexeme("CLOSURE", "CLOSURE", params, right)
    return close

# def evalJOIN(tree, env):
# print("In evalJOIN")
#     pass

def evalSTRING(tree,env):
    # print("In evalSTRING")
    return tree

def evalINTEGER(tree,env):
    # print("In evalINTEGER")
    return tree

# def evalFUNCTION(tree,env):
# print("In evalFUNCTION")
#     pass

# def evalVAR(tree,env):
# print("In evalVAR")
#     pass

# def evalWHILE(tree,env):
# print("In evalWHILE")
#     pass

# def evalIF(tree,env):
# print("In evalIF")
#     pass

# def evalELSE(tree,env):
# print("In evalELSE")
#     pass

# def evalRETURN(tree,env):
# print("In evalRETURN")
#     pass

def evalID(tree,env):
    # print("In evalID")
    return env.lookup(tree)

# def evalNIL(tree, env):
# print("In evalNIL")
#     pass

# def evalTRUE(tree, env):
# print("In evalTRUE")
#     pass

# def evalFALSE(tree, env):
# print("In evalFALSE")
#     pass

# def evalCLOSURE(tree, env):
# print("In evalCLOSURE")
#     pass

def evalPRINT(tree, env):
    # print("In evalPRINT")
    eargs = evaluate(tree.right.right.left, env);
    print(eargs)

# def evalEQUAL(tree, env):
#     return tree

# def evalNOTEQUAL(tree, env):
#     return tree

# def evalGREATER(tree, env):
#     return tree

# def evalLESS(tree, env):
#     return tree

# def evalGREATEREQUAL(tree, env):
#     return tree

# def evalLESSEQUAL(tree, env):
#     return tree

# def evalPLUS(tree, env):
#     return tree

# def evalMINUS(tree, env):
#     return tree

# def evalMULTIPLY(tree, env):
#     return tree

# def evalDIVIDE(tree, env):
#     return tree

# def evalPOWER(tree, env):
#     return tree

# def evalAND(tree, env):
#     return tree

# def evalOR(tree, env):
#     return tree

# def evalASSIGN(tree, env):
#     return tree

# def evalDOUBLEEQUAL(tree, env):
#     return tree



import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/simple.rwall"
main(filename)
