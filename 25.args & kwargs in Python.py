# This * is called Asteris

# *args
def adder (*num):
    sum = 0

    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

# **kwargs
def info(**kwargs):
    for name,regno in kwargs.items():
        print(f"{name}'s registration number is {regno}")

students = {"Rohan" : "142" , "Harry" : "344" , "Ayush" : "18" , "Shivam" : "2"}

info(**students)