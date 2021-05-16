# Decorators - These are functions that wrap around any given function and modify it externally.

def inner1(func):
    def inner2():
        print("Before function execution\n");
        func()
        print("After function execution")
    return inner2

@inner1
def function_to_be_used():
    print("This is inside the function\n")

function_to_be_used()