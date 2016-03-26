from lex import Lexer
from lexeme import Lexeme
from conscell import ConsCell

class Parser():

    def __init__(self, filename):
        self.file = open(filename)
        self.pending = None
        self.lexer = Lexer(self.file)

    def fatal(self, problem, line):
        print("LINE: "+str(line)+"\nERROR: "+problem)
        exit(1)

    def parse(self):
        # print("In parse")
        self.advance()
        root = self.k_file()
        self.match("END_OF_INPUT")
        return root
        # print("Done")

    def check(self, t):
        # print("Check: "+self.pending.ltype+" vs "+t)
        return self.pending.ltype == t

    def advance(self):
        # print("In advance")
        old = self.pending
        self.pending = self.lexer.lex()
        # print("New Lexeme is "+self.pending.ltype)
        return old

    def match(self, t) :
        # print("Match: "+t)
        if(self.check(t)):
            # print("Token: "+str(self.pending))
            return self.advance()
        self.fatal("Syntax Error. Expected "+str(t)+" , Received "+str(self.pending), self.lexer.lineNumber)

    def cons(value, left, right):
        return ConsCell(value, ConsCell(left, ConsCell(right, None)))

# =============================================================================
#   BELOW HERE IS THE GRAMMAR PORTION OF THE PARSING CLASS
# =============================================================================


    # file : EMPTY
    #      | include file
    #      | program
    def k_file(self):
        # print("In k_file")
        if (self.includePending()):
            i = self.include()
            f = self.k_file()
            return cons("FILE", i, cons("JOIN", f, None))
        elif (self.programPending()):
            p = self.program()
            return cons("FILE", p, None)
        else:
            return cons("FILE", None, None)

    # include : INCLUDE STRING
    def include(self):
        # print("In include")
        i = self.match("INCLUDE")
        s = self.match("STRING")
        return cons("INCLUDE", i, cons("JOIN", s, None))

    # program : definition
    #         | definition program
    def program(self):
        # print("In program")
        d = self.definition()
        if (self.programPending()):
            p = self.program()
            return cons(d, p)
        return cons("PROGRAM", d, None)

    # definition : variableDefinition
    #            | functionDefinition
    #            | idDef SEMI
    def definition(self):
        # print("In definition")
        if(self.variableDefinitionPending()):
            v =self.variableDefinition()
            return cons("DEFINITION", v, None)
        elif(self.functionDefinitionPending()):
            f = self.functionDefinition()
            return cons("DEFINITION", f, None)
        elif(self.idDefPending()):
            i = self.idDef()
            s = self.match("SEMI")
            return cons("DEFINITION", i, cons("JOIN", s, None))

    # variableDefinition : VAR ID EQUAL expr SEMI
    def variableDefinition(self):
        # print("In variableDefinition")
        v = self.match("VAR")
        i = self.match("ID")
        eq = self.match("EQUAL")
        e = self.expr()
        s = self.match("SEMI")
        return cons("VARDEF", v, cons("JOIN", i, cons("JOIN", eq, cons("JOIN", e, cons("JOIN", s, None)))))

    # functionDefinition : FUNCTION ID OPAREN optParamList CPAREN block
    def functionDefinition(self):
        # print("In functionDefinition")
        f = self.match("FUNCTION")
        e = self.match("ID")
        o = self.match("OPAREN")
        op = self.optParamList()
        c = self.match("CPAREN")
        b = self.block()
        return cons("FUNCDEF", f, cons("JOIN", e, cons("JOIN", o, cons("JOIN", op, cons("JOIN", c, cons("JOIN", b, None))))))

    # idDef : ID
    #       | ID OPAREN optExprList CPAREN
    #       | ID OBRACKET expr CBRACKET
    def idDef(self):
        # print("In idDef")
        i = self.match("ID")
        if (self.check("OPAREN")):
            o = self.match("OPAREN")
            e = self.optExprList()
            c = self.match("CPAREN")
            return cons("IDDEF", i, cons("JOIN", o, cons("JOIN", e, cons("JOIN", c, None))))
        elif (self.check("OBRACKET")):
            o = self.match("OBRACKET")
            e = self.expr()
            c = self.match("CBRACKET")
            return cons("IDDEF", i, cons("JOIN", o, cons("JOIN", e, cons("JOIN", c, None))))
        else:
            return cons("IDDEF", i, None)

    # optParamList : EMPTY
    #              | paramList
    def optParamList(self):
        # print("In optParamList")
        if(self.paramListPending()):
            p = self.paramList()
            return cons("OPTPARAMLIST", p, None)
        else:
            return cons("OPTPARAMLIST", None, None)

    # paramList : ID
    #           | ID COMMA paramList
    def paramList(self):
        # print("In paramList")
        i = self.match("ID")
        if (self.check("COMMA")):
            c = self.match("COMMA")
            p = self.paramList()
            return cons("PARAMLIST", i, cons("JOIN", c, cons("JOIN", p, None)))
        return cons("PARAMLIST", i, None)

    # optExprList : EMPTY
    #            | exprList
    def optExprList(self):
        # print("In optExprList")
        if(self.exprListPending()):
            e = self.exprList()
            return cons("OPTEXPRLIST", e, None)
        return cons("OPTEXPRLIST", None, None)

    # exprList : expr
    #          | expr COMMA exprList
    def exprList(self):
        # print("In exprList")
        e = self.expr()
        if (self.check("COMMA")):
            c = self.match("COMMA")
            ex = self.exprList()
            return cons("EXPRLIST", e, cons("JOIN", c, cons("JOIN", ex, None)))
        return cons("EXPRLIST", e, None)

    # expr : primary
    #      | primary operator expr
    def expr(self):
        # print("In expr")
        p = self.primary()
        if(self.operatorPending()):
            o = self.operator()
            e = self.expr()
            return cons("EXPR", p, cons("JOIN", o, cons("JOIN", e, None)))
        return cons("EXPR", p, None)

# =============================================================================
#   WHERE I STOPPED
# =============================================================================

    # primary : idDef
    #         | STRING
    #         | INTEGER
    #         | NOT primary
    #         | OPAREN expr CPAREN
    #         | k_lambda
    #         | functionDefinition
    #         | OBRACKET optExprList CBRACKET
    def primary(self):
        # print("In primary")
        if (self.idDefPending()):
            self.idDef()
        elif (self.check("STRING")):
            self.match("STRING")
        elif (self.check("INTEGER")):
            self.match("INTEGER")
        elif (self.check("NOT")):
            self.match("NOT")
            self.primary()
        elif (self.check("OPAREN")):
            self.match("OPAREN")
            self.expr()
            self.match("CPAREN")
        elif (self.k_lambdaPending()):
            self.k_lambda()
        elif (self.functionDefinitionPending()):
            self.functionDefinition()
        elif (self.check("OBRACKET")):
            self.match("OBRACKET")
            self.optExprList()
            self.match("OBRACKET")

    # operator : EQUAL
    #          | NOTEQUAL
    #          | GREATER
    #          | LESS
    #          | GREATEREQUAL
    #          | LESSEQUAL
    #          | PLUS
    #          | MINUS
    #          | MULTIPLY
    #          | DIVIDE
    #          | POWER
    #          | AND
    #          | OR
    #          | DOUBLEEQUAL
    def operator(self):
        # print("In operator")
        if(self.check("EQUAL")):
            self.match("EQUAL")
        elif(self.check("NOTEQUAL")):
            self.match("NOTEQUAL")
        elif(self.check("GREATER")):
            self.match("GREATER")
        elif(self.check("LESS")):
            self.match("LESS")
        elif(self.check("GREATEREQUAL")):
            self.match("GREATEREQUAL")
        elif(self.check("LESSEQUAL")):
            self.match("LESSEQUAL")
        elif(self.check("PLUS")):
            self.match("PLUS")
        elif(self.check("MINUS")):
            self.match("MINUS")
        elif(self.check("MULTIPLY")):
            self.match("MULTIPLY")
        elif(self.check("DIVIDE")):
            self.match("DIVIDE")
        elif(self.check("POWER")):
            self.match("POWER")
        elif(self.check("AND")):
            self.match("AND")
        elif(self.check("OR")):
            self.match("OR")
        elif(self.check("ASSIGN")):
            self.match("ASSIGN")

    # block : OBRACE optStatementList CBRACE
    def block(self):
        # print("In block")
        self.match("OBRACE")
        self.optStatementList()
        self.match("CBRACE")

    # optStatementList : EMPTY
    #                  | statementList
    def optStatementList(self):
        # print("In optStatementList")
        if (self.statementListPending()):
            self.statementList()

    # statementList : statement
    #               | statement statementList
    def statementList(self):
        # print("In statementList")
        self.statement()
        if(self.statementListPending()):
            self.statementList()

    # statement : variableDefinition
    #           | functionDefinition
    #           | expr SEMI
    #           | whileLoop
    #           | ifStatement
    #           | RETURN expr SEMI
    def statement(self):
        # print("In statement")
        if(self.variableDefinitionPending()):
            self.variableDefinition()
        elif(self.functionDefinitionPending()):
            self.functionDefinition()
        elif(self.exprPending()):
            self.expr()
            self.match("SEMI")
        elif(self.whileLoopPending()):
            self.whileLoop()
        elif(self.ifStatementPending()):
            self.ifStatement()
        elif(self.check("RETURN")):
            self.match("RETURN")
            self.expr()
            self.match("SEMI")

    # whileLoop : WHILE OPAREN expr CPAREN block
    def whileLoop(self):
        # print("In whileLoop")
        self.match("WHILE")
        self.match("OPAREN")
        self.expr()
        self.match("CPAREN")
        self.block()

    # ifStatement : IF OPAREN expr CPAREN block optElseStatement
    def ifStatement(self):
        # print("In ifStatement")
        self.match("IF")
        self.match("OPAREN")
        self.expr()
        self.match("CPAREN")
        self.block()
        self.optElseStatement()

    # optElseStatement : EMPTY
    #                  | elseStatement
    def optElseStatement(self):
        # print("In optElseStatement")
        if (self.elseStatementPending()):
            self.elseStatement()

    # elseStatement : ELSE block
    #               | ELSE ifStatement
    def elseStatement(self):
        # print("In elseStatement")
        self.match("ELSE")
        if(self.blockPending()):
            self.block()
        elif(self.ifStatementPending()):
            self.ifStatement()

    # k_lambda : LAMBDA OPAREN optParamList CPAREN block
    def k_lambda(self):
        # print("In k_lambda")
        self.match("LAMBDA")
        self.match("OPAREN")
        self.optParamList()
        self.match("CPAREN")
        self.block()

    def includePending(self):
        # print("In includePending")
        return self.check("INCLUDE")

    def programPending(self):
        # print("In programPending")
        return self.definitionPending()

    def definitionPending(self):
        # print("In definitionPending")
        return self.variableDefinitionPending() or self.functionDefinitionPending() or self.idDefPending()

    def variableDefinitionPending(self):
        # print("In variableDefinitionPending")
        return self.check("VAR")

    def functionDefinitionPending(self):
        # print("In functionDefinitionPending")
        return self.check("FUNCTION")

    def idDefPending(self):
        # print("In idDefPending")
        return self.check("ID")

    def paramListPending(self):
        # print("In paramListPending")
        return self.check("ID")

    def exprListPending(self):
        # print("In exprListPending")
        return self.exprPending()

    def exprPending(self):
        # print("In exprPending")
        return self.primaryPending()

    def primaryPending(self):
        # print("In primaryPending")
        return self.idDefPending() or self.check("STRING") or self.check("INTEGER") or self.check("NOT") or self.check("OPAREN") or self.k_lambdaPending() or self.functionDefinitionPending() or self.check("OBRACKET")

    def operatorPending(self):
        # print("In operatorPending")
        return self.check("EQUAL") or self.check("NOTEQUAL") or self.check("GREATER") or self.check("LESS") or self.check("GREATEREQUAL") or self.check("LESSEQUAL") or self.check("PLUS") or self.check("MINUS") or self.check("MULTIPLY") or self.check("DIVIDE") or self.check("POWER") or self.check("AND") or self.check("OR") or self.check("ASSIGN")

    def blockPending(self):
        # print("In blockPending")
        return self.check("OBRACE")

    def statementListPending(self):
        # print("In statementListPending")
        return self.statementPending()

    def statementPending(self):
        # print("In statementPending")
        return self.variableDefinitionPending() or self.functionDefinitionPending() or self.exprPending() or self.whileLoopPending() or self.ifStatementPending() or self.check("RETURN")

    def whileLoopPending(self):
        # print("In whileLoopPending")
        return self.check("WHILE")

    def ifStatementPending(self):
        # print("In ifStatementPending")
        return self.check("IF")

    def elseStatementPending(self):
        # print("In elseStatementPending")
        return self.check("ELSE")

    def k_lambdaPending(self):
        # print("In k_lambdaPending")
        return self.check("LAMBDA")