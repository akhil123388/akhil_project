class A:
    def foo(self):
        print ("A Class foo")

class B:
    def foo(self):
        print ("B Class foo")



class C(A, B):
    def foo(self):
        print ("C Class foo")


c = C()
c.foo() # C - A - B
