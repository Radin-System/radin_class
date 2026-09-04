# Chiz -> Object
# Tarif Yek she -> Model/Class/Blueprint/... -> Python -> Class


class Rack:
    # 1. Ganoon haye na gozari Varible -> inja ham sedgh mikone
    # pep8: CaptialCase
    color = "Black"

    # be tabe toye yek class tarif mishan
    # migan 'Metod'

    def __init__(self, name, units, depth, color="Black"):
        self.name = name
        self.units = units
        self.depth = depth
        self.color = color

    def open(self):
        print(f"{self}'s door was opened.")

    def close(self):
        print(f"{self}'s door was closed.")

    # Dunder method --> duble undescore method
    # Magic method --> Karaye jalebi mikone

    def __str__(self):
        return f"{self.name} ({self.units}:{self.depth})"

    def __bool__(self):
        return self.units > 0

    def __eq__(self, other):
        return self.name == other.name and self.units == other.units and self.depth == other.depth


"""

# Rack -> instance -> my_rack
my_rack = Rack("My rack", 12, 100)
third_rack = Rack("My rack", 12, 100)
zero_rack = Rack("Zero", 0, 0)
your_rack = Rack("Your rack", 18, 120, "White")


if zero_rack:
    print("Zero rack is True")


print(f"{my_rack.units=}")
print(f"{my_rack.depth=}")
print(f"{my_rack.color=}")

print(f"{your_rack.units=}")
print(f"{your_rack.depth=}")
print(f"{your_rack.color=}")


my_rack.open()
your_rack.open()


print(third_rack == my_rack)
"""

class NationMix:
    nation = None

    def set_nation(self, nation):
        self.nation = nation


class Person:
    def __init__(
        self,
        id,
        first_name,
        last_name,
        age,
        height=None,
        weight=None,
        skin_tone=None,
    ):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.skin_tone = skin_tone

    def fullname(self):
        return f"{self.first_name} {self.last_name}".title()

    def __str__(self) -> str:
        return self.fullname()


class Student(Person, NationMix):
    scores = ()

    def add_score(self, score):
        self.scores = tuple(list(self.scores) + list((score,)))

    def __str__(self):
        return f"{self.fullname()}: scores={self.scores}"


class Teacher(Person):
    def __init__(self, id, first_name, last_name, age, degree, height=None, weight=None, skin_tone=None):
        self.degree = degree
        super().__init__(id, first_name, last_name, age, height, weight, skin_tone)


person = Person(
    id="12345789",
    first_name="ali",
    last_name="alavi",
    age=18,
)
student = Student(
    id="12345789",
    first_name="ali",
    last_name="alavi",
    age=18,
)
teacher = Teacher(
    id="12345789",
    first_name="ali",
    last_name="alavi",
    age=18,
    degree="",
)

student.add_score(18)
student.set_nation('Iran')
print(student.nation)
print(student)
print(person)


class MyList(list):
    def __str__(self):
        string = ""
        for i in self:
            string += str(i) + ','

        return string


my_list = MyList((1, 2, 3, 4))

print(my_list)