# A set is a collection of well-defined objects and non-repetetive elements.

                              # Set Methods
                            # Creating Python sets

# Different types of sets in Python
my_set = {0,1,2,3}                        # set of integers
print(my_set)
my__set = {1.0,"Hello",(1,2,3)}         # set of mixed data types
print(my__set)

                            # Modifying a set
my_set = {0,1,2,3}
# add an element
my_set.add(4)
print(my_set)
# add multiple elements
my_set.update([5,6,7])
print(my_set)

#my set = {0, 1, 2, 3, 4, 5, 6, 7, (1, 2, 3), 'Hello'}

# Set Union
print(my_set | my__set)
print(my_set.union(my__set))

# Set Intersection
print(my_set & my__set)
print(my_set.intersection(my__set))

# Set Difference
print(my_set - my__set)
print(my_set.difference(my__set))

# Set symmetric difference
print(my_set.symmetric_difference(my__set))

                            # Removing elements from a set
# Difference between discard() and remove()
my_set = {0,1,2,3}
print(my_set)

# discard an element
my_set.discard(1)
print(my_set)

# remove an element
my_set.remove(3)
print(my_set)

# discard an element not present
my_set.discard(4)
print(my_set)

# remove an element not present
'''my_set.remove(4)
print(my_set)'''