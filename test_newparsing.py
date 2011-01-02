from newparsing import *

def test_class():
    Parser
    Empty
    Null
    Token
    And
    Or
    Action

def test_constructor():
    Empty()
    Null()
    a = Token('a')
    b = Token('b')
    And(a, b)
    Or(a, b)

def test_recursive():
    a = Token('a')
    alist = Forward()
    alist << Or(And(a, alist), Null())
