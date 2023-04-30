class Person:

    def __init__(self, name:str, age:int, years_worked:float) -> None:
        self.name = name
        self.age = age
        self.years_worked = years_worked


def celebrate_birthday(person: Person) -> None:
    person.age += 1
    print(f"Happy birthday {person.name}")


def update_cv(person: Person, extra_work:float) -> None:
    person.years_worked += extra_work

# -------------------

first_person = Person("Guido", 27, 2.5)
second_person = Person("Ellie", 22, 0.5)

print(first_person.age)
celebrate_birthday(first_person)
print(first_person.age)

print(second_person.years_worked)
update_cv(second_person, 4)
print(second_person.years_worked)