

class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("Config is",self.cpu,self.ram)


com1 = Computer('i5',12)
com2 = Computer('i7',16)

print(type(com1))

Computer.config(com1)
Computer.config(com2)

a = 10

a.bit_length()

com1.config()
com2.config()
