from lex import Lexer
from lexeme import Lexeme

class Parser():

    def __init__(self, filename):
        with open(filename) as self.file:
            self.pending = None
            self.lexer = Lexer(self.file)

    def parse(file):
        self.pending = self.lexer.lex()
        file()
        match("END_OF_INPUT")

    def check(self, t) :
        return self.pending.ltype == t

    def advance(self) :
        old = self.pending
        self.pending = self.lexer.lex()
        return old

    def match(self, t) :
        matchNoAdvance(t)
        advance();

    def matchNoAdvance(self, t):
        if (not (check(t))):
            fatal("syntax error")

    # file : EMPTY
    #      | include file
    #      | program
    def file():
        if (includePending()):
            include()
            file()
        elif (programPending()):
            program()

    # include : INCLUDE STRING
    def include():
        match("INCLUDE")
        match("STRING")

    def includePending():
        return check("INCLUDE")


    # program : definition
    #         | definition program
    def program():
        definition()
        if (programPending()):
            program()

    def programPending():
        return definitionPending()

    # definition : variableDefinition
    #            | functionDefinition
    def definition():
        if(variableDefinitionPending()):
            variableDefinition()
        elif(functionDefinitionPending()):
            functionDefinition()

    def definitionPending():
        return variableDefinitionPending() or functionDefinitionPending()

    # variableDefinition : ID EQUAL expr SEMI
    def variableDefinition():
        match("ID")
        match("EQUAL")
        expr()
        match("SEMI")

    def variableDefinitionPending():
        return check("ID")

    # functionDefinition : FUNCTION ID OPAREN optParamList CPAREN block
    def functionDefinition():
        match("FUNCTION")
        match("ID")
        match("OPAREN")
        optParamList()
        match("CPAREN")
        block()

    def functionDefinitionPending():
        return check("FUNCTION")

    # optParamList : EMPTY
    #              | paramList
    def optParamList():
        if(paramListPending()):
            return paramList()

    # paramList : ID
    #           | ID COMMA paramList
    def paramList():
        match("ID")
        if (check("COMMA")):
            match("COMMA")
            paramList()

    def paramListPending():
        return check("ID")

    # optExprList : EMPTY
    #            | exprList
    def optExprList():
        if(exprListPending()):
            return exprList()

    # exprList : expr
    #          | expr COMMA exprList
    def exprList():
        expr()
        if (check("COMMA")):
            match("COMMA")
            exprList()

    def exprListPending():
        return exprPending()

    # expr : primary
    #      | primary operator expr
    def expr():
        primary()
        if(operatorPending()):
            operator()
            expr()

    def exprPending():
        return primaryPending()

    # primary : idDef
    #         | STRING
    #         | INTEGER
    #         | NOT primary
    #         | OPAREN expr CPAREN
    #         | k_lambda
    #         | functionDefinition
    #         | OBRACKET optExprList CBRACKET
    def primary():
        if (idDefPending()):
            idDef()
        elif (check("STRING")):
            match("STRING")
        elif (check("INTEGER")):
            match("INTEGER")
        elif (check("NOT")):
            match("NOT")
            primary()
        elif (check("OPAREN")):
            match("OPAREN")
            expr()
            match("CPAREN")
        elif (k_lambdaPending()):
            k_lambda()
        elif (functionDefinitionPending()):
            functionDefinition()
        elif (check("OBRACKET")):
            match("OBRACKET")
            optExprList()
            match("OBRACKET")

    def primaryPending():
        return idDefPending() or check("STRING") or check("INTEGER") or check("NOT") or check("OPAREN") or k_lambdaPending() or functionDefinitionPending() or check("OBRACKET")

    # idDef : ID
    #       | ID OPAREN optExprList CPAREN
    #       | ID OBRACKET expr CBRACKET
    def idDef():
        match("ID")
        if (check("OPAREN")):
            match("OPAREN")
            optExprList()
            match("CPAREN")
        elif (check("OBRACKET")):
            match("OBRACKET")
            expr()
            match("CBRACKET")

    def idDefPending():
        return check("ID")

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
    #          | ASSIGN
    def operator():
        if(check("EQUAL")):
            match("EQUAL")
        elif(check("NOTEQUAL")):
            match("NOTEQUAL")
        elif(check("GREATER")):
            match("GREATER")
        elif(check("LESS")):
            match("LESS")
        elif(check("GREATEREQUAL")):
            match("GREATEREQUAL")
        elif(check("LESSEQUAL")):
            match("LESSEQUAL")
        elif(check("PLUS")):
            match("PLUS")
        elif(check("MINUS")):
            match("MINUS")
        elif(check("MULTIPLY")):
            match("MULTIPLY")
        elif(check("DIVIDE")):
            match("DIVIDE")
        elif(check("POWER")):
            match("POWER")
        elif(check("AND")):
            match("AND")
        elif(check("OR")):
            match("OR")
        elif(check("ASSIGN")):
            match("ASSIGN")

    def operatorPending():
        return check("EQUAL") or check("NOTEQUAL") or check("GREATER") or check("LESS") or check("GREATEREQUAL") or check("LESSEQUAL") or check("PLUS") or check("MINUS") or check("MULTIPLY") or check("DIVIDE") or check("POWER") or check("AND") or check("OR") or check("ASSIGN")

    # block : OBRACE optStatementList CBRACE
    def block():
        match("OBRACE")
        optStatementList()
        match("CBRACE")

    def blockPending():
        return check("OBRACE")

    # optStatementList : EMPTY
    #                  | statementList
    def optStatementList():
        if (statementListPending()):
            statementList()

    # statementList : statement
    #               | statement statementList
    def statementList():
        statement()
        if(statementListPending()):
            statementList()

    def statementListPending():
        return statementPending()

    # statement : variableDefinition
    #           | functionDefinition
    #           | expr SEMI
    #           | whileLoop
    #           | ifStatement
    #           | RETURN expr SEMI
    def statement():
        if(variableDefinitionPending()):
            variableDefinition()
        elif(functionDefinitionPending()):
            functionDefinition()
        elif(exprPending()):
            expr()
            match("SEMI")
        elif(whileLoopPending()):
            whileLoop()
        elif(ifStatementPending()):
            ifStatement()
        elif(check("RETURN")):
            match("RETURN")
            expr()
            match("SEMI")

    def statementPending():
        return variableDefinitionPending() or functionDefinitionPending() or exprPending() or whileLoopPending() or ifStatementPending() or returnPending()

    # whileLoop : WHILE OPAREN expr CPAREN block
    def whileLoop():
        match("WHILE")
        match("OPAREN")
        expr()
        match("CPAREN")
        block()

    def whileLoopPending():
        return check("WHILE")

    # ifStatement : IF OPAREN expr CPAREN block optElseStatement
    def ifStatement():
        match("IF")
        match("OPAREN")
        expr()
        match("CPAREN")
        block()
        optElseStatement()

    def ifStatementPending():
        return check("IF")

    # optElseStatement : EMPTY
    #                  | elseStatement
    def optElseStatement():
        if (elseStatementPending()):
            elseStatement()

    # elseStatement : ELSE block
    #               | ELSE ifStatement
    def elseStatement():
        match("ELSE")
        if(blockPending()):
            block()
        elif(ifStatementPending()):
            ifStatement()

    def elseStatementPending():
        return check("ELSE")

    # k_lambda : LAMBDA OPAREN optParamList CPAREN block
    def k_lambda():
        match("LAMBDA")
        match("OPAREN")
        optParamList()
        match("CPAREN")
        block()