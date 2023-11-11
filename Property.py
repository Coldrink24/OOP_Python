class Person:
    def __init__(self, name):
        self.name = name
        print(f"Instance Created, Hello {self.name}")
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if name == " ":
            print("Not Valid!")
        else:
            self.__name = name

p1 = Person("Somaya")
print(p1.name)
p1.name = " "
print(p1.name)
