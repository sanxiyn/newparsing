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
empty_and_empty = And(empty, empty)
empty_and_null = And(empty, null)
null_and_empty = And(null, empty)
null_and_null = And(null, null)
empty_or_empty = Or(empty, empty)
empty_or_null = Or(empty, null)
null_or_empty = Or(null, empty)
null_or_null = Or(null, null)

def test_isNullable():
    a = Token('a')
    assert not empty.isNullable()
    assert null.isNullable()
    assert not a.isNullable()

def test_And_isNullable():
    assert not empty_and_empty.isNullable()
    assert not empty_and_null.isNullable()
    assert not null_and_empty.isNullable()
    assert null_and_null.isNullable()

def test_Or_isNullable():
    assert not empty_or_empty.isNullable()
    assert empty_or_null.isNullable()
    assert null_or_empty.isNullable()
    assert null_or_null.isNullable()

def test_Forward_isNullable():
    x = Forward()
    x << Or(x, null)
    assert x.isNullable()

def test_isEmpty():
    a = Token('a')
    assert empty.isEmpty()
    assert not null.isEmpty()
    assert not a.isEmpty()

def test_And_isEmpty():
    assert empty_and_empty.isEmpty()
    assert empty_and_null.isEmpty()
    assert null_and_empty.isEmpty()
    assert not null_and_null.isEmpty()

def test_Or_isEmpty():
    assert empty_or_empty.isEmpty()
    assert not empty_or_null.isEmpty()
    assert not null_or_empty.isEmpty()
    assert not null_or_null.isEmpty()
