# There are 4 ways to do string formatting in Python

# 1.Using % Operator
name = "Jack"
n = "My name is %s."%name
print(n)

# 2.Using Tuple()
name = "Ayush"
roll_no = 18

info ="%s's roll no is %d"%(name,roll_no)
print(info)

# 3.Using str.format
x = "This is a {} {}"
a = "Formatted"
b = "String."
y = x.format(a,b)

print(y)

# 4.Using F-Strings
greet = "Hello!"
name = "Ayush"
z = f"{greet} This is {name}"

print(z)