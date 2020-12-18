#Lists in Python

[]                           # list with no value
[1,2,3]                      # list of integers
[1,2.5,3.7,9]                # list of integers and float
['a','b','c']                # list of characters
['a',1,'b',3.5,'zero']       # list of mixed values
['One','Two','Three']        # list of strings

#List Slicing

list1 = [1,65,73,33,9,17,29,55,72,4]
#seq = list1[start:stop:skip]

print(list1[0:10:2])          # It will skip 1 element
print(list1[2:10:3])          # It will skip every 3rd element

#List Methods

l1 =[34,54,75,12,59,34,12,39,5,26]
(l1.append(12))
print(l1)

(l1.pop())
print(l1)

(l1.remove(75))
print(l1)

(l1.sort())
print(l1)

(l1.reverse())
print(l1)

(l1.copy())
print(l1)

print(l1.index(39))

(l1.extend(list1))
print(l1)

(l1.clear())
print(l1)

#Tuples in Python

x=()                          #It's an empty tuple
y=(1,)                        #It's an tuple with single value
tup1=(1,2,3,4,5)              #Tuple with integers
tup2=('harry',5,'demo',5.8)   #Tuple with mixed values

# Q.How to swap or switch places of two numbers in Python

a = 10
b = 15

print(a,b)                    #It will give output as: 10 15

a,b=b,a

print(a,b)                    #It will give output as: 15 10