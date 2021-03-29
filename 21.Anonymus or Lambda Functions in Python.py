# Anonymous or Lambda Functions
# The Main objective of this function is that,when we need a function just once,anonumous functions come in handy.

# Basic way of defining a function
def add(a, b):
    return a+b
print(add(35, 5))

# Defining a function using Lambda
add = lambda x, y: x+y

print(add(35, 5))

# Using Lambda in sort()
o = [[25,4], [1,12], [11,5]]
o.sort(key=lambda x:x[1])
print(o)