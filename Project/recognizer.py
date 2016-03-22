from lex import Lexer
from lexeme import Lexeme

class Recognizer():

    def __init__(self, filename):
        self.file = open(filename)
        self.pending = None
        self.lexer = Lexer(self.file)

    def fatal(self, problem, line):
        print("LINE: "+str(line)+"\nERROR: "+problem)
        exit(1)

    def parse(self):
        self.pending = self.lexer.lex()
        self.k_file()
        self.match("END_OF_INPUT")

    def check(self, t) :
        print("Check: "+self.pending.ltype+" vs "+t)
        return self.pending.ltype == t

    def advance(self) :
        old = self.pending
        self.pending = self.lexer.lex()
        return old

    def match(self, t) :
        print("Match: "+t)
        if(self.check(t)): return self.advance()
        self.fatal("syntax error", self.lexer.lineNumber)

    # file : EMPTY
    #      | include file
    #      | program
    def k_file(self):
        if (self.includePending()):
            self.include()
            self.k_file()
        elif (self.programPending()):
            self.program()

    # include : INCLUDE STRING
    def include(self):
        self.match("INCLUDE")
        self.match("STRING")

    def includePending(self):
        return self.check("INCLUDE")


    # program : definition
    #         | definition program
    def program(self):
        self.definition()
        if (self.programPending()):
            self.program()

    def programPending(self):
        return self.definitionPending()

    # definition : variableDefinition
    #            | functionDefinition
    #            | idDef SEMI
    def definition(self):
        if(self.variableDefinitionPending()):
            self.variableDefinition()
        elif(self.functionDefinitionPending()):
            self.functionDefinition()
        elif(self.idDefPending()):
            self.idDef()
            self.match("SEMI")

    def definitionPending(self):
        return self.variableDefinitionPending() or self.functionDefinitionPending() or self.idDefPending()

    # variableDefinition : VAR ID EQUAL expr SEMI
    def variableDefinition(self):
        self.match("VAR")
        self.match("ID")
        self.match("EQUAL")
        print("debug")
        self.expr()
        self.match("SEMI")

    def variableDefinitionPending(self):
        return self.check("VAR")

    # functionDefinition : FUNCTION ID OPAREN optParamList CPAREN block
    def functionDefinition(self):
        self.match("FUNCTION")
        self.match("ID")
        self.match("OPAREN")
        self.optParamList()
        self.match("CPAREN")
        self.block()

    def functionDefinitionPending(self):
        return self.check("FUNCTION")

    # optParamList : EMPTY
    #              | paramList
    def optParamList(self):
        if(self.paramListPending()):
            self.paramList()

    # paramList : ID
    #           | ID COMMA paramList
    def paramList(self):
        self.match("ID")
        if (self.check("COMMA")):
            self.match("COMMA")
            self.paramList()

    def paramListPending(self):
        return self.check("ID")

    # optExprList : EMPTY
    #            | exprList
    def optExprList(self):
        if(self.exprListPending()):
            self.exprList()

    # exprList : expr
    #          | expr COMMA exprList
    def exprList(self):
        self.expr()
        if (self.check("COMMA")):
            self.match("COMMA")
            self.exprList()

    def exprListPending(self):
        return self.exprPending()

    # expr : primary
    #      | primary operator expr
    def expr(self):
        self.primary()
        if(self.operatorPending()):
            self.operator()
            self.expr()

    def exprPending(self):
        return self.primaryPending()

    # primary : idDef
    #         | STRING
    #         | INTEGER
    #         | NOT primary
    #         | OPAREN expr CPAREN
    #         | k_lambda
    #         | functionDefinition
    #         | OBRACKET optExprList CBRACKET
    def primary(self):
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

    def primaryPending(self):
        return self.idDefPending() or self.check("STRING") or self.check("INTEGER") or self.check("NOT") or self.check("OPAREN") or self.k_lambdaPending() or self.functionDefinitionPending() or self.check("OBRACKET")

    # idDef : ID
    #       | ID OPAREN optExprList CPAREN
    #       | ID OBRACKET expr CBRACKET
    def idDef(self):
        self.match("ID")
        if (self.check("OPAREN")):
            self.match("OPAREN")
            self.optExprList()
            self.match("CPAREN")
        elif (self.check("OBRACKET")):
            self.match("OBRACKET")
            self.expr()
            self.match("CBRACKET")

    def idDefPending(self):
        return self.check("ID")

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

    def operatorPending(self):
        return self.check("EQUAL") or self.check("NOTEQUAL") or self.check("GREATER") or self.check("LESS") or self.check("GREATEREQUAL") or self.check("LESSEQUAL") or self.check("PLUS") or self.check("MINUS") or self.check("MULTIPLY") or self.check("DIVIDE") or self.check("POWER") or self.check("AND") or self.check("OR") or self.check("ASSIGN")

    # block : OBRACE optStatementList CBRACE
    def block(self):
        self.match("OBRACE")
        self.optStatementList()
        self.match("CBRACE")

    def blockPending(self):
        return self.check("OBRACE")

    # optStatementList : EMPTY
    #                  | statementList
    def optStatementList(self):
        if (self.statementListPending()):
            self.statementList()

    # statementList : statement
    #               | statement statementList
    def statementList(self):
        self.statement()
        if(self.statementListPending()):
            self.statementList()

    def statementListPending(self):
        return self.statementPending()

    # statement : variableDefinition
    #           | functionDefinition
    #           | expr SEMI
    #           | whileLoop
    #           | ifStatement
    #           | RETURN expr SEMI
    def statement(self):
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

    def statementPending(self):
        return self.variableDefinitionPending() or self.functionDefinitionPending() or self.exprPending() or self.whileLoopPending() or self.ifStatementPending() or self.check("RETURN")

    # whileLoop : WHILE OPAREN expr CPAREN block
    def whileLoop(self):
        self.match("WHILE")
        self.match("OPAREN")
        self.expr()
        self.match("CPAREN")
        self.block()

    def whileLoopPending(self):
        return self.check("WHILE")

    # ifStatement : IF OPAREN expr CPAREN block optElseStatement
    def ifStatement(self):
        self.match("IF")
        self.match("OPAREN")
        self.expr()
        self.match("CPAREN")
        self.block()
        self.optElseStatement()

    def ifStatementPending(self):
        return self.check("IF")

    # optElseStatement : EMPTY
    #                  | elseStatement
    def optElseStatement(self):
        if (self.elseStatementPending()):
            self.elseStatement()

    # elseStatement : ELSE block
    #               | ELSE ifStatement
    def elseStatement(self):
        self.match("ELSE")
        if(self.blockPending()):
            self.block()
        elif(self.ifStatementPending()):
            self.ifStatement()

    def elseStatementPending(self):
        return self.check("ELSE")

    # k_lambda : LAMBDA OPAREN optParamList CPAREN block
    def k_lambda(self):
        self.match("LAMBDA")
        self.match("OPAREN")
        self.optParamList()
        self.match("CPAREN")
        self.block()

    def k_lambdaPending(self):
        return self.check("LAMBDA")