class Parser(object):

    pass

class Empty(Parser):

    def isNullable(self):
        return False

    def isEmpty(self):
        return True

class Null(Parser):

    def isNullable(self):
        return True

    def isEmpty(self):
        return False

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
