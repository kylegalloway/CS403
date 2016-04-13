from parser import Parser

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    prettyPrint(parse_tree)

def prettyPrint(tree):
    if(tree != None):
        # print(tree.ltype)
        if(tree.ltype == "PARSE"):
            printParse(tree)
        elif(tree.ltype == "FILE"):
            printFile(tree)
        elif(tree.ltype == "INCLUSION"):
            printInclusion(tree)
        elif(tree.ltype == "PROGRAM"):
            printProgram(tree)
        elif(tree.ltype == "DEFINITION"):
            printDefinition(tree)
        elif(tree.ltype == "VARDEF"):
            printVariableDefinition(tree)
        elif(tree.ltype == "FUNCDEF"):
            printFunctionDefinition(tree)
        elif(tree.ltype == "IDDEF"):
            printIDDef(tree)
        elif(tree.ltype == "OPTPARAMLIST"):
            printOptParamList(tree)
        elif(tree.ltype == "PARAMLIST"):
            printParamList(tree)
        elif(tree.ltype == "OPTEXPRLIST"):
            printOptExprList(tree)
        elif(tree.ltype == "EXPRLIST"):
            printExprList(tree)
        elif(tree.ltype == "EXPR"):
            printExpr(tree)
        elif(tree.ltype == "PRIMARY"):
            printPrimary(tree)
        elif(tree.ltype == "OPERATOR"):
            printOperator(tree)
        elif(tree.ltype == "BLOCK"):
            printBlock(tree)
        elif(tree.ltype == "OPTSTATEMENTLIST"):
            printOptStatementList(tree)
        elif(tree.ltype == "STATEMENTLIST"):
            printStatementList(tree)
        elif(tree.ltype == "STATEMENT"):
            printStatement(tree)
        elif(tree.ltype == "WHILELOOP"):
            printWhileLoop(tree)
        elif(tree.ltype == "IFSTATEMENT"):
            printIfStatement(tree)
        elif(tree.ltype == "OPTELSESTATEMENT"):
            printOptElseStatement(tree)
        elif(tree.ltype == "ELSESTATEMENT"):
            printElseStatement(tree)
        elif(tree.ltype == "K_LAMBDA"):
            printK_Lambda(tree)
        elif(tree.ltype == "JOIN"):
            printJoin(tree)
        elif(tree.ltype == "SEMI"):
            printSEMI(tree)
        elif(tree.ltype == "COMMA"):
            printCOMMA(tree)
        elif(tree.ltype == "OPAREN"):
            printOPAREN(tree)
        elif(tree.ltype == "CPAREN"):
            printCPAREN(tree)
        elif(tree.ltype == "OBRACE"):
            printOBRACE(tree)
        elif(tree.ltype == "CBRACE"):
            printCBRACE(tree)
        elif(tree.ltype == "OBRACKET"):
            printOBRACKET(tree)
        elif(tree.ltype == "CBRACKET"):
            printCBRACKET(tree)
        elif(tree.ltype == "PLUS"):
            printPLUS(tree)
        elif(tree.ltype == "MINUS"):
            printMINUS(tree)
        elif(tree.ltype == "TIMES"):
            printTIMES(tree)
        elif(tree.ltype == "DIVIDE"):
            printDIVIDE(tree)
        elif(tree.ltype == "MODULO"):
            printMODULO(tree)
        elif(tree.ltype == "EXPONENT"):
            printEXPONENT(tree)
        elif(tree.ltype == "AMPERSAND"):
            printAMPERSAND(tree)
        elif(tree.ltype == "PERIOD"):
            printPERIOD(tree)
        elif(tree.ltype == "BAR"):
            printBAR(tree)
        elif(tree.ltype == "GREATEREQUAL"):
            printGREATEREQUAL(tree)
        elif(tree.ltype == "GREATER"):
            printGREATER(tree)
        elif(tree.ltype == "LESSEQUAL"):
            printLESSEQUAL(tree)
        elif(tree.ltype == "LESS"):
            printLESS(tree)
        elif(tree.ltype == "DOUBLEEQUAL"):
            printDOUBLEEQUAL(tree)
        elif(tree.ltype == "EQUAL"):
            printEQUAL(tree)
        elif(tree.ltype == "NOTEQUAL"):
            printNOTEQUAL(tree)
        elif(tree.ltype == "NOT"):
            printNOT(tree)
        elif(tree.ltype == "STRING"):
            printSTRING(tree)
        elif(tree.ltype == "INTEGER"):
            printINTEGER(tree)
        elif(tree.ltype == "FUNCTION"):
            printFUNCTION(tree)
        elif(tree.ltype == "VAR"):
            printVAR(tree)
        elif(tree.ltype == "WHILE"):
            printWHILE(tree)
        elif(tree.ltype == "IF"):
            printIF(tree)
        elif(tree.ltype == "ELSE"):
            printELSE(tree)
        elif(tree.ltype == "RETURN"):
            printRETURN(tree)
        elif(tree.ltype == "INCLUDE"):
            printINCLUDE(tree)
        elif(tree.ltype == "ID"):
            printID(tree)
        else:
            print(tree.ltype+" : "+tree.lvalue)

def printParse(tree):
    prettyPrint(tree.left)
    print("\n")

def printFile(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printInclusion(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printProgram(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printDefinition(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printVariableDefinition(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printFunctionDefinition(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printIDDef(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOptParamList(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printParamList(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOptExprList(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printExprList(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printExpr(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printPrimary(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOperator(tree):
    prettyPrint(tree.left)

def printBlock(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printOptStatementList(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printStatementList(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printStatement(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printWhileLoop(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printIfStatement(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printOptElseStatement(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printElseStatement(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printK_Lambda(tree):
    prettyPrint(tree.left)
    prettyPrint(tree.right)

def printJoin(tree):
    prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printSEMI(tree):
    print(tree.lvalue)

def printCOMMA(tree):
    print(tree.lvalue)

def printOPAREN(tree):
    print(tree.lvalue)

def printCPAREN(tree):
    print(tree.lvalue)

def printOBRACE(tree):
    print(tree.lvalue)

def printCBRACE(tree):
    print(tree.lvalue)

def printOBRACKET(tree):
    print(tree.lvalue)

def printCBRACKET(tree):
    print(tree.lvalue)

def printPLUS(tree):
    print(tree.lvalue)

def printMINUS(tree):
    print(tree.lvalue)

def printTIMES(tree):
    print(tree.lvalue)

def printDIVIDE(tree):
    print(tree.lvalue)

def printMODULO(tree):
    print(tree.lvalue)

def printEXPONENT(tree):
    print(tree.lvalue)

def printAMPERSAND(tree):
    print(tree.lvalue)

def printPERIOD(tree):
    print(tree.lvalue)

def printBAR(tree):
    print(tree.lvalue)

def printGREATEREQUAL(tree):
    print(tree.lvalue)

def printGREATER(tree):
    print(tree.lvalue)

def printLESSEQUAL(tree):
    print(tree.lvalue)

def printLESS(tree):
    print(tree.lvalue)

def printDOUBLEEQUAL(tree):
    print(tree.lvalue)

def printEQUAL(tree):
    print(tree.lvalue)

def printNOTEQUAL(tree):
    print(tree.lvalue)

def printNOT(tree):
    print(tree.lvalue)

def printSTRING(tree):
    print(tree.lvalue)

def printINTEGER(tree):
    print(tree.lvalue)

def printFUNCTION(tree):
    print(tree.lvalue)

def printVAR(tree):
    print(tree.lvalue)

def printWHILE(tree):
    print(tree.lvalue)

def printIF(tree):
    print(tree.lvalue)

def printELSE(tree):
    print(tree.lvalue)

def printRETURN(tree):
    print(tree.lvalue)

def printINCLUDE(tree):
    print(tree.lvalue)

def printID(tree):
    print(tree.lvalue)


import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/program.rwall"
main(filename)
