
# DURK
class PyCharm:

    def execute(self):
        print("Compiling")
        print("Runing")

class otherIDE:

    def execute(self):
        print("Spell Check")
        print("Compiling")
        print("Compiling")
        print("Runing")


class Laptop:

    def code(self,ide):
        ide.execute()


ide = PyCharm()
orther = otherIDE()


lap1 = Laptop()
lap1.code(ide)
lap1.code(orther)
