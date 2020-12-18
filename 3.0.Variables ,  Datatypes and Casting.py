#Variables
Integers = 34
floatNumbers = 23.2
Strings = "Hello World"
#Booleans =
#None =

print(type(Integers))
print(type(floatNumbers))
print(type(Strings))

#Varialbls in Python
abc = "It's a string variable"
_abcnum = 40                     #It is a int variable
abc123 = 55.854                  #It is a float variable

print (_abcnum + abc123)         #It will give sum of 40 + 55.854

#type() Function in Python
Ayush = "16"
demo  = 55.5
demo2 = 40

print(type(Ayush))               #It will give output as string
demo3 = type(demo)
print(demo3)                     #It will give output as float
print (type(demo2))              #It will give output as integer

                               #IMPORTANT - we can't add string to a number
var1 = "It's a string"
var2 = 5

#print(var1 + var2)       '''It will give an error we cant't add string to any number'''

                    #IMPORTANT -We can add two or more strings together
variable1 = "My name is "
variable2 = "Ayush"

variable3 = variable1 + variable2 + " & I am a Good Boy."

print (variable3)

#Typecasting in Python:

a = "34"
b = 6
print(int(a) + b)                       #Output : 40

#Input Function in Python
print ("Enter you name")
name = input()                           #It will take input
print("Nice to meet you", name)