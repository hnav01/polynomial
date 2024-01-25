class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x) #call eval method of Int if p1 is Int object, else calls eval of class X if p1 is an object of class X. Same for p2.

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"

    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return "( " + repr(self.p1) + " ) - ( " + repr(self.p2) + " )"

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

# Test cases for division and subtraction
div_poly = Div(poly, Int(2))
sub_poly = Sub(poly, Mul(X(), Int(3)))

print(div_poly)
print(sub_poly)

result = poly.evaluate(-1)
print("Result:", result) #8

result1 = poly.evaluate(0)
print("Result1:", result1) #8

result2 = poly.evaluate(10)
print("Result2:", result2) #118
