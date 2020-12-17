#using class

class A:
    a=10
    b=20
    def __init__(self,x,y):
        x=x
        y=y
        print(x,y)
        
    def f1(self):
        print(self.a)
        d=100
        print(d)
    def f2(self):
        pass
        
obj1 = A(200,300)
obj1.f1()


