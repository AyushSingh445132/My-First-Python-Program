                            # Short Hand If Else Notation

x = int(input("enter x :\n"))
y = int(input("enter y :\n"))

# Concise but not Obivious Readability in Code
if x>y: print("A is greater than B")

# Less Concise but Better Readability in Code
if x>y:
    print("A is greater than B")

# Short Hand if else
print("A is greater than B") if x>y else print("A is less than or equal to B")