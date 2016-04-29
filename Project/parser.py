from lex import Lexer
from lexeme import Lexeme

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
        root = self.program()
        eof = self.match("END_OF_INPUT")
        return self.cons("PARSE", root, eof)
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
        self.fatal("Syntax Error. Expected "+str(t)+" , Received "+str(self.pending.lvalue), self.lexer.lineNumber)

    def cons(self, value, left, right):
        return Lexeme(value, value, left, right)

# =============================================================================
#   GRAMMAR PORTION OF THE PARSING CLASS
# =============================================================================

    # program : definition
    #         | definition program
    def program(self):
        # print("In program")
        d = self.definition()
        if (self.programPending()):
            p = self.program()
            return self.cons("PROGRAM", d, self.cons("JOIN", p, None))
        return self.cons("PROGRAM", d, None)

    # definition : variableDefinition
    #            | functionDefinition
    #            | idDef SEMI
    def definition(self):
        # print("In definition")
        if(self.variableDefinitionPending()):
            v =self.variableDefinition()
            return self.cons("DEFINITION", v, None)
        elif(self.functionDefinitionPending()):
            f = self.functionDefinition()
            return self.cons("DEFINITION", f, None)

    # variableDefinition : VAR ID EQUAL expr SEMI
    def variableDefinition(self):
        # print("In variableDefinition")
        v = self.match("VAR")
        i = self.match("ID")
        eq = self.match("EQUAL")
        e = self.expr()
        s = self.match("SEMI")
        return self.cons("VARDEF", v, self.cons("JOIN", i, self.cons("JOIN", eq, self.cons("JOIN", e, self.cons("JOIN", s, None)))))

    # functionDefinition : FUNCTION ID OPAREN optParamList CPAREN block
    def functionDefinition(self):
        # print("In functionDefinition")
        f = self.match("FUNCTION")
        e = self.match("ID")
        o = self.match("OPAREN")
        op = self.optParamList()
        c = self.match("CPAREN")
        b = self.block()
        return self.cons("FUNCDEF", f, self.cons("JOIN", e, self.cons("JOIN", o, self.cons("JOIN", op, self.cons("JOIN", c, self.cons("JOIN", b, None))))))

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
            return self.cons("FUNCCALL", i, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))
        elif (self.check("OBRACKET")):
            o = self.match("OBRACKET")
            e = self.expr()
            c = self.match("CBRACKET")
            return self.cons("ARRAYACCESS", i, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))
        else:
            return self.cons("IDDEF", i, None)

    # optParamList : EMPTY
    #              | paramList
    def optParamList(self):
        # print("In optParamList")
        if(self.paramListPending()):
            p = self.paramList()
            return self.cons("OPTPARAMLIST", p, None)
        return self.cons("OPTPARAMLIST", None, None)

    # paramList : ID
    #           | ID COMMA paramList
    def paramList(self):
        # print("In paramList")
        i = self.match("ID")
        if (self.check("COMMA")):
            c = self.match("COMMA")
            p = self.paramList()
            return self.cons("PARAMLIST", i, self.cons("JOIN", c, self.cons("JOIN", p, None)))
        return self.cons("PARAMLIST", i, None)

    # optExprList : EMPTY
    #            | exprList
    def optExprList(self):
        # print("In optExprList")
        if(self.exprListPending()):
            e = self.exprList()
            return self.cons("OPTEXPRLIST", e, None)
        return self.cons("OPTEXPRLIST", None, None)

    # exprList : expr
    #          | expr COMMA exprList
    def exprList(self):
        # print("In exprList")
        e = self.expr()
        if (self.check("COMMA")):
            c = self.match("COMMA")
            ex = self.exprList()
            return self.cons("EXPRLIST", e, self.cons("JOIN", c, self.cons("JOIN", ex, None)))
        return self.cons("EXPRLIST", e, None)

    # expr : primary
    #      | primary operator expr
    def expr(self):
        # print("In expr")
        p = self.primary()
        if(self.operatorPending()):
            o = self.operator()
            e = self.expr()
            return Lexeme("EXPR", "EXPR", Lexeme("OPERATOR", o, p, e))
        return self.cons("EXPR", p, None)

    # primary : idDef
    #         | STRING
    #         | INTEGER
    #         | NOT primary
    #         | OPAREN expr CPAREN
    #         | k_lambda
    #         | functionDefinition
    #         | OBRACKET optExprList CBRACKET
    #         | NIL
    #         | BOOLEAN
    #         | PRINT OPAREN exprList CPAREN
    #         | APPEND OPAREN exprList CPAREN
    #         | REMOVE OPAREN exprList CPAREN
    #         | SET OPAREN exprList CPAREN
    #         | LENGTH OPAREN exprList CPAREN
    def primary(self):
        # print("In primary")
        if (self.idDefPending()):
            p = self.idDef()
            return self.cons("PRIMARY", p, None)
        elif (self.check("STRING")):
            p = self.match("STRING")
            return self.cons("PRIMARY", p, None)
        elif (self.check("INTEGER")):
            p = self.match("INTEGER")
            return self.cons("PRIMARY", p, None)
        elif (self.check("NOT")):
            n = self.match("NOT")
            p = self.primary()
            return self.cons("PRIMARY", n, self.cons("JOIN", p, None))
        elif (self.check("OPAREN")):
            o = self.match("OPAREN")
            e = self.expr()
            c = self.match("CPAREN")
            return self.cons("PRIMARY", o, self.cons("JOIN", e, self.cons("JOIN", c, None)))
        elif (self.k_lambdaPending()):
            p = self.k_lambda()
            return self.cons("PRIMARY", p, None)
        elif (self.functionDefinitionPending()):
            p = self.functionDefinition()
            return self.cons("PRIMARY", p, None)
        elif (self.check("OBRACKET")):
            o = self.match("OBRACKET")
            e = self.optExprList()
            c = self.match("CBRACKET")
            return self.cons("PRIMARY", o, self.cons("JOIN", e, self.cons("JOIN", c, None)))
        elif (self.check("NIL")):
            n = self.match("NIL")
            return self.cons("PRIMARY", n, None)
        elif (self.check("BOOLEAN")):
            b = self.match("BOOLEAN")
            return self.cons("PRIMARY", b, None)
        elif (self.check("PRINT")):
            f = self.match("PRINT")
            o = self.match("OPAREN")
            e = self.exprList()
            c = self.match("CPAREN")
            return self.cons("PRINT", f, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))
        elif (self.check("APPEND")):
            f = self.match("APPEND")
            o = self.match("OPAREN")
            e = self.exprList()
            c = self.match("CPAREN")
            return self.cons("APPEND", f, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))
        elif (self.check("INSERT")):
            f = self.match("INSERT")
            o = self.match("OPAREN")
            e = self.exprList()
            c = self.match("CPAREN")
            return self.cons("INSERT", f, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))
        elif (self.check("REMOVE")):
            f = self.match("REMOVE")
            o = self.match("OPAREN")
            e = self.exprList()
            c = self.match("CPAREN")
            return self.cons("REMOVE", f, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))
        elif (self.check("SET")):
            f = self.match("SET")
            o = self.match("OPAREN")
            e = self.exprList()
            c = self.match("CPAREN")
            return self.cons("SET", f, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))
        elif (self.check("LENGTH")):
            f = self.match("LENGTH")
            o = self.match("OPAREN")
            e = self.exprList()
            c = self.match("CPAREN")
            return self.cons("LENGTH", f, self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, None))))

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
            op = self.match("EQUAL")
            return self.cons("EQUAL", op, None)
        elif(self.check("NOTEQUAL")):
            op = self.match("NOTEQUAL")
            return self.cons("NOTEQUAL", op, None)
        elif(self.check("GREATER")):
            op = self.match("GREATER")
            return self.cons("GREATER", op, None)
        elif(self.check("LESS")):
            op = self.match("LESS")
            return self.cons("LESS", op, None)
        elif(self.check("GREATEREQUAL")):
            op = self.match("GREATEREQUAL")
            return self.cons("GREATEREQUAL", op, None)
        elif(self.check("LESSEQUAL")):
            op = self.match("LESSEQUAL")
            return self.cons("LESSEQUAL", op, None)
        elif(self.check("PLUS")):
            op = self.match("PLUS")
            return self.cons("PLUS", op, None)
        elif(self.check("MINUS")):
            op = self.match("MINUS")
            return self.cons("MINUS", op, None)
        elif(self.check("MULTIPLY")):
            op = self.match("MULTIPLY")
            return self.cons("MULTIPLY", op, None)
        elif(self.check("DIVIDE")):
            op = self.match("DIVIDE")
            return self.cons("DIVIDE", op, None)
        elif(self.check("POWER")):
            op = self.match("POWER")
            return self.cons("POWER", op, None)
        elif(self.check("AND")):
            op = self.match("AND")
            return self.cons("AND", op, None)
        elif(self.check("OR")):
            op = self.match("OR")
            return self.cons("OR", op, None)
        elif(self.check("ASSIGN")):
            op = self.match("ASSIGN")
            return self.cons("ASSIGN", op, None)
        elif(self.check("DOUBLEEQUAL")):
            op = self.match("DOUBLEEQUAL")
            return self.cons("DOUBLEEQUAL", op, None)

    # block : OBRACE optStatementList CBRACE
    def block(self):
        # print("In block")
        o = self.match("OBRACE")
        s = self.optStatementList()
        c = self.match("CBRACE")
        return self.cons("BLOCK", o, self.cons("JOIN", s, self.cons("JOIN", c, None)))

    # optStatementList : EMPTY
    #                  | statementList
    def optStatementList(self):
        # print("In optStatementList")
        if (self.statementListPending()):
            s = self.statementList()
            return self.cons("OPTSTATEMENTLIST", s, None)
        return self.cons("OPTSTATEMENTLIST", None, None)

    # statementList : statement
    #               | statement statementList
    def statementList(self):
        # print("In statementList")
        s= self.statement()
        if(self.statementListPending()):
            sl = self.statementList()
            return self.cons("STATEMENTLIST", s, self.cons("JOIN", sl, None))
        return self.cons("STATEMENTLIST", s, None)

    # statement : variableDefinition
    #           | functionDefinition
    #           | expr SEMI
    #           | whileLoop
    #           | ifStatement
    #           | RETURN expr SEMI
    def statement(self):
        # print("In statement")
        if(self.variableDefinitionPending()):
            v = self.variableDefinition()
            return self.cons("STATEMENT", v, None)
        elif(self.functionDefinitionPending()):
            f = self.functionDefinition()
            return self.cons("STATEMENT", f, None)
        elif(self.exprPending()):
            e = self.expr()
            s = self.match("SEMI")
            return self.cons("STATEMENT", e, self.cons("JOIN", s, None))
        elif(self.whileLoopPending()):
            w = self.whileLoop()
            return self.cons("STATEMENT", w, None)
        elif(self.ifStatementPending()):
            i = self.ifStatement()
            return self.cons("STATEMENT", i, None)
        elif(self.check("RETURN")):
            r = self.match("RETURN")
            e = self.expr()
            s = self.match("SEMI")
            return self.cons("STATEMENT", r ,self.cons("JOIN", e, self.cons("JOIN", s, None)))

    # whileLoop : WHILE OPAREN expr CPAREN block
    def whileLoop(self):
        # print("In whileLoop")
        w = self.match("WHILE")
        o = self.match("OPAREN")
        e = self.expr()
        c = self.match("CPAREN")
        b = self.block()
        return self.cons("WHILELOOP", w ,self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, self.cons("JOIN", b, None)))))

    # ifStatement : IF OPAREN expr CPAREN block optElseStatement
    def ifStatement(self):
        # print("In ifStatement")
        i = self.match("IF")
        o = self.match("OPAREN")
        e = self.expr()
        c = self.match("CPAREN")
        b = self.block()
        oe = self.optElseStatement()
        return self.cons("IFSTATEMENT", i ,self.cons("JOIN", o, self.cons("JOIN", e, self.cons("JOIN", c, self.cons("JOIN", b, self.cons("JOIN", oe, None))))))

    # optElseStatement : EMPTY
    #                  | elseStatement
    def optElseStatement(self):
        # print("In optElseStatement")
        if (self.elseStatementPending()):
            e = self.elseStatement()
            return self.cons("OPTELSESTATEMENT", e, None)
        return self.cons("OPTELSESTATEMENT", None, None)

    # elseStatement : ELSE block
    #               | ELSE ifStatement
    def elseStatement(self):
        # print("In elseStatement")
        e = self.match("ELSE")
        if(self.blockPending()):
            b = self.block()
            return self.cons("ELSESTATEMENT", e, self.cons("JOIN", b, None))
        elif(self.ifStatementPending()):
            i = self.ifStatement()
            return self.cons("ELSESTATEMENT", e, self.cons("JOIN", i, None))

    # k_lambda : LAMBDA OPAREN optParamList CPAREN block
    def k_lambda(self):
        # print("In k_lambda")
        l = self.match("LAMBDA")
        o = self.match("OPAREN")
        op = self.optParamList()
        c = self.match("CPAREN")
        b = self.block()
        return self.cons("LAMBDA", l ,self.cons("JOIN", o, self.cons("JOIN", op, self.cons("JOIN", c, self.cons("JOIN", b, None)))))

# =============================================================================
#   Pending Statements
# =============================================================================

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
        return self.idDefPending() or self.check("STRING") or self.check("INTEGER") or self.check("NOT") or self.check("OPAREN") or self.k_lambdaPending() or self.functionDefinitionPending() or self.check("OBRACKET") or self.check("NIL") or self.check("BOOLEAN") or self.check("PRINT") or self.check("APPEND") or self.check("INSERT") or self.check("REMOVE") or self.check("SET") or self.check("LENGTH")

    def operatorPending(self):
        # print("In operatorPending")
        return self.check("EQUAL") or self.check("NOTEQUAL") or self.check("GREATER") or self.check("LESS") or self.check("GREATEREQUAL") or self.check("LESSEQUAL") or self.check("PLUS") or self.check("MINUS") or self.check("MULTIPLY") or self.check("DIVIDE") or self.check("POWER") or self.check("AND") or self.check("OR") or self.check("ASSIGN") or self.check("DOUBLEEQUAL")

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
