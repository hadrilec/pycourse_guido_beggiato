# bare minimum
def add(a, b):
    res = a + b
    return res


# function with 
# - type hints
# - type checking
# - docstring
def better_add(a:int, b:int) -> int:
    """this functions takes 2 integers and returns their sum"""
    assert isinstance(a, int)
    assert isinstance(b, int)
    return a + b


# a 'void' function
def sum_and_show(a:int, b:int) -> None:
    """sums 2 numbers and prints their sum to the screen"""
    assert isinstance(a, int)
    assert isinstance(b, int)
    r = better_add(a=a, b=b)
    sentence = f"{a} + {b} = {r}"
    print(sentence)
    # this implicitly returns nothing
    # side effects are evil

x = add(1, 3)
sum_and_show(10, b=20)
# print(a) # why it does not work ?