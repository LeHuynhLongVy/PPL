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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u01e1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\7\4\u009b\n\4\f\4\16\4\u009e\13\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5\u00a8\n\5\f\5\16\5\u00ab")
        buf.write("\13\5\3\5\3\5\3\6\6\6\u00b0\n\6\r\6\16\6\u00b1\3\7\6\7")
        buf.write("\u00b5\n\7\r\7\16\7\u00b6\3\7\3\7\5\7\u00bb\n\7\3\7\5")
        buf.write("\7\u00be\n\7\3\7\5\7\u00c1\n\7\3\b\3\b\3\t\3\t\7\t\u00c7")
        buf.write("\n\t\f\t\16\t\u00ca\13\t\3\n\3\n\5\n\u00ce\n\n\3\n\6\n")
        buf.write("\u00d1\n\n\r\n\16\n\u00d2\3\13\3\13\5\13\u00d7\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\7\f\u00df\n\f\f\f\16\f\u00e2\13")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\5?\u01a8\n?\3?\3?\3?\7")
        buf.write("?\u01ad\n?\f?\16?\u01b0\13?\3@\3@\3A\3A\3B\6B\u01b7\n")
        buf.write("B\rB\16B\u01b8\3B\3B\3C\3C\3C\3D\3D\7D\u01c2\nD\fD\16")
        buf.write("D\u01c5\13D\3D\5D\u01c8\nD\3D\3D\3E\3E\7E\u01ce\nE\fE")
        buf.write("\16E\u01d1\13E\3E\3E\3E\3F\3F\5F\u01d8\nF\3G\3G\3G\3H")
        buf.write("\3H\3H\5H\u01e0\nH\3\u009c\2I\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\2\21\2\23\2\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20")
        buf.write("%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\329\33")
        buf.write(";\34=\35?\36A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60")
        buf.write("e\61g\62i\63k\64m\65o\66q\67s8u9w:y;{<}=\177\2\u0081\2")
        buf.write("\u0083>\u0085?\u0087@\u0089A\u008b\2\u008d\2\u008f\2\3")
        buf.write("\2\r\4\2\f\f\16\17\3\2\62;\4\2GGgg\4\2--//\b\2^^ddhhp")
        buf.write("pttvv\6\2\n\f\16\17$$^^\4\2C\\c|\5\2\13\f\16\17\"\"\7")
        buf.write("\3\n\f\16\17$$))^^\t\2$$^^ddhhppttvv\3\2^^\2\u01ef\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\3\u0091\3\2\2")
        buf.write("\2\5\u0093\3\2\2\2\7\u0096\3\2\2\2\t\u00a4\3\2\2\2\13")
        buf.write("\u00af\3\2\2\2\r\u00b4\3\2\2\2\17\u00c2\3\2\2\2\21\u00c4")
        buf.write("\3\2\2\2\23\u00cb\3\2\2\2\25\u00d6\3\2\2\2\27\u00d8\3")
        buf.write("\2\2\2\31\u00e6\3\2\2\2\33\u00ee\3\2\2\2\35\u00f4\3\2")
        buf.write("\2\2\37\u00fa\3\2\2\2!\u0103\3\2\2\2#\u0106\3\2\2\2%\u010b")
        buf.write("\3\2\2\2\'\u0113\3\2\2\2)\u0119\3\2\2\2+\u011c\3\2\2\2")
        buf.write("-\u0120\3\2\2\2/\u0124\3\2\2\2\61\u012b\3\2\2\2\63\u0130")
        buf.write("\3\2\2\2\65\u0134\3\2\2\2\67\u013b\3\2\2\29\u0140\3\2")
        buf.write("\2\2;\u0146\3\2\2\2=\u014b\3\2\2\2?\u014f\3\2\2\2A\u0154")
        buf.write("\3\2\2\2C\u015a\3\2\2\2E\u0161\3\2\2\2G\u0164\3\2\2\2")
        buf.write("I\u016b\3\2\2\2K\u016d\3\2\2\2M\u016f\3\2\2\2O\u0171\3")
        buf.write("\2\2\2Q\u0173\3\2\2\2S\u0175\3\2\2\2U\u0177\3\2\2\2W\u017a")
        buf.write("\3\2\2\2Y\u017d\3\2\2\2[\u017f\3\2\2\2]\u0181\3\2\2\2")
        buf.write("_\u0184\3\2\2\2a\u0187\3\2\2\2c\u018a\3\2\2\2e\u018d\3")
        buf.write("\2\2\2g\u018f\3\2\2\2i\u0191\3\2\2\2k\u0193\3\2\2\2m\u0195")
        buf.write("\3\2\2\2o\u0197\3\2\2\2q\u0199\3\2\2\2s\u019b\3\2\2\2")
        buf.write("u\u019d\3\2\2\2w\u019f\3\2\2\2y\u01a1\3\2\2\2{\u01a3\3")
        buf.write("\2\2\2}\u01a7\3\2\2\2\177\u01b1\3\2\2\2\u0081\u01b3\3")
        buf.write("\2\2\2\u0083\u01b6\3\2\2\2\u0085\u01bc\3\2\2\2\u0087\u01bf")
        buf.write("\3\2\2\2\u0089\u01cb\3\2\2\2\u008b\u01d7\3\2\2\2\u008d")
        buf.write("\u01d9\3\2\2\2\u008f\u01df\3\2\2\2\u0091\u0092\7?\2\2")
        buf.write("\u0092\4\3\2\2\2\u0093\u0094\7<\2\2\u0094\u0095\7?\2\2")
        buf.write("\u0095\6\3\2\2\2\u0096\u0097\7\61\2\2\u0097\u0098\7,\2")
        buf.write("\2\u0098\u009c\3\2\2\2\u0099\u009b\13\2\2\2\u009a\u0099")
        buf.write("\3\2\2\2\u009b\u009e\3\2\2\2\u009c\u009d\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009f\u00a0\7,\2\2\u00a0\u00a1\7\61\2\2\u00a1\u00a2\3")
        buf.write("\2\2\2\u00a2\u00a3\b\4\2\2\u00a3\b\3\2\2\2\u00a4\u00a5")
        buf.write("\7%\2\2\u00a5\u00a9\13\2\2\2\u00a6\u00a8\n\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3")
        buf.write("\2\2\2\u00ac\u00ad\b\5\2\2\u00ad\n\3\2\2\2\u00ae\u00b0")
        buf.write("\5\17\b\2\u00af\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\f\3\2\2\2\u00b3")
        buf.write("\u00b5\5\17\b\2\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3\2\2")
        buf.write("\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00c0")
        buf.write("\3\2\2\2\u00b8\u00ba\5\21\t\2\u00b9\u00bb\5\23\n\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00c1\3\2\2\2")
        buf.write("\u00bc\u00be\5\21\t\2\u00bd\u00bc\3\2\2\2\u00bd\u00be")
        buf.write("\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\5\23\n\2\u00c0")
        buf.write("\u00b8\3\2\2\2\u00c0\u00bd\3\2\2\2\u00c1\16\3\2\2\2\u00c2")
        buf.write("\u00c3\t\3\2\2\u00c3\20\3\2\2\2\u00c4\u00c8\7\60\2\2\u00c5")
        buf.write("\u00c7\5\17\b\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca\3\2\2")
        buf.write("\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\22\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cd\t\4\2\2\u00cc\u00ce")
        buf.write("\t\5\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00d0\3\2\2\2\u00cf\u00d1\5\17\b\2\u00d0\u00cf\3\2\2")
        buf.write("\2\u00d1\u00d2\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\24\3\2\2\2\u00d4\u00d7\5\67\34\2\u00d5")
        buf.write("\u00d7\59\35\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3\2\2\2")
        buf.write("\u00d7\26\3\2\2\2\u00d8\u00e0\7$\2\2\u00d9\u00da\7^\2")
        buf.write("\2\u00da\u00df\t\6\2\2\u00db\u00dc\7^\2\2\u00dc\u00df")
        buf.write("\7$\2\2\u00dd\u00df\n\7\2\2\u00de\u00d9\3\2\2\2\u00de")
        buf.write("\u00db\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3")
        buf.write("\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\7$\2\2\u00e4\u00e5")
        buf.write("\b\f\3\2\u00e5\30\3\2\2\2\u00e6\u00e7\7d\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb")
        buf.write("\7g\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed\32")
        buf.write("\3\2\2\2\u00ee\u00ef\7d\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7m\2\2\u00f3\34")
        buf.write("\3\2\2\2\u00f4\u00f5\7e\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9\7u\2\2\u00f9\36")
        buf.write("\3\2\2\2\u00fa\u00fb\7e\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd")
        buf.write("\7p\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7w\2\2\u0101\u0102\7g\2\2\u0102 \3")
        buf.write("\2\2\2\u0103\u0104\7f\2\2\u0104\u0105\7q\2\2\u0105\"\3")
        buf.write("\2\2\2\u0106\u0107\7g\2\2\u0107\u0108\7n\2\2\u0108\u0109")
        buf.write("\7u\2\2\u0109\u010a\7g\2\2\u010a$\3\2\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010c\u010d\7z\2\2\u010d\u010e\7v\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\u0110\7p\2\2\u0110\u0111\7f\2\2\u0111\u0112")
        buf.write("\7u\2\2\u0112&\3\2\2\2\u0113\u0114\7h\2\2\u0114\u0115")
        buf.write("\7n\2\2\u0115\u0116\7q\2\2\u0116\u0117\7c\2\2\u0117\u0118")
        buf.write("\7v\2\2\u0118(\3\2\2\2\u0119\u011a\7k\2\2\u011a\u011b")
        buf.write("\7h\2\2\u011b*\3\2\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7v\2\2\u011f,\3\2\2\2\u0120\u0121")
        buf.write("\7p\2\2\u0121\u0122\7g\2\2\u0122\u0123\7y\2\2\u0123.\3")
        buf.write("\2\2\2\u0124\u0125\7u\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7t\2\2\u0127\u0128\7k\2\2\u0128\u0129\7p\2\2\u0129\u012a")
        buf.write("\7i\2\2\u012a\60\3\2\2\2\u012b\u012c\7v\2\2\u012c\u012d")
        buf.write("\7j\2\2\u012d\u012e\7g\2\2\u012e\u012f\7p\2\2\u012f\62")
        buf.write("\3\2\2\2\u0130\u0131\7h\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7t\2\2\u0133\64\3\2\2\2\u0134\u0135\7t\2\2\u0135\u0136")
        buf.write("\7g\2\2\u0136\u0137\7v\2\2\u0137\u0138\7w\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139\u013a\7p\2\2\u013a\66\3\2\2\2\u013b\u013c")
        buf.write("\7v\2\2\u013c\u013d\7t\2\2\u013d\u013e\7w\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f8\3\2\2\2\u0140\u0141\7h\2\2\u0141\u0142")
        buf.write("\7c\2\2\u0142\u0143\7n\2\2\u0143\u0144\7u\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145:\3\2\2\2\u0146\u0147\7x\2\2\u0147\u0148")
        buf.write("\7q\2\2\u0148\u0149\7k\2\2\u0149\u014a\7f\2\2\u014a<\3")
        buf.write("\2\2\2\u014b\u014c\7p\2\2\u014c\u014d\7k\2\2\u014d\u014e")
        buf.write("\7n\2\2\u014e>\3\2\2\2\u014f\u0150\7v\2\2\u0150\u0151")
        buf.write("\7j\2\2\u0151\u0152\7k\2\2\u0152\u0153\7u\2\2\u0153@\3")
        buf.write("\2\2\2\u0154\u0155\7h\2\2\u0155\u0156\7k\2\2\u0156\u0157")
        buf.write("\7p\2\2\u0157\u0158\7c\2\2\u0158\u0159\7n\2\2\u0159B\3")
        buf.write("\2\2\2\u015a\u015b\7u\2\2\u015b\u015c\7v\2\2\u015c\u015d")
        buf.write("\7c\2\2\u015d\u015e\7v\2\2\u015e\u015f\7k\2\2\u015f\u0160")
        buf.write("\7e\2\2\u0160D\3\2\2\2\u0161\u0162\7v\2\2\u0162\u0163")
        buf.write("\7q\2\2\u0163F\3\2\2\2\u0164\u0165\7f\2\2\u0165\u0166")
        buf.write("\7q\2\2\u0166\u0167\7y\2\2\u0167\u0168\7p\2\2\u0168\u0169")
        buf.write("\7v\2\2\u0169\u016a\7q\2\2\u016aH\3\2\2\2\u016b\u016c")
        buf.write("\7-\2\2\u016cJ\3\2\2\2\u016d\u016e\7/\2\2\u016eL\3\2\2")
        buf.write("\2\u016f\u0170\7,\2\2\u0170N\3\2\2\2\u0171\u0172\7\61")
        buf.write("\2\2\u0172P\3\2\2\2\u0173\u0174\7^\2\2\u0174R\3\2\2\2")
        buf.write("\u0175\u0176\7\'\2\2\u0176T\3\2\2\2\u0177\u0178\7#\2\2")
        buf.write("\u0178\u0179\7?\2\2\u0179V\3\2\2\2\u017a\u017b\7?\2\2")
        buf.write("\u017b\u017c\7?\2\2\u017cX\3\2\2\2\u017d\u017e\7>\2\2")
        buf.write("\u017eZ\3\2\2\2\u017f\u0180\7@\2\2\u0180\\\3\2\2\2\u0181")
        buf.write("\u0182\7>\2\2\u0182\u0183\7?\2\2\u0183^\3\2\2\2\u0184")
        buf.write("\u0185\7@\2\2\u0185\u0186\7?\2\2\u0186`\3\2\2\2\u0187")
        buf.write("\u0188\7~\2\2\u0188\u0189\7~\2\2\u0189b\3\2\2\2\u018a")
        buf.write("\u018b\7(\2\2\u018b\u018c\7(\2\2\u018cd\3\2\2\2\u018d")
        buf.write("\u018e\7#\2\2\u018ef\3\2\2\2\u018f\u0190\7`\2\2\u0190")
        buf.write("h\3\2\2\2\u0191\u0192\7]\2\2\u0192j\3\2\2\2\u0193\u0194")
        buf.write("\7_\2\2\u0194l\3\2\2\2\u0195\u0196\7}\2\2\u0196n\3\2\2")
        buf.write("\2\u0197\u0198\7\177\2\2\u0198p\3\2\2\2\u0199\u019a\7")
        buf.write("*\2\2\u019ar\3\2\2\2\u019b\u019c\7+\2\2\u019ct\3\2\2\2")
        buf.write("\u019d\u019e\7=\2\2\u019ev\3\2\2\2\u019f\u01a0\7<\2\2")
        buf.write("\u01a0x\3\2\2\2\u01a1\u01a2\7\60\2\2\u01a2z\3\2\2\2\u01a3")
        buf.write("\u01a4\7.\2\2\u01a4|\3\2\2\2\u01a5\u01a8\5\177@\2\u01a6")
        buf.write("\u01a8\5\u0081A\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2")
        buf.write("\2\2\u01a8\u01ae\3\2\2\2\u01a9\u01ad\5\177@\2\u01aa\u01ad")
        buf.write("\5\u0081A\2\u01ab\u01ad\5\17\b\2\u01ac\u01a9\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01ad\u01b0\3\2\2\2")
        buf.write("\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2\u01af~\3\2\2")
        buf.write("\2\u01b0\u01ae\3\2\2\2\u01b1\u01b2\t\b\2\2\u01b2\u0080")
        buf.write("\3\2\2\2\u01b3\u01b4\7a\2\2\u01b4\u0082\3\2\2\2\u01b5")
        buf.write("\u01b7\t\t\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\3")
        buf.write("\2\2\2\u01ba\u01bb\bB\2\2\u01bb\u0084\3\2\2\2\u01bc\u01bd")
        buf.write("\13\2\2\2\u01bd\u01be\bC\4\2\u01be\u0086\3\2\2\2\u01bf")
        buf.write("\u01c3\7$\2\2\u01c0\u01c2\5\u008bF\2\u01c1\u01c0\3\2\2")
        buf.write("\2\u01c2\u01c5\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c3\u01c4")
        buf.write("\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6")
        buf.write("\u01c8\t\n\2\2\u01c7\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9\u01ca\bD\5\2\u01ca\u0088\3\2\2\2\u01cb\u01cf\7")
        buf.write("$\2\2\u01cc\u01ce\5\u008bF\2\u01cd\u01cc\3\2\2\2\u01ce")
        buf.write("\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3\5")
        buf.write("\u008fH\2\u01d3\u01d4\bE\6\2\u01d4\u008a\3\2\2\2\u01d5")
        buf.write("\u01d8\n\7\2\2\u01d6\u01d8\5\u008dG\2\u01d7\u01d5\3\2")
        buf.write("\2\2\u01d7\u01d6\3\2\2\2\u01d8\u008c\3\2\2\2\u01d9\u01da")
        buf.write("\7^\2\2\u01da\u01db\t\13\2\2\u01db\u008e\3\2\2\2\u01dc")
        buf.write("\u01dd\7^\2\2\u01dd\u01e0\n\13\2\2\u01de\u01e0\n\f\2\2")
        buf.write("\u01df\u01dc\3\2\2\2\u01df\u01de\3\2\2\2\u01e0\u0090\3")
        buf.write("\2\2\2\31\2\u009c\u00a9\u00b1\u00b6\u00ba\u00bd\u00c0")
        buf.write("\u00c8\u00cd\u00d2\u00d6\u00de\u00e0\u01a7\u01ac\u01ae")
        buf.write("\u01b8\u01c3\u01c7\u01cf\u01d7\u01df\7\b\2\2\3\f\2\3C")
        buf.write("\3\3D\4\3E\5")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ASM = 1
    GAN = 2
    BCOMMENT = 3
    LCOMMENT = 4
    INTLIT = 5
    FLOATLIT = 6
    BOOLIT = 7
    STRINGLIT = 8
    BOOLEAN = 9
    BREAK = 10
    CLASS = 11
    CONTINUE = 12
    DO = 13
    ELSE = 14
    EXTENDS = 15
    FLOAT = 16
    IF = 17
    INT = 18
    NEW = 19
    STRING = 20
    THEN = 21
    FOR = 22
    RETURN = 23
    TRUE = 24
    FALSE = 25
    VOID = 26
    NIL = 27
    THIS = 28
    FINAL = 29
    STATIC = 30
    TO = 31
    DOWNTO = 32
    ADD = 33
    SUB = 34
    MUL = 35
    FDIV = 36
    IDIV = 37
    MOD = 38
    NEQ = 39
    EQ = 40
    LESS = 41
    GREATER = 42
    LESSOE = 43
    GREATEROE = 44
    OR = 45
    AND = 46
    NOT = 47
    CONCAT = 48
    LSB = 49
    RSB = 50
    LCP = 51
    RCP = 52
    LB = 53
    RB = 54
    SMCOLON = 55
    COLON = 56
    DOT = 57
    COMMA = 58
    ID = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "':='", "'boolean'", "'break'", "'class'", "'continue'", 
            "'do'", "'else'", "'extends'", "'float'", "'if'", "'int'", "'new'", 
            "'string'", "'then'", "'for'", "'return'", "'true'", "'false'", 
            "'void'", "'nil'", "'this'", "'final'", "'static'", "'to'", 
            "'downto'", "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", "'!'", 
            "'^'", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "':'", 
            "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ASM", "GAN", "BCOMMENT", "LCOMMENT", "INTLIT", "FLOATLIT", 
            "BOOLIT", "STRINGLIT", "BOOLEAN", "BREAK", "CLASS", "CONTINUE", 
            "DO", "ELSE", "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", 
            "THEN", "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
            "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", "FDIV", 
            "IDIV", "MOD", "NEQ", "EQ", "LESS", "GREATER", "LESSOE", "GREATEROE", 
            "OR", "AND", "NOT", "CONCAT", "LSB", "RSB", "LCP", "RCP", "LB", 
            "RB", "SMCOLON", "COLON", "DOT", "COMMA", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ASM", "GAN", "BCOMMENT", "LCOMMENT", "INTLIT", "FLOATLIT", 
                  "DIGIT", "DECIMAL", "EXPONENT", "BOOLIT", "STRINGLIT", 
                  "BOOLEAN", "BREAK", "CLASS", "CONTINUE", "DO", "ELSE", 
                  "EXTENDS", "FLOAT", "IF", "INT", "NEW", "STRING", "THEN", 
                  "FOR", "RETURN", "TRUE", "FALSE", "VOID", "NIL", "THIS", 
                  "FINAL", "STATIC", "TO", "DOWNTO", "ADD", "SUB", "MUL", 
                  "FDIV", "IDIV", "MOD", "NEQ", "EQ", "LESS", "GREATER", 
                  "LESSOE", "GREATEROE", "OR", "AND", "NOT", "CONCAT", "LSB", 
                  "RSB", "LCP", "RCP", "LB", "RB", "SMCOLON", "COLON", "DOT", 
                  "COMMA", "ID", "LETTER", "UNDERSCORE", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STR_CHAR", "ESC_SEQUENCE", 
                  "ESC_ILLEGAL" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.STRINGLIT_action 
            actions[65] = self.ERROR_CHAR_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		wrong_string = str(self.text)
            		esc_squence = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if wrong_string[-1] in esc_squence:
            			raise UncloseString(wrong_string[1:-1])
            		else:
            			raise UncloseString(wrong_string[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		wrong_string = str(self.text)
            		raise IllegalEscape(wrong_string[1:])
            	
     


