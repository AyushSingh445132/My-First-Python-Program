# How to use If Else & Elif in Python
print ("What's the temperature Outside(in Celsius)?")
T1 = int(input())
if T1>35:
    print("Wear Cotton Clothes,don't stay outside in the sun for too long.")
elif T1>20<35:
   print("Go Outside and Enjoy the wheather.")
elif T1>10<20:
   print("It might be cold outside.Get some Exersize done to feel better or you will be a lazy sloth.")
elif T1<10:
    print("Try keeping your body warm and Be Aware not to catch a cold.")
elif T1> 50:
    print("You probably live in a desert or in a volcano.")
elif T1< 0:
    print("You should probably eat fire to keep youself warm.")
else :
    print("Invalid input")