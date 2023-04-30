from typing import Any


class Person:

    def __init__(self, name:str, age:int, years_worked:float) -> None:
        self.name = name
        self.age = age
        self.years_worked = years_worked

    def celebrate_birthday(self) -> None:
        self.age += 1
        print(f"Happy birthday {self.name} !")

    def update_cv(self, extra_work:float) -> None:
        self.years_worked += extra_work

    def asdict(self) -> dict[str, Any]:
        return {
            "name":self.name,
            "age":self.age,
            "years worked":self.years_worked
        }


first_person = Person("Guido", 27, 2.5)
second_person = Person("Ellie", 22, 0.5)

print(first_person.age)
first_person.celebrate_birthday()
print(first_person.age)

print(second_person.years_worked)
second_person.update_cv(4.0)
print(second_person.years_worked)

first_person_dict = first_person.asdict()
print(first_person_dict)