'''enumerate function assingns an index to every element or value in the object that we want to
iterate, so we do not have to assign a specific variable for  incremental function.'''

# Examples of using enumerate function
# On a Python list:-
list_1 = ["zero","one","two"]
for index,val in enumerate(list_1):
    print(index,val)

# On a list with start index:-
list_2 = ["Python","Programming","is","Fun"]
result = enumerate(list_2,5)
print(list(result))


# Sortlisting a list on the basis of even
sort_list = ["Mango", "Potato", "chopsticks", "Noodles"]

for index, item in enumerate(sort_list, start=0):

    if index % 2 == 0:
        print(f"Jarvis please buy {item}")