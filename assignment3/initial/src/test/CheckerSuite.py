import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_redeclared_class(self):
        input = """class a{}
        class a{}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_attribute_class_scope_same_type(self):
        input = """
        class a{
        int b;
        int b;
        }
        """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_attribute_class_scope_diff_type(self):
        input = """
        class a{
        int b;
        float b;
        }
        """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_var_method_scope_same_type(self):
        input = """
        class a{
        int foo(){
        int b;
        int b;
        return 0;
        }
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_var_method_scope_diff_type(self):
        input = """
        class a{
        int foo(){
        int b;
        float b;
        return 0;
        }
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_var_block_scope_same_type(self):
        input = """
        class a{
        int foo(){
            if true then
            {
                int b;
                int b;
            }
            else return 0;
        }
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_var_block_scope_diff_type(self):
        input = """
        class a{
        int foo(){
            if true then
            {
                int b;
                float b;
            }
            else return 0;
        }
        }
        """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_constant_attr_same_type(self):
        input = """
        class a{
            final int b = 5;
            final int b = 5;
        }
        """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_constant_attr_diff_type(self):
        input = """
        class a{
            final int b = 5;
            final float b = 5.0;
        }
        """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_constant_in_function_same_type(self):
        input = """
        class a{
        float getb(){
            final int b = 5;
            final int b = 5;
            return b;
        }
        }
        """
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_redeclared_constant_in_function_diff_type(self):
        input = """
        class a{
        float getb(){
            final int b = 5;
            final float b = 5.0;
            return b;
        }
        }
        """
        expect = "Redeclared Constant: b"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_redeclared_attribute(self):
        input = """
        class a{
            int b;
            float b;
        }
        """
        expect = "Redeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_redeclared_class_simple(self):
        input = """class a{}
        class b{}
        class a{}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_class_after_many_class(self):
        input = """class a{}
        class b{}
        class c{}
        class d{}
        class a{}
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_class_simple_body(self):
        input = """
        class a{
            int a;
            int b;
        }
        class a{
            int c;
            int d;
        }
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_redeclared_class_detail_body(self):
        input = """
        class a{
            int a;
            int foo(){
                int a;
                a := 10;
                return a;
            }
        }
        class a{
            float a;
            float foo(){
                float b;
                b := 5.5;
                return b;
            }

        }
        """
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_redeclared_static_attribute_same_type(self):
        input = """
        class a{
            static int a;
            static int a;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_redeclared_static_attribute_diff_type(self):
        input = """
        class a{
            static int a;
            static float a;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_redeclared_var_multiple_scope(self):
        input = """
        class a{
            int b;
            int foo1(){
                int a;
                float b;
                return a;
            }

            int foo2(){
                int a;
                int a;
                return a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_redeclared_method_simple_same_type_single_class(self):
        input = """
        class a{
            int foo(){
                return 0;
            }
            int foo(){
                return 0;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_redeclared_method_simple_diff_type_single_class(self):
        input = """
        class a{
            int foo(){
                return 0;
            }
            float foo(){
                return 0;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_redeclared_method_simple_same_type_multiple_class(self):
        input = """
        class a{
            int foo(){
                return 0;
            }
        }
        class b{
            int foo(){
                return 0;
            }
            int foo1(){
                return 0;
            }
            int foo1(){
                return 0;
            }
        }
        """
        expect = "Redeclared Method: foo1"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_redeclared_method_simple_diff_type_multiple_class(self):
        input = """
        class a{
            int foo(){
                return 0;
            }
        }
        class b{
            boolean foo(){
                return 0;
            }
            int foo1(){
                return 0;
            }
            float foo1(){
                return 0;
            }
        }
        """
        expect = "Redeclared Method: foo1"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_redeclared_method_detail_same_type_single_class(self):
        input = """
        class a{
            int foo(){
                int a;
                a := 10 + 10;
                return a;
            }
            int foo(){
                int b;
                b := 10 + 10;
                return b;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_redeclared_method_detail_diff_type_single_class(self):
        input = """
        class a{
            int foo(){
                int a;
                a := 10 + 10;
                return a;
            }
            float foo(){
                float b;
                b := 10 + 0.5;
                return b;
            }
        }
        """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_redeclared_method_detail_same_type_multiple_class(self):
        input = """
        class a{
            int foo(){
                int a;
                a := 10;
                return a;
            }
        }
        class b{
            int foo(){
                int a;
                a := 10;
                return a;
            }
            int foo1(){
                int b;
                b := 1;
                return b;
            }
            int foo1(){
                int c;
                c := 34;
                return c;
            }
        }
        """
        expect = "Redeclared Method: foo1"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_redeclare_para_simple_single_para_same_type(self):
        input = """
        class a{
            int foo(int a){
                int a;
                a := 0;
                return a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_redeclare_para_simple_single_para_diff_type(self):
        input = """
        class a{
            int foo(int a){
                float a;
                a := 0;
                return a;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_redeclare_para_simple_multiple_para_same_type(self):
        input = """
        class a{
            int foo(int a, b, c){
                int d;
                int c;
                a := 0;
                return a;
            }
        }
        """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_redeclare_para_simple_multiple_para_diff_type(self):
        input = """
         class a{
             int foo(int a; float b; boolean c){
                 int d;
                 float c;
                 a := 0;
                 return a;
             }
         }
         """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_redeclare_para_in_para_declaration_same_type(self):
        input = """
         class a{
             int foo(int b, b){
                 int a;
                 a := 10;
                 return a;
             }
         }
         """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_redeclare_para_in_para_declaration_same_type_2(self):
        input = """
         class a{
             int foo(int b; int b){
                 int a;
                 a := 10;
                 return a;
             }
         }
         """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_redeclare_para_in_para_declaration_diff_type(self):
        input = """
         class a{
             int foo(int b; float b){
                 int a;
                 a := 10;
                 return a;
             }
         }
         """
        expect = "Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input, expect, 432))
#next
    def test_undeclared_attribute_in_left_hand_side(self):
        input = """
         class abc{
             int a;
             int func(){
             b := 10;
             }
         }
         """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_undeclared_attribute_in_right_hand_side(self):
        input = """
         class abc{
             int a;
             int func(){
             a := b;
             }
         }
         """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_undeclared_variable_in_method_in_left_hand_side(self):
        input = """
         class abc{
             int a;
             int foo(){
                c := 10;
                return b;
             }
         }
         """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_undeclared_variable_in_method_in_right_hand_side(self):
        input = """
         class abc{
             int a;
             int foo(){
                c := 10;
                return b;
             }
         }
         """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_undeclare_parent_class(self):
        input = """
        class SON extends MOM{
        }
         """
        expect = "Undeclared Class: MOM"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_undeclare_parent_class_many_classes(self):
        input = """
        class SON extends MOM{}
        class MOM extends SOMEONE{
        }
         """
        expect = "Undeclared Class: SOMEONE"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_cannot_assign_to_const_in_class(self):
        input = """
        class ABC{
            final int constant = 10;
            int foo(){
            constant := 100;
            return a;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(constant),IntLit(100))"
        self.assertTrue(TestChecker.test(input, expect, 439))
#gere
    def test_cannot_assign_to_const_method_scope(self):
        input = """
        class ABC{
            int func(){
                final int constant = 10;
                constant := 100;
                return constant;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(constant),IntLit(100))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_cannot_assign_to_const_with_variable(self):
        input = """
        class ABC{
        int func(){
            final int constant = 10;
            int variable = 100;
            constant := variable;
        }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(constant),Id(variable))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_cannot_assign_to_const_with_variable_diff_type(self):
        input = """
        class ABC{
        int func(){
            final int constant = 10;
            float variable = 100;
            constant := variable;
        }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(constant),Id(variable))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_cannot_assign_to_const_with_float(self):
        input = """
        class ABC{
            final int constant = 10;
            int func(){
            constant := 10.5;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(constant),FloatLit(10.5))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_cannot_assign_to_const_with_bool(self):
        input = """
        class ABC{
            final int constant = 10;
            int func(){
            constant := true;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(constant),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_undeclare_class_object(self):
        input = """
        class A{
        }
        class C{
            A a;
            B b;
        }

        """
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_undeclare_class_object_in_function(self):
        input = """
         class A{
             int foo(){
                B b;
                return a;
             }
        }
        """
        expect = "Undeclared Class: B"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_undeclare_class_in_function_multiple_class(self):
        input = """
        class A{
        }
        class B{
        }
        class C{
        int foo(){
            A a;
            B b;
            D c;
        }
        }
        """
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_undeclare_class_in_function_multiple_class_2(self):
        input = """
        class A{
        }
        class C{
        int foo(){
            A a;
            B b;
            D c;
        }
        }
        class B{
        }
        """
        expect = "Undeclared Class: D"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_type_mismatch_if_stmt_int_lit(self):
        input = """
         class A{
            int foo(){
                if 1 then
                {
                    int a = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(IntLit(1),Block([VarDecl(Id(a),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_type_mismatch_if_stmt_float_lit(self):
        input = """
         class A{
            int foo(){
                if 1.5 then
                {
                    int a = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(FloatLit(1.5),Block([VarDecl(Id(a),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_type_mismatch_if_stmt_int_var(self):
        input = """
         class A{
            int foo(){
                int a = 10;
                if a then
                {
                    int b = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([VarDecl(Id(b),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_type_mismatch_if_stmt_float_var(self):
        input = """
         class A{
            int foo(){
                float a = 1.5;
                if a then
                {
                    int b = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(Id(a),Block([VarDecl(Id(b),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_type_mismatch_if_stmt_plus_op(self):
        input = """
         class A{
            int foo(){
                if 10 + 10 then
                {
                    int b = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,IntLit(10),IntLit(10)),Block([VarDecl(Id(b),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_type_mismatch_if_stmt_sub_op(self):
        input = """
         class A{
            int foo(){
                if 10 - 10 then
                {
                    int b = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(-,IntLit(10),IntLit(10)),Block([VarDecl(Id(b),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_type_mismatch_if_stmt_mul_op(self):
        input = """
         class A{
            int foo(){
                if 10 * 10 then
                {
                    int b = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(*,IntLit(10),IntLit(10)),Block([VarDecl(Id(b),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_type_mismatch_if_stmt_div_op(self):
        input = """
         class A{
            int foo(){
                if 10 / 10 then
                {
                    int b = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(/,IntLit(10),IntLit(10)),Block([VarDecl(Id(b),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_type_mismatch_if_stmt_remain_op(self):
        input = """
         class A{
            int foo(){
                if 10 % 10 then
                {
                    int b = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: If(BinaryOp(%,IntLit(10),IntLit(10)),Block([VarDecl(Id(b),IntType,IntLit(10))],[Return(IntLit(0))]))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_type_mismatch_for_stmt_wrong_exp1_float_lit(self):
        input = """
         class A{
            int foo(){
                for i:= 1.5 to 100 do
                {
                    int a = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),FloatLit(1.5),IntLit(100),True,Block([VarDecl(Id(a),IntType,IntLit(10))],[Return(IntLit(0))])])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_type_mismatch_for_stmt_wrong_exp1_bool_lit(self):
        input = """
         class A{
            int foo(){
                for i:= true to 100 do
                {
                    int a = 10;
                    return a;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),BooleanLit(True),IntLit(100),True,Block([VarDecl(Id(a),IntType,IntLit(10))],[Return(Id(a))])])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_type_mismatch_for_stmt_wrong_exp2_float_lit(self):
        input = """
         class A{
            int foo(){
                for i:= 1 to 100.5 do
                {
                    int a = 10;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),FloatLit(100.5),True,Block([VarDecl(Id(a),IntType,IntLit(10))],[Return(IntLit(0))])])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_type_mismatch_for_stmt_wrong_exp2_bool_lit(self):
        input = """
         class A{
         float a;
            int foo(){
                for i:= 1 to a do
                {
                    int a = 0;
                    return 0;
                }
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),Id(a),True,Block([VarDecl(Id(a),IntType,IntLit(0))],[Return(IntLit(0))])])"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_type_mismatch_for_stmt_wrong_exp_float_var(self):
        input = """
         class A{
         int a;
            int foo(){
                float b = 1.5;
                for i:= 1 to b do a := 0;
                return 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),Id(b),True,AssignStmt(Id(a),IntLit(0))])"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_type_mismatch_for_stmt_wrong_exp_add_op(self):
        input = """
         class A{
            int foo(){
                float b = 1.5;
                for i:= 1 to b + 1 do a := 0;
                return 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),BinaryOp(+,Id(b),IntLit(1)),True,AssignStmt(Id(a),IntLit(0))])"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_type_mismatch_for_stmt_wrong_exp_add_op_float(self):
        input = """
         class A{
            int foo(){
                for i:= 1 to 1.5 + 10 do a := 0;
                return 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),BinaryOp(+,FloatLit(1.5),IntLit(10)),True,AssignStmt(Id(a),IntLit(0))])"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_type_mismatch_for_stmt_wrong_exp_bool_op(self):
        input = """
         class A{
            int foo(){
                for i:= 1 to true && false do a := 0;
                return 0;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),BinaryOp(&&,BooleanLit(True),BooleanLit(False)),True,AssignStmt(Id(a),IntLit(0))])"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_assign_int_to_float_lit(self):
        input = """
        class A{
            int a = 1.5;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,FloatLit(1.5))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_assign_int_to_float_var(self):
        input = """
        class A{
            float b = 1.5;
            int a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_assign_int_to_bool_lit(self):
        input = """
        class A{
            int a = true;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_assign_int_to_bool_var(self):
        input = """
        class A{
            boolean b = true;
            int a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_assign_int_to_str_lit(self):
        input = """
        class A{
            int a = "abc";
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_assign_int_to_str_var(self):
        input = """
        class A{
            string b = "abc";
            int a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),IntType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_assign_float_to_bool_lit(self):
        input = """
        class A{
            float a = false;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),FloatType,BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_assign_float_to_bool_var(self):
        input = """
        class A{
            boolean b = true;
            float a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),FloatType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_assign_float_to_str_lit(self):
        input = """
        class A{
            float a = "abc";
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),FloatType,StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_assign_float_to_str_var(self):
        input = """
        class A{
            string b = "abc";
            float a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),FloatType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_assign_bool_to_int_lit(self):
        input = """
        class A{
            boolean a = 1;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),BoolType,IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_assign_bool_to_int_var(self):
        input = """
        class A{
            int b = 1;
            boolean a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),BoolType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_assign_bool_to_float_lit(self):
        input = """
        class A{
            boolean a = 1.5;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),BoolType,FloatLit(1.5))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_assign_bool_to_float_var(self):
        input = """
        class A{
            float b = 1.5;
            boolean a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),BoolType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_assign_bool_to_str_lit(self):
        input = """
        class A{
            boolean a = "abc";
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),BoolType,StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_assign_bool_to_str_var(self):
        input = """
        class A{
            string b = "abc";
            boolean a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),BoolType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_assign_str_to_int_lit(self):
        input = """
        class A{
            string a = 10;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,IntLit(10))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_assign_str_to_int_var(self):
        input = """
        class A{
            int b = 10;
            string a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_assign_str_to_float_lit(self):
        input = """
        class A{
            string a = 10.5;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,FloatLit(10.5))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_assign_str_to_float_var(self):
        input = """
        class A{
            float b = 10.5;
            string a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_assign_str_to_bool_lit(self):
        input = """
        class A{
            string a = true;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_assign_str_to_bool_var(self):
        input = """
        class A{
            boolean b = false;
            string a = b;
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),StringType,Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_illegal_constant_exp_none(self):
        input = """
        class A{
            final int a;
        }
        """
        expect = "Illegal Constant Expression: None"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_illegal_constant_exp_id(self):
        input = """
        class A{
            int b;
            final int a = b;
        }
        """
        expect = "Illegal Constant Expression: Id(b)"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_type_mismatch_constant_exp_type(self):
        input = """
        class A{
            final int a = 5.4;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),IntType,FloatLit(5.4))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_type_mismatch_constant_float_not_int_float(self):
        input = """
        class A{
            final float a = true;
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(a),FloatType,BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_break_must_in_loop(self):
        input = """
                class A{
                int foo(){
                    for i:=0 to 5 do {
                        i := i + 1;
                    }
                    break;
                }
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_continue_must_in_loop(self):
        input = """
                class A{
                int foo(){
                    for i:=0 to 5 do {
                        i := i + 1;
                    }
                    continue;
                }
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_break_must_in_if(self):
        input = """
                class A{
                static int i;
                int foo(){
                    if true then 
                    {
                        i := i + 1;
                    }
                    break;
                }
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_continue_must_in_if(self):
        input = """
                class A{
                static int i;
                int foo(){
                    if true then 
                    {
                        i := i + 1;
                    }
                    continue;
                }
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_2break_must_in_loop(self):
        input = """
                class A{
                int foo(){
                    for i:=0 to 5 do {
                        i := i + 1;
                        break;
                    }
                    break;
                }
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_2continue_must_in_loop(self):
        input = """
                class A{
                int foo(){
                    for i:=0 to 5 do {
                        i := i + 1;
                        continue;
                    }
                    continue;
                }
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_2break_must_in_if(self):
        input = """
                class A{
                static int i;
                int foo(){
                    if true then 
                    {
                        i := i + 1;
                        break;
                    }
                    break;
                }
                }
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_2continue_must_in_if(self):
        input = """
                class A{
                static int i;
                int foo(){
                    if true then 
                    {
                        i := i + 1;
                        continue;
                    }
                    continue;
                }
                }
                """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 499))
