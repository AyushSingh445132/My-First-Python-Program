# How to Open a file?

# open ("filename","mode")

# How to Read a file? (Use only one read argument at a time to avoid errors)

f = open("demofile.txt", "r")
# content = f.read()

# print(content)

# How to Read Only parts of File?

# print(f.read(5))

# print(f.readline())

# print(f.readlines())

# for item in f:
#     print(item)

# It's always necessary to close a File.

f.close()