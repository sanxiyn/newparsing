class Parser(object):

    pass

class Empty(Parser):

    def isNullable(self):
        return False

class Null(Parser):

    def isNullable(self):
        return True

class Token(Parser):

    def __init__(self, token):
        self.token = token

    def isNullable(self):
        return False

class And(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def isNullable(self):
        return self.first.isNullable() and self.second.isNullable()

class Or(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def isNullable(self):
        return self.first.isNullable() or self.second.isNullable()

class Action(Parser):

    pass

class Forward(Parser):

    def __lshift__(self, parser):
        self.parser = parser
