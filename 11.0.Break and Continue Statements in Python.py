# Break Statement
# In for loop
list = [5,6,13,20,86,23.3,446,72]

for var in list:
    print(var)
    if var > 25:
     break
    print("code not broken")

print("code broken")

# In while loop
i = 0
while i < 101:
    print(i)
    i += 1
    if i > 5:
        break
        print("code not broken")

print("code broken")

# Continue Statement
# In for loop

for var in list:
    print(var)
    continue
    print("code not continued")

print("code continued")

# In while loop

i = 0
while i < 11:
    print(i)
    i += 1
    if i > 5:
     continue
    print("code not continued")

print("code continued")