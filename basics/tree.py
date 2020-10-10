class Expr:
    pass

class Times (Expr):
    '''
        multiplication handler
    '''
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Plus (Expr):
    '''
        addition handler
    '''
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Const (Expr):
    def __init__(self, val):
        self.val = val

class Var (Expr):
        def __init__(self, name):
            self.name = name


e1 = Times(Const(3),Plus(Var("y"), Var("x")))