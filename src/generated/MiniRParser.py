# Generated from grammar/MiniR.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,47,243,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        3,2,70,8,2,1,3,1,3,1,3,1,3,3,3,76,8,3,1,4,1,4,1,4,1,4,1,4,4,4,83,
        8,4,11,4,12,4,84,1,4,3,4,88,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        97,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,5,11,130,8,11,10,11,12,11,133,9,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,3,15,153,8,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,3,17,166,8,17,1,17,1,17,3,17,170,8,17,1,18,1,18,1,18,5,
        18,175,8,18,10,18,12,18,178,9,18,1,18,3,18,181,8,18,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,5,20,190,8,20,10,20,12,20,193,9,20,1,21,1,
        21,1,21,5,21,198,8,21,10,21,12,21,201,9,21,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,3,22,211,8,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,219,8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,5,22,236,8,22,10,22,12,22,239,9,22,1,23,1,
        23,1,23,0,1,44,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,0,7,1,0,10,14,2,0,15,16,44,44,1,0,41,44,1,0,
        32,34,1,0,30,31,1,0,35,40,2,0,17,18,41,44,250,0,51,1,0,0,0,2,60,
        1,0,0,0,4,62,1,0,0,0,6,71,1,0,0,0,8,77,1,0,0,0,10,96,1,0,0,0,12,
        98,1,0,0,0,14,102,1,0,0,0,16,107,1,0,0,0,18,114,1,0,0,0,20,119,1,
        0,0,0,22,124,1,0,0,0,24,136,1,0,0,0,26,140,1,0,0,0,28,145,1,0,0,
        0,30,147,1,0,0,0,32,156,1,0,0,0,34,158,1,0,0,0,36,171,1,0,0,0,38,
        182,1,0,0,0,40,186,1,0,0,0,42,194,1,0,0,0,44,218,1,0,0,0,46,240,
        1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,
        51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,1,1,0,
        0,0,56,61,3,4,2,0,57,61,3,8,4,0,58,61,3,6,3,0,59,61,3,34,17,0,60,
        56,1,0,0,0,60,57,1,0,0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,3,1,0,0,
        0,62,63,5,41,0,0,63,64,5,22,0,0,64,65,5,1,0,0,65,66,5,26,0,0,66,
        67,5,44,0,0,67,69,5,27,0,0,68,70,5,24,0,0,69,68,1,0,0,0,69,70,1,
        0,0,0,70,5,1,0,0,0,71,72,5,41,0,0,72,73,5,22,0,0,73,75,3,44,22,0,
        74,76,5,24,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,7,1,0,0,0,77,78,5,
        41,0,0,78,79,5,22,0,0,79,80,5,41,0,0,80,82,5,23,0,0,81,83,3,10,5,
        0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,
        1,0,0,0,86,88,5,24,0,0,87,86,1,0,0,0,87,88,1,0,0,0,88,9,1,0,0,0,
        89,97,3,12,6,0,90,97,3,14,7,0,91,97,3,16,8,0,92,97,3,18,9,0,93,97,
        3,20,10,0,94,97,3,22,11,0,95,97,3,30,15,0,96,89,1,0,0,0,96,90,1,
        0,0,0,96,91,1,0,0,0,96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,96,
        95,1,0,0,0,97,11,1,0,0,0,98,99,5,2,0,0,99,100,5,26,0,0,100,101,5,
        27,0,0,101,13,1,0,0,0,102,103,5,3,0,0,103,104,5,26,0,0,104,105,3,
        44,22,0,105,106,5,27,0,0,106,15,1,0,0,0,107,108,5,4,0,0,108,109,
        5,26,0,0,109,110,5,41,0,0,110,111,5,22,0,0,111,112,3,44,22,0,112,
        113,5,27,0,0,113,17,1,0,0,0,114,115,5,5,0,0,115,116,5,26,0,0,116,
        117,3,40,20,0,117,118,5,27,0,0,118,19,1,0,0,0,119,120,5,6,0,0,120,
        121,5,26,0,0,121,122,3,40,20,0,122,123,5,27,0,0,123,21,1,0,0,0,124,
        125,5,7,0,0,125,126,5,26,0,0,126,131,3,24,12,0,127,128,5,25,0,0,
        128,130,3,24,12,0,129,127,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,
        0,131,132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,27,0,
        0,135,23,1,0,0,0,136,137,5,41,0,0,137,138,5,22,0,0,138,139,3,26,
        13,0,139,25,1,0,0,0,140,141,3,28,14,0,141,142,5,26,0,0,142,143,5,
        41,0,0,143,144,5,27,0,0,144,27,1,0,0,0,145,146,7,0,0,0,146,29,1,
        0,0,0,147,148,5,8,0,0,148,149,5,26,0,0,149,152,5,41,0,0,150,151,
        5,25,0,0,151,153,3,32,16,0,152,150,1,0,0,0,152,153,1,0,0,0,153,154,
        1,0,0,0,154,155,5,27,0,0,155,31,1,0,0,0,156,157,7,1,0,0,157,33,1,
        0,0,0,158,159,5,9,0,0,159,160,5,41,0,0,160,161,5,26,0,0,161,162,
        5,41,0,0,162,163,5,27,0,0,163,165,5,28,0,0,164,166,3,36,18,0,165,
        164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,169,5,29,0,0,168,
        170,5,24,0,0,169,168,1,0,0,0,169,170,1,0,0,0,170,35,1,0,0,0,171,
        176,3,38,19,0,172,173,5,25,0,0,173,175,3,38,19,0,174,172,1,0,0,0,
        175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,180,1,0,0,0,
        178,176,1,0,0,0,179,181,5,25,0,0,180,179,1,0,0,0,180,181,1,0,0,0,
        181,37,1,0,0,0,182,183,5,41,0,0,183,184,5,23,0,0,184,185,7,2,0,0,
        185,39,1,0,0,0,186,191,5,41,0,0,187,188,5,25,0,0,188,190,5,41,0,
        0,189,187,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,
        0,192,41,1,0,0,0,193,191,1,0,0,0,194,199,3,44,22,0,195,196,5,25,
        0,0,196,198,3,44,22,0,197,195,1,0,0,0,198,201,1,0,0,0,199,197,1,
        0,0,0,199,200,1,0,0,0,200,43,1,0,0,0,201,199,1,0,0,0,202,203,6,22,
        -1,0,203,204,5,21,0,0,204,219,3,44,22,10,205,206,5,31,0,0,206,219,
        3,44,22,9,207,208,5,41,0,0,208,210,5,26,0,0,209,211,3,42,21,0,210,
        209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,219,5,27,0,0,213,
        214,5,26,0,0,214,215,3,44,22,0,215,216,5,27,0,0,216,219,1,0,0,0,
        217,219,3,46,23,0,218,202,1,0,0,0,218,205,1,0,0,0,218,207,1,0,0,
        0,218,213,1,0,0,0,218,217,1,0,0,0,219,237,1,0,0,0,220,221,10,8,0,
        0,221,222,7,3,0,0,222,236,3,44,22,9,223,224,10,7,0,0,224,225,7,4,
        0,0,225,236,3,44,22,8,226,227,10,6,0,0,227,228,7,5,0,0,228,236,3,
        44,22,7,229,230,10,5,0,0,230,231,5,19,0,0,231,236,3,44,22,6,232,
        233,10,4,0,0,233,234,5,20,0,0,234,236,3,44,22,5,235,220,1,0,0,0,
        235,223,1,0,0,0,235,226,1,0,0,0,235,229,1,0,0,0,235,232,1,0,0,0,
        236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,0,0,238,45,1,0,0,0,239,
        237,1,0,0,0,240,241,7,6,0,0,241,47,1,0,0,0,19,51,60,69,75,84,87,
        96,131,152,165,169,176,180,191,199,210,218,235,237
    ]

class MiniRParser ( Parser ):

    grammarFileName = "MiniR.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'read'", "'dropna'", "'filter'", "'add'", 
                     "'select'", "'groupby'", "'summarize'", "'sort'", "'plot'", 
                     "'sum'", "'mean'", "'count'", "'max'", "'min'", "'asc'", 
                     "'desc'", "'true'", "'false'", "'and'", "'or'", "'not'", 
                     "'='", "':'", "';'", "','", "'('", "')'", "'{'", "'}'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", 
                     "'>='", "'<='", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "READ", "DROPNA", "FILTER", "ADD", "SELECT", 
                      "GROUPBY", "SUMMARIZE", "SORT", "PLOT", "SUM", "MEAN", 
                      "COUNT", "MAX", "MIN", "ASC", "DESC", "TRUE", "FALSE", 
                      "AND", "OR", "NOT", "ASSIGN", "COLON", "SEMI", "COMMA", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "PLUS", "MINUS", 
                      "MULT", "DIV", "MOD", "EQ", "NEQ", "GTE", "LTE", "GT", 
                      "LT", "ID", "INT", "FLOAT", "STRING", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_loadStmt = 2
    RULE_assignStmt = 3
    RULE_transformStmt = 4
    RULE_transformOp = 5
    RULE_dropnaOp = 6
    RULE_filterOp = 7
    RULE_addOp = 8
    RULE_selectOp = 9
    RULE_groupbyOp = 10
    RULE_summarizeOp = 11
    RULE_summarizeItem = 12
    RULE_aggCall = 13
    RULE_aggFunc = 14
    RULE_sortOp = 15
    RULE_sortOrder = 16
    RULE_plotStmt = 17
    RULE_plotPropertyList = 18
    RULE_plotProperty = 19
    RULE_idList = 20
    RULE_exprList = 21
    RULE_expr = 22
    RULE_primary = 23

    ruleNames =  [ "program", "statement", "loadStmt", "assignStmt", "transformStmt", 
                   "transformOp", "dropnaOp", "filterOp", "addOp", "selectOp", 
                   "groupbyOp", "summarizeOp", "summarizeItem", "aggCall", 
                   "aggFunc", "sortOp", "sortOrder", "plotStmt", "plotPropertyList", 
                   "plotProperty", "idList", "exprList", "expr", "primary" ]

    EOF = Token.EOF
    READ=1
    DROPNA=2
    FILTER=3
    ADD=4
    SELECT=5
    GROUPBY=6
    SUMMARIZE=7
    SORT=8
    PLOT=9
    SUM=10
    MEAN=11
    COUNT=12
    MAX=13
    MIN=14
    ASC=15
    DESC=16
    TRUE=17
    FALSE=18
    AND=19
    OR=20
    NOT=21
    ASSIGN=22
    COLON=23
    SEMI=24
    COMMA=25
    LPAREN=26
    RPAREN=27
    LBRACE=28
    RBRACE=29
    PLUS=30
    MINUS=31
    MULT=32
    DIV=33
    MOD=34
    EQ=35
    NEQ=36
    GTE=37
    LTE=38
    GT=39
    LT=40
    ID=41
    INT=42
    FLOAT=43
    STRING=44
    WS=45
    LINE_COMMENT=46
    BLOCK_COMMENT=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniRParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniRParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniRParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniRParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==41:
                self.state = 48
                self.statement()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(MiniRParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStmt(self):
            return self.getTypedRuleContext(MiniRParser.LoadStmtContext,0)


        def transformStmt(self):
            return self.getTypedRuleContext(MiniRParser.TransformStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(MiniRParser.AssignStmtContext,0)


        def plotStmt(self):
            return self.getTypedRuleContext(MiniRParser.PlotStmtContext,0)


        def getRuleIndex(self):
            return MiniRParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniRParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.loadStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.transformStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.assignStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.plotStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniRParser.ASSIGN, 0)

        def READ(self):
            return self.getToken(MiniRParser.READ, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def STRING(self):
            return self.getToken(MiniRParser.STRING, 0)

        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(MiniRParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_loadStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStmt" ):
                return visitor.visitLoadStmt(self)
            else:
                return visitor.visitChildren(self)




    def loadStmt(self):

        localctx = MiniRParser.LoadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(MiniRParser.ID)
            self.state = 63
            self.match(MiniRParser.ASSIGN)
            self.state = 64
            self.match(MiniRParser.READ)
            self.state = 65
            self.match(MiniRParser.LPAREN)
            self.state = 66
            self.match(MiniRParser.STRING)
            self.state = 67
            self.match(MiniRParser.RPAREN)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 68
                self.match(MiniRParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniRParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MiniRParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_assignStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MiniRParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(MiniRParser.ID)
            self.state = 72
            self.match(MiniRParser.ASSIGN)
            self.state = 73
            self.expr(0)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 74
                self.match(MiniRParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransformStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.ID)
            else:
                return self.getToken(MiniRParser.ID, i)

        def ASSIGN(self):
            return self.getToken(MiniRParser.ASSIGN, 0)

        def COLON(self):
            return self.getToken(MiniRParser.COLON, 0)

        def transformOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.TransformOpContext)
            else:
                return self.getTypedRuleContext(MiniRParser.TransformOpContext,i)


        def SEMI(self):
            return self.getToken(MiniRParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_transformStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransformStmt" ):
                return visitor.visitTransformStmt(self)
            else:
                return visitor.visitChildren(self)




    def transformStmt(self):

        localctx = MiniRParser.TransformStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_transformStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(MiniRParser.ID)
            self.state = 78
            self.match(MiniRParser.ASSIGN)
            self.state = 79
            self.match(MiniRParser.ID)
            self.state = 80
            self.match(MiniRParser.COLON)
            self.state = 82 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 81
                self.transformOp()
                self.state = 84 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 508) != 0)):
                    break

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 86
                self.match(MiniRParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransformOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dropnaOp(self):
            return self.getTypedRuleContext(MiniRParser.DropnaOpContext,0)


        def filterOp(self):
            return self.getTypedRuleContext(MiniRParser.FilterOpContext,0)


        def addOp(self):
            return self.getTypedRuleContext(MiniRParser.AddOpContext,0)


        def selectOp(self):
            return self.getTypedRuleContext(MiniRParser.SelectOpContext,0)


        def groupbyOp(self):
            return self.getTypedRuleContext(MiniRParser.GroupbyOpContext,0)


        def summarizeOp(self):
            return self.getTypedRuleContext(MiniRParser.SummarizeOpContext,0)


        def sortOp(self):
            return self.getTypedRuleContext(MiniRParser.SortOpContext,0)


        def getRuleIndex(self):
            return MiniRParser.RULE_transformOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTransformOp" ):
                return visitor.visitTransformOp(self)
            else:
                return visitor.visitChildren(self)




    def transformOp(self):

        localctx = MiniRParser.TransformOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_transformOp)
        try:
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.dropnaOp()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.filterOp()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.addOp()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.selectOp()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.groupbyOp()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.summarizeOp()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                self.sortOp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropnaOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DROPNA(self):
            return self.getToken(MiniRParser.DROPNA, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_dropnaOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropnaOp" ):
                return visitor.visitDropnaOp(self)
            else:
                return visitor.visitChildren(self)




    def dropnaOp(self):

        localctx = MiniRParser.DropnaOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dropnaOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(MiniRParser.DROPNA)
            self.state = 99
            self.match(MiniRParser.LPAREN)
            self.state = 100
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(MiniRParser.FILTER, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_filterOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterOp" ):
                return visitor.visitFilterOp(self)
            else:
                return visitor.visitChildren(self)




    def filterOp(self):

        localctx = MiniRParser.FilterOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_filterOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MiniRParser.FILTER)
            self.state = 103
            self.match(MiniRParser.LPAREN)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(MiniRParser.ADD, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniRParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniRParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_addOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = MiniRParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_addOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(MiniRParser.ADD)
            self.state = 108
            self.match(MiniRParser.LPAREN)
            self.state = 109
            self.match(MiniRParser.ID)
            self.state = 110
            self.match(MiniRParser.ASSIGN)
            self.state = 111
            self.expr(0)
            self.state = 112
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MiniRParser.SELECT, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def idList(self):
            return self.getTypedRuleContext(MiniRParser.IdListContext,0)


        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_selectOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectOp" ):
                return visitor.visitSelectOp(self)
            else:
                return visitor.visitChildren(self)




    def selectOp(self):

        localctx = MiniRParser.SelectOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_selectOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MiniRParser.SELECT)
            self.state = 115
            self.match(MiniRParser.LPAREN)
            self.state = 116
            self.idList()
            self.state = 117
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupbyOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUPBY(self):
            return self.getToken(MiniRParser.GROUPBY, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def idList(self):
            return self.getTypedRuleContext(MiniRParser.IdListContext,0)


        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_groupbyOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupbyOp" ):
                return visitor.visitGroupbyOp(self)
            else:
                return visitor.visitChildren(self)




    def groupbyOp(self):

        localctx = MiniRParser.GroupbyOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_groupbyOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MiniRParser.GROUPBY)
            self.state = 120
            self.match(MiniRParser.LPAREN)
            self.state = 121
            self.idList()
            self.state = 122
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummarizeOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMMARIZE(self):
            return self.getToken(MiniRParser.SUMMARIZE, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def summarizeItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.SummarizeItemContext)
            else:
                return self.getTypedRuleContext(MiniRParser.SummarizeItemContext,i)


        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.COMMA)
            else:
                return self.getToken(MiniRParser.COMMA, i)

        def getRuleIndex(self):
            return MiniRParser.RULE_summarizeOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummarizeOp" ):
                return visitor.visitSummarizeOp(self)
            else:
                return visitor.visitChildren(self)




    def summarizeOp(self):

        localctx = MiniRParser.SummarizeOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_summarizeOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(MiniRParser.SUMMARIZE)
            self.state = 125
            self.match(MiniRParser.LPAREN)
            self.state = 126
            self.summarizeItem()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 127
                self.match(MiniRParser.COMMA)
                self.state = 128
                self.summarizeItem()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummarizeItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniRParser.ASSIGN, 0)

        def aggCall(self):
            return self.getTypedRuleContext(MiniRParser.AggCallContext,0)


        def getRuleIndex(self):
            return MiniRParser.RULE_summarizeItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummarizeItem" ):
                return visitor.visitSummarizeItem(self)
            else:
                return visitor.visitChildren(self)




    def summarizeItem(self):

        localctx = MiniRParser.SummarizeItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_summarizeItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MiniRParser.ID)
            self.state = 137
            self.match(MiniRParser.ASSIGN)
            self.state = 138
            self.aggCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggFunc(self):
            return self.getTypedRuleContext(MiniRParser.AggFuncContext,0)


        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)

        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_aggCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggCall" ):
                return visitor.visitAggCall(self)
            else:
                return visitor.visitChildren(self)




    def aggCall(self):

        localctx = MiniRParser.AggCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_aggCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.aggFunc()
            self.state = 141
            self.match(MiniRParser.LPAREN)
            self.state = 142
            self.match(MiniRParser.ID)
            self.state = 143
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUM(self):
            return self.getToken(MiniRParser.SUM, 0)

        def MEAN(self):
            return self.getToken(MiniRParser.MEAN, 0)

        def COUNT(self):
            return self.getToken(MiniRParser.COUNT, 0)

        def MAX(self):
            return self.getToken(MiniRParser.MAX, 0)

        def MIN(self):
            return self.getToken(MiniRParser.MIN, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_aggFunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggFunc" ):
                return visitor.visitAggFunc(self)
            else:
                return visitor.visitChildren(self)




    def aggFunc(self):

        localctx = MiniRParser.AggFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_aggFunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SORT(self):
            return self.getToken(MiniRParser.SORT, 0)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)

        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def COMMA(self):
            return self.getToken(MiniRParser.COMMA, 0)

        def sortOrder(self):
            return self.getTypedRuleContext(MiniRParser.SortOrderContext,0)


        def getRuleIndex(self):
            return MiniRParser.RULE_sortOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortOp" ):
                return visitor.visitSortOp(self)
            else:
                return visitor.visitChildren(self)




    def sortOp(self):

        localctx = MiniRParser.SortOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_sortOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MiniRParser.SORT)
            self.state = 148
            self.match(MiniRParser.LPAREN)
            self.state = 149
            self.match(MiniRParser.ID)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 150
                self.match(MiniRParser.COMMA)
                self.state = 151
                self.sortOrder()


            self.state = 154
            self.match(MiniRParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SortOrderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniRParser.STRING, 0)

        def ASC(self):
            return self.getToken(MiniRParser.ASC, 0)

        def DESC(self):
            return self.getToken(MiniRParser.DESC, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_sortOrder

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSortOrder" ):
                return visitor.visitSortOrder(self)
            else:
                return visitor.visitChildren(self)




    def sortOrder(self):

        localctx = MiniRParser.SortOrderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sortOrder)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17592186142720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOT(self):
            return self.getToken(MiniRParser.PLOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.ID)
            else:
                return self.getToken(MiniRParser.ID, i)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniRParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniRParser.RBRACE, 0)

        def plotPropertyList(self):
            return self.getTypedRuleContext(MiniRParser.PlotPropertyListContext,0)


        def SEMI(self):
            return self.getToken(MiniRParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_plotStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlotStmt" ):
                return visitor.visitPlotStmt(self)
            else:
                return visitor.visitChildren(self)




    def plotStmt(self):

        localctx = MiniRParser.PlotStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_plotStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MiniRParser.PLOT)
            self.state = 159
            self.match(MiniRParser.ID)
            self.state = 160
            self.match(MiniRParser.LPAREN)
            self.state = 161
            self.match(MiniRParser.ID)
            self.state = 162
            self.match(MiniRParser.RPAREN)
            self.state = 163
            self.match(MiniRParser.LBRACE)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 164
                self.plotPropertyList()


            self.state = 167
            self.match(MiniRParser.RBRACE)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 168
                self.match(MiniRParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotPropertyListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def plotProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.PlotPropertyContext)
            else:
                return self.getTypedRuleContext(MiniRParser.PlotPropertyContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.COMMA)
            else:
                return self.getToken(MiniRParser.COMMA, i)

        def getRuleIndex(self):
            return MiniRParser.RULE_plotPropertyList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlotPropertyList" ):
                return visitor.visitPlotPropertyList(self)
            else:
                return visitor.visitChildren(self)




    def plotPropertyList(self):

        localctx = MiniRParser.PlotPropertyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_plotPropertyList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.plotProperty()
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self.match(MiniRParser.COMMA)
                    self.state = 173
                    self.plotProperty() 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 179
                self.match(MiniRParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.ID)
            else:
                return self.getToken(MiniRParser.ID, i)

        def COLON(self):
            return self.getToken(MiniRParser.COLON, 0)

        def STRING(self):
            return self.getToken(MiniRParser.STRING, 0)

        def INT(self):
            return self.getToken(MiniRParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniRParser.FLOAT, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_plotProperty

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlotProperty" ):
                return visitor.visitPlotProperty(self)
            else:
                return visitor.visitChildren(self)




    def plotProperty(self):

        localctx = MiniRParser.PlotPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_plotProperty)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MiniRParser.ID)
            self.state = 183
            self.match(MiniRParser.COLON)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32985348833280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.ID)
            else:
                return self.getToken(MiniRParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.COMMA)
            else:
                return self.getToken(MiniRParser.COMMA, i)

        def getRuleIndex(self):
            return MiniRParser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = MiniRParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(MiniRParser.ID)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 187
                self.match(MiniRParser.COMMA)
                self.state = 188
                self.match(MiniRParser.ID)
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniRParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniRParser.COMMA)
            else:
                return self.getToken(MiniRParser.COMMA, i)

        def getRuleIndex(self):
            return MiniRParser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = MiniRParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expr(0)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 195
                self.match(MiniRParser.COMMA)
                self.state = 196
                self.expr(0)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniRParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniRParser.ExprContext,i)

        def AND(self):
            return self.getToken(MiniRParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniRParser.ExprContext,i)

        def MULT(self):
            return self.getToken(MiniRParser.MULT, 0)
        def DIV(self):
            return self.getToken(MiniRParser.DIV, 0)
        def MOD(self):
            return self.getToken(MiniRParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MiniRParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniRParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniRParser.ExprContext,i)

        def EQ(self):
            return self.getToken(MiniRParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MiniRParser.NEQ, 0)
        def LT(self):
            return self.getToken(MiniRParser.LT, 0)
        def LTE(self):
            return self.getToken(MiniRParser.LTE, 0)
        def GT(self):
            return self.getToken(MiniRParser.GT, 0)
        def GTE(self):
            return self.getToken(MiniRParser.GTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpr" ):
                return visitor.visitRelationalExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniRParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary(self):
            return self.getTypedRuleContext(MiniRParser.PrimaryContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniRParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(MiniRParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(MiniRParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniRParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniRParser.ExprContext,i)

        def OR(self):
            return self.getToken(MiniRParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(MiniRParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniRParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniRParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MiniRParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniRParser.RPAREN, 0)
        def exprList(self):
            return self.getTypedRuleContext(MiniRParser.ExprListContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniRParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = MiniRParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 203
                self.match(MiniRParser.NOT)
                self.state = 204
                self.expr(10)
                pass

            elif la_ == 2:
                localctx = MiniRParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                self.match(MiniRParser.MINUS)
                self.state = 206
                self.expr(9)
                pass

            elif la_ == 3:
                localctx = MiniRParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                self.match(MiniRParser.ID)
                self.state = 208
                self.match(MiniRParser.LPAREN)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32987565916160) != 0):
                    self.state = 209
                    self.exprList()


                self.state = 212
                self.match(MiniRParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = MiniRParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 213
                self.match(MiniRParser.LPAREN)
                self.state = 214
                self.expr(0)
                self.state = 215
                self.match(MiniRParser.RPAREN)
                pass

            elif la_ == 5:
                localctx = MiniRParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 217
                self.primary()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 235
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = MiniRParser.MulDivExprContext(self, MiniRParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 220
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 221
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 222
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = MiniRParser.AddSubExprContext(self, MiniRParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 223
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 224
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 225
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = MiniRParser.RelationalExprContext(self, MiniRParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 226
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 228
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = MiniRParser.AndExprContext(self, MiniRParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 229
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 230
                        self.match(MiniRParser.AND)
                        self.state = 231
                        self.expr(6)
                        pass

                    elif la_ == 5:
                        localctx = MiniRParser.OrExprContext(self, MiniRParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 232
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 233
                        self.match(MiniRParser.OR)
                        self.state = 234
                        self.expr(5)
                        pass

             
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniRParser.ID, 0)

        def INT(self):
            return self.getToken(MiniRParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniRParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniRParser.STRING, 0)

        def TRUE(self):
            return self.getToken(MiniRParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniRParser.FALSE, 0)

        def getRuleIndex(self):
            return MiniRParser.RULE_primary

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MiniRParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_primary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32985349226496) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         




