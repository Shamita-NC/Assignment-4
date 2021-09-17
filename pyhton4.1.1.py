class sides:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
class A(sides):
    def area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
obj = A(3,4,5)
print("Area of triangle : {}".format(obj.area()))