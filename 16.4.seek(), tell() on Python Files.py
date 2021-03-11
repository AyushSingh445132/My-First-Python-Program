# tell in Python

f = open("16.5. demofile.txt", "r")
print(f.tell())
print(f.readline())
print(f.tell())

# seek in Python

f = open("16.5. demofile.txt", "r")
print(f.readline())
f.seek(7)
print(f.readline())