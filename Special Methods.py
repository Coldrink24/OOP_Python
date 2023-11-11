class Human:
    def __init__(self, name):
        self.name = name

    # for readable code, print(self) == print(self.__str__())
    def __str__(self):
        return f"I'm Human, my name is {self.name} "

    def __call__(self):
        print("Hey, did you called!")


# Before defining __str__ method
man = Human("Ahmed")
print(man)   # <class '__main__.Human'>

# After defining __str__ method
print(man)  # I'm Human, my name is Ahmed


# Before defining __call__ method
man()  # TypeError: 'Human' object is not callable

# After defining __call__ method
man()  # Hey, did you call!


class Animal:
    def __init__(self, legs):
        self.legs = legs

    def __len__(self):
        return self.legs


# Before defining __len__ method
Bear = Animal(4)
print(len(Bear))  # TypeError: object of type 'Animal' has no len()

# After defining __len__ method
print(len(Bear))   # 4
