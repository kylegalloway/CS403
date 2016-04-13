from parser import Parser
from environment import Environment

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    env = Environment()
    evaluate(parse_tree, env)

def evaluate(tree, env):
    if(tree != None):
        # print(tree.ltype)
        if(tree.ltype == "PARSE"):
            evalParse(tree,env)
        elif(tree.ltype == "FILE"):
            evalFile(tree,env)
        elif(tree.ltype == "INCLUSION"):
            evalInclusion(tree,env)
        elif(tree.ltype == "PROGRAM"):
            evalProgram(tree,env)
        elif(tree.ltype == "DEFINITION"):
            evalDefinition(tree,env)
        elif(tree.ltype == "VARDEF"):
            evalVariableDefinition(tree,env)
        elif(tree.ltype == "FUNCDEF"):
            evalFunctionDefinition(tree,env)
        elif(tree.ltype == "IDDEF"):
            evalIDDef(tree,env)
        elif(tree.ltype == "OPTPARAMLIST"):
            evalOptParamList(tree,env)
        elif(tree.ltype == "PARAMLIST"):
            evalParamList(tree,env)
        elif(tree.ltype == "OPTEXPRLIST"):
            evalOptExprList(tree,env)
        elif(tree.ltype == "EXPRLIST"):
            evalExprList(tree,env)
        elif(tree.ltype == "EXPR"):
            evalExpr(tree,env)
        elif(tree.ltype == "PRIMARY"):
            evalPrimary(tree,env)
        elif(tree.ltype == "OPERATOR"):
            evalOperator(tree,env)
        elif(tree.ltype == "BLOCK"):
            evalBlock(tree,env)
        elif(tree.ltype == "OPTSTATEMENTLIST"):
            evalOptStatementList(tree,env)
        elif(tree.ltype == "STATEMENTLIST"):
            evalStatementList(tree,env)
        elif(tree.ltype == "STATEMENT"):
            evalStatement(tree,env)
        elif(tree.ltype == "WHILELOOP"):
            evalWhileLoop(tree,env)
        elif(tree.ltype == "IFSTATEMENT"):
            evalIfStatement(tree,env)
        elif(tree.ltype == "OPTELSESTATEMENT"):
            evalOptElseStatement(tree,env)
        elif(tree.ltype == "ELSESTATEMENT"):
            evalElseStatement(tree,env)
        elif(tree.ltype == "K_LAMBDA"):
            evalK_Lambda(tree,env)
        elif(tree.ltype == "JOIN"):
            evalJoin(tree,env)
        elif(tree.ltype == "SEMI"):
            evalSEMI(tree,env)
        elif(tree.ltype == "COMMA"):
            evalCOMMA(tree,env)
        elif(tree.ltype == "OPAREN"):
            evalOPAREN(tree,env)
        elif(tree.ltype == "CPAREN"):
            evalCPAREN(tree,env)
        elif(tree.ltype == "OBRACE"):
            evalOBRACE(tree,env)
        elif(tree.ltype == "CBRACE"):
            evalCBRACE(tree,env)
        elif(tree.ltype == "OBRACKET"):
            evalOBRACKET(tree,env)
        elif(tree.ltype == "CBRACKET"):
            evalCBRACKET(tree,env)
        elif(tree.ltype == "PLUS"):
            evalPLUS(tree,env)
        elif(tree.ltype == "MINUS"):
            evalMINUS(tree,env)
        elif(tree.ltype == "TIMES"):
            evalTIMES(tree,env)
        elif(tree.ltype == "DIVIDE"):
            evalDIVIDE(tree,env)
        elif(tree.ltype == "MODULO"):
            evalMODULO(tree,env)
        elif(tree.ltype == "EXPONENT"):
            evalEXPONENT(tree,env)
        elif(tree.ltype == "AMPERSAND"):
            evalAMPERSAND(tree,env)
        elif(tree.ltype == "PERIOD"):
            evalPERIOD(tree,env)
        elif(tree.ltype == "BAR"):
            evalBAR(tree,env)
        elif(tree.ltype == "GREATEREQUAL"):
            evalGREATEREQUAL(tree,env)
        elif(tree.ltype == "GREATER"):
            evalGREATER(tree,env)
        elif(tree.ltype == "LESSEQUAL"):
            evalLESSEQUAL(tree,env)
        elif(tree.ltype == "LESS"):
            evalLESS(tree,env)
        elif(tree.ltype == "DOUBLEEQUAL"):
            evalDOUBLEEQUAL(tree,env)
        elif(tree.ltype == "EQUAL"):
            evalEQUAL(tree,env)
        elif(tree.ltype == "NOTEQUAL"):
            evalNOTEQUAL(tree,env)
        elif(tree.ltype == "NOT"):
            evalNOT(tree,env)
        elif(tree.ltype == "STRING"):
            evalSTRING(tree,env)
        elif(tree.ltype == "INTEGER"):
            evalINTEGER(tree,env)
        elif(tree.ltype == "FUNCTION"):
            evalFUNCTION(tree,env)
        elif(tree.ltype == "VAR"):
            evalVAR(tree,env)
        elif(tree.ltype == "WHILE"):
            evalWHILE(tree,env)
        elif(tree.ltype == "IF"):
            evalIF(tree,env)
        elif(tree.ltype == "ELSE"):
            evalELSE(tree,env)
        elif(tree.ltype == "RETURN"):
            evalRETURN(tree,env)
        elif(tree.ltype == "INCLUDE"):
            evalINCLUDE(tree,env)
        elif(tree.ltype == "ID"):
            evalID(tree,env)
        else:
            print("ERROR: "+tree.ltype+" : "+tree.lvalue)

def evalParse(tree,env):
    evaluate(tree.left, env)
    print("\n")

def evalFile(tree,env):
    if(tree.left):
        evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalInclusion(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalProgram(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalDefinition(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalVariableDefinition(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalFunctionDefinition(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalIDDef(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalOptParamList(tree,env):
    if(tree.left):
        evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalParamList(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalOptExprList(tree,env):
    if(tree.left):
        evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalExprList(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalExpr(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalPrimary(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalOperator(tree,env):
    evaluate(tree.left, env)

def evalBlock(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalOptStatementList(tree,env):
    if(tree.left):
        evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalStatementList(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalStatement(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalWhileLoop(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalIfStatement(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalOptElseStatement(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalElseStatement(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalK_Lambda(tree,env):
    evaluate(tree.left, env)
    evaluate(tree.right, env)

def evalJoin(tree,env):
    evaluate(tree.left, env)
    if(tree.right):
        evaluate(tree.right, env)

def evalSEMI(tree,env):
    print(tree.lvalue)

def evalCOMMA(tree,env):
    print(tree.lvalue)

def evalOPAREN(tree,env):
    print(tree.lvalue)

def evalCPAREN(tree,env):
    print(tree.lvalue)

def evalOBRACE(tree,env):
    print(tree.lvalue)

def evalCBRACE(tree,env):
    print(tree.lvalue)

def evalOBRACKET(tree,env):
    print(tree.lvalue)

def evalCBRACKET(tree,env):
    print(tree.lvalue)

def evalPLUS(tree,env):
    print(tree.lvalue)

def evalMINUS(tree,env):
    print(tree.lvalue)

def evalTIMES(tree,env):
    print(tree.lvalue)

def evalDIVIDE(tree,env):
    print(tree.lvalue)

def evalMODULO(tree,env):
    print(tree.lvalue)

def evalEXPONENT(tree,env):
    print(tree.lvalue)

def evalAMPERSAND(tree,env):
    print(tree.lvalue)

def evalPERIOD(tree,env):
    print(tree.lvalue)

def evalBAR(tree,env):
    print(tree.lvalue)

def evalGREATEREQUAL(tree,env):
    print(tree.lvalue)

def evalGREATER(tree,env):
    print(tree.lvalue)

def evalLESSEQUAL(tree,env):
    print(tree.lvalue)

def evalLESS(tree,env):
    print(tree.lvalue)

def evalDOUBLEEQUAL(tree,env):
    print(tree.lvalue)

def evalEQUAL(tree,env):
    print(tree.lvalue)

def evalNOTEQUAL(tree,env):
    print(tree.lvalue)

def evalNOT(tree,env):
    print(tree.lvalue)

def evalSTRING(tree,env):
    print(tree.lvalue)

def evalINTEGER(tree,env):
    print(tree.lvalue)

def evalFUNCTION(tree,env):
    print(tree.lvalue)

def evalVAR(tree,env):
    print(tree.lvalue)

def evalWHILE(tree,env):
    print(tree.lvalue)

def evalIF(tree,env):
    print(tree.lvalue)

def evalELSE(tree,env):
    print(tree.lvalue)

def evalRETURN(tree,env):
    print(tree.lvalue)

def evalINCLUDE(tree,env):
    print(tree.lvalue)

def evalID(tree,env):
    print(tree.lvalue)


import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/program.rwall"
main(filename)
