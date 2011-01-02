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

    def parseNull(self):
        return []

    def derive(self, token):
        return empty

empty = Empty()

class Null(Parser):

    def __init__(self, result=None):
        if result is None:
            result = [None]
        self.result = result

    def isNullable(self):
        return True

    def isEmpty(self):
        return False

    def parseNull(self):
        return self.result

    def derive(self, token):
        return empty

null = Null()

class Token(Parser):

    def __init__(self, token):
        self.token = token

    def isNullable(self):
        return False

    def isEmpty(self):
        return False

    def parseNull(self):
        return []

    def derive(self, token):
        if self.token == token:
            return Null([token])
        return empty

class And(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def isNullable(self):
        return self.first.isNullable() and self.second.isNullable()

    def isEmpty(self):
        return self.first.isEmpty() or self.second.isEmpty()

    def parseNull(self):
        result = []
        for a in self.first.parseNull():
            for b in self.second.parseNull():
                result.append((a, b))
        return result

    def derive(self, token):
        if self.first.isNullable():
            return (self.first.derive(token) + self.second |
                    Null(self.first.parseNull()) + self.second.derive(token))
        return self.first.derive(token) + self.second

class Or(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def isNullable(self):
        return self.first.isNullable() or self.second.isNullable()

    def isEmpty(self):
        return self.first.isEmpty() and self.second.isEmpty()

    def parseNull(self):
        result = []
        for a in self.first.parseNull():
            if a not in result:
                result.append(a)
        for b in self.second.parseNull():
            if b not in result:
                result.append(b)
        return result

    def derive(self, token):
        if self.first.isEmpty():
            return self.second.derive(token)
        if self.second.isEmpty():
            return self.first.derive(token)
        return self.first.derive(token) | self.second.derive(token)

class Action(Parser):

    pass

class Forward(Parser):

    def __lshift__(self, parser):
        self.parser = parser
        self.isNullable_called = False
        self.isNullable_value = False
        self.isEmpty_called = False
        self.isEmpty_value = True
        self.parseNull_called = False
        self.parseNull_value = []
        self.cache = {}

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

    def parseNull(self):
        if self.parseNull_called:
            return self.parseNull_value
        self.parseNull_called = True
        while True:
            value = self.parser.parseNull()
            if self.parseNull_value == value:
                break
            self.parseNull_value = value
        return value

    def derive(self, token):
        if token in self.cache:
            return self.cache[token]
        derivative = self.parser.derive(token)
        self.cache[token] = derivative
        return derivative
