# more OOP concepts
# introduction to importing modules
# learning more about standard container types

from typing import NamedTuple


class Person(NamedTuple):
    name:str
    birthplace:str

    def introduce(self):
        print(f"{self.name} was born in {self.birthplace}")


def list_methods():
    lst = [1, 2, 3]
    print(lst)
    lst.append(4)
    print(lst)
    element = lst.pop()
    print(lst, element)
    lst2 = [1, 2, 4] + [8, 16, 32]
    print(lst2)


def dict_methods():
    d = {"a":1, "b":2, "c":3}
    print(d)
    d.update({"d":4})
    print(d)
    for key, value in d.items():
        print(key, value)


def namedtuple_example():
    person = Person("Andy", "NYC")
    person.introduce()


def main():
    list_methods()
    dict_methods()
    namedtuple_example()
    return 0


if __name__ == "__main__":
    main()