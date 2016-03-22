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
        print("In parse")
        self.advance()
        self.k_file()
        self.match("END_OF_INPUT")
        print("Done")

    def check(self, t):
        print("Check: "+self.pending.ltype+" vs "+t)
        return self.pending.ltype == t

    def advance(self):
        print("In advance")
        old = self.pending
        self.pending = self.lexer.lex()
        print("New Lexeme is "+self.pending.ltype)
        return old

    def match(self, t) :
        print("Match: "+t)
        if(self.check(t)):
            print("Match Successful")
            return self.advance()
        self.fatal("syntax error", self.lexer.lineNumber)

    # file : EMPTY
    #      | include file
    #      | program
    def k_file(self):
        print("In k_file")
        if (self.includePending()):
            self.include()
            self.k_file()
        elif (self.programPending()):
            self.program()

    # include : INCLUDE STRING
    def include(self):
        print("In include")
        self.match("INCLUDE")
        self.match("STRING")

    def includePending(self):
        print("In includePending")
        return self.check("INCLUDE")


    # program : definition
    #         | definition program
    def program(self):
        print("In program")
        self.definition()
        if (self.programPending()):
            self.program()

    def programPending(self):
        print("In programPending")
        return self.definitionPending()

    # definition : variableDefinition
    #            | functionDefinition
    #            | idDef SEMI
    def definition(self):
        print("In definition")
        if(self.variableDefinitionPending()):
            self.variableDefinition()
        elif(self.functionDefinitionPending()):
            self.functionDefinition()
        elif(self.idDefPending()):
            self.idDef()
            self.match("SEMI")

    def definitionPending(self):
        print("In definitionPending")
        return self.variableDefinitionPending() or self.functionDefinitionPending() or self.idDefPending()

    # variableDefinition : VAR ID EQUAL expr SEMI
    def variableDefinition(self):
        print("In variableDefinition")
        self.match("VAR")
        self.match("ID")
        self.match("EQUAL")
        print("debug")
        self.expr()
        self.match("SEMI")

    def variableDefinitionPending(self):
        print("In variableDefinitionPending")
        return self.check("VAR")

    # functionDefinition : FUNCTION ID OPAREN optParamList CPAREN block
    def functionDefinition(self):
        print("In functionDefinition")
        self.match("FUNCTION")
        self.match("ID")
        self.match("OPAREN")
        self.optParamList()
        self.match("CPAREN")
        self.block()

    def functionDefinitionPending(self):
        print("In functionDefinitionPending")
        return self.check("FUNCTION")

    # optParamList : EMPTY
    #              | paramList
    def optParamList(self):
        print("In optParamList")
        if(self.paramListPending()):
            self.paramList()

    # paramList : ID
    #           | ID COMMA paramList
    def paramList(self):
        print("In paramList")
        self.match("ID")
        if (self.check("COMMA")):
            self.match("COMMA")
            self.paramList()

    def paramListPending(self):
        print("In paramListPending")
        return self.check("ID")

    # optExprList : EMPTY
    #            | exprList
    def optExprList(self):
        print("In optExprList")
        if(self.exprListPending()):
            self.exprList()

    # exprList : expr
    #          | expr COMMA exprList
    def exprList(self):
        print("In exprList")
        self.expr()
        if (self.check("COMMA")):
            self.match("COMMA")
            self.exprList()

    def exprListPending(self):
        print("In exprListPending")
        return self.exprPending()

    # expr : primary
    #      | primary operator expr
    def expr(self):
        print("In expr")
        self.primary()
        if(self.operatorPending()):
            self.operator()
            self.expr()

    def exprPending(self):
        print("In exprPending")
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
        print("In primary")
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
        print("In primaryPending")
        return self.idDefPending() or self.check("STRING") or self.check("INTEGER") or self.check("NOT") or self.check("OPAREN") or self.k_lambdaPending() or self.functionDefinitionPending() or self.check("OBRACKET")

    # idDef : ID
    #       | ID OPAREN optExprList CPAREN
    #       | ID OBRACKET expr CBRACKET
    def idDef(self):
        print("In idDef")
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
        print("In idDefPending")
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
        print("In operator")
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
        print("In operatorPending")
        return self.check("EQUAL") or self.check("NOTEQUAL") or self.check("GREATER") or self.check("LESS") or self.check("GREATEREQUAL") or self.check("LESSEQUAL") or self.check("PLUS") or self.check("MINUS") or self.check("MULTIPLY") or self.check("DIVIDE") or self.check("POWER") or self.check("AND") or self.check("OR") or self.check("ASSIGN")

    # block : OBRACE optStatementList CBRACE
    def block(self):
        print("In block")
        self.match("OBRACE")
        self.optStatementList()
        self.match("CBRACE")

    def blockPending(self):
        print("In blockPending")
        return self.check("OBRACE")

    # optStatementList : EMPTY
    #                  | statementList
    def optStatementList(self):
        print("In optStatementList")
        if (self.statementListPending()):
            self.statementList()

    # statementList : statement
    #               | statement statementList
    def statementList(self):
        print("In statementList")
        self.statement()
        if(self.statementListPending()):
            self.statementList()

    def statementListPending(self):
        print("In statementListPending")
        return self.statementPending()

    # statement : variableDefinition
    #           | functionDefinition
    #           | expr SEMI
    #           | whileLoop
    #           | ifStatement
    #           | RETURN expr SEMI
    def statement(self):
        print("In statement")
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
        print("In statementPending")
        return self.variableDefinitionPending() or self.functionDefinitionPending() or self.exprPending() or self.whileLoopPending() or self.ifStatementPending() or self.check("RETURN")

    # whileLoop : WHILE OPAREN expr CPAREN block
    def whileLoop(self):
        print("In whileLoop")
        self.match("WHILE")
        self.match("OPAREN")
        self.expr()
        self.match("CPAREN")
        self.block()

    def whileLoopPending(self):
        print("In whileLoopPending")
        return self.check("WHILE")

    # ifStatement : IF OPAREN expr CPAREN block optElseStatement
    def ifStatement(self):
        print("In ifStatement")
        self.match("IF")
        self.match("OPAREN")
        self.expr()
        self.match("CPAREN")
        self.block()
        self.optElseStatement()

    def ifStatementPending(self):
        print("In ifStatementPending")
        return self.check("IF")

    # optElseStatement : EMPTY
    #                  | elseStatement
    def optElseStatement(self):
        print("In optElseStatement")
        if (self.elseStatementPending()):
            self.elseStatement()

    # elseStatement : ELSE block
    #               | ELSE ifStatement
    def elseStatement(self):
        print("In elseStatement")
        self.match("ELSE")
        if(self.blockPending()):
            self.block()
        elif(self.ifStatementPending()):
            self.ifStatement()

    def elseStatementPending(self):
        print("In elseStatementPending")
        return self.check("ELSE")

    # k_lambda : LAMBDA OPAREN optParamList CPAREN block
    def k_lambda(self):
        print("In k_lambda")
        self.match("LAMBDA")
        self.match("OPAREN")
        self.optParamList()
        self.match("CPAREN")
        self.block()

    def k_lambdaPending(self):
        print("In k_lambdaPending")
        return self.check("LAMBDA")