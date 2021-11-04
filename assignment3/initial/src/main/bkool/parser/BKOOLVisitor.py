# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classtype.
    def visitClasstype(self, ctx:BKOOLParser.ClasstypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#classdecl.
    def visitClassdecl(self, ctx:BKOOLParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#memberlist.
    def visitMemberlist(self, ctx:BKOOLParser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nextmember.
    def visitNextmember(self, ctx:BKOOLParser.NextmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#member.
    def visitMember(self, ctx:BKOOLParser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attributedecl.
    def visitAttributedecl(self, ctx:BKOOLParser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#attnamelist.
    def visitAttnamelist(self, ctx:BKOOLParser.AttnamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nextattributename.
    def visitNextattributename(self, ctx:BKOOLParser.NextattributenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methoddecl.
    def visitMethoddecl(self, ctx:BKOOLParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paralist.
    def visitParalist(self, ctx:BKOOLParser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nextparadecl.
    def visitNextparadecl(self, ctx:BKOOLParser.NextparadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paradecl.
    def visitParadecl(self, ctx:BKOOLParser.ParadeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nextid.
    def visitNextid(self, ctx:BKOOLParser.NextidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#constructor.
    def visitConstructor(self, ctx:BKOOLParser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#primitivetype.
    def visitPrimitivetype(self, ctx:BKOOLParser.PrimitivetypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraytype.
    def visitArraytype(self, ctx:BKOOLParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp.
    def visitExp(self, ctx:BKOOLParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp1.
    def visitExp1(self, ctx:BKOOLParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp2.
    def visitExp2(self, ctx:BKOOLParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp3.
    def visitExp3(self, ctx:BKOOLParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp4.
    def visitExp4(self, ctx:BKOOLParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp5.
    def visitExp5(self, ctx:BKOOLParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp6.
    def visitExp6(self, ctx:BKOOLParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp7.
    def visitExp7(self, ctx:BKOOLParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp8.
    def visitExp8(self, ctx:BKOOLParser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp9.
    def visitExp9(self, ctx:BKOOLParser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exp10.
    def visitExp10(self, ctx:BKOOLParser.Exp10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#operand.
    def visitOperand(self, ctx:BKOOLParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#index_op.
    def visitIndex_op(self, ctx:BKOOLParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#explist.
    def visitExplist(self, ctx:BKOOLParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nextexp.
    def visitNextexp(self, ctx:BKOOLParser.NextexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#blockstmt.
    def visitBlockstmt(self, ctx:BKOOLParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecllist.
    def visitVardecllist(self, ctx:BKOOLParser.VardecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nextvardec.
    def visitNextvardec(self, ctx:BKOOLParser.NextvardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmtlist.
    def visitStmtlist(self, ctx:BKOOLParser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nextstmt.
    def visitNextstmt(self, ctx:BKOOLParser.NextstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardec.
    def visitVardec(self, ctx:BKOOLParser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#asmstmt.
    def visitAsmstmt(self, ctx:BKOOLParser.AsmstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ifstmt.
    def visitIfstmt(self, ctx:BKOOLParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#forstmt.
    def visitForstmt(self, ctx:BKOOLParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#breakstmt.
    def visitBreakstmt(self, ctx:BKOOLParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#continuestmt.
    def visitContinuestmt(self, ctx:BKOOLParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#returnstmt.
    def visitReturnstmt(self, ctx:BKOOLParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#methodinvocstmt.
    def visitMethodinvocstmt(self, ctx:BKOOLParser.MethodinvocstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#arraylit.
    def visitArraylit(self, ctx:BKOOLParser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#literals.
    def visitLiterals(self, ctx:BKOOLParser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#nulliteral.
    def visitNulliteral(self, ctx:BKOOLParser.NulliteralContext):
        return self.visitChildren(ctx)



del BKOOLParser