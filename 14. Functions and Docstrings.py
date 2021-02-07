# In-built function
v = sum((5,7))
print(v)

# User defined function

def Average(a,b):
    '''This function gives the average of two numbers.
   Warning : Don't use more than two numbers'''
    average = (a+b)/2
    print("Average :",average)

Average(5,7)

# doc strings
print(Average.__doc__)