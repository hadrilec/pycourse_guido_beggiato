def greet(name:str) -> None:
    """simple function to greet the user"""
    assert isinstance(name, str)
    print(f"Hello {name} !")


if __name__ == "__main__":
    print("this is the main file")

#  this else block is here for explanation purposes
# should never be present in production code
else:
    print(f"the file {__file__} was imported")