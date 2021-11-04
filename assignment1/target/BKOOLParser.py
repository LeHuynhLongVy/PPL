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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u01d9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\3\2\6\2j\n\2\r\2\16\2k\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3v\n\3\3\4\3\4\3\5\3\5\3\5\3\5\5\5~\n\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\5\6\u0088\n\6\3\7\3\7\3\7\3\7\5")
        buf.write("\7\u008e\n\7\3\b\3\b\3\b\5\b\u0093\n\b\3\t\5\t\u0096\n")
        buf.write("\t\3\t\5\t\u0099\n\t\3\t\5\t\u009c\n\t\3\t\5\t\u009f\n")
        buf.write("\t\5\t\u00a1\n\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00aa")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00b2\n\13\3\13")
        buf.write("\3\13\5\13\u00b6\n\13\3\f\5\f\u00b9\n\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00c6\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00cd\n\16\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00dd\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25")
        buf.write("\u00f1\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00f8\n\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\7\27\u0100\n\27\f\27\16\27")
        buf.write("\u0103\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u010b")
        buf.write("\n\30\f\30\16\30\u010e\13\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u0116\n\31\f\31\16\31\u0119\13\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u0121\n\32\f\32\16\32\u0124")
        buf.write("\13\32\3\33\3\33\3\33\5\33\u0129\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u012e\n\34\3\35\3\35\3\35\3\35\3\35\7\35\u0135\n\35")
        buf.write("\f\35\16\35\u0138\13\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u0144\n\36\7\36\u0146\n\36\f")
        buf.write("\36\16\36\u0149\13\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u0152\n\37\3 \3 \3 \3 \3 \3 \3 \5 \u015b\n \3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0165\n\"\3#\3#\3#\3#\3")
        buf.write("#\5#\u016c\n#\3$\3$\3$\3$\3$\3%\3%\3%\3%\5%\u0177\n%\3")
        buf.write("&\3&\3&\3&\5&\u017d\n&\3\'\3\'\3\'\3\'\5\'\u0183\n\'\3")
        buf.write("(\3(\3(\3(\5(\u0189\n(\3)\5)\u018c\n)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\5*\u019a\n*\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(",\3,\3,\3,\5,\u01a7\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u01c8\n")
        buf.write("\62\f\62\16\62\u01cb\13\62\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\3\63\5\63\u01d5\n\63\3\64\3\64\3\64\2\b,.\60")
        buf.write("\628:\65\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdf\2\n\7\2\13\13")
        buf.write("\22\22\24\24\26\26\34\34\6\2\13\13\22\22\24\24\26\26\3")
        buf.write("\2+.\3\2)*\3\2/\60\3\2#$\3\2%(\3\2!\"\2\u01e4\2i\3\2\2")
        buf.write("\2\4u\3\2\2\2\6w\3\2\2\2\by\3\2\2\2\n\u0087\3\2\2\2\f")
        buf.write("\u008d\3\2\2\2\16\u0092\3\2\2\2\20\u00a0\3\2\2\2\22\u00a6")
        buf.write("\3\2\2\2\24\u00b5\3\2\2\2\26\u00b8\3\2\2\2\30\u00c5\3")
        buf.write("\2\2\2\32\u00cc\3\2\2\2\34\u00ce\3\2\2\2\36\u00d1\3\2")
        buf.write("\2\2 \u00dc\3\2\2\2\"\u00de\3\2\2\2$\u00e4\3\2\2\2&\u00e6")
        buf.write("\3\2\2\2(\u00f0\3\2\2\2*\u00f7\3\2\2\2,\u00f9\3\2\2\2")
        buf.write(".\u0104\3\2\2\2\60\u010f\3\2\2\2\62\u011a\3\2\2\2\64\u0128")
        buf.write("\3\2\2\2\66\u012d\3\2\2\28\u012f\3\2\2\2:\u0139\3\2\2")
        buf.write("\2<\u0151\3\2\2\2>\u015a\3\2\2\2@\u015c\3\2\2\2B\u0164")
        buf.write("\3\2\2\2D\u016b\3\2\2\2F\u016d\3\2\2\2H\u0176\3\2\2\2")
        buf.write("J\u017c\3\2\2\2L\u0182\3\2\2\2N\u0188\3\2\2\2P\u018b\3")
        buf.write("\2\2\2R\u0199\3\2\2\2T\u019b\3\2\2\2V\u01a0\3\2\2\2X\u01a8")
        buf.write("\3\2\2\2Z\u01b1\3\2\2\2\\\u01b4\3\2\2\2^\u01b7\3\2\2\2")
        buf.write("`\u01bb\3\2\2\2b\u01c3\3\2\2\2d\u01d4\3\2\2\2f\u01d6\3")
        buf.write("\2\2\2hj\5\b\5\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2\2")
        buf.write("\2lm\3\2\2\2mn\7\2\2\3n\3\3\2\2\2ov\7\24\2\2pv\7\22\2")
        buf.write("\2qv\7\13\2\2rv\7\26\2\2sv\5&\24\2tv\5\6\4\2uo\3\2\2\2")
        buf.write("up\3\2\2\2uq\3\2\2\2ur\3\2\2\2us\3\2\2\2ut\3\2\2\2v\5")
        buf.write("\3\2\2\2wx\7=\2\2x\7\3\2\2\2yz\7\r\2\2z}\7=\2\2{|\7\21")
        buf.write("\2\2|~\7=\2\2}{\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\7\65\2\2\u0080\u0081\5\n\6\2\u0081\u0082\7\66\2\2\u0082")
        buf.write("\t\3\2\2\2\u0083\u0084\5\16\b\2\u0084\u0085\5\f\7\2\u0085")
        buf.write("\u0088\3\2\2\2\u0086\u0088\3\2\2\2\u0087\u0083\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\13\3\2\2\2\u0089\u008a\5\16")
        buf.write("\b\2\u008a\u008b\5\f\7\2\u008b\u008e\3\2\2\2\u008c\u008e")
        buf.write("\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008c\3\2\2\2\u008e")
        buf.write("\r\3\2\2\2\u008f\u0093\5\26\f\2\u0090\u0093\5\20\t\2\u0091")
        buf.write("\u0093\5\"\22\2\u0092\u008f\3\2\2\2\u0092\u0090\3\2\2")
        buf.write("\2\u0092\u0091\3\2\2\2\u0093\17\3\2\2\2\u0094\u0096\7")
        buf.write(" \2\2\u0095\u0094\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098")
        buf.write("\3\2\2\2\u0097\u0099\7\37\2\2\u0098\u0097\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u00a1\3\2\2\2\u009a\u009c\7\37\2")
        buf.write("\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009e")
        buf.write("\3\2\2\2\u009d\u009f\7 \2\2\u009e\u009d\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u0095\3\2\2\2")
        buf.write("\u00a0\u009b\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\5")
        buf.write("\4\3\2\u00a3\u00a4\5\22\n\2\u00a4\u00a5\79\2\2\u00a5\21")
        buf.write("\3\2\2\2\u00a6\u00a9\7=\2\2\u00a7\u00a8\7\3\2\2\u00a8")
        buf.write("\u00aa\5(\25\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ab\3\2\2\2\u00ab\u00ac\5\24\13\2\u00ac\23\3")
        buf.write("\2\2\2\u00ad\u00ae\7<\2\2\u00ae\u00b1\7=\2\2\u00af\u00b0")
        buf.write("\7\3\2\2\u00b0\u00b2\5(\25\2\u00b1\u00af\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b6\5\24\13")
        buf.write("\2\u00b4\u00b6\3\2\2\2\u00b5\u00ad\3\2\2\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b6\25\3\2\2\2\u00b7\u00b9\7 \2\2\u00b8\u00b7")
        buf.write("\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bb\5$\23\2\u00bb\u00bc\7=\2\2\u00bc\u00bd\7\67\2\2")
        buf.write("\u00bd\u00be\5\30\r\2\u00be\u00bf\78\2\2\u00bf\u00c0\5")
        buf.write("F$\2\u00c0\27\3\2\2\2\u00c1\u00c2\5\34\17\2\u00c2\u00c3")
        buf.write("\5\32\16\2\u00c3\u00c6\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5")
        buf.write("\u00c1\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\31\3\2\2\2\u00c7")
        buf.write("\u00c8\79\2\2\u00c8\u00c9\5\34\17\2\u00c9\u00ca\5\32\16")
        buf.write("\2\u00ca\u00cd\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00c7")
        buf.write("\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd\33\3\2\2\2\u00ce\u00cf")
        buf.write("\5\4\3\2\u00cf\u00d0\5\36\20\2\u00d0\35\3\2\2\2\u00d1")
        buf.write("\u00d2\7=\2\2\u00d2\u00d3\5 \21\2\u00d3\37\3\2\2\2\u00d4")
        buf.write("\u00d5\7<\2\2\u00d5\u00d6\7=\2\2\u00d6\u00dd\5 \21\2\u00d7")
        buf.write("\u00d8\79\2\2\u00d8\u00d9\5\34\17\2\u00d9\u00da\5 \21")
        buf.write("\2\u00da\u00dd\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00d4")
        buf.write("\3\2\2\2\u00dc\u00d7\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("!\3\2\2\2\u00de\u00df\7=\2\2\u00df\u00e0\7\67\2\2\u00e0")
        buf.write("\u00e1\5\30\r\2\u00e1\u00e2\78\2\2\u00e2\u00e3\5F$\2\u00e3")
        buf.write("#\3\2\2\2\u00e4\u00e5\t\2\2\2\u00e5%\3\2\2\2\u00e6\u00e7")
        buf.write("\t\3\2\2\u00e7\u00e8\7\63\2\2\u00e8\u00e9\7\7\2\2\u00e9")
        buf.write("\u00ea\7\64\2\2\u00ea\'\3\2\2\2\u00eb\u00ec\5*\26\2\u00ec")
        buf.write("\u00ed\t\4\2\2\u00ed\u00ee\5*\26\2\u00ee\u00f1\3\2\2\2")
        buf.write("\u00ef\u00f1\5*\26\2\u00f0\u00eb\3\2\2\2\u00f0\u00ef\3")
        buf.write("\2\2\2\u00f1)\3\2\2\2\u00f2\u00f3\5,\27\2\u00f3\u00f4")
        buf.write("\t\5\2\2\u00f4\u00f5\5,\27\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f8\5,\27\2\u00f7\u00f2\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8+\3\2\2\2\u00f9\u00fa\b\27\1\2\u00fa\u00fb\5.\30")
        buf.write("\2\u00fb\u0101\3\2\2\2\u00fc\u00fd\f\4\2\2\u00fd\u00fe")
        buf.write("\t\6\2\2\u00fe\u0100\5.\30\2\u00ff\u00fc\3\2\2\2\u0100")
        buf.write("\u0103\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102-\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0105\b\30\1")
        buf.write("\2\u0105\u0106\5\60\31\2\u0106\u010c\3\2\2\2\u0107\u0108")
        buf.write("\f\4\2\2\u0108\u0109\t\7\2\2\u0109\u010b\5\60\31\2\u010a")
        buf.write("\u0107\3\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2")
        buf.write("\u010c\u010d\3\2\2\2\u010d/\3\2\2\2\u010e\u010c\3\2\2")
        buf.write("\2\u010f\u0110\b\31\1\2\u0110\u0111\5\62\32\2\u0111\u0117")
        buf.write("\3\2\2\2\u0112\u0113\f\4\2\2\u0113\u0114\t\b\2\2\u0114")
        buf.write("\u0116\5\62\32\2\u0115\u0112\3\2\2\2\u0116\u0119\3\2\2")
        buf.write("\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\61\3")
        buf.write("\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\b\32\1\2\u011b")
        buf.write("\u011c\5\64\33\2\u011c\u0122\3\2\2\2\u011d\u011e\f\4\2")
        buf.write("\2\u011e\u011f\7\62\2\2\u011f\u0121\5\64\33\2\u0120\u011d")
        buf.write("\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\63\3\2\2\2\u0124\u0122\3\2\2\2\u0125")
        buf.write("\u0126\7\61\2\2\u0126\u0129\5\64\33\2\u0127\u0129\5\66")
        buf.write("\34\2\u0128\u0125\3\2\2\2\u0128\u0127\3\2\2\2\u0129\65")
        buf.write("\3\2\2\2\u012a\u012b\t\7\2\2\u012b\u012e\5\66\34\2\u012c")
        buf.write("\u012e\58\35\2\u012d\u012a\3\2\2\2\u012d\u012c\3\2\2\2")
        buf.write("\u012e\67\3\2\2\2\u012f\u0130\b\35\1\2\u0130\u0131\5:")
        buf.write("\36\2\u0131\u0136\3\2\2\2\u0132\u0133\f\4\2\2\u0133\u0135")
        buf.write("\5@!\2\u0134\u0132\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u01379\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0139\u013a\b\36\1\2\u013a\u013b\5<\37\2\u013b")
        buf.write("\u0147\3\2\2\2\u013c\u013d\f\4\2\2\u013d\u013e\7;\2\2")
        buf.write("\u013e\u0143\7=\2\2\u013f\u0140\7\67\2\2\u0140\u0141\5")
        buf.write("B\"\2\u0141\u0142\78\2\2\u0142\u0144\3\2\2\2\u0143\u013f")
        buf.write("\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145")
        buf.write("\u013c\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148;\3\2\2\2\u0149\u0147\3\2\2")
        buf.write("\2\u014a\u014b\7\25\2\2\u014b\u014c\5<\37\2\u014c\u014d")
        buf.write("\7\67\2\2\u014d\u014e\5B\"\2\u014e\u014f\78\2\2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u0152\5> \2\u0151\u014a\3\2\2\2\u0151")
        buf.write("\u0150\3\2\2\2\u0152=\3\2\2\2\u0153\u015b\7\7\2\2\u0154")
        buf.write("\u015b\7\b\2\2\u0155\u015b\7\t\2\2\u0156\u015b\7\n\2\2")
        buf.write("\u0157\u015b\5b\62\2\u0158\u015b\7=\2\2\u0159\u015b\7")
        buf.write("\36\2\2\u015a\u0153\3\2\2\2\u015a\u0154\3\2\2\2\u015a")
        buf.write("\u0155\3\2\2\2\u015a\u0156\3\2\2\2\u015a\u0157\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015b?\3\2\2")
        buf.write("\2\u015c\u015d\7\63\2\2\u015d\u015e\5(\25\2\u015e\u015f")
        buf.write("\7\64\2\2\u015fA\3\2\2\2\u0160\u0161\5(\25\2\u0161\u0162")
        buf.write("\5D#\2\u0162\u0165\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0160")
        buf.write("\3\2\2\2\u0164\u0163\3\2\2\2\u0165C\3\2\2\2\u0166\u0167")
        buf.write("\7<\2\2\u0167\u0168\5(\25\2\u0168\u0169\5D#\2\u0169\u016c")
        buf.write("\3\2\2\2\u016a\u016c\3\2\2\2\u016b\u0166\3\2\2\2\u016b")
        buf.write("\u016a\3\2\2\2\u016cE\3\2\2\2\u016d\u016e\7\65\2\2\u016e")
        buf.write("\u016f\5H%\2\u016f\u0170\5L\'\2\u0170\u0171\7\66\2\2\u0171")
        buf.write("G\3\2\2\2\u0172\u0173\5P)\2\u0173\u0174\5J&\2\u0174\u0177")
        buf.write("\3\2\2\2\u0175\u0177\3\2\2\2\u0176\u0172\3\2\2\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177I\3\2\2\2\u0178\u0179\5P)\2\u0179")
        buf.write("\u017a\5J&\2\u017a\u017d\3\2\2\2\u017b\u017d\3\2\2\2\u017c")
        buf.write("\u0178\3\2\2\2\u017c\u017b\3\2\2\2\u017dK\3\2\2\2\u017e")
        buf.write("\u017f\5R*\2\u017f\u0180\5N(\2\u0180\u0183\3\2\2\2\u0181")
        buf.write("\u0183\3\2\2\2\u0182\u017e\3\2\2\2\u0182\u0181\3\2\2\2")
        buf.write("\u0183M\3\2\2\2\u0184\u0185\5R*\2\u0185\u0186\5N(\2\u0186")
        buf.write("\u0189\3\2\2\2\u0187\u0189\3\2\2\2\u0188\u0184\3\2\2\2")
        buf.write("\u0188\u0187\3\2\2\2\u0189O\3\2\2\2\u018a\u018c\7\37\2")
        buf.write("\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d")
        buf.write("\3\2\2\2\u018d\u018e\5\4\3\2\u018e\u018f\5\22\n\2\u018f")
        buf.write("\u0190\79\2\2\u0190Q\3\2\2\2\u0191\u019a\5F$\2\u0192\u019a")
        buf.write("\5T+\2\u0193\u019a\5V,\2\u0194\u019a\5X-\2\u0195\u019a")
        buf.write("\5Z.\2\u0196\u019a\5\\/\2\u0197\u019a\5^\60\2\u0198\u019a")
        buf.write("\5`\61\2\u0199\u0191\3\2\2\2\u0199\u0192\3\2\2\2\u0199")
        buf.write("\u0193\3\2\2\2\u0199\u0194\3\2\2\2\u0199\u0195\3\2\2\2")
        buf.write("\u0199\u0196\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u0198\3")
        buf.write("\2\2\2\u019aS\3\2\2\2\u019b\u019c\5(\25\2\u019c\u019d")
        buf.write("\7\4\2\2\u019d\u019e\5(\25\2\u019e\u019f\79\2\2\u019f")
        buf.write("U\3\2\2\2\u01a0\u01a1\7\23\2\2\u01a1\u01a2\5(\25\2\u01a2")
        buf.write("\u01a3\7\27\2\2\u01a3\u01a6\5R*\2\u01a4\u01a5\7\20\2\2")
        buf.write("\u01a5\u01a7\5R*\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2")
        buf.write("\2\2\u01a7W\3\2\2\2\u01a8\u01a9\7\30\2\2\u01a9\u01aa\7")
        buf.write("=\2\2\u01aa\u01ab\7\4\2\2\u01ab\u01ac\5(\25\2\u01ac\u01ad")
        buf.write("\t\t\2\2\u01ad\u01ae\5(\25\2\u01ae\u01af\7\17\2\2\u01af")
        buf.write("\u01b0\5R*\2\u01b0Y\3\2\2\2\u01b1\u01b2\7\f\2\2\u01b2")
        buf.write("\u01b3\79\2\2\u01b3[\3\2\2\2\u01b4\u01b5\7\16\2\2\u01b5")
        buf.write("\u01b6\79\2\2\u01b6]\3\2\2\2\u01b7\u01b8\7\31\2\2\u01b8")
        buf.write("\u01b9\5(\25\2\u01b9\u01ba\79\2\2\u01ba_\3\2\2\2\u01bb")
        buf.write("\u01bc\5(\25\2\u01bc\u01bd\7;\2\2\u01bd\u01be\7=\2\2\u01be")
        buf.write("\u01bf\7\67\2\2\u01bf\u01c0\5B\"\2\u01c0\u01c1\78\2\2")
        buf.write("\u01c1\u01c2\79\2\2\u01c2a\3\2\2\2\u01c3\u01c4\7\65\2")
        buf.write("\2\u01c4\u01c9\5d\63\2\u01c5\u01c6\7<\2\2\u01c6\u01c8")
        buf.write("\5d\63\2\u01c7\u01c5\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cc\u01cd\7\66\2\2\u01cdc\3\2\2")
        buf.write("\2\u01ce\u01d5\7\7\2\2\u01cf\u01d5\7\b\2\2\u01d0\u01d5")
        buf.write("\7\t\2\2\u01d1\u01d5\7\n\2\2\u01d2\u01d5\5f\64\2\u01d3")
        buf.write("\u01d5\5b\62\2\u01d4\u01ce\3\2\2\2\u01d4\u01cf\3\2\2\2")
        buf.write("\u01d4\u01d0\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d4\u01d3\3\2\2\2\u01d5e\3\2\2\2\u01d6\u01d7")
        buf.write("\7\35\2\2\u01d7g\3\2\2\2,ku}\u0087\u008d\u0092\u0095\u0098")
        buf.write("\u009b\u009e\u00a0\u00a9\u00b1\u00b5\u00b8\u00c5\u00cc")
        buf.write("\u00dc\u00f0\u00f7\u0101\u010c\u0117\u0122\u0128\u012d")
        buf.write("\u0136\u0143\u0147\u0151\u015a\u0164\u016b\u0176\u017c")
        buf.write("\u0182\u0188\u018b\u0199\u01a6\u01c9\u01d4")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "':='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'boolean'", "'break'", "'class'", "'continue'", "'do'", 
                     "'else'", "'extends'", "'float'", "'if'", "'int'", 
                     "'new'", "'string'", "'then'", "'for'", "'return'", 
                     "'true'", "'false'", "'void'", "'nil'", "'this'", "'final'", 
                     "'static'", "'to'", "'downto'", "'+'", "'-'", "'*'", 
                     "'/'", "'\\'", "'%'", "'!='", "'=='", "'<'", "'>'", 
                     "'<='", "'>='", "'||'", "'&&'", "'!'", "'^'", "'['", 
                     "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", "'.'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "ASM", "GAN", "BCOMMENT", "LCOMMENT", 
                      "INTLIT", "FLOATLIT", "BOOLIT", "STRINGLIT", "BOOLEAN", 
                      "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", "EXTENDS", 
                      "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", "FOR", 
                      "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                      "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", 
                      "FDIV", "IDIV", "MOD", "NEQ", "EQ", "LESS", "GREATER", 
                      "LESSOE", "GREATEROE", "OR", "AND", "NOT", "CONCAT", 
                      "LSB", "RSB", "LCP", "RCP", "LB", "RB", "SMCOLON", 
                      "COLON", "DOT", "COMMA", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_typ = 1
    RULE_classtype = 2
    RULE_classdecl = 3
    RULE_memberlist = 4
    RULE_nextmember = 5
    RULE_member = 6
    RULE_attributedecl = 7
    RULE_attnamelist = 8
    RULE_nextattributename = 9
    RULE_methoddecl = 10
    RULE_paralist = 11
    RULE_nextparadecl = 12
    RULE_paradecl = 13
    RULE_idlist = 14
    RULE_nextid = 15
    RULE_constructor = 16
    RULE_primitivetype = 17
    RULE_arraytype = 18
    RULE_exp = 19
    RULE_exp1 = 20
    RULE_exp2 = 21
    RULE_exp3 = 22
    RULE_exp4 = 23
    RULE_exp5 = 24
    RULE_exp6 = 25
    RULE_exp7 = 26
    RULE_exp8 = 27
    RULE_exp9 = 28
    RULE_exp10 = 29
    RULE_operand = 30
    RULE_index_op = 31
    RULE_explist = 32
    RULE_nextexp = 33
    RULE_blockstmt = 34
    RULE_vardecllist = 35
    RULE_nextvardec = 36
    RULE_stmtlist = 37
    RULE_nextstmt = 38
    RULE_vardec = 39
    RULE_stmt = 40
    RULE_asmstmt = 41
    RULE_ifstmt = 42
    RULE_forstmt = 43
    RULE_breakstmt = 44
    RULE_continuestmt = 45
    RULE_returnstmt = 46
    RULE_methodinvocstmt = 47
    RULE_arraylit = 48
    RULE_literals = 49
    RULE_nulliteral = 50

    ruleNames =  [ "program", "typ", "classtype", "classdecl", "memberlist", 
                   "nextmember", "member", "attributedecl", "attnamelist", 
                   "nextattributename", "methoddecl", "paralist", "nextparadecl", 
                   "paradecl", "idlist", "nextid", "constructor", "primitivetype", 
                   "arraytype", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", 
                   "exp6", "exp7", "exp8", "exp9", "exp10", "operand", "index_op", 
                   "explist", "nextexp", "blockstmt", "vardecllist", "nextvardec", 
                   "stmtlist", "nextstmt", "vardec", "stmt", "asmstmt", 
                   "ifstmt", "forstmt", "breakstmt", "continuestmt", "returnstmt", 
                   "methodinvocstmt", "arraylit", "literals", "nulliteral" ]

    EOF = Token.EOF
    ASM=1
    GAN=2
    BCOMMENT=3
    LCOMMENT=4
    INTLIT=5
    FLOATLIT=6
    BOOLIT=7
    STRINGLIT=8
    BOOLEAN=9
    BREAK=10
    CLASS=11
    CONTINUE=12
    DO=13
    ELSE=14
    EXTENDS=15
    FLOAT=16
    IF=17
    INT=18
    NEW=19
    STRING=20
    THEN=21
    FOR=22
    RETURN=23
    TRUE=24
    FALSE=25
    VOID=26
    NIL=27
    THIS=28
    FINAL=29
    STATIC=30
    TO=31
    DOWNTO=32
    ADD=33
    SUB=34
    MUL=35
    FDIV=36
    IDIV=37
    MOD=38
    NEQ=39
    EQ=40
    LESS=41
    GREATER=42
    LESSOE=43
    GREATEROE=44
    OR=45
    AND=46
    NOT=47
    CONCAT=48
    LSB=49
    RSB=50
    LCP=51
    RCP=52
    LB=53
    RB=54
    SMCOLON=55
    COLON=56
    DOT=57
    COMMA=58
    ID=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

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

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ClassdeclContext,i)


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
            self.state = 103 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 102
                self.classdecl()
                self.state = 105 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.CLASS):
                    break

            self.state = 107
            self.match(BKOOLParser.EOF)
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

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def arraytype(self):
            return self.getTypedRuleContext(BKOOLParser.ArraytypeContext,0)


        def classtype(self):
            return self.getTypedRuleContext(BKOOLParser.ClasstypeContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typ)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 109
                self.match(BKOOLParser.INT)
                pass

            elif la_ == 2:
                self.state = 110
                self.match(BKOOLParser.FLOAT)
                pass

            elif la_ == 3:
                self.state = 111
                self.match(BKOOLParser.BOOLEAN)
                pass

            elif la_ == 4:
                self.state = 112
                self.match(BKOOLParser.STRING)
                pass

            elif la_ == 5:
                self.state = 113
                self.arraytype()
                pass

            elif la_ == 6:
                self.state = 114
                self.classtype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClasstypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasstype" ):
                return visitor.visitClasstype(self)
            else:
                return visitor.visitChildren(self)




    def classtype(self):

        localctx = BKOOLParser.ClasstypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(BKOOLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(BKOOLParser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LCP(self):
            return self.getToken(BKOOLParser.LCP, 0)

        def memberlist(self):
            return self.getTypedRuleContext(BKOOLParser.MemberlistContext,0)


        def RCP(self):
            return self.getToken(BKOOLParser.RCP, 0)

        def EXTENDS(self):
            return self.getToken(BKOOLParser.EXTENDS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = BKOOLParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(BKOOLParser.CLASS)
            self.state = 120
            self.match(BKOOLParser.ID)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.EXTENDS:
                self.state = 121
                self.match(BKOOLParser.EXTENDS)
                self.state = 122
                self.match(BKOOLParser.ID)


            self.state = 125
            self.match(BKOOLParser.LCP)
            self.state = 126
            self.memberlist()
            self.state = 127
            self.match(BKOOLParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def nextmember(self):
            return self.getTypedRuleContext(BKOOLParser.NextmemberContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_memberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = BKOOLParser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberlist)
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.member()
                self.state = 130
                self.nextmember()
                pass
            elif token in [BKOOLParser.RCP]:
                self.enterOuterAlt(localctx, 2)

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


    class NextmemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(BKOOLParser.MemberContext,0)


        def nextmember(self):
            return self.getTypedRuleContext(BKOOLParser.NextmemberContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_nextmember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextmember" ):
                return visitor.visitNextmember(self)
            else:
                return visitor.visitChildren(self)




    def nextmember(self):

        localctx = BKOOLParser.NextmemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_nextmember)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.VOID, BKOOLParser.FINAL, BKOOLParser.STATIC, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.member()
                self.state = 136
                self.nextmember()
                pass
            elif token in [BKOOLParser.RCP]:
                self.enterOuterAlt(localctx, 2)

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


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methoddecl(self):
            return self.getTypedRuleContext(BKOOLParser.MethoddeclContext,0)


        def attributedecl(self):
            return self.getTypedRuleContext(BKOOLParser.AttributedeclContext,0)


        def constructor(self):
            return self.getTypedRuleContext(BKOOLParser.ConstructorContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = BKOOLParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 141
                self.methoddecl()
                pass

            elif la_ == 2:
                self.state = 142
                self.attributedecl()
                pass

            elif la_ == 3:
                self.state = 143
                self.constructor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def attnamelist(self):
            return self.getTypedRuleContext(BKOOLParser.AttnamelistContext,0)


        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = BKOOLParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 146
                    self.match(BKOOLParser.STATIC)


                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 149
                    self.match(BKOOLParser.FINAL)


                pass

            elif la_ == 2:
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.FINAL:
                    self.state = 152
                    self.match(BKOOLParser.FINAL)


                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.STATIC:
                    self.state = 155
                    self.match(BKOOLParser.STATIC)


                pass


            self.state = 160
            self.typ()
            self.state = 161
            self.attnamelist()
            self.state = 162
            self.match(BKOOLParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttnamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def nextattributename(self):
            return self.getTypedRuleContext(BKOOLParser.NextattributenameContext,0)


        def ASM(self):
            return self.getToken(BKOOLParser.ASM, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_attnamelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttnamelist" ):
                return visitor.visitAttnamelist(self)
            else:
                return visitor.visitChildren(self)




    def attnamelist(self):

        localctx = BKOOLParser.AttnamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attnamelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKOOLParser.ID)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ASM:
                self.state = 165
                self.match(BKOOLParser.ASM)
                self.state = 166
                self.exp()


            self.state = 169
            self.nextattributename()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NextattributenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def nextattributename(self):
            return self.getTypedRuleContext(BKOOLParser.NextattributenameContext,0)


        def ASM(self):
            return self.getToken(BKOOLParser.ASM, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_nextattributename

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextattributename" ):
                return visitor.visitNextattributename(self)
            else:
                return visitor.visitChildren(self)




    def nextattributename(self):

        localctx = BKOOLParser.NextattributenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nextattributename)
        self._la = 0 # Token type
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(BKOOLParser.COMMA)
                self.state = 172
                self.match(BKOOLParser.ID)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKOOLParser.ASM:
                    self.state = 173
                    self.match(BKOOLParser.ASM)
                    self.state = 174
                    self.exp()


                self.state = 177
                self.nextattributename()
                pass
            elif token in [BKOOLParser.SMCOLON]:
                self.enterOuterAlt(localctx, 2)

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


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitivetype(self):
            return self.getTypedRuleContext(BKOOLParser.PrimitivetypeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paralist(self):
            return self.getTypedRuleContext(BKOOLParser.ParalistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def STATIC(self):
            return self.getToken(BKOOLParser.STATIC, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = BKOOLParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.STATIC:
                self.state = 181
                self.match(BKOOLParser.STATIC)


            self.state = 184
            self.primitivetype()
            self.state = 185
            self.match(BKOOLParser.ID)
            self.state = 186
            self.match(BKOOLParser.LB)
            self.state = 187
            self.paralist()
            self.state = 188
            self.match(BKOOLParser.RB)
            self.state = 189
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paradecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParadeclContext,0)


        def nextparadecl(self):
            return self.getTypedRuleContext(BKOOLParser.NextparadeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = BKOOLParser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paralist)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.BOOLEAN, BKOOLParser.FLOAT, BKOOLParser.INT, BKOOLParser.STRING, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.paradecl()
                self.state = 192
                self.nextparadecl()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class NextparadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def paradecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParadeclContext,0)


        def nextparadecl(self):
            return self.getTypedRuleContext(BKOOLParser.NextparadeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_nextparadecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextparadecl" ):
                return visitor.visitNextparadecl(self)
            else:
                return visitor.visitChildren(self)




    def nextparadecl(self):

        localctx = BKOOLParser.NextparadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_nextparadecl)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.SMCOLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(BKOOLParser.SMCOLON)
                self.state = 198
                self.paradecl()
                self.state = 199
                self.nextparadecl()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ParadeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paradecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParadecl" ):
                return visitor.visitParadecl(self)
            else:
                return visitor.visitChildren(self)




    def paradecl(self):

        localctx = BKOOLParser.ParadeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paradecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.typ()
            self.state = 205
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def nextid(self):
            return self.getTypedRuleContext(BKOOLParser.NextidContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_idlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(BKOOLParser.ID)
            self.state = 208
            self.nextid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NextidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def nextid(self):
            return self.getTypedRuleContext(BKOOLParser.NextidContext,0)


        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def paradecl(self):
            return self.getTypedRuleContext(BKOOLParser.ParadeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_nextid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextid" ):
                return visitor.visitNextid(self)
            else:
                return visitor.visitChildren(self)




    def nextid(self):

        localctx = BKOOLParser.NextidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_nextid)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(BKOOLParser.COMMA)
                self.state = 211
                self.match(BKOOLParser.ID)
                self.state = 212
                self.nextid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(BKOOLParser.SMCOLON)
                self.state = 214
                self.paradecl()
                self.state = 215
                self.nextid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def paralist(self):
            return self.getTypedRuleContext(BKOOLParser.ParalistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = BKOOLParser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BKOOLParser.ID)
            self.state = 221
            self.match(BKOOLParser.LB)
            self.state = 222
            self.paralist()
            self.state = 223
            self.match(BKOOLParser.RB)
            self.state = 224
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitivetypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def VOID(self):
            return self.getToken(BKOOLParser.VOID, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primitivetype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitivetype" ):
                return visitor.visitPrimitivetype(self)
            else:
                return visitor.visitChildren(self)




    def primitivetype(self):

        localctx = BKOOLParser.PrimitivetypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primitivetype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING) | (1 << BKOOLParser.VOID))) != 0)):
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


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(BKOOLParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(BKOOLParser.STRING, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = BKOOLParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.BOOLEAN) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 229
            self.match(BKOOLParser.LSB)
            self.state = 230
            self.match(BKOOLParser.INTLIT)
            self.state = 231
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp1Context,i)


        def LESS(self):
            return self.getToken(BKOOLParser.LESS, 0)

        def GREATER(self):
            return self.getToken(BKOOLParser.GREATER, 0)

        def LESSOE(self):
            return self.getToken(BKOOLParser.LESSOE, 0)

        def GREATEROE(self):
            return self.getToken(BKOOLParser.GREATEROE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.exp1()
                self.state = 234
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.LESS) | (1 << BKOOLParser.GREATER) | (1 << BKOOLParser.LESSOE) | (1 << BKOOLParser.GREATEROE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 235
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Exp2Context,i)


        def EQ(self):
            return self.getToken(BKOOLParser.EQ, 0)

        def NEQ(self):
            return self.getToken(BKOOLParser.NEQ, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = BKOOLParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.exp2(0)
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.NEQ or _la==BKOOLParser.EQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKOOLParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKOOLParser.AND, 0)

        def OR(self):
            return self.getToken(BKOOLParser.OR, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 250
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 251
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.OR or _la==BKOOLParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 252
                    self.exp3(0) 
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKOOLParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 266
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 261
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 262
                    _la = self._input.LA(1)
                    if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 263
                    self.exp4(0) 
                self.state = 268
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKOOLParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(BKOOLParser.MUL, 0)

        def MOD(self):
            return self.getToken(BKOOLParser.MOD, 0)

        def FDIV(self):
            return self.getToken(BKOOLParser.FDIV, 0)

        def IDIV(self):
            return self.getToken(BKOOLParser.IDIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.exp5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.MUL) | (1 << BKOOLParser.FDIV) | (1 << BKOOLParser.IDIV) | (1 << BKOOLParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 274
                    self.exp5(0) 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKOOLParser.Exp5Context,0)


        def CONCAT(self):
            return self.getToken(BKOOLParser.CONCAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.exp6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 288
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 283
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 284
                    self.match(BKOOLParser.CONCAT)
                    self.state = 285
                    self.exp6() 
                self.state = 290
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKOOLParser.NOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKOOLParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = BKOOLParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp6)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(BKOOLParser.NOT)
                self.state = 292
                self.exp6()
                pass
            elif token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.LCP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
                self.exp7()
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


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKOOLParser.Exp7Context,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKOOLParser.SUB, 0)

        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKOOLParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ADD, BKOOLParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                _la = self._input.LA(1)
                if not(_la==BKOOLParser.ADD or _la==BKOOLParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 297
                self.exp7()
                pass
            elif token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.LCP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.exp8(0)
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


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def exp8(self):
            return self.getTypedRuleContext(BKOOLParser.Exp8Context,0)


        def index_op(self):
            return self.getTypedRuleContext(BKOOLParser.Index_opContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)



    def exp8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.exp9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 308
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp8)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    self.index_op() 
                self.state = 310
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def exp9(self):
            return self.getTypedRuleContext(BKOOLParser.Exp9Context,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)



    def exp9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Exp9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exp9, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.exp10()
            self._ctx.stop = self._input.LT(-1)
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Exp9Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp9)
                    self.state = 314
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 315
                    self.match(BKOOLParser.DOT)
                    self.state = 316
                    self.match(BKOOLParser.ID)
                    self.state = 321
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        self.state = 317
                        self.match(BKOOLParser.LB)
                        self.state = 318
                        self.explist()
                        self.state = 319
                        self.match(BKOOLParser.RB)

             
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(BKOOLParser.NEW, 0)

        def exp10(self):
            return self.getTypedRuleContext(BKOOLParser.Exp10Context,0)


        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def operand(self):
            return self.getTypedRuleContext(BKOOLParser.OperandContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exp10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = BKOOLParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp10)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(BKOOLParser.NEW)
                self.state = 329
                self.exp10()
                self.state = 330
                self.match(BKOOLParser.LB)
                self.state = 331
                self.explist()
                self.state = 332
                self.match(BKOOLParser.RB)
                pass
            elif token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.THIS, BKOOLParser.LCP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.operand()
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


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLIT(self):
            return self.getToken(BKOOLParser.BOOLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def arraylit(self):
            return self.getTypedRuleContext(BKOOLParser.ArraylitContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def THIS(self):
            return self.getToken(BKOOLParser.THIS, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = BKOOLParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_operand)
        try:
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.match(BKOOLParser.BOOLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 340
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.LCP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 341
                self.arraylit()
                pass
            elif token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 342
                self.match(BKOOLParser.ID)
                pass
            elif token in [BKOOLParser.THIS]:
                self.enterOuterAlt(localctx, 7)
                self.state = 343
                self.match(BKOOLParser.THIS)
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


    class Index_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKOOLParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKOOLParser.RSB, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_index_op

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_op" ):
                return visitor.visitIndex_op(self)
            else:
                return visitor.visitChildren(self)




    def index_op(self):

        localctx = BKOOLParser.Index_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_index_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(BKOOLParser.LSB)
            self.state = 347
            self.exp()
            self.state = 348
            self.match(BKOOLParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def nextexp(self):
            return self.getTypedRuleContext(BKOOLParser.NextexpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_explist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplist" ):
                return visitor.visitExplist(self)
            else:
                return visitor.visitChildren(self)




    def explist(self):

        localctx = BKOOLParser.ExplistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_explist)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.NEW, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LCP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.exp()
                self.state = 351
                self.nextexp()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class NextexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def nextexp(self):
            return self.getTypedRuleContext(BKOOLParser.NextexpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_nextexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextexp" ):
                return visitor.visitNextexp(self)
            else:
                return visitor.visitChildren(self)




    def nextexp(self):

        localctx = BKOOLParser.NextexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_nextexp)
        try:
            self.state = 361
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(BKOOLParser.COMMA)
                self.state = 357
                self.exp()
                self.state = 358
                self.nextexp()
                pass
            elif token in [BKOOLParser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCP(self):
            return self.getToken(BKOOLParser.LCP, 0)

        def vardecllist(self):
            return self.getTypedRuleContext(BKOOLParser.VardecllistContext,0)


        def stmtlist(self):
            return self.getTypedRuleContext(BKOOLParser.StmtlistContext,0)


        def RCP(self):
            return self.getToken(BKOOLParser.RCP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = BKOOLParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_blockstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(BKOOLParser.LCP)
            self.state = 364
            self.vardecllist()
            self.state = 365
            self.stmtlist()
            self.state = 366
            self.match(BKOOLParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec(self):
            return self.getTypedRuleContext(BKOOLParser.VardecContext,0)


        def nextvardec(self):
            return self.getTypedRuleContext(BKOOLParser.NextvardecContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecllist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecllist" ):
                return visitor.visitVardecllist(self)
            else:
                return visitor.visitChildren(self)




    def vardecllist(self):

        localctx = BKOOLParser.VardecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_vardecllist)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.vardec()
                self.state = 369
                self.nextvardec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NextvardecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardec(self):
            return self.getTypedRuleContext(BKOOLParser.VardecContext,0)


        def nextvardec(self):
            return self.getTypedRuleContext(BKOOLParser.NextvardecContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_nextvardec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextvardec" ):
                return visitor.visitNextvardec(self)
            else:
                return visitor.visitChildren(self)




    def nextvardec(self):

        localctx = BKOOLParser.NextvardecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_nextvardec)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.vardec()
                self.state = 375
                self.nextvardec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def nextstmt(self):
            return self.getTypedRuleContext(BKOOLParser.NextstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = BKOOLParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmtlist)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LCP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.stmt()
                self.state = 381
                self.nextstmt()
                pass
            elif token in [BKOOLParser.RCP]:
                self.enterOuterAlt(localctx, 2)

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


    class NextstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def nextstmt(self):
            return self.getTypedRuleContext(BKOOLParser.NextstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_nextstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNextstmt" ):
                return visitor.visitNextstmt(self)
            else:
                return visitor.visitChildren(self)




    def nextstmt(self):

        localctx = BKOOLParser.NextstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_nextstmt)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT, BKOOLParser.FLOATLIT, BKOOLParser.BOOLIT, BKOOLParser.STRINGLIT, BKOOLParser.BREAK, BKOOLParser.CONTINUE, BKOOLParser.IF, BKOOLParser.NEW, BKOOLParser.FOR, BKOOLParser.RETURN, BKOOLParser.THIS, BKOOLParser.ADD, BKOOLParser.SUB, BKOOLParser.NOT, BKOOLParser.LCP, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.stmt()
                self.state = 387
                self.nextstmt()
                pass
            elif token in [BKOOLParser.RCP]:
                self.enterOuterAlt(localctx, 2)

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


    class VardecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def attnamelist(self):
            return self.getTypedRuleContext(BKOOLParser.AttnamelistContext,0)


        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def FINAL(self):
            return self.getToken(BKOOLParser.FINAL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec" ):
                return visitor.visitVardec(self)
            else:
                return visitor.visitChildren(self)




    def vardec(self):

        localctx = BKOOLParser.VardecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_vardec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.FINAL:
                self.state = 392
                self.match(BKOOLParser.FINAL)


            self.state = 395
            self.typ()
            self.state = 396
            self.attnamelist()
            self.state = 397
            self.match(BKOOLParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BlockstmtContext,0)


        def asmstmt(self):
            return self.getTypedRuleContext(BKOOLParser.AsmstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(BKOOLParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(BKOOLParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(BKOOLParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(BKOOLParser.ReturnstmtContext,0)


        def methodinvocstmt(self):
            return self.getTypedRuleContext(BKOOLParser.MethodinvocstmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.blockstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.asmstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 402
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 403
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 404
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 405
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 406
                self.methodinvocstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsmstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def GAN(self):
            return self.getToken(BKOOLParser.GAN, 0)

        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_asmstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsmstmt" ):
                return visitor.visitAsmstmt(self)
            else:
                return visitor.visitChildren(self)




    def asmstmt(self):

        localctx = BKOOLParser.AsmstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_asmstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.exp()
            self.state = 410
            self.match(BKOOLParser.GAN)
            self.state = 411
            self.exp()
            self.state = 412
            self.match(BKOOLParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKOOLParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKOOLParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(BKOOLParser.ELSE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = BKOOLParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(BKOOLParser.IF)
            self.state = 415
            self.exp()
            self.state = 416
            self.match(BKOOLParser.THEN)
            self.state = 417
            self.stmt()
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 418
                self.match(BKOOLParser.ELSE)
                self.state = 419
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKOOLParser.FOR, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def GAN(self):
            return self.getToken(BKOOLParser.GAN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ExpContext,i)


        def DO(self):
            return self.getToken(BKOOLParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def TO(self):
            return self.getToken(BKOOLParser.TO, 0)

        def DOWNTO(self):
            return self.getToken(BKOOLParser.DOWNTO, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = BKOOLParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(BKOOLParser.FOR)
            self.state = 423
            self.match(BKOOLParser.ID)
            self.state = 424
            self.match(BKOOLParser.GAN)
            self.state = 425
            self.exp()
            self.state = 426
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.TO or _la==BKOOLParser.DOWNTO):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 427
            self.exp()
            self.state = 428
            self.match(BKOOLParser.DO)
            self.state = 429
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKOOLParser.BREAK, 0)

        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = BKOOLParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(BKOOLParser.BREAK)
            self.state = 432
            self.match(BKOOLParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKOOLParser.CONTINUE, 0)

        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = BKOOLParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(BKOOLParser.CONTINUE)
            self.state = 435
            self.match(BKOOLParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKOOLParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = BKOOLParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(BKOOLParser.RETURN)
            self.state = 438
            self.exp()
            self.state = 439
            self.match(BKOOLParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodinvocstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def DOT(self):
            return self.getToken(BKOOLParser.DOT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def explist(self):
            return self.getTypedRuleContext(BKOOLParser.ExplistContext,0)


        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def SMCOLON(self):
            return self.getToken(BKOOLParser.SMCOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_methodinvocstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvocstmt" ):
                return visitor.visitMethodinvocstmt(self)
            else:
                return visitor.visitChildren(self)




    def methodinvocstmt(self):

        localctx = BKOOLParser.MethodinvocstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_methodinvocstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.exp()
            self.state = 442
            self.match(BKOOLParser.DOT)
            self.state = 443
            self.match(BKOOLParser.ID)
            self.state = 444
            self.match(BKOOLParser.LB)
            self.state = 445
            self.explist()
            self.state = 446
            self.match(BKOOLParser.RB)
            self.state = 447
            self.match(BKOOLParser.SMCOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraylitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCP(self):
            return self.getToken(BKOOLParser.LCP, 0)

        def literals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LiteralsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LiteralsContext,i)


        def RCP(self):
            return self.getToken(BKOOLParser.RCP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_arraylit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraylit" ):
                return visitor.visitArraylit(self)
            else:
                return visitor.visitChildren(self)




    def arraylit(self):

        localctx = BKOOLParser.ArraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(BKOOLParser.LCP)
            self.state = 450
            self.literals()
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COMMA:
                self.state = 451
                self.match(BKOOLParser.COMMA)
                self.state = 452
                self.literals()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 458
            self.match(BKOOLParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKOOLParser.FLOATLIT, 0)

        def BOOLIT(self):
            return self.getToken(BKOOLParser.BOOLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKOOLParser.STRINGLIT, 0)

        def nulliteral(self):
            return self.getTypedRuleContext(BKOOLParser.NulliteralContext,0)


        def arraylit(self):
            return self.getTypedRuleContext(BKOOLParser.ArraylitContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_literals

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = BKOOLParser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_literals)
        try:
            self.state = 466
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(BKOOLParser.INTLIT)
                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.match(BKOOLParser.FLOATLIT)
                pass
            elif token in [BKOOLParser.BOOLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.match(BKOOLParser.BOOLIT)
                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 463
                self.match(BKOOLParser.STRINGLIT)
                pass
            elif token in [BKOOLParser.NIL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 464
                self.nulliteral()
                pass
            elif token in [BKOOLParser.LCP]:
                self.enterOuterAlt(localctx, 6)
                self.state = 465
                self.arraylit()
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


    class NulliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NIL(self):
            return self.getToken(BKOOLParser.NIL, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_nulliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNulliteral" ):
                return visitor.visitNulliteral(self)
            else:
                return visitor.visitChildren(self)




    def nulliteral(self):

        localctx = BKOOLParser.NulliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_nulliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(BKOOLParser.NIL)
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
        self._predicates[21] = self.exp2_sempred
        self._predicates[22] = self.exp3_sempred
        self._predicates[23] = self.exp4_sempred
        self._predicates[24] = self.exp5_sempred
        self._predicates[27] = self.exp8_sempred
        self._predicates[28] = self.exp9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp8_sempred(self, localctx:Exp8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp9_sempred(self, localctx:Exp9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




