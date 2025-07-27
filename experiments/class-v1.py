#!/usr/bin/python3

class Computer:

    def __init__(self):
        self.name = "Marius"
        self.age = 33

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

# c1.name = "Mihai"
# c1.age = 31
#
c1.update()

if c1.compare(c2):
    print("They are the same")
else:
    print("They are different")

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)
