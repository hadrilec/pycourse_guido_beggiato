#  scalar elements
secret = 42
string = "Hello World"
x = 3.3


# list
numbers = [1, 5, 3]


first_num = numbers[0]
last_num = numbers[-1]
slice_of_nums = numbers[1:]


for number in numbers:
    print(number)
# the following works as well, but it's not 
# as pythonic and also more difficult to read
for i in range(len(numbers)):
    print(numbers[i])

mixed_list = ["Guido", 27, 2.5]

# dict 
my_map = {
    "name": "Guido",
    "age": 27,
    "years worked": 2.5
}

for i in my_map:
    print(i)

for k, v in my_map.items():
    print(f"{k} -> {v}")