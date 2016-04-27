from parser import Parser
from lexeme import Lexeme
from collections import OrderedDict

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    # E = Environment()
    E = create(None)
    # print(evaluate(parse_tree, env))
    evaluate(parse_tree, E)

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
        raise "ERROR: "+tree.ltype+" : "+tree.lvalue

def evalPARSE(tree, env):
    # print("In evalPARSE")
    return evaluate(tree.left, env)

def evalPROGRAM(tree, env):
    # print("In evalPROGRAM")
    while(tree.right != None):
        evaluate(tree.left, env)
        tree = tree.right.left
    if(tree.right == None):
        return evaluate(tree.left, env)

def evalDEFINITION(tree, env):
    # print("In evalDEFINITION")
    return evaluate(tree.left, env)

def evalVARDEF(tree, env):
    # print("In evalVARDEF")
    variable = str(tree.right.left.lvalue)
    value = evaluate(tree.right.right.right.left, env)
    return insert(variable, value, env)

def evalFUNCDEF(tree, env):
    # print("In evalFUNCDEF")
    variable = str(tree.right.left.lvalue)
    params = tree.right.right.right.left.left
    body = tree.right.right.right.right.right.left
    right = Lexeme("JOIN", "JOIN", body, env)
    close = Lexeme("CLOSURE", "CLOSURE", params, right)
    ret = insert(variable, close, env)
    return ret

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
    funcName = getFunction(tree)
    # print(funcName)
    # Eval the function def to get the entire closure
    closure = evaluate(funcName, env)
    # print(type(closure))

    if(closure == None):
        raise "ERROR: Closure was None"
    elif(closure.ltype != "CLOSURE"):
            raise "ERROR: Tried to call "+closure+" as function."

    # This gets the defining environment from the closure
    denv = getEnv(closure)
    # This gets the function body from the closure
    body = getBody(closure)
    # This gets the formal parameters from the closure
    params = getParams(closure)

    # This evaluates the arguments in the calling environment
    eargs = evaluate(args, env)

    # This evaluates the params in the calling environment
    eparams = makeParamList(params)

    eeargs = makeArgList(eargs, env)

    if(len(eeargs) != len(eparams)):
        raise "ERROR: Wrong number of arguments."

    # This builds the new table and attaches it to the denv
    xenv = extend(eparams, eeargs, denv)

    # print("CALLFUNCTION")
    # print("args", end=" : ")
    # print(args)
    # print("funcName", end=" : ")
    # print(funcName)
    # print("closure", end=" : ")
    # print(closure)
    # print("denv", end=" : ")
    # print(denv)
    # print("body", end=" : ")
    # print(body)
    # print("params", end=" : ")
    # print(params.left.left)
    print("eargs", end=" : ")
    print(eargs)
    print(type(eargs))
    print(eargs)
    # print("eparams", end=" : ")
    # print(eparams)
    print("eeargs", end=" : ")
    print(eeargs)
    # print("xenv", end=" : ")
    print(xenv)
    # This evaluates the function in the new extended environment
    return evaluate(body, xenv)

def makeParamList(params):
    # print("makeParamList")
    pArr = []
    while(params):
        if(params.ltype == "PARAMLIST"):
            pArr.append(params.left.lvalue)
            if(params.right):
                params = params.right.right.left
            else:
                params = params.right
    return pArr

def makeArgList(args, env):
    # print("makeArgList")
    argArr = []
    # While args != None
    while(args):
        # If args is of type Lexeme
        if(isinstance(args, Lexeme)):
            # If args tag is JOIN
            if(args.ltype == "JOIN"):
                # If args.left is of type Lexeme
                if(isinstance(args.left, Lexeme)):
                    argArr.append(args.left.lvalue)
                else:
                    argArr.append(args.left)
            if(args.right):
                args = args.right
            else:
                argArr.append(args.lvalue)
                break
        else:
            argArr.append(args)
            break
    return argArr


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
        return evaluate(tree.left, env)
    if(tree.right.right.left != None):
        r = evaluate(tree.right.right.left, env)
        new = Lexeme("JOIN", "JOIN", evaluate(tree.left, env), r)
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
        return evaluate(tree.left, env)
    if(tree.right.right.left != None):
        r = evaluate(tree.right.right.left, env)
        new = Lexeme("JOIN", "JOIN", evaluate(tree.left, env), r)
    return new

def evalEXPR(tree, env):
    # print("In evalEXPR")
    if(tree.right == None):
        return evaluate(tree.left, env)
    else:
        return evaluate(tree.right, env)

def evalPRIMARY(tree, env):
    # print("In evalPRIMARY")
    if(tree.right == None):
        return evaluate(tree.left, env)
    elif(tree.left == "OPAREN"):
        return evaluate(tree.right.left, env)
    elif(tree.left == "OBRACKET"):
        return evaluate(Lexeme("ARRAY", evaluate(tree.right.left, env), None, None), env)

def evalOPERATOR(tree, env):
    # print("In evalOPERATOR")
    l = tree.left
    r = tree.right
    op = tree.lvalue
    # op = tree.lvalue.left
    new = Lexeme(str(op).strip(), str(op).strip(), l, r)
    return evaluate(new, env)

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
    while(tree):
        result = evaluate(tree.left, env)
        if(tree.right):
            tree = tree.right.left
        else:
            break
    return result

def evalSTATEMENT(tree, env):
    # print("In evalSTATEMENT")
    if(tree.right == None):
        return evaluate(tree.left, env)
    elif(tree.left.ltype == "EXPR"):
        return evaluate(tree.left, env)
    elif(tree.left.ltype == "RETURN"):
        return evaluate(tree.right.left, env)
    elif(tree.left.ltype == "PRINT"):
        return evaluate(tree.left, env)
    else:
        raise("ERROR: BAD STATEMENT")

def evalRETURN(tree, env):
    print("In evalRETURN")
    return evaluate(tree)

def evalWHILELOOP(tree, env):
    print("In evalWHILELOOP")
    conditional = tree.right.right.left
    block = tree.right.right.right.right.left
    x = None
    while(evaluate(conditional, env) == True):
        x = evaluate(block, env)
    return x

def evalIFSTATEMENT(tree, env):
    # print("In evalIFSTATEMENT")
    conditional = tree.right.right.left
    block = tree.right.right.right.right.left
    optElse = tree.right.right.right.right.right.left
    # print(evaluate(conditional, env))
    if(evaluate(conditional, env) == True):
        return evaluate(block, env)
    else:
        return evaluate(optElse, env)

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

def evalSTRING(tree,env):
    # print("In evalSTRING")
    return tree

def evalINTEGER(tree,env):
    # print("In evalINTEGER")
    return tree

def evalID(tree,env):
    # print("In evalID")
    # print(tree)
    return lookup(str(tree.lvalue), env)

def evalEQUAL(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    return (l == r)

def evalNOTEQUAL(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    return (l != r)

def evalGREATER(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    return (l > r)

def evalLESS(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l < r)

def evalGREATEREQUAL(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l >= r)

def evalLESSEQUAL(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l <= r)

def evalPLUS(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l + r)

def evalMINUS(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l - r)

def evalMULTIPLY(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l * r)

def evalDIVIDE(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l / r)

def evalPOWER(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l ** r)

def evalAND(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l and r)

def evalOR(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l or r)

def evalDOUBLEEQUAL(tree, env):
    # l = eval(evaluate(tree.left, env).lvalue)
    # r = eval(evaluate(tree.right, env).lvalue)
    l = evaluate(tree.left, env)
    if(not(isinstance(l, int)) and not(isinstance(l, str))):
        l = eval(l.lvalue)
    r = evaluate(tree.right, env)
    if(not(isinstance(r, int)) and not(isinstance(r, str))):
        r = eval(r.lvalue)

    if(isinstance(l, str) and isinstance(r, int)):
        l = int(l)
    elif(isinstance(l, int) and isinstance(r, str)):
        r = int(r)
    return (l == r)

def evalPRINT(tree, env):
    # print("In evalPRINT")
    eargs = evaluate(tree.right.right.left, env);
    print(eargs)

def evalNIL(tree, env):
    return None


#==============================================================================
### Evaluator
#==============================================================================
def create(outerscope):
    t = OrderedDict()
    t['outerscope'] = outerscope
    return t

def lookup(variable, env):
    while (env):
        if (variable in env):
            return env[variable]
        env = env['outerscope']
    print("\n\nUndefined Variable '"+variable+"' found. \n\n")
    return None

def update(variable, value, env):
    while (env):
        if (env[variable] != None):
            env[variable] = value
            return value
        env = env['outerscope']
    print("\n\nUndefined Variable '"+variable+"' found. \n\n")
    return None

def insert(variable, value, env):
    env[variable] = value

def extend(variables,values,env):
    temp = create(env)
    for x in range(len(variables)):
        temp[variables[x]] = values[x]
    return temp

#==============================================================================




import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/simple.rwall"
main(filename)
