from parser import Parser
from environment import Environment

def main(filename):
    p = Parser(filename)
    parse_tree = p.parse()
    env = Environment()
    print(evaluate(parse_tree, env))

def evaluate(tree, env):
    # print(tree.ltype)
    if(tree.ltype == "PARSE"):
        return evalPARSE(tree, env)
    # elif(tree.ltype == "INCLUDEFILE"):
    #     return evalINCLUDEFILE(tree, env)
    # elif(tree.ltype == "FILE"):
    #     return evalFILE(tree, env)
    # elif(tree.ltype == "EMPTYFILE"):
    #     return evalEMPTYFILE(tree, env)
    # elif(tree.ltype == "INCLUSION"):
    #     return evalINCLUSION(tree, env)
    # elif(tree.ltype == "PROGRAM"):
    #     return evalPROGRAM(tree, env)
    # elif(tree.ltype == "LASTDEF"):
    #     return evalLASTDEF(tree, env)
    # elif(tree.ltype == "VARDEFINITION"):
    #     return evalVARDEFINITION(tree, env)
    # elif(tree.ltype == "FUNCDEFINITION"):
    #     return evalFUNCDEFINITION(tree, env)
    # elif(tree.ltype == "DEFINITION"):
    #     return evalDEFINITION(tree, env)
    # elif(tree.ltype == "VARDEF"):
    #     return evalVARDEF(tree, env)
    # elif(tree.ltype == "FUNCDEF"):
    #     return evalFUNCDEF(tree, env)
    # elif(tree.ltype == "IDDEF"):
    #     return evalIDDEF(tree, env)
    # elif(tree.ltype == "ARRAYACCESS"):
    #     return evalARRAYACCESS(tree, env)
    # elif(tree.ltype == "LONEID"):
    #     return evalID(tree, env)
    # elif(tree.ltype == "OPTPARAMLIST"):
    #     return evalOPTPARAMLIST(tree, env)
    # elif(tree.ltype == "EMPTYOPTPARAMLIST"):
    #     return evalEMPTYOPTPARAMLIST(tree, env)
    # elif(tree.ltype == "PARAMLIST"):
    #     return evalPARAMLIST(tree, env)
    # elif(tree.ltype == "LASTPARAM"):
    #     return evalLASTPARAM(tree, env)
    # elif(tree.ltype == "OPTEXPRLIST"):
    #     return evalOPTEXPRLIST(tree, env)
    # elif(tree.ltype == "EMPTYOPTEXPRLIST"):
    #     return evalEMPTYOPTEXPRLIST(tree, env)
    # elif(tree.ltype == "EXPRLIST"):
    #     return evalEXPRLIST(tree, env)
    # elif(tree.ltype == "LASTEXPR"):
    #     return evalLASTEXPR(tree, env)
    # elif(tree.ltype == "EXPR"):
    #     return evalEXPR(tree, env)
    # elif(tree.ltype == "SINGLEPRIMARY"):
    #     return evalSINGLEPRIMARY(tree, env)
    # elif(tree.ltype == "IDPRIMARY"):
    #     return evalIDPRIMARY(tree, env)
    # elif(tree.ltype == "STRINGPRIMARY"):
    #     return evalSTRINGPRIMARY(tree, env)
    # elif(tree.ltype == "INTEGERPRIMARY"):
    #     return evalINTEGERPRIMARY(tree, env)
    # elif(tree.ltype == "NOTPRIMARY"):
    #     return evalNOTPRIMARY(tree, env)
    # elif(tree.ltype == "EXPRPRIMARY"):
    #     return evalEXPRPRIMARY(tree, env)
    # elif(tree.ltype == "LAMBDAPRIMARY"):
    #     return evalLAMBDAPRIMARY(tree, env)
    # elif(tree.ltype == "FUNCDEFPRIMARY"):
    #     return evalFUNCDEFPRIMARY(tree, env)
    # elif(tree.ltype == "EXPRLISTPRIMARY"):
    #     return evalEXPRLISTPRIMARY(tree, env)
    # elif(tree.ltype == "EQUALOPERATOR"):
    #     return evalEQUALOPERATOR(tree, env)
    # elif(tree.ltype == "NOTEQUALOPERATOR"):
    #     return evalNOTEQUALOPERATOR(tree, env)
    # elif(tree.ltype == "GREATEROPERATOR"):
    #     return evalGREATEROPERATOR(tree, env)
    # elif(tree.ltype == "LESSOPERATOR"):
    #     return evalLESSOPERATOR(tree, env)
    # elif(tree.ltype == "GREATEREQUALOPERATOR"):
    #     return evalGREATEREQUALOPERATOR(tree, env)
    # elif(tree.ltype == "LESSEQUALOPERATOR"):
    #     return evalLESSEQUALOPERATOR(tree, env)
    # elif(tree.ltype == "PLUSOPERATOR"):
    #     return evalPLUSOPERATOR(tree, env)
    # elif(tree.ltype == "MINUSOPERATOR"):
    #     return evalMINUSOPERATOR(tree, env)
    # elif(tree.ltype == "MULTIPLYOPERATOR"):
    #     return evalMULTIPLYOPERATOR(tree, env)
    # elif(tree.ltype == "DIVIDEOPERATOR"):
    #     return evalDIVIDEOPERATOR(tree, env)
    # elif(tree.ltype == "POWEROPERATOR"):
    #     return evalPOWEROPERATOR(tree, env)
    # elif(tree.ltype == "ANDOPERATOR"):
    #     return evalANDOPERATOR(tree, env)
    # elif(tree.ltype == "OROPERATOR"):
    #     return evalOROPERATOR(tree, env)
    # elif(tree.ltype == "ASSIGNOPERATOR"):
    #     return evalASSIGNOPERATOR(tree, env)
    # elif(tree.ltype == "BLOCK"):
    #     return evalBLOCK(tree, env)
    # elif(tree.ltype == "OPTSTATEMENTLIST"):
    #     return evalOPTSTATEMENTLIST(tree, env)
    # elif(tree.ltype == "EMPTYOPTSTATEMENTLIST"):
    #     return evalEMPTYOPTSTATEMENTLIST(tree, env)
    # elif(tree.ltype == "STATEMENTLIST"):
    #     return evalSTATEMENTLIST(tree, env)
    # elif(tree.ltype == "LASTSTATEMENT"):
    #     return evalLASTSTATEMENT(tree, env)
    # elif(tree.ltype == "VARDEFSTATEMENT"):
    #     return evalVARDEFSTATEMENT(tree, env)
    # elif(tree.ltype == "FUNCDEFSTATEMENT"):
    #     return evalFUNCDEFSTATEMENT(tree, env)
    # elif(tree.ltype == "EXPRSTATEMENT"):
    #     return evalEXPRSTATEMENT(tree, env)
    # elif(tree.ltype == "WHILELOOPSTATEMENT"):
    #     return evalWHILELOOPSTATEMENT(tree, env)
    # elif(tree.ltype == "IFSTATEMENTSTATEMENT"):
    #     return evalIFSTATEMENTSTATEMENT(tree, env)
    # elif(tree.ltype == "RETURNSTATEMENT"):
    #     return evalRETURNSTATEMENT(tree, env)
    # elif(tree.ltype == "WHILELOOP"):
    #     return evalWHILELOOP(tree, env)
    # elif(tree.ltype == "IFSTATEMENT"):
    #     return evalIFSTATEMENT(tree, env)
    # elif(tree.ltype == "OPTELSESTATEMENT"):
    #     return evalOPTELSESTATEMENT(tree, env)
    # elif(tree.ltype == "EMPTYOPTELSESTATEMENT"):
    #     return evalEMPTYOPTELSESTATEMENT(tree, env)
    # elif(tree.ltype == "ELSESTATEMENT"):
    #     return evalELSESTATEMENT(tree, env)
    # elif(tree.ltype == "ELSEIFSTATEMENT"):
    #     return evalELSEIFSTATEMENT(tree, env)
    # elif(tree.ltype == "LAMBDA")
    #     return evalLAMBDA(tree, env):
    # elif(tree.ltype == "JOIN")
    #     return evalJOIN(tree, env):
    # elif(tree.ltype == "STRING"):
    #     return evalSTRING(tree,env)
    # elif(tree.ltype == "INTEGER"):
    #     return evalINTEGER(tree,env)
    # elif(tree.ltype == "FUNCTION"):
    #     return evalFUNCTION(tree,env)
    # elif(tree.ltype == "VAR"):
    #     return evalVAR(tree,env)
    # elif(tree.ltype == "WHILE"):
    #     return evalWHILE(tree,env)
    # elif(tree.ltype == "IF"):
    #     return evalIF(tree,env)
    # elif(tree.ltype == "ELSE"):
    #     return evalELSE(tree,env)
    # elif(tree.ltype == "RETURN"):
    #     return evalRETURN(tree,env)
    # elif(tree.ltype == "INCLUDE"):
    #     return evalINCLUDE(tree,env)
    # elif(tree.ltype == "ID"):
    #     return evalID(tree,env)
    else:
        return "ERROR: "+tree.ltype+" : "+tree.lvalue

def evalPARSE(tree, env):
    return evalPROGRAM(tree.left, env)

def evalPROGRAM(tree, env):
    if(tree.right.ltype == "JOIN"):
        evalDEFINITION(tree.left, env)
        evalProgram(tree.right.left, env)
    else:
        return evalDEFINITION(tree.left, env)

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
