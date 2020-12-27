# Making a Faulty Calculator
# 45*3 = 555
# 56+9 = 77
# 56/6 = 6
print("Welcome to Calculator.Made by Ayush Singh")
op = input("Please type the mathematical operation you would like to do:\n"
           "+ for addition\n"
           "- for subtraction\n"
           "* for multiplication\n"
           "/ for division \n")
num1 = int(input("Enter First Number\n"))
num2 = int(input("Enter Second Number\n"))

if op=="+" and num1==56 and num2==9:
    print (77)
elif op=="+":
    print(num1 + num2)
elif op=="-":
    print(num1 - num2)
elif op=="*" and num1==45 and num2==3:
    print(555)
elif op == "*":
    print(num1 * num2)
elif op=="/" and num1==56 and num2==6:
    print(6)
elif op=="/":
    print(num1 / num2)
else :
    print("Unexpected Error!!Please check your equation again.")
