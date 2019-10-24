

class Student:
    school = 'Telusko'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def agv(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self,val):
        self.m1 = val

    @staticmethod
    def info(self):
        print("This is a class!")

    @classmethod
    def info(cls):
            return cls.school



s1 = Student(332,32,32)

s2 = Student(32,43,54)

print(s1.agv())

print(Student.info())
Student.info()