
# WARNING :- Run only one function at a time

# "w" Mode

'''f = open("demofile1.txt","w")
f.write("Hi! Just testing if it works of not.\n")'''

# "a" Mode

f = open("demofile1.txt","a")
a = f.write("Testing Appending multiple times.\n")

# It will print the number of words printed till now
# print(a)

# "r+" Mode

"""f = open("demofile1.txt", "r+")

f.write("Program Succesfully Completed.\n")

print(f.read())"""

f.close()