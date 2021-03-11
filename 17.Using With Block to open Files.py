# Using With Block

with open("16.5. demofile.txt") as f:
    a = f.read()
    print(a)

# Using With Block to open multiple files

with open("16.5. demofile.txt") as f,open("16.6. demofile1.txt") as g:
    x = f.readline()
    print(x)
    y = g.readline()
    print(y)
