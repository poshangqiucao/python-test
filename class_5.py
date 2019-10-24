

class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.Laptop = self.Laptop()

    def show(self):
        print(self.name,self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = 'i5'
            self.ram = 5

        def show(self):
            print(self.cpu,self.brand,self.ram)



# s1 = Student("xiao",2,'das','dsasa',232)
s2 = Student("Jxi",3)

s2.show()

lap2 = s2.Laptop

print(s2.Laptop.brand)

s2.Laptop.show()

