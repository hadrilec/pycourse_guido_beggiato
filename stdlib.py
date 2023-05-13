import collections
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import dataclasses
import datetime
import functools
import itertools
import pathlib
from pprint import pprint
from typing import NamedTuple

# ============================================================================

class ColorTuple(NamedTuple):
    """tuple representing an rgb color combination"""
    red: int
    blue: int
    green:int


def example_namedtuple():
    c = (255, 0, 0)
    print(c)

    Color = collections.namedtuple("Color", "red, blue, green")
    red = Color(255, 0, 0)
    print(red)

    blue = ColorTuple(0, 255, 0)
    print(blue)

# ============================================================================

class Person:

    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, i'm {self.name}, {self.age} years old")


@dataclasses.dataclass()
class Student:
    name:str
    age:int
    major:str

    def greet(self):
        print(f"Hello, i'm {self.name}, i'm studying {self.major}")


def example_dataclass():

    person = Person("Bob", 42)
    person.greet()

    student = Student("Alix", 22, "Math")
    student.greet()

# ============================================================================

def example_datetime():
    # creation
    today = datetime.datetime.now()
    pi_day = datetime.datetime.fromisoformat("2023-03-14") 
    print(today)

    # 'math'
    delta_since_pi_day = (today - pi_day)
    print(type(delta_since_pi_day))

    # timedeltas
    days_since_pi_day = delta_since_pi_day.days
    print(days_since_pi_day)

    # comparison
    print(today > pi_day)

    # just dates
    next_holiday = datetime.date(2023, 8, 15)
    print(next_holiday)

    # attributes and methods
    print(next_holiday.day)
    print(next_holiday.month)
    print(next_holiday.year)
    print(next_holiday.weekday())


# ============================================================================

def example_pathlib():

    this_file = pathlib.Path(__file__)
    print(__file__)

    print(this_file)
    print(this_file.name)
    print(this_file.stem)
    print(this_file.suffix)
    print(this_file.exists())
    print(this_file.is_file())
    print(this_file.is_dir())

    this_file_folder = this_file.parent
    for f in this_file_folder.iterdir():
        print(f)

    new_file = this_file_folder / "groceries.txt"
    print(new_file)
    print(new_file.exists())

    fruits = ["apple", "banana", "cherry"]
    notes = this_file.with_name("notes.txt")
    with notes.open(mode="w") as f:
        for fruit in fruits:
            f.write(f"{fruit}\n")

    # add an extra fruit
    with notes.open("a") as f:
        f.write(f"kiwi\n")

    content = notes.read_text()
    print(content)

# ============================================================================

def doubler(x:int) -> int:
    """returns the double of a number"""
    return 2*x


def example_concurrent():
    numbers = range(10)
    with ThreadPool() as pool:
        doubles = tuple(pool.map(doubler, numbers))
    print(doubles)

# ============================================================================

if __name__ == "__main__":
    from os import system
    _ = system("cls") 
    # run examples
    print()
    example_namedtuple()
    print()
    example_dataclass()
    print()
    example_datetime()
    print()
    example_pathlib()
    print()
    example_concurrent()