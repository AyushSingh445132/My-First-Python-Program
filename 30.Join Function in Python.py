'''Join is a function in Python,
 that returns a string by joining the elements of an iterable,
 using a string or character of our choice.'''


# How to use join() function

numList = ['1','2','3','4']
separator = ','

print(separator.join(numList))

# Limitation of join() function

myDictionary = {"name":"Jack","country":"America"}
separator = "__separator__"

print(separator.join(myDictionary))