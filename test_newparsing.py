from newparsing import *

def test_class():
    Empty
    Null
    Token
    And
    Or
    Action
    Forward

a = Token('a')
b = Token('b')
x = Forward()

def test_constructor():
    Empty()
    Null()
    And(a, b)
    Or(a, b)

def test_syntax():
    a + b
    a | b
    x << x

empty_and_empty = empty + empty
empty_and_null = empty + null
null_and_empty = null + empty
null_and_null = null + null
empty_or_empty = empty | empty
empty_or_null = empty | null
null_or_empty = null | empty
null_or_null = null | null

def test_isNullable():
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
    x << (x | empty)
    assert not x.isNullable()
    x << (x | null)
    assert x.isNullable()

def test_isEmpty():
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

def test_Forward_isEmpty():
    x << (x | empty)
    assert x.isEmpty()
    x << (x | null)
    assert not x.isEmpty()

def test_parse():
    alist = Forward()
    alist << (
        a + alist >> (lambda (a, b): [a] + b) |
        null >> (lambda a: []))
    assert alist.parse('aaaa') == [['a', 'a', 'a', 'a']]

    vs = Forward()
    l = Token('(') + vs + Token(')') >> (lambda ((a, b), c): b)
    v = a | l
    vs << (
        v + vs >> (lambda (a, b): [a] + b) |
        null >> (lambda a: []))
    assert l.parse('()') == [[]]
    assert l.parse('(a)') == [['a']]
    assert l.parse('(a(a))') == [['a', ['a']]]
