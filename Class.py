class Person:
    name = "Ivan"
    age = 16

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    course = 1

    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

Anton = Person("Антон", 33)
print(Anton.name + " " + str(Anton.age))

igor = Student("Игорь", 44, )
igor.set("Igor", 19, 2)
print(igor.name + " " + str(igor.age) + " " + str(igor.course))

vlad = Person("Иван", 19)
vlad.set("Ivan", 25)
print(vlad.name + " " + str(vlad.age))
