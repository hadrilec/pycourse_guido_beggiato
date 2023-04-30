
person_list = ["Guido", 27, 2.5]


person_dict = {
    "name": "Guido",
    "age": 27,
    "years worked": 2.5
}


class Person:

    def __init__(self, name:str, age:int, years_worked:float) -> None:
        self.name = name
        self.age = age
        self.years_worked = years_worked

person_struct = Person("Guido", 27, 2.5)
another_person = Person("Ellie", 22, 0.5)

print(person_struct.name)
person_struct.age = 42

if person_struct.age > another_person.age:
    print(f"{person_struct.name} is older than {another_person.name}")