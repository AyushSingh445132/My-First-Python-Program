#####################MAP#######################

items = [1, 2, 3, 4, 5]
a=list(map((lambda x: x*x), items))
print(a)

#####################FILTER#######################

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [1, 3, 5, 7, 9]
c = list(filter(lambda x : x not in b, a))

print(c)

#####################REDUCE#######################

from functools import reduce

a = reduce((lambda x, y: x*y),[1, 2, 3, 4])

print(a)