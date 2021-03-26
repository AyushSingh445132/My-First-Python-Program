# What is a Scope in Python?
'''Scope refers to the coding area where a paticular Variable is acessible in Python.'''

# Local Variable
# A variable that is decleared inside a function or loop is called a local variable.

def sum():
    a = 10 # local variable cannot be accessed outside the function
    b = 20
    sum = a+b
    print(sum)

# print(a)   # this gives an error

# Global Variable
# A Global variable is not decleared inside a function and can be accessed anywhere in Program.

x = 180
def print_Number():
    print(x) # takes the value of x outside the function.

print_Number()

# How to modify global variable inside a Function?
# For this,we use global keyword.

def global_keyword():
    global x
    x = x+20
    print(x)

global_keyword()

# What if we have a Nested Function.How does the scope change?

y = 35
def Basic_function():
    y = 20
    def Nested_function():
        global y # This makes this y=50 a global variable
        y = 50
    # print("before calling Nested function()",y)
    Nested_function()
    print("after calling Nested function()",y)



Basic_function()
print(y)