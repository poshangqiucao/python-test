
class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B(A):
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


class C(B):
    def feature5(self):
        print("feature 5 working")




a = A()
a.feature1()
a.feature2()

b = B()

b.feature3()
b.feature1()

c = C()

c.feature2()
