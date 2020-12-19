# How to write a For Loop
name = ["Ayush","Aditi","Shivam","Shubham"]

for item in name:
    print(item)

# print two or more items
name_age = [["Ayush",15],["Aditi",12],["Shivam",19],["Shubham",14]]

dict1 = dict(name_age)

for item,age in dict1.items():
    print(item,"is",age,"years old.")

# using for loop with conditions
list1 = [5,34,21,5.6,"hello world",35,111,23,664]

for item in list1:
    if str(item).isnumeric() and item>10:
        print(item)