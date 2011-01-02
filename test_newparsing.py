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

empty = Empty()
null = Null()

def test_isNullable():
    a = Token('a')
    assert not empty.isNullable()
    assert null.isNullable()
    assert not a.isNullable()

def test_And_isNullable():
    empty_and_empty = And(empty, empty)
    empty_and_null = And(empty, null)
    null_and_empty = And(null, empty)
    null_and_null = And(null, null)
    assert not empty_and_empty.isNullable()
    assert not empty_and_null.isNullable()
    assert not null_and_empty.isNullable()
    assert null_and_null.isNullable()

def test_Or_isNullable():
    empty_or_empty = Or(empty, empty)
    empty_or_null = Or(empty, null)
    null_or_empty = Or(null, empty)
    null_or_null = Or(null, null)
    assert not empty_or_empty.isNullable()
    assert empty_or_null.isNullable()
    assert null_or_empty.isNullable()
    assert null_or_null.isNullable()
