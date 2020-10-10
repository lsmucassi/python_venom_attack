class Expr:
    pass

class Times (Expr):
    '''
        multiplication handler
    '''
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + "x" + str(self.right)

class Plus (Expr):
    '''
        addition handler
    '''
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + "+" + str(self.right)

class Const (Expr):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

class Var (Expr):
        def __init__(self, name):
            self.name = name
        
        def __str__(self):
            return self.name


e1 = Times(Const(3),Plus(Var("y"), Var("x")))
e2 = Plus(Times(Const(3), Var("y")), Var("x"))

print(e1)
print(e2)