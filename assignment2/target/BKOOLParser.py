# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write(")\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\7\4\35\n\4\f\4\16\4 \13\4\3\5\3\5\3\5\5\5%\n\5\3")
        buf.write("\6\3\6\3\6\2\2\7\2\4\6\b\n\2\3\3\2\3\4\2&\2\r\3\2\2\2")
        buf.write("\4\23\3\2\2\2\6\31\3\2\2\2\b$\3\2\2\2\n&\3\2\2\2\f\16")
        buf.write("\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20")
        buf.write("\3\2\2\2\20\21\3\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24")
        buf.write("\7\7\2\2\24\25\5\6\4\2\25\26\7\5\2\2\26\27\5\n\6\2\27")
        buf.write("\30\7\b\2\2\30\5\3\2\2\2\31\36\5\b\5\2\32\33\7\6\2\2\33")
        buf.write("\35\5\b\5\2\34\32\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36")
        buf.write("\37\3\2\2\2\37\7\3\2\2\2 \36\3\2\2\2!%\7\t\2\2\"#\7\n")
        buf.write("\2\2#%\7\t\2\2$!\3\2\2\2$\"\3\2\2\2%\t\3\2\2\2&\'\t\2")
        buf.write("\2\2\'\13\3\2\2\2\5\17\36$")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'@'", "','", "'sym'", 
                     "';'", "<INVALID>", "'...'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "AT", "CM", "SYM", "SM", 
                      "ID", "TDOTS", "WS" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_decl = 2
    RULE_var = 3
    RULE_typ = 4

    ruleNames =  [ "program", "decls", "decl", "var", "typ" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    AT=3
    CM=4
    SYM=5
    SM=6
    ID=7
    TDOTS=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.DeclsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.DeclsContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.decls()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.SYM):
                    break

            self.state = 15
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYM(self):
            return self.getToken(BKOOLParser.SYM, 0)

        def decl(self):
            return self.getTypedRuleContext(BKOOLParser.DeclContext,0)


        def AT(self):
            return self.getToken(BKOOLParser.AT, 0)

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = BKOOLParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(BKOOLParser.SYM)
            self.state = 18
            self.decl()
            self.state = 19
            self.match(BKOOLParser.AT)
            self.state = 20
            self.typ()
            self.state = 21
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VarContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VarContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.CM)
            else:
                return self.getToken(BKOOLParser.CM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.var()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.CM:
                self.state = 24
                self.match(BKOOLParser.CM)
                self.state = 25
                self.var()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def TDOTS(self):
            return self.getToken(BKOOLParser.TDOTS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = BKOOLParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.state = 31
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.TDOTS]:
                self.state = 32
                self.match(BKOOLParser.TDOTS)
                self.state = 33
                self.match(BKOOLParser.ID)
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


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
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





