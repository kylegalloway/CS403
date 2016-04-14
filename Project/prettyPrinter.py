from parser import Parser

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    prettyPrint(parse_tree)

def prettyPrint(tree):
    if(tree != None):
        # print(tree.ltype)
        if(tree.ltype == "PARSE"):
            printPARSE(tree)
        elif(tree.ltype == "INCLUDEFILE"):
            printINCLUDEFILE(tree)
        elif(tree.ltype == "FILE"):
            printFILE(tree)
        elif(tree.ltype == "EMPTYFILE"):
            printEMPTYFILE(tree)
        elif(tree.ltype == "INCLUSION"):
            printINCLUSION(tree)
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
        elif(tree.ltype == "ID"):
            printID(tree)
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
        elif(tree.ltype == "LAMBDA")
            printLAMBDA(tree):
        elif(tree.ltype == "JOIN")
            printJOIN(tree):
        elif(tree.ltype == "STRING"):
            printSTRING(tree
        elif(tree.ltype == "INTEGER"):
            printINTEGER(tree
        elif(tree.ltype == "FUNCTION"):
            printFUNCTION(tree
        elif(tree.ltype == "VAR"):
            printVAR(tree
        elif(tree.ltype == "WHILE"):
            printWHILE(tree
        elif(tree.ltype == "IF"):
            printIF(tree
        elif(tree.ltype == "ELSE"):
            printELSE(tree
        elif(tree.ltype == "RETURN"):
            printRETURN(tree
        elif(tree.ltype == "INCLUDE"):
            printINCLUDE(tree
        elif(tree.ltype == "ID"):
            printID(tree
        else:
            print("ERROR: "+tree.ltype+" : "+tree.lvalue)

def printPARSE(tree):
    pass

def printINCLUDEFILE(tree):
    pass

def printFILE(tree):
    pass

def printEMPTYFILE(tree):
    pass

def printINCLUSION(tree):
    pass

def printPROGRAM(tree):
    pass

def printLASTDEF(tree):
    pass

def printVARDEFINITION(tree):
    pass

def printFUNCDEFINITION(tree):
    pass

def printDEFINITION(tree):
    pass

def printVARDEF(tree):
    pass

def printFUNCDEF(tree):
    pass

def printIDDEF(tree):
    pass

def printARRAYACCESS(tree):
    pass

def printID(tree):
    pass

def printOPTPARAMLIST(tree):
    pass

def printEMPTYOPTPARAMLIST(tree):
    pass

def printPARAMLIST(tree):
    pass

def printLASTPARAM(tree):
    pass

def printOPTEXPRLIST(tree):
    pass

def printEMPTYOPTEXPRLIST(tree):
    pass

def printEXPRLIST(tree):
    pass

def printLASTEXPR(tree):
    pass

def printEXPR(tree):
    pass

def printSINGLEPRIMARY(tree):
    pass

def printIDPRIMARY(tree):
    pass

def printSTRINGPRIMARY(tree):
    pass

def printINTEGERPRIMARY(tree):
    pass

def printNOTPRIMARY(tree):
    pass

def printEXPRPRIMARY(tree):
    pass

def printLAMBDAPRIMARY(tree):
    pass

def printFUNCDEFPRIMARY(tree):
    pass

def printEXPRLISTPRIMARY(tree):
    pass

def printEQUALOPERATOR(tree):
    pass

def printNOTEQUALOPERATOR(tree):
    pass

def printGREATEROPERATOR(tree):
    pass

def printLESSOPERATOR(tree):
    pass

def printGREATEREQUALOPERATOR(tree):
    pass

def printLESSEQUALOPERATOR(tree):
    pass

def printPLUSOPERATOR(tree):
    pass

def printMINUSOPERATOR(tree):
    pass

def printMULTIPLYOPERATOR(tree):
    pass

def printDIVIDEOPERATOR(tree):
    pass

def printPOWEROPERATOR(tree):
    pass

def printANDOPERATOR(tree):
    pass

def printOROPERATOR(tree):
    pass

def printASSIGNOPERATOR(tree):
    pass

def printBLOCK(tree):
    pass

def printOPTSTATEMENTLIST(tree):
    pass

def printEMPTYOPTSTATEMENTLIST(tree):
    pass

def printSTATEMENTLIST(tree):
    pass

def printLASTSTATEMENT(tree):
    pass

def printVARDEFSTATEMENT(tree):
    pass

def printFUNCDEFSTATEMENT(tree):
    pass

def printEXPRSTATEMENT(tree):
    pass

def printWHILELOOPSTATEMENT(tree):
    pass

def printIFSTATEMENTSTATEMENT(tree):
    pass

def printRETURNSTATEMENT(tree):
    pass

def printWHILELOOP(tree):
    pass

def printIFSTATEMENT(tree):
    pass

def printOPTELSESTATEMENT(tree):
    pass

def printEMPTYOPTELSESTATEMENT(tree):
    pass

def printELSESTATEMENT(tree):
    pass

def printELSEIFSTATEMENT(tree):
    pass

def printLAMBDA(tree):
    pass

def printJOIN(tree):
    pass

def printSTRING(tree:
    pass

def printINTEGER(tree:
    pass

def printFUNCTION(tree:
    pass

def printVAR(tree:
    pass

def printWHILE(tree:
    pass

def printIF(tree:
    pass

def printELSE(tree:
    pass

def printRETURN(tree:
    pass

def printINCLUDE(tree:
    pass

def printID(tree:
    pass

import sys
if(len(sys.argv) == 2):
    filename = sys.argv[1]
else:
    filename = "redwall/program.rwall"
main(filename)
