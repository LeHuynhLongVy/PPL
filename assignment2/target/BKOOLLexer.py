# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("\66\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\b\6\b+\n\b\r\b\16\b,\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\4")
        buf.write("\4\2C\\c|\5\2\f\f\17\17\"\"\2\66\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\31")
        buf.write("\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r\'\3\2\2")
        buf.write("\2\17*\3\2\2\2\21.\3\2\2\2\23\62\3\2\2\2\25\26\7k\2\2")
        buf.write("\26\27\7p\2\2\27\30\7v\2\2\30\4\3\2\2\2\31\32\7h\2\2\32")
        buf.write("\33\7n\2\2\33\34\7q\2\2\34\35\7c\2\2\35\36\7v\2\2\36\6")
        buf.write("\3\2\2\2\37 \7B\2\2 \b\3\2\2\2!\"\7.\2\2\"\n\3\2\2\2#")
        buf.write("$\7u\2\2$%\7{\2\2%&\7o\2\2&\f\3\2\2\2\'(\7=\2\2(\16\3")
        buf.write("\2\2\2)+\t\2\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2")
        buf.write("\2-\20\3\2\2\2./\7\60\2\2/\60\7\60\2\2\60\61\7\60\2\2")
        buf.write("\61\22\3\2\2\2\62\63\t\3\2\2\63\64\3\2\2\2\64\65\b\n\2")
        buf.write("\2\65\24\3\2\2\2\4\2,\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    AT = 3
    CM = 4
    SYM = 5
    SM = 6
    ID = 7
    TDOTS = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'@'", "','", "'sym'", "';'", "'...'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "AT", "CM", "SYM", "SM", "ID", "TDOTS", "WS" ]

    ruleNames = [ "INT", "FLOAT", "AT", "CM", "SYM", "SM", "ID", "TDOTS", 
                  "WS" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


