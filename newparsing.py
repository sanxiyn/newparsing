__all__ = ['Empty', 'Null', 'Token', 'And', 'Or', 'Action', 'Forward',
    'empty', 'null']

class Parser(object):

    def __add__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

class Empty(Parser):

    def isNullable(self):
        return False

    def isEmpty(self):
        return True

empty = Empty()

class Null(Parser):

    def isNullable(self):
        return True

    def isEmpty(self):
        return False

null = Null()

class Token(Parser):

    def __init__(self, token):
        self.token = token

    def isNullable(self):
        return False

    def isEmpty(self):
        return False

class And(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def isNullable(self):
        return self.first.isNullable() and self.second.isNullable()

    def isEmpty(self):
        return self.first.isEmpty() or self.second.isEmpty()

class Or(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def isNullable(self):
        return self.first.isNullable() or self.second.isNullable()

    def isEmpty(self):
        return self.first.isEmpty() and self.second.isEmpty()

class Action(Parser):

    pass

class Forward(Parser):

    def __lshift__(self, parser):
        self.parser = parser
        self.isNullable_called = False
        self.isNullable_value = False
        self.isEmpty_called = False
        self.isEmpty_value = True

    def isNullable(self):
        if self.isNullable_called:
            return self.isNullable_value
        self.isNullable_called = True
        while True:
            value = self.parser.isNullable()
            if self.isNullable_value == value:
                break
            self.isNullable_value = value
        return value

    def isEmpty(self):
        if self.isEmpty_called:
            return self.isEmpty_value
        self.isEmpty_called = True
        while True:
            value = self.parser.isEmpty()
            if self.isEmpty_value == value:
                break
            self.isEmpty_value = value
        return value

