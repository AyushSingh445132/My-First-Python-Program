import time

# time.time()
seconds = time.time()
print("Seconds since epoch = ",seconds)

# time.asctime()
result = time.asctime()
print("Result :", result)

# time.sleep()
print("This is printed immediately.")
time.sleep(3)

print("This is printed after 3 seconds")

# time.localtime()
obj = time.localtime()
print(obj)

t = time.asctime(obj)
print(t)