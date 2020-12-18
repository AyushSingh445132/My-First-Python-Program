 #"Strings"

'Single Quote Strings'
"Double Quote Strings"
'''Triple Quote Strings'''

# len() Function
x = "String Demo"
print(len(x))

#String Slicing

word = "how are you?"
print(word[0:7])
print(word[0:3])
print(word[2:5])
print(word[-7:-3])
print(word[-5:-1])

# Q.What happens if we leave a blank?

print(word[ :6])
print(word[ 3:])
print(word[ : ])

# Skip_value

print(word[ : :2])
print(word[ : :3])
print(word[1:5:2])

#Some of the most used string Function:

#string.endswith
print(word.endswith("you"))
print(word.endswith("?"))

#string.count()
print(word.count("a"))

#string.upper()
print(word.upper())

#string.lower()
print(word.lower())

#string.find()
print(word.find("you"))

#string.replace
print(word.replace("how","who"))

#string.capitalize
print(word.capitalize())