import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    """test program rule"""

    def test_valid_program_rule_example_in_part_9_1(self):
        """Example program in part 9.1"""
        input = """
                class Example1 {
                    int factorial(int n){
                        if n == 0 then return 1; else return n * this.factorial(n - 1);
                    }
                    void main(){
                        int x;
                        x := io.readInt();
                        io.writeIntLn(this.factorial(x));
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_valid_program_rule_example_in_part_9_2(self):
        """Example program in part 9.2"""
        input = """
                class Shape {
                    float length,width;
                    float getArea() {}
                    Shape(float length,width){
                        this.length := length;
                        this.width := width;
                    }
                }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_valid_simple_program_one_class(self):
        """Simple program with 1 class"""
        input = """class simple1 {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_valid_simple_program_many_classes(self):
        """Simple program with many classes"""
        input = """class simple1 {}
                class simple2 {}
                class simple3 {}
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_program_rule_with_example_in_part_2_1(self):
        """Test program rule with the example in part 2.1"""
        input = """class Shape {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                float length,width;
                static int getNumOfShape() {
                    return numOfShape;
                    }
                }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_wrong_program_wrong_class_token(self):
        """Wrong program with wrong class keyword"""
        input = """classes simple1 {}"""
        expect = "Error on line 1 col 0: classes"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_wrong_program_missing_open_curly_bracket(self):
        """Wrong program with missing open bracket"""
        input = """class Shape 
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                float length,width;
                static int getNumOfShape() {
                    return numOfShape;
                    }
                }
                """
        expect = "Error on line 2 col 16: static"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_wrong_program_missing_end_curly_bracket(self):
        """Wrong program with missing close bracket"""
        input = """class Shape {
                static final int numOfShape = 0;
                final int immuAttribute = 0;
                float length,width;
                static int getNumOfShape() {
                    return numOfShape;
                    }

                """
        expect = "Error on line 9 col 16: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_wrong_program_empty_program(self):
        """Wrong program missing everything"""
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 209))

    """test classdecl rule"""

    def test_valid_class_declaration(self):
        """Simple class foo"""
        input = """
                class foo {
                    final static int foo1;
                    static final float foo2;
                    string foo3;
                    string printToscreen(){
                        io.writeStr(foo3);
                    }
                    void main(){
                        return 0;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_valid_class_declaration_with_null_memberlist(self):
        """This class is an empty class"""
        input = """class empty{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_valid_class_declaration_with_methodecl(self):
        """This class has memberlist: methoddecl"""
        input = """
                class methoddecl {
                    static int method1(){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_valid_class_declaration_with_attributedecl(self):
        """This class has memberlist: attributedecl"""
        input = """
                class attributedecl {
                    final static int My1stCons = 1 + 5,My2ndCons = 2;
                    static final int My3rdCons = 2, My4thCons= 1;
                    int x,y = 0;
                    float a,b,c;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_valid_class_declaration_with_constructor(self):
        """This class has memberlist: constructor"""
        input = """
                class constructorabc {
                    constructorabc(){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_valid_class_declaration_with_three_members(self):
        """This class has memberlist: attributedecl, methoddecl, constructor"""
        input = """
                class methodattriconstruc {
                    static int method1(){}
                    final static int My1stCons = 1 + 5,My2ndCons = 2;
                    static final int My3rdCons = 2, My4thCons= 1;
                    int x,y = 0;
                    float a,b,c;
                    methodattriconstruc(){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_valid_class_declaration_with_extends(self):
        """This class extends another class"""
        input = """
                class methodattriconstruc extends ABC {
                    static int method1(){}
                    final static int My1stCons = 1 + 5,My2ndCons = 2;
                    static final int My3rdCons = 2, My4thCons= 1;
                    int x,y = 0;
                    float a,b,c;
                    methodattriconstruc(){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_wrong_class_declaration_with_extends(self):
        """This class wrong because it has double extends keyword"""
        input = """
                class methodattriconstruc extends extends ABC {
                    static int method1(){}
                    final static int My1stCons = 1 + 5,My2ndCons = 2;
                    static final int My3rdCons = 2, My4thCons= 1;
                    int x,y = 0;
                    float a,b,c;
                    methodattriconstruc(){}
                }
                """
        expect = "Error on line 2 col 50: extends"
        self.assertTrue(TestParser.test(input, expect, 217))

    """test attributedecl rule"""

    def test_valid_attribute_declaration(self):
        """These are all kinds of different attribute declaration"""
        input = """
                class attributedecl {
                    static final int numOfclass = 1;
                    final static float numOfclass2 = 1.0;
                    static string text = "abc";
                    final boolean a = true;
                    int[5] a;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_valid_mutable_int_attribute_declaration(self):
        """This class has some integer mutable attributes"""
        input = """
                class mutableintatt {
                    static int numOfclass = 1;
                    int numOfclass2 = 2;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_valid_mutable_float_attribute_declaration(self):
        """This class has some float mutable attributes"""
        input = """
                class mutablefloatatt {
                    static float numOfclass = 1.0;
                    float numOfclass2 = 1.0e-12;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_valid_mutable_boolean_attribute_declaration(self):
        """This class has some boolean mutable attributes"""
        input = """
                class mutableboolatt {
                    static boolean a = true;
                    boolean b = false;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_valid_mutable_string_attribute_declaration(self):
        """This class has some string mutable attributes"""
        input = """
                class mutablestringatt {
                    static string text = "abc";
                    string text2 = "cde asd";
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_valid_immutable_int_attribute_declaration(self):
        """This class has some integer immutable attributes"""
        input = """
                class immutableintatt {
                    final static int numOfclass = 1;
                    int numOfclass2 = 2;
                    final int numOfclass3 = 3;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_valid_immutable_float_attribute_declaration(self):
        """This class has some float immutable attributes"""
        input = """
                class immutablefloatatt {
                    static float numOfclass = 1.0;
                    float numOfclass2 = 1.0e-12;
                    final float numOfclass3 = 3.;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_valid_immutable_boolean_attribute_declaration(self):
        """This class has some boolean immutable attributes"""
        input = """
                class immutableboolatt {
                    static boolean a = true;
                    boolean b = false;
                    final boolean numOfclass3 = true;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_valid_immutable_string_attribute_declaration(self):
        """This class has some string immutable attributes"""
        input = """
                class immutablestringatt {
                    static string text = "abc";
                    string text2 = "cde asd";
                    final string text3 = "immutable attribute";
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_valid_array_type_attribute_declaration(self):
        """This class has some array type immutable attributes"""
        input = """
                class immutablearraytypeatt {
                    static int[5] a = {1,2,3,4,5};
                    final static float[2] b = {1.0,2.2e-2};
                    final string[2] text = {"immutable attribute","mutable attribute"};
                    static final boolean[1] c = {true};
                    int[2] d ={1,6};
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_wrong_attribute_declaration_missing_attribute_name(self):
        """This class has attribute declaration that has no attributename/list"""
        input = """
                class missingattributename {
                    static int a = 1;
                    int ;
                }
                """
        expect = "Error on line 4 col 24: ;"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_wrong_attribute_declaration_missing_type(self):
        """This class has attribute declaration that has no attribute type"""
        input = """
                class missingattributetype {
                    static a = 1;
                }
                """
        expect = "Error on line 3 col 29: ="
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_wrong_attribute_declaration_missing_smcolon(self):
        """This class has attribute declaration that has no attribute type"""
        input = """
                class missingsemicolon {
                    static int a = 1
                }
                """
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 230))

    """test methoddecl rule"""

    def test_valid_methoddecl(self):
        """This class has valid method declarations"""
        input = """
                class validmethoddecl {
                    static int a() {}
                    static float b(float b) {}
                    static boolean c(boolean e,f) {}
                    static string d(string g,h;int i,j) {}
                    static void main() {return 0;}
                    int a1() {}
                    float b1(float b) {}
                    boolean c1(boolean e,f) {}
                    string d1(string g,h;int i,j) {}
                    void main1() {a := b; return 0;}
                    static int a2() {}
                    static float b2() {}
                    static boolean c2() {}
                    static string d2() {}
                    static void main2() {}
                    int a3() {}
                    float b3() {}
                    boolean c3() {}
                    string d3() {}
                    void main3() {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_empty_method(self):
        """This class has 5 empty methods"""
        input = """
                class emptymethod1 {
                    int empty1(){}
                    float empty2(){}
                    boolean empty3(){}
                    string empty4(){}
                    void empty5(){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_empty_static_method(self):
        """This class has 5 empty static methods"""
        input = """
                class emptymethod1 {
                    static int empty1(){}
                    static float empty2(){}
                    static boolean empty3(){}
                    static string empty4(){}
                    static void empty5(){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_static_method_with_one_parameter(self):
        """This class has 5 static methods that has 1 parameter"""
        input = """
                class staticmethodhas1parameter {
                    static int para(int parameter){}
                    static float para1(float parameter){}
                    static boolean para2(string parameter){}
                    static string para3(boolean parameter){}
                    static void para4(int[5] parameter){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_static_method_with_many_parameters_in_same_type(self):
        """This class has 5 static methods that has many parameters in the same type"""
        input = """
                class staticmethodhasmanyparameter {
                    static int para(int parameter, parameter2){}
                    static float para1(float parameter, parameter2){}
                    static boolean para2(string parameter, parameter2){}
                    static string para3(boolean parameter, parameter2){}
                    static void para4(int[5] parameter, parameter2){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_static_method_with_many_parameters_in_different_type(self):
        """This class has 5 static methods that has many parameters in different types"""
        input = """
                class staticmethodhasmanyparameter_differenttype {
                    static int para(int parameter, parameter2; float para3,para4){}
                    static float para1(float parameter, parameter2; string para5,para6){}
                    static boolean para2(string parameter, parameter2; int a,b,c){}
                    static string para3(boolean parameter, parameter2; int[2] arrays){}
                    static void para4(int[5] parameter, parameter2;int a,b;float c,d){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_empty_static_method_with_blockstmt(self):
        """This class has 4 static methods with blockstmt and no para"""
        input = """
                class emptymethod1 {
                    static int empty1(){
                        int a;
                        return a;
                    }
                    static float empty2(){
                        float b;
                        return b;
                    }
                    static boolean empty3(){
                        boolean abc = true;
                        return abc;
                    }
                    static string empty4(){
                        return "yes";
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_static_method_with_one_parameter_and_blockstmt(self):
        """This class has static methods that has 1 parameter and a blockstmt"""
        input = """
                class staticmethodhas1parameter {
                    static int para(int parameter){
                        parameter := 5 + 5;
                        return parameter;
                    }
                    static float para1(float parameter1){
                        return parameter - 1.0;
                    }
                    static boolean para2(string parameter2){
                        parameter2 := false;
                        return parameter || true;
                    }
                    static string para3(boolean parameter3){
                        parameter3 := "this is a string";
                        return parameter ^ "ABC";
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_static_method_with_many_parameters_and_a_blockstmt(self):
        """This class has static methods that has many parameters and a blockstmt"""
        input = """
                class staticmethodhasmanyparameter {
                    static int para(int parameter, parameter2){
                        int result =  parameter - parameter2;
                        return result;
                    }
                    static float para1(float parameter, parameter2){}
                    static boolean para2(string parameter, parameter2){}
                    static string para3(boolean parameter, parameter2){}
                    static void para4(int[5] parameter, parameter2){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_constructor(self):
        """This class has a constructor"""
        input = """
                class square {
                    square (float radius) {
                        this.radius := radius;
                    }
                    float area(float radius) {
                        return radius*3.14*radius;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_complete_method(self):
        """This class has a complete method"""
        input = """
                class Shape {
                    float length,width;
                    float getArea() {}
                    Shape(float length,width){
                        this.length := length;
                        this.width := width;
                    }
                }
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_wrong_method_missing_method_name(self):
        """This class has a method without method name"""
        input = """
                class example {
                    float (){}
                }
                """
        expect = "Error on line 3 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_wrong_method_missing_parameter_bracket(self):
        """This class has a method without parameter bracket"""
        input = """
                class example {
                    float methoda){}
                }
                """
        expect = "Error on line 3 col 33: )"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_wrong_method_missing_parameters_colon_separator(self):
        """This class has a method without parameter separator"""
        input = """
                class example {
                    float methoda(float a b){}
                }
                """
        expect = "Error on line 3 col 42: b"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_wrong_method_missing_parameters_semicolon_separator(self):
        """This class has a method without parameter separator"""
        input = """
                class example {
                    float methoda(float a,b int c){}
                }
                """
        expect = "Error on line 3 col 44: int"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_wrong_method_missing_blockstmt(self):
        """This class has a method without block statement"""
        input = """
                class example {
                    float methoda(float a,b; int c)
                }
                """
        expect = "Error on line 4 col 16: }"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_wrong_method_missing_blockstmt_open_bracket(self):
        """This class has a method without block statement open bracket"""
        input = """
                class example {
                    float methoda(float a,b; int c) }
                }
                """
        expect = "Error on line 3 col 52: }"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_wrong_method_missing_blockstmt_end_bracket(self):
        """This class has a method without block statement end bracket"""
        """this example it take the right curly bracket for the method, so => this is missing end bracket for class"""
        input = """
                class example {
                    float methoda(float a,b; int c) {
                        return a;
                }
                """
        expect = "Error on line 6 col 16: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 248))

    """test array type"""

    def test_valid_array_type(self):
        """This class has array type att and the method has array type parameter """
        input = """
                class example {
                    int[5] array_type_attribute;
                    float method(float a,b; int[2] c){}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_wrong_array_type_missing_end_bracket(self):
        """This class has wrong declaration of array type att"""
        input = """
                class example {
                    int[5 array_type_attribute;
                }
                """
        expect = "Error on line 3 col 26: array_type_attribute"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_wrong_array_type_missing_element_type(self):
        """This class has wrong declaration of array type att"""
        input = """
                class example {
                    [5] array_type_attribute;
                }
                """
        expect = "Error on line 3 col 20: ["
        self.assertTrue(TestParser.test(input, expect, 251))

    """test exp rule"""

    def test_relational_exp(self):
        """This class has valid relational expression"""
        input = """
                class example{
                void main(){
                    if x < y then continue;
                    if x <= y then continue;
                    if x > y then continue;
                    if x >= y then continue;
                    if x == y then continue;
                    if x != y then return 0;
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_and_or_exp(self):
        """This class has valid and or expression"""
        input = """
                class example{
                void main(){
                    boolean x,y;
                    if x || y then continue;
                    if x && y then continue;
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_arithmetic_exp(self):
        """This class has valid arithmetic expression"""
        input = """
                class example{
                void main(){
                    int x = 1,y = 2,z = 3;
                    float a = 2.0 ,b = 1.0;
                    if x ==  y + z then continue;
                    if x == y - z then continue;
                    if x == y * z then continue;
                    if x == y \\ z then continue;
                    if x == a / b then continue;
                    if x == y % z then continue;
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_string_concat_exp(self):
        """This class has valid string concatenation expression"""
        input = """
                class example{
                void main(){
                    string x = "abc",y = "cde";
                    string result;
                    result := x ^ y;
                    return result;                    
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_unary_exp(self):
        """This class has valid unary expression"""
        input = """
                class example{
                void main(){
                    int x = -3,y = +5;
                    string result;
                    result := x - y;
                    return result;                    
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_not_exp(self):
        """This class has valid not expression"""
        input = """
                class example{
                void main(){
                    boolean x = true,y = false;
                    string result;
                    result := !y;
                    return result;                    
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_double_not_exp(self):
        """This class has valid not expression: double not"""
        input = """
                class example{
                void main(){
                    boolean x = true,y = false;
                    string result;
                    result := !!y;
                    return result;                    
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    """test indexop"""

    def test_indexop(self):
        """This class has valid index operator"""
        input = """
                class example{
                void main(){
                    a[3+x.foo(2)] := a[b[2]] +3;
                    x.b[2] := x.m()[3];   
                    a[3] := b[2];
                    a[1] := 0;
                    a[2] := 5+5;  
                    a[1] := b[3] - b[2];          
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_indexop_with_memberaccess(self):
        """This class has valid index operator with memberacess"""
        input = """
                class example{
                void main(){
                    a[3+x.foo(2)] := a[b[2]] +3;
                    x.b[2] := x.m()[3];                
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_indexop_with_integer(self):
        """This class has valid index operator with integer"""
        input = """
                class example{
                void main(){
                    3[2] := 2[3];                
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_indexop_with_valid_operator(self):
        """This class has valid index operator with +,-,*,\\,%"""
        input = """
                class example{
                void main(){
                    a+b[2] := a[b[2]] + 3;
                    a-b[2] := a[b[2]] + 3;
                    a*b[2] := a[b[2]] + 3;
                    a\\b[2] := a[b[2]] + 3;
                    a%b[2] := a[b[2]] + 3;         
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_indexop_with_valid_this_keyword(self):
        """This class has valid index operator with this keyword"""
        input = """
                class example{
                void main(){
                    this.a[2] := 2;     
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_indexop_with_valid_this_id(self):
        """This class has valid index operator with id"""
        input = """
                class example{
                void main(){
                    thisisid.a[2] := 2;     
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_wrong_indexop_missing_bracket(self):
        """This class has invalid index operator: missing bracket"""
        input = """
                class example{
                void main(){
                    a[2 := 2;     
                }
                }
                """
        expect = "Error on line 4 col 24: :="
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_wrong_indexop_missing_exproplist_between_brackets(self):
        """This class has invalid index operator: missing exproplist"""
        input = """
                class example{
                void main(){
                    a[] := 2;     
                }
                }
                """
        expect = "Error on line 4 col 22: ]"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_wrong_indexop_invalid_float_between_brackets(self):
        """This class has invalid index operator: float can't be in the brackets"""
        input = """
                class example{
                void main(){
                    a[1.0] := 2;     
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_double_indexop(self):
        """This class has valid double index operator"""
        input = """
                class example{
                void main(){
                    a[3+x.foo(2)] := a[b[2]] +3;
                    a[b[3]] := 3;              
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_triple_indexop(self):
        """This class has valid triple index operator"""
        input = """
                class example{
                void main(){
                    a[3+x.foo(2)] := a[b[c[2]]] + 3;
                    a[b[c[3]]] := 3 + 1;              
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    """test member access"""

    def test_valid_instance_attribute_access(self):
        """This class has valid instance attribute access"""
        input = """
                class example{
                void main(){
                    this.foo := this.b;    
                }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_valid_static_attribute_access(self):
        """This class has valid static attribute access"""
        input = """
                class example{
                    void main(){
                        x.foo := a.b;       
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_valid_instance_method_invocation(self):
        """This class has valid instance method invocation"""
        input = """
                class example{
                    void main(){
                        this.foo() := this.b();        
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_valid_static_method_invocation(self):
        """This class has valid static method invocation"""
        input = """
                class example{
                void main(){
                    x.foo() := a.b();  
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_complex_member_access(self):
        """This class has valid member acceess"""
        input = """
                class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    """test object create"""

    def test_object_create(self):
        """This class has valid object create"""
        input = """
                class Rectangle{}
                class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_wrong_object_create_missing_id(self):
        """This class has invalid object create: missing id"""
        input = """
                class Rectangle{}
                class Example2 {
                    void main(){
                        s:= new ()
                    }
                }
                """
        expect = "Error on line 5 col 32: ("
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_wrong_object_create_missing_left_side_object(self):
        """This class has invalid object create: missing lhs object"""
        input = """
                class Rectangle{}
                class Example2 {
                    void main(){
                        new Rectangle()
                    }
                }
                """
        expect = "Error on line 6 col 20: }"
        self.assertTrue(TestParser.test(input, expect, 277))

    """test statement"""

    """test block statement"""

    def test_valid_empty_block_statement(self):
        """This class has empty block statement"""
        input = """
                class empty {
                    void emptyblock(){
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_valid_block_statement_with_only_vardecllist(self):
        """This class has valid block statement declaration: with only variables"""
        input = """
                class Example2 {
                    void main(){
                        float r,s;
                        int[5] a,b;
                    }
                }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_valid_block_statement_with_only_stmt(self):
        """This class has valid block statement declaration: with only stmts"""
        input = """
                class Example2 {
                    void main(){
                        r:=2.0;
                        continue;
                        return none;
                    }
                }
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_wrong_block_stmt_wrong_order(self):
        """The block statement has wrong order: stmt -> var"""
        input = """
                class Example2 {
                    void main(){
                        r:=2.0;
                        s:=r*r*this.myPI;
                        a[0]:= s;
                        float r,s;
                        int[5] a,b;
                    }
                }
                """
        expect = "Error on line 7 col 24: float"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_valid_method_block_stmt_with_comment(self):
        """The method in this class has valid block statement with comment inside of it"""
        input = """
                class Example2 {
                    void main(){
                        #start of declaration part
                        float r,s;
                        int[5] a,b;
                        #list of statements
                        r:=2.0;
                        s:=r*r*this.myPI;
                        a[0]:= s;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_asmstmt(self):
        """Test assignment statement"""
        input = """
                class Example2 {
                    void assignmentSTMT(){
                        this.aPI := 3.14;
                        value := x.foo(5);
                        l[3] := value * 2;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_if_stmt(self):
        """Test if statement"""
        input = """
                class Example2 {
                    void ifelsestmt(){
                        if flag then
                            io.writeStrLn("Expression is true");
                        else
                            io.writeStrLn ("Expression is false");
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_if_stmt_without_else(self):
        """Test if statement without else part"""
        input = """
                class Example2 {
                    void ifstmt(){
                        if flag then
                            io.writeStrLn("Expression is true");
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_for_to_stmt(self):
        """Test for to statement"""
        input = """
                class Example2 {
                    void forto(){
                        for i := 1 to 100 do {
                            io.writeIntLn(i);
                            Intarray[i] := i + 1;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_for_downto_stmt(self):
        """Test for downto statement"""
        input = """
                class Example2 {
                    void fordownto(){
                        for x := 5 downto 2 do
                            io.writeIntLn(x);
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_for_downto_stmt_with_block_stmt(self):
        """Test for downto statement with block statement"""
        input = """
                class Example2 {
                    void fordownto(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            return x;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_for_to_stmt_with_block_stmt(self):
        """Test for to statement with block statement"""
        input = """
                class Example2 {
                    void forto(){
                        for x := 5 to 2 do {
                            io.writeIntLn(x);
                            return x;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_break_stmt(self):
        """Test break statement"""
        input = """
                class Example2 {
                    void breakstmt(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            if x == 3 then break;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_continue_stmt(self):
        """Test continue statement"""
        input = """
                class Example2 {
                    void continuestmt(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            if x == 3 then continue;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_return_stmt(self):
        """Test return statement"""
        input = """
                class Example2 {
                    void assignmentSTMT(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            if x == 3 then return 0; else return x+1;
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_method_invocation_stmt(self):
        """Test method invocation statement"""
        input = """
                class Shape {
                    static int getNumOfShape(){}
                }
                class Example2 {
                    void getSum(){
                        Shape s;
                        s.getNumOfShape();
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_object_create_stmt(self):
        """Test object create statement"""
        input = """
                class Shape {
                    static int getNumOfShape(){}
                }
                class Bob {
                }
                class Example2 {
                    void getSum(){
                        Shape s;
                        Bob a;
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_wrong_assignment_stmt(self):
        """Wrong asm token"""
        input = """
                class Example2 {
                    void assignmentSTMT(){
                        value := x.foo(5);
                        l[3] := value * 2;
                        this.aPI = 3.14;
                    }
                }
                """
        expect = "Error on line 6 col 33: ="
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_wrong_if_stmt(self):
        """Wrong if token"""
        input = """
                class Example2 {
                    void ifstmt(){
                        IF flag then
                            io.writeStrLn("Expression is true");
                    }
                }
                """
        expect = "Error on line 4 col 32: then"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_wrong_for_stmt(self):
        """Wrong for token"""
        input = """
                class Example2 {
                    void forto(){
                        For x := 5 to 2 do {
                            io.writeIntLn(x);
                            return x;
                        }
                    }
                }
                """
        expect = "Error on line 4 col 30: :="
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_wrong_break_stmt(self):
        """Test wrong break statement: missing semicolon"""
        input = """
                class Example2 {
                    void breakstmt(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            if x == 3 then break
                        }
                    }
                }
                """
        expect = "Error on line 5 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_wrong_continue_stmt(self):
        """Test wrong continue statement: missing semicolon"""
        input = """
                class Example2 {
                    void breakstmt(){
                        for x := 5 downto 2 do {
                            io.writeIntLn(x);
                            if x == 3 then continue
                        }
                    }
                }
                """
        expect = "Error on line 5 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_full_program(self):
        input = """
                #this is class example 1
                class Example1 {
                    int factorial(int n){
                        if n == 0 then return 1; else return n * this.factorial(n - 1);
                    }
                    void main(){
                        int x;
                        x := io.readInt();
                        io.writeIntLn(this.factorial(x));
                        }
                }
                /* this is
                class shape
                which is quite
                interesting!!! */
                class Shape {
                    float length,width;
                    float getArea() {}
                    Shape(float length,width){
                        this.length := length;
                        this.width := width;
                    }
                }
                # Here u have inheritance which is a characteristic of OOP
                class Rectangle extends Shape {
                    float getArea(){
                        return this.length*this.width;
                    }
                }
                class Triangle extends Shape {
                    float getArea(){
                        return this.length*this.width / 2;
                    }
                }
                # And all of the comment are skipped. /*This block comment don't have meaning in the line comment*/
                class Example2 {
                    void main(){
                        Shape s;
                        s := new Rectangle(3,4);
                        io.writeFloatLn(s.getArea());
                        s := new Triangle(3,4);
                        io.writeFloatLn(s.getArea());
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))











