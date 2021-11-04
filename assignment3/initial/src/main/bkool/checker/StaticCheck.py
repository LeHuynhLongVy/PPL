"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *

class Utils:
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

class CCheck:
    def __init__(self, name, parentname = None, members=None):
        self.name = name
        self.parentname = parentname
        self.members = members

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, kind=None):
        self.name = name
        self.mtype = mtype
        self.kind = kind

class StaticChecker(BaseVisitor, Utils):
    global_envi = [
        CCheck(
            "io",
            None,
            [
                Symbol("readInt", MType([], IntType())),
                Symbol("writeInt", MType([IntType()], VoidType())),
                Symbol("writeIntLn", MType([IntType()], VoidType())),
                Symbol("readFloat", MType([], FloatType())),
                Symbol("writeFloat", MType([FloatType()], VoidType())),
                Symbol("writeFloatLn", MType([FloatType()], VoidType())),
                Symbol("readBool", MType([], BoolType())),
                Symbol("writeBool", MType([BoolType()], VoidType())),
                Symbol("writeBoolLn", MType([BoolType()], VoidType())),
                Symbol("readStr", MType([], StringType())),
                Symbol("writeStr", MType([StringType()], VoidType())),
                Symbol("writeStrLn", MType([StringType()], VoidType())),
            ],
        ),
    ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        cList = c
        allclassName = [] + c
        for cDecl in ast.decl:
            if self.lookup(cDecl.classname.name, allclassName, lambda x: x.name):
                raise Redeclared(Class(), cDecl.classname.name)
            allclassName = allclassName + [
                CCheck(
                    cDecl.classname.name,
                    None,
                    [],
                )
            ]

        for cDecl in ast.decl:
            if self.lookup(cDecl.classname.name, cList, lambda x: x.name):
                raise Redeclared(Class(), cDecl.classname.name)
            memberDecl = [[], [0], None, False, allclassName]
            for each_decl in cDecl.memlist:
                if type(each_decl) == MethodDecl:
                    if self.lookup(each_decl.name.name, memberDecl[0], lambda x: x.name):
                        raise Redeclared(Method(), each_decl.name.name)
                    partype = [param.varType for param in each_decl.param]
                    memberDecl[0] = memberDecl[0] + [
                        Symbol(
                            each_decl.name.name, MType(partype, each_decl.returnType), each_decl.kind
                        )
                    ]
                elif type(each_decl) == AttributeDecl:
                    memberDecl[0] = memberDecl[0] + [self.visit(each_decl, memberDecl)]
            cList = cList + [
                CCheck(
                    cDecl.classname.name,
                    None,
                    memberDecl,
                )
            ]
        for cDecl in ast.decl:
            self.visit(cDecl, cList)

    def visitClassDecl(self, ast, c):
        each_class = self.lookup(ast.classname.name, c, lambda x: x.name)
        each_class_index = c.index(each_class)
        if ast.parentname:
            parent = self.lookup(ast.parentname.name, c, lambda x: x.name)
            if parent is None:
                raise Undeclared(Class(), ast.parentname.name)
            else:
                each_class.parentname = parent
                c[each_class_index] = each_class
        memberList = each_class.members
        for member in ast.memlist:
            if type(member) == MethodDecl:
                partype = [param.varType for param in member.param]
                memberList[1] = memberList[1] + [len(memberList[0])]
                memberList[2] = Symbol(
                    member.name.name, MType(partype, member.returnType), member.kind
                )
                memberList[4] = c
                self.visit(member, memberList)

    def visitMethodDecl(self, ast, c):
        parameter_list = []
        if ast.param:
            for param in ast.param:
                if self.lookup(param.variable.name, parameter_list, lambda x: x.name):
                    raise Redeclared(Parameter(), param.variable.name)
                else:
                    parameter_list = parameter_list + [Symbol(param.variable.name, param.varType, None)]
        c[0] = c[0] + parameter_list
        self.visit(ast.body, c)

    def visitAttributeDecl(self, ast, c):
        if type(ast.decl) == ConstDecl:
            variable_type = ast.decl.constType
            if self.lookup(ast.decl.constant.name, c[0][c[1][-1]:], lambda x: x.name):
                raise Redeclared(Attribute(), ast.decl.constant.name)
            if ast.decl.value is None:
                raise IllegalConstantExpression(None)
            value_type, value_kind = self.visit(ast.decl.value, c)
            if type(value_kind) != Constant:
                raise IllegalConstantExpression(ast.decl.value)
            if type(variable_type) == FloatType:
                if type(value_type) not in [FloatType, IntType]:
                    raise TypeMismatchInConstant(ast.decl)
            elif type(variable_type) != type(value_type):
                raise TypeMismatchInConstant(ast.decl)
            elif type(variable_type) == ArrayType:
                if type(variable_type.eleType) != type(value_type.eleType):
                    if type(variable_type.eleType) != FloatType and type(value_type.eleType) != IntType:
                        raise TypeMismatchInStatement(ast)
            return Symbol(ast.decl.constant.name, ast.decl.constType, Constant())
        elif type(ast.decl) == VarDecl:
            if self.lookup(ast.decl.variable.name, c[0][c[1][-1]:], lambda x: x.name):
                raise Redeclared(Attribute(), ast.decl.variable.name)
            variable_type = ast.decl.varType
            if ast.decl.varInit:
                value_type, value_kind = self.visit(ast.decl.varInit, c)
                if type(variable_type) == FloatType:
                    if type(value_type) not in [FloatType, IntType]:
                        raise TypeMismatchInStatement(ast.decl)
                elif type(variable_type) != type(value_type):
                    raise TypeMismatchInStatement(ast.decl)
                elif type(variable_type) == ArrayType:
                    if type(variable_type.eleType) != type(value_type.eleType):
                        if type(variable_type.eleType) != FloatType and type(value_type.eleType) != IntType:
                            raise TypeMismatchInStatement(ast)
            if type(variable_type) == ClassType:
                class_name = variable_type.classname.name
                if not self.lookup(class_name, c[4], lambda x: x.name):
                    raise Undeclared(Class(), class_name)
            return Symbol(ast.decl.variable.name, ast.decl.varType, None)

    def visitConstDecl(self, ast, c):
        if self.lookup(ast.constant.name, c[0][c[1][-1]:], lambda x: x.name):
            raise Redeclared(Constant(), ast.constant.name)
        variable_type = ast.constType
        if ast.value is None:
            raise IllegalConstantExpression(None)
        value_type, value_kind = self.visit(ast.value, c)
        if type(value_kind) != Constant:
            raise IllegalConstantExpression(ast.value)
        if type(variable_type) == FloatType and type(value_type) not in [FloatType, IntType]:
            raise TypeMismatchInConstant(ast)
        elif type(variable_type) != type(value_type):
            raise TypeMismatchInConstant(ast)
        elif type(variable_type) == ArrayType:
            if type(variable_type.eleType) != type(value_type.eleType):
                if type(variable_type.eleType) != FloatType and type(value_type.eleType) != IntType:
                    raise TypeMismatchInStatement(ast)
        return Symbol(ast.constant.name, ast.constType, Constant())

    def visitVarDecl(self, ast, c):
        if self.lookup(ast.variable.name, c[0][c[1][-1]:], lambda x: x.name):
            raise Redeclared(Variable(), ast.variable.name)
        variable_type = ast.varType
        if ast.varInit:
            value_type, value_kind = self.visit(ast.varInit, c)
            if type(variable_type) == FloatType:
                if type(value_type) not in [FloatType, IntType]:
                    raise TypeMismatchInStatement(ast)
            elif type(variable_type) != type(value_type):
                    raise TypeMismatchInStatement(ast)
            elif type(variable_type) == ArrayType:
                if type(variable_type.eleType) != type(value_type.eleType):
                    if type(variable_type.eleType) != FloatType and type(value_type.eleType) != IntType:
                        raise TypeMismatchInStatement(ast)
        if type(variable_type) is ClassType:
            class_name = variable_type.classname.name
            if not self.lookup(class_name, c[4], lambda x: x.name):
                raise Undeclared(Class(), class_name)
        return Symbol(ast.variable.name, ast.varType, None)

    def visitBlock(self, ast, c):
        decl_part = ast.decl
        stmt_part = ast.stmt
        for each_decl in decl_part:
            c[0] = c[0] + [self.visit(each_decl, c)]
        for stmt in stmt_part:
            if type(stmt) == For:
                c[3] = True
                self.visit(stmt, c)
                c[3] = False
            elif type(stmt) == Block:
                c[1] = c[1] + [len(c[0])]
                self.visit(stmt, c)
            elif type(stmt) == If:
                self.visit(stmt, c)
            elif type(stmt) in [Break, Continue]:
                if c[3] == False:
                    raise MustInLoop(stmt)
            else:
                self.visit(stmt, c)
        for y in range(c[1][-1], len(c[0])):
            c[0].pop()
        c[1].pop()

    def visitAssign(self, ast, c):
        lhs_type, lhs_kind = self.visit(ast.lhs, c)
        rhs_type, rhs_kind = self.visit(ast.exp, c)
        if type(lhs_kind) == Constant:
            raise CannotAssignToConstant(ast)
        if type(lhs_type) == FloatType:
            if type(rhs_type) not in [FloatType, IntType]:
                raise TypeMismatchInStatement(ast)
        elif type(lhs_type) != type(rhs_type):
            raise TypeMismatchInStatement(ast)

    def visitIf(self, ast, c):
        expr, kind = self.visit(ast.expr, c)
        if type(expr) != BoolType:
            raise TypeMismatchInStatement(ast)
        if type(ast.thenStmt) in [Break, Continue]:
            raise MustInLoop(ast.thenStmt)
        if type(ast.thenStmt) == Block:
            c[1] = c[1] + [len(c[0])]
        self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            if type(ast.elseStmt) in [Break, Continue]:
                raise MustInLoop(ast.elseStmt)

    def visitFor(self, ast, c):
        c[1] = c[1] + [len(c[0])]
        c[0] = c[0] + [Symbol(ast.id.name, IntType(), None)]
        expr1, kind = self.visit(ast.expr1, c)
        expr2, kind = self.visit(ast.expr2, c)
        if type(expr1) != IntType or type(expr2) != IntType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.loop, c)

    def visitReturn(self, ast, c):
        rhs_type, rhs_kind = self.visit(ast.expr, c)
        func = c[2]
        return_type = func.mtype.rettype
        if type(return_type) == FloatType:
            if type(rhs_type) not in [FloatType, IntType]:
                raise TypeMismatchInStatement(ast)
        elif type(return_type) != type(rhs_type):
            raise TypeMismatchInStatement(ast)

    def visitUnaryOp(self, ast, c):
        right_type, right_kind = self.visit(ast.body, c)
        if ast.op in ["+", "-"]:
            if type(right_type) not in [FloatType, IntType]:
                raise TypeMismatchInExpression(ast)
            else:
                return right_type, right_kind
        elif ast.op == "!":
            if type(right_type) == BoolType:
                return right_type, right_kind
            else:
                raise TypeMismatchInExpression(ast)
        return None

    def visitBinaryOp(self, ast, c):
        left_type, left_kind = self.visit(ast.left, c)
        right_type, right_kind = self.visit(ast.right, c)
        kind = None if None in [left_kind, right_kind] else Constant()
        if ast.op in ["&&", "||"]:
            if type(left_type) != BoolType or type(right_type) != BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType(), kind
        if type(left_type) in [IntType, FloatType] and type(right_type) in [IntType, FloatType]:
            if ast.op in ["<", "<=", ">", ">="]:
                return BoolType(), kind
            elif ast.op in ["+", "-", "*", "/", "\\", "%"]:
                if type(left_type) == type(right_type) and type(left_type) == IntType:
                    return IntType(), kind
                elif FloatType in [type(left_type), type(right_type)]:
                    return FloatType(), kind
        elif ast.op in ["==", "!="]:
            if type(left_type) != type(right_type) or type(right_type) not in [IntType, BoolType]:
                TypeMismatchInExpression(ast)
        elif ast.op in ["^"]:
            if type(left_type) != type(right_type) or type(right_type) != StringType:
                TypeMismatchInExpression(ast)
        else:
            if type(left_type) in [BoolType, StringType] or type(right_type) in [BoolType, StringType]:
                if ast.op in ["+", "-", "*", "/", "\\", "%"]:
                    raise TypeMismatchInExpression(ast)
                elif ast.op in ["<", "<=", ">", ">=", "!=", "=="] and StringType in [type(left_type),type(right_type)]:
                    raise TypeMismatchInExpression(ast)
            elif type(left_type) != type(right_type):
                raise TypeMismatchInExpression(ast)

    def visitFloatLiteral(self, ast, c):
        return FloatType(), Constant()

    def visitBooleanLiteral(self, ast, c):
        return BoolType(), Constant()

    def visitIntLiteral(self, ast, c):
        return IntType(), Constant()

    def visitArrayLiteral(self, ast, c):
        lit_type, lit_kind = self.visit(ast.value[0], c)
        for literal in ast.value[1:]:
            next_type, next_kind = self.visit(literal, c)
            if type(lit_type) != type(next_type):
                raise IllegalArrayLiteral(ast)
        return ArrayType(len(ast.value), lit_type), Constant()

    def visitStringLiteral(self, ast, c):
        return StringType(), Constant()

    def visitId(self, ast, c):
        item = self.lookup(ast.name, c[0][::-1], lambda x: x.name)
        if item is None:
            raise Undeclared(Identifier(), ast.name)
        kind = Constant() if type(item.kind) == Constant else None
        return item.mtype, kind

    def visitNewExpr(self, ast, c):
        class_instance = self.lookup(ast.classname.name, c[4], lambda x: x.name)
        if not class_instance:
            raise Undeclared(Class(), ast.classname.name)
        return ClassType(ast.classname), None

    def visitArrayCell(self, ast, c):
        return None

    def visitFieldAccess(self, ast, c):
        return None,None

    def visitCallStmt(self, ast, c):
        return None

    def visitCallExpr(self, ast, c):
        return None
