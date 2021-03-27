i = int(input("Enter the Number "))

# Iteration Approach
# In Iterative,loop ends when it has reached the end of it's sequence.


def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

print("The factorial iterative of", i ,"is",factorial_iterative(i))

# Recursive Approach
# In Recurtion,fucnction stops trminating when a base condition is satisfied.

def factorial_recursive(n):
    if n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print("The factorial recursive of", i ,"is",factorial_recursive(i))

# Fibonachi Number
# 0 1 1 2 3 5 8 13
def fibonachi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)

print(fibonachi(i))