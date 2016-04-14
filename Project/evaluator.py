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
            evalPARSE(tree, env)
        elif(tree.ltype == "INCLUDEFILE"):
            evalINCLUDEFILE(tree, env)
        elif(tree.ltype == "FILE"):
            evalFILE(tree, env)
        elif(tree.ltype == "EMPTYFILE"):
            evalEMPTYFILE(tree, env)
        elif(tree.ltype == "INCLUSION"):
            evalINCLUSION(tree, env)
        elif(tree.ltype == "PROGRAM"):
            evalPROGRAM(tree, env)
        elif(tree.ltype == "LASTDEF"):
            evalLASTDEF(tree, env)
        elif(tree.ltype == "VARDEFINITION"):
            evalVARDEFINITION(tree, env)
        elif(tree.ltype == "FUNCDEFINITION"):
            evalFUNCDEFINITION(tree, env)
        elif(tree.ltype == "DEFINITION"):
            evalDEFINITION(tree, env)
        elif(tree.ltype == "VARDEF"):
            evalVARDEF(tree, env)
        elif(tree.ltype == "FUNCDEF"):
            evalFUNCDEF(tree, env)
        elif(tree.ltype == "IDDEF"):
            evalIDDEF(tree, env)
        elif(tree.ltype == "ARRAYACCESS"):
            evalARRAYACCESS(tree, env)
        elif(tree.ltype == "LONEID"):
            evalID(tree, env)
        elif(tree.ltype == "OPTPARAMLIST"):
            evalOPTPARAMLIST(tree, env)
        elif(tree.ltype == "EMPTYOPTPARAMLIST"):
            evalEMPTYOPTPARAMLIST(tree, env)
        elif(tree.ltype == "PARAMLIST"):
            evalPARAMLIST(tree, env)
        elif(tree.ltype == "LASTPARAM"):
            evalLASTPARAM(tree, env)
        elif(tree.ltype == "OPTEXPRLIST"):
            evalOPTEXPRLIST(tree, env)
        elif(tree.ltype == "EMPTYOPTEXPRLIST"):
            evalEMPTYOPTEXPRLIST(tree, env)
        elif(tree.ltype == "EXPRLIST"):
            evalEXPRLIST(tree, env)
        elif(tree.ltype == "LASTEXPR"):
            evalLASTEXPR(tree, env)
        elif(tree.ltype == "EXPR"):
            evalEXPR(tree, env)
        elif(tree.ltype == "SINGLEPRIMARY"):
            evalSINGLEPRIMARY(tree, env)
        elif(tree.ltype == "IDPRIMARY"):
            evalIDPRIMARY(tree, env)
        elif(tree.ltype == "STRINGPRIMARY"):
            evalSTRINGPRIMARY(tree, env)
        elif(tree.ltype == "INTEGERPRIMARY"):
            evalINTEGERPRIMARY(tree, env)
        elif(tree.ltype == "NOTPRIMARY"):
            evalNOTPRIMARY(tree, env)
        elif(tree.ltype == "EXPRPRIMARY"):
            evalEXPRPRIMARY(tree, env)
        elif(tree.ltype == "LAMBDAPRIMARY"):
            evalLAMBDAPRIMARY(tree, env)
        elif(tree.ltype == "FUNCDEFPRIMARY"):
            evalFUNCDEFPRIMARY(tree, env)
        elif(tree.ltype == "EXPRLISTPRIMARY"):
            evalEXPRLISTPRIMARY(tree, env)
        elif(tree.ltype == "EQUALOPERATOR"):
            evalEQUALOPERATOR(tree, env)
        elif(tree.ltype == "NOTEQUALOPERATOR"):
            evalNOTEQUALOPERATOR(tree, env)
        elif(tree.ltype == "GREATEROPERATOR"):
            evalGREATEROPERATOR(tree, env)
        elif(tree.ltype == "LESSOPERATOR"):
            evalLESSOPERATOR(tree, env)
        elif(tree.ltype == "GREATEREQUALOPERATOR"):
            evalGREATEREQUALOPERATOR(tree, env)
        elif(tree.ltype == "LESSEQUALOPERATOR"):
            evalLESSEQUALOPERATOR(tree, env)
        elif(tree.ltype == "PLUSOPERATOR"):
            evalPLUSOPERATOR(tree, env)
        elif(tree.ltype == "MINUSOPERATOR"):
            evalMINUSOPERATOR(tree, env)
        elif(tree.ltype == "MULTIPLYOPERATOR"):
            evalMULTIPLYOPERATOR(tree, env)
        elif(tree.ltype == "DIVIDEOPERATOR"):
            evalDIVIDEOPERATOR(tree, env)
        elif(tree.ltype == "POWEROPERATOR"):
            evalPOWEROPERATOR(tree, env)
        elif(tree.ltype == "ANDOPERATOR"):
            evalANDOPERATOR(tree, env)
        elif(tree.ltype == "OROPERATOR"):
            evalOROPERATOR(tree, env)
        elif(tree.ltype == "ASSIGNOPERATOR"):
            evalASSIGNOPERATOR(tree, env)
        elif(tree.ltype == "BLOCK"):
            evalBLOCK(tree, env)
        elif(tree.ltype == "OPTSTATEMENTLIST"):
            evalOPTSTATEMENTLIST(tree, env)
        elif(tree.ltype == "EMPTYOPTSTATEMENTLIST"):
            evalEMPTYOPTSTATEMENTLIST(tree, env)
        elif(tree.ltype == "STATEMENTLIST"):
            evalSTATEMENTLIST(tree, env)
        elif(tree.ltype == "LASTSTATEMENT"):
            evalLASTSTATEMENT(tree, env)
        elif(tree.ltype == "VARDEFSTATEMENT"):
            evalVARDEFSTATEMENT(tree, env)
        elif(tree.ltype == "FUNCDEFSTATEMENT"):
            evalFUNCDEFSTATEMENT(tree, env)
        elif(tree.ltype == "EXPRSTATEMENT"):
            evalEXPRSTATEMENT(tree, env)
        elif(tree.ltype == "WHILELOOPSTATEMENT"):
            evalWHILELOOPSTATEMENT(tree, env)
        elif(tree.ltype == "IFSTATEMENTSTATEMENT"):
            evalIFSTATEMENTSTATEMENT(tree, env)
        elif(tree.ltype == "RETURNSTATEMENT"):
            evalRETURNSTATEMENT(tree, env)
        elif(tree.ltype == "WHILELOOP"):
            evalWHILELOOP(tree, env)
        elif(tree.ltype == "IFSTATEMENT"):
            evalIFSTATEMENT(tree, env)
        elif(tree.ltype == "OPTELSESTATEMENT"):
            evalOPTELSESTATEMENT(tree, env)
        elif(tree.ltype == "EMPTYOPTELSESTATEMENT"):
            evalEMPTYOPTELSESTATEMENT(tree, env)
        elif(tree.ltype == "ELSESTATEMENT"):
            evalELSESTATEMENT(tree, env)
        elif(tree.ltype == "ELSEIFSTATEMENT"):
            evalELSEIFSTATEMENT(tree, env)
        elif(tree.ltype == "LAMBDA")
            evalLAMBDA(tree, env):
        elif(tree.ltype == "JOIN")
            evalJOIN(tree, env):
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

def evalPARSE(tree, env):
    pass

def evalINCLUDEFILE(tree, env):
    pass

def evalFILE(tree, env):
    pass

def evalEMPTYFILE(tree, env):
    pass

def evalINCLUSION(tree, env):
    pass

def evalPROGRAM(tree, env):
    pass

def evalLASTDEF(tree, env):
    pass

def evalVARDEFINITION(tree, env):
    pass

def evalFUNCDEFINITION(tree, env):
    pass

def evalDEFINITION(tree, env):
    pass

def evalVARDEF(tree, env):
    pass

def evalFUNCDEF(tree, env):
    pass

def evalIDDEF(tree, env):
    pass

def evalARRAYACCESS(tree, env):
    pass

def evalLONEID(tree, env):
    pass

def evalOPTPARAMLIST(tree, env):
    pass

def evalEMPTYOPTPARAMLIST(tree, env):
    pass

def evalPARAMLIST(tree, env):
    pass

def evalLASTPARAM(tree, env):
    pass

def evalOPTEXPRLIST(tree, env):
    pass

def evalEMPTYOPTEXPRLIST(tree, env):
    pass

def evalEXPRLIST(tree, env):
    pass

def evalLASTEXPR(tree, env):
    pass

def evalEXPR(tree, env):
    pass

def evalSINGLEPRIMARY(tree, env):
    pass

def evalIDPRIMARY(tree, env):
    pass

def evalSTRINGPRIMARY(tree, env):
    pass

def evalINTEGERPRIMARY(tree, env):
    pass

def evalNOTPRIMARY(tree, env):
    pass

def evalEXPRPRIMARY(tree, env):
    pass

def evalLAMBDAPRIMARY(tree, env):
    pass

def evalFUNCDEFPRIMARY(tree, env):
    pass

def evalEXPRLISTPRIMARY(tree, env):
    pass

def evalEQUALOPERATOR(tree, env):
    pass

def evalNOTEQUALOPERATOR(tree, env):
    pass

def evalGREATEROPERATOR(tree, env):
    pass

def evalLESSOPERATOR(tree, env):
    pass

def evalGREATEREQUALOPERATOR(tree, env):
    pass

def evalLESSEQUALOPERATOR(tree, env):
    pass

def evalPLUSOPERATOR(tree, env):
    pass

def evalMINUSOPERATOR(tree, env):
    pass

def evalMULTIPLYOPERATOR(tree, env):
    pass

def evalDIVIDEOPERATOR(tree, env):
    pass

def evalPOWEROPERATOR(tree, env):
    pass

def evalANDOPERATOR(tree, env):
    pass

def evalOROPERATOR(tree, env):
    pass

def evalASSIGNOPERATOR(tree, env):
    pass

def evalBLOCK(tree, env):
    pass

def evalOPTSTATEMENTLIST(tree, env):
    pass

def evalEMPTYOPTSTATEMENTLIST(tree, env):
    pass

def evalSTATEMENTLIST(tree, env):
    pass

def evalLASTSTATEMENT(tree, env):
    pass

def evalVARDEFSTATEMENT(tree, env):
    pass

def evalFUNCDEFSTATEMENT(tree, env):
    pass

def evalEXPRSTATEMENT(tree, env):
    pass

def evalWHILELOOPSTATEMENT(tree, env):
    pass

def evalIFSTATEMENTSTATEMENT(tree, env):
    pass

def evalRETURNSTATEMENT(tree, env):
    pass

def evalWHILELOOP(tree, env):
    pass

def evalIFSTATEMENT(tree, env):
    pass

def evalOPTELSESTATEMENT(tree, env):
    pass

def evalEMPTYOPTELSESTATEMENT(tree, env):
    pass

def evalELSESTATEMENT(tree, env):
    pass

def evalELSEIFSTATEMENT(tree, env):
    pass

def evalLAMBDA(tree, env):
    pass

def evalJOIN(tree, env):
    pass

def evalSTRING(tree,env):
    pass

def evalINTEGER(tree,env):
    pass

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
    filename = "redwall/program.rwall"
main(filename)
