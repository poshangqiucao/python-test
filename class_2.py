

class Computer:
    def __init__(self):
        self.name = "cheng"
        self.age = 23

    def update(self):
        self.age = 12

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1 = Computer()
c1.age = 32
c2 = Computer()


if c1.compare(c2):
    print("They are same")
else:
    print("not same")
print(id(c1))
print(c1.name)
print(c1.age)
print(c2.age)
c1.update()
print(c1.age)
print(c2.age)
c1.name = "xiaoming"
print(c1.name)
