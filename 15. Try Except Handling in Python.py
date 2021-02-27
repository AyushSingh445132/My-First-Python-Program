                            # Try Except Handling

num1 = input("Enter num 1:-")
num2 = input("Enter num 2:-")

try:
    print("the sum of these two number is", int(num1)+int(num2))

except Exception as e:
    print(e)

print("The line is very important")