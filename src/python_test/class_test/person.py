class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name, self.last_name)


class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.graduation_year = year


x = Person("John", "Doe")
x.print_name()

x = Student("Mikee", "Olsen", 2019)
x.print_name()
