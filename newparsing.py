class Parser(object):

    pass

class Empty(Parser):

    pass

class Null(Parser):

    pass

class Token(Parser):

    def __init__(self, token):
        self.token = token

class And(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

class Or(Parser):

    def __init__(self, first, second):
        self.first = first
        self.second = second

class Action(Parser):

    pass

class Forward(Parser):

    def __lshift__(self, parser):
        self.parser = parser
