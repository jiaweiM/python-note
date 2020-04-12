def add(a, b):
    """This program adds two
    numbers and return the result"""

    result = a + b
    return result


class Parrot:
    """This is a docstring. I have created a Parrot"""
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)

print(Parrot.__doc__)
