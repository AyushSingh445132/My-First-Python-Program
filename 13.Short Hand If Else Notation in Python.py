                            # Short Hand If Else Notation

x = int(input("enter x :\n"))
y = int(input("enter y :\n"))

# Concise but not Obivious Readability in Code
if x>y: print("x is greater than y")

# Less Concise but Better Readability in Code
if x>y:
    print("x is greater than y")

# Short Hand if else
print("x is greater than y") if x>y else print("x is less than or equal to y")