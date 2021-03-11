'''Question
 In this we have to print an right-angled shaped triangle with the help of "*".'''

'''Rules for Exercise :-
1.You have to take an integer variable,and the input of the variable will determine
  the length of the triangle.
2.Take another interger and typecast it to a Boolean.
3.When the value of Boolean is 1 i.e True the pattern will be printed as shown:-
 *
 **
 ***
 ****
4.But if the value of Boolean is 0 i.e False the pattern will be printed upside down.
  Like this:- ****
              ***
              **
              *'''

# Solution

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
