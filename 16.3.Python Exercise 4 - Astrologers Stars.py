Input = input("How Many Row You Want To Print\n")
num = int(Input)
decide = input("Choose between 1 and 0\n")
bool = int(decide)

if bool == True:
  for i in range(0, num):
    for j in range(0, i+1):
        print("*", end=' ')
    print(" ")

elif bool == False:
  for i in range(num+1,0,-1):
    for j in range(0, i-1):
        print("*", end=' ')
    print(" ")

else:
    print("Error Input")
