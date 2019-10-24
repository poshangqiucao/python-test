
class A:
    def __init__(self):
        print("init A")
    def feature1(self):
        print("feature 1 working")

    def feature2(self):
        print("feature 2 working")

class B():

    def __init__(self):
        # super.__init__()
        print("init B")
    def feature3(self):
        print("feature 3 working")

    def feature4(self):
        print("feature 4 working")


class C(B,A):

    def __init__(self):
        super().__init__()
        print("init C")

    def feature5(self):
        print("feature 5 working!")

c = C()
c.feature4()


# a = A()
# c = C()


