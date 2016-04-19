from parser import Parser

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    prettyPrint(parse_tree)

def prettyPrint(tree):
    if(tree != None):
        # pritf(tree.ltype + " ", end="")
        if(tree.ltype == "PARSE"):
            printPARSE(tree)
        elif(tree.ltype == "PROGRAM"):
            printPROGRAM(tree)
        elif(tree.ltype == "LASTDEF"):
            printLASTDEF(tree)
        elif(tree.ltype == "VARDEFINITION"):
            printVARDEFINITION(tree)
        elif(tree.ltype == "FUNCDEFINITION"):
            printFUNCDEFINITION(tree)
        elif(tree.ltype == "DEFINITION"):
            printDEFINITION(tree)
        elif(tree.ltype == "VARDEF"):
            printVARDEF(tree)
        elif(tree.ltype == "FUNCDEF"):
            printFUNCDEF(tree)
        elif(tree.ltype == "IDDEF"):
            printIDDEF(tree)
        elif(tree.ltype == "ARRAYACCESS"):
            printARRAYACCESS(tree)
        elif(tree.ltype == "LONEID"):
            printLONEID(tree)
        elif(tree.ltype == "OPTPARAMLIST"):
            printOPTPARAMLIST(tree)
        elif(tree.ltype == "EMPTYOPTPARAMLIST"):
            printEMPTYOPTPARAMLIST(tree)
        elif(tree.ltype == "PARAMLIST"):
            printPARAMLIST(tree)
        elif(tree.ltype == "LASTPARAM"):

            printLASTPARAM(tree)
        elif(tree.ltype == "OPTEXPRLIST"):
            printOPTEXPRLIST(tree)
        elif(tree.ltype == "EMPTYOPTEXPRLIST"):
            printEMPTYOPTEXPRLIST(tree)
        elif(tree.ltype == "EXPRLIST"):
            printEXPRLIST(tree)
        elif(tree.ltype == "LASTEXPR"):
            printLASTEXPR(tree)
        elif(tree.ltype == "EXPR"):
            printEXPR(tree)
        elif(tree.ltype == "SINGLEPRIMARY"):
            printSINGLEPRIMARY(tree)
        elif(tree.ltype == "IDPRIMARY"):
            printIDPRIMARY(tree)
        elif(tree.ltype == "STRINGPRIMARY"):
            printSTRINGPRIMARY(tree)
        elif(tree.ltype == "INTEGERPRIMARY"):
            printINTEGERPRIMARY(tree)
        elif(tree.ltype == "NOTPRIMARY"):
            printNOTPRIMARY(tree)
        elif(tree.ltype == "EXPRPRIMARY"):
            printEXPRPRIMARY(tree)
        elif(tree.ltype == "LAMBDAPRIMARY"):
            printLAMBDAPRIMARY(tree)
        elif(tree.ltype == "FUNCDEFPRIMARY"):
            printFUNCDEFPRIMARY(tree)
        elif(tree.ltype == "EXPRLISTPRIMARY"):
            printEXPRLISTPRIMARY(tree)
        elif(tree.ltype == "EQUALOPERATOR"):
            printEQUALOPERATOR(tree)
        elif(tree.ltype == "NOTEQUALOPERATOR"):
            printNOTEQUALOPERATOR(tree)
        elif(tree.ltype == "GREATEROPERATOR"):
            printGREATEROPERATOR(tree)
        elif(tree.ltype == "LESSOPERATOR"):
            printLESSOPERATOR(tree)
        elif(tree.ltype == "GREATEREQUALOPERATOR"):
            printGREATEREQUALOPERATOR(tree)
        elif(tree.ltype == "LESSEQUALOPERATOR"):
            printLESSEQUALOPERATOR(tree)
        elif(tree.ltype == "PLUSOPERATOR"):
            printPLUSOPERATOR(tree)
        elif(tree.ltype == "MINUSOPERATOR"):
            printMINUSOPERATOR(tree)
        elif(tree.ltype == "MULTIPLYOPERATOR"):
            printMULTIPLYOPERATOR(tree)
        elif(tree.ltype == "DIVIDEOPERATOR"):
            printDIVIDEOPERATOR(tree)
        elif(tree.ltype == "POWEROPERATOR"):
            printPOWEROPERATOR(tree)
        elif(tree.ltype == "ANDOPERATOR"):
            printANDOPERATOR(tree)
        elif(tree.ltype == "OROPERATOR"):
            printOROPERATOR(tree)
        elif(tree.ltype == "ASSIGNOPERATOR"):
            printASSIGNOPERATOR(tree)
        elif(tree.ltype == "BLOCK"):
            printBLOCK(tree)
        elif(tree.ltype == "OPTSTATEMENTLIST"):
            printOPTSTATEMENTLIST(tree)
        elif(tree.ltype == "EMPTYOPTSTATEMENTLIST"):
            printEMPTYOPTSTATEMENTLIST(tree)
        elif(tree.ltype == "STATEMENTLIST"):
            printSTATEMENTLIST(tree)
        elif(tree.ltype == "LASTSTATEMENT"):
            printLASTSTATEMENT(tree)
        elif(tree.ltype == "VARDEFSTATEMENT"):
            printVARDEFSTATEMENT(tree)
        elif(tree.ltype == "FUNCDEFSTATEMENT"):
            printFUNCDEFSTATEMENT(tree)
        elif(tree.ltype == "EXPRSTATEMENT"):
            printEXPRSTATEMENT(tree)
        elif(tree.ltype == "WHILELOOPSTATEMENT"):
            printWHILELOOPSTATEMENT(tree)
        elif(tree.ltype == "IFSTATEMENTSTATEMENT"):
            printIFSTATEMENTSTATEMENT(tree)
        elif(tree.ltype == "RETURNSTATEMENT"):
            printRETURNSTATEMENT(tree)
        elif(tree.ltype == "WHILELOOP"):
            printWHILELOOP(tree)
        elif(tree.ltype == "IFSTATEMENT"):
            printIFSTATEMENT(tree)
        elif(tree.ltype == "OPTELSESTATEMENT"):
            printOPTELSESTATEMENT(tree)
        elif(tree.ltype == "EMPTYOPTELSESTATEMENT"):
            printEMPTYOPTELSESTATEMENT(tree)
        elif(tree.ltype == "ELSESTATEMENT"):
            printELSESTATEMENT(tree)
        elif(tree.ltype == "ELSEIFSTATEMENT"):
            printELSEIFSTATEMENT(tree)
        elif(tree.ltype == "LAMBDA"):
            printLAMBDA(tree)
        elif(tree.ltype == "JOIN"):
            printJOIN(tree)
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
        elif(tree.ltype == "END_OF_INPUT"):
            print("\n" + " ", end="")
        else:
            print("ERROR: "+tree.ltype+" : "+tree.lvalue + " ", end="")

def printPARSE(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printPROGRAM(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLASTDEF(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printVARDEFINITION(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printFUNCDEFINITION(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printDEFINITION(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printVARDEF(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printFUNCDEF(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printIDDEF(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printARRAYACCESS(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLONEID(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOPTPARAMLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEMPTYOPTPARAMLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printPARAMLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLASTPARAM(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOPTEXPRLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEMPTYOPTEXPRLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEXPRLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLASTEXPR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEXPR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printSINGLEPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printIDPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printSTRINGPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printINTEGERPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printNOTPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEXPRPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLAMBDAPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printFUNCDEFPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEXPRLISTPRIMARY(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEQUALOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printNOTEQUALOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printGREATEROPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLESSOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printGREATEREQUALOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLESSEQUALOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printPLUSOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printMINUSOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printMULTIPLYOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printDIVIDEOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printPOWEROPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printANDOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOROPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printASSIGNOPERATOR(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printBLOCK(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOPTSTATEMENTLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEMPTYOPTSTATEMENTLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printSTATEMENTLIST(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLASTSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printVARDEFSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printFUNCDEFSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEXPRSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printWHILELOOPSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printIFSTATEMENTSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printRETURNSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printWHILELOOP(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printIFSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printOPTELSESTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printEMPTYOPTELSESTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printELSESTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printELSEIFSTATEMENT(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printLAMBDA(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printJOIN(tree):
    if(tree.left):
        prettyPrint(tree.left)
    if(tree.right):
        prettyPrint(tree.right)

def printSTRING(tree):
    print(tree.lvalue + " ", end="")

def printINTEGER(tree):
    print(tree.lvalue + " ", end="")

def printFUNCTION(tree):
    print(tree.lvalue + " ", end="")

def printVAR(tree):
    print(tree.lvalue + " ", end="")

def printWHILE(tree):
    print(tree.lvalue + " ", end="")

def printIF(tree):
    print(tree.lvalue + " ", end="")

def printELSE(tree):
    print(tree.lvalue + " ", end="")

def printRETURN(tree):
    print(tree.lvalue + " ", end="")

def printINCLUDE(tree):
    print(tree.lvalue + " ", end="")

def printID(tree):
    print(tree.lvalue + " ", end="")

def printSEMI(tree):
    print(tree.lvalue + "\n", end="")

def printCOMMA(tree):
    print(tree.lvalue + " ", end="")

def printOPAREN(tree):
    print(tree.lvalue, end="")

def printCPAREN(tree):
    print(tree.lvalue, end="")

def printOBRACE(tree):
    print(tree.lvalue + "\n", end="")

def printCBRACE(tree):
    print(tree.lvalue + "\n\n", end="")

def printOBRACKET(tree):
    print(tree.lvalue, end="")

def printCBRACKET(tree):
    print(tree.lvalue, end="")

def printPLUS(tree):
    print(tree.lvalue + " ", end="")

def printMINUS(tree):
    print(tree.lvalue + " ", end="")

def printTIMES(tree):
    print(tree.lvalue + " ", end="")

def printDIVIDE(tree):
    print(tree.lvalue + " ", end="")

def printMODULO(tree):
    print(tree.lvalue + " ", end="")

def printEXPONENT(tree):
    print(tree.lvalue + " ", end="")

def printAMPERSAND(tree):
    print(tree.lvalue + " ", end="")

def printPERIOD(tree):
    print(tree.lvalue + " ", end="")

def printBAR(tree):
    print(tree.lvalue + " ", end="")

def printGREATEREQUAL(tree):
    print(tree.lvalue + " ", end="")

def printGREATER(tree):
    print(tree.lvalue + " ", end="")

def printLESSEQUAL(tree):
    print(tree.lvalue + " ", end="")

def printLESS(tree):
    print(tree.lvalue + " ", end="")

def printDOUBLEEQUAL(tree):
    print(tree.lvalue + " ", end="")

def printEQUAL(tree):
    print(tree.lvalue + " ", end="")

def printNOTEQUAL(tree):
    print(tree.lvalue + " ", end="")

def printNOT(tree):
    print(tree.lvalue + " ", end="")


import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/program.rwall"
main(filename)
