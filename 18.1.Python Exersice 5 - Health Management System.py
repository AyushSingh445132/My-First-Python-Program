def gettime():
    import datetime
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("18.2.Harry_Exercise.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("18.3.Harry_Food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("18.4.Rohan_Exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("18.4.Rohan_Food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("18.3.Hammad_Exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("18.3.Hammad_Food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("18.2.harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("18.2.harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("18.4.rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("18.4.rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("18.3.hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("18.3.hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")
print("health management system: ")
a=int(input("press 1 for lock the value and 2 for retrieve "))

if a==1:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)



# Health Management System
# client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
# log_list = {1: "Exercise", 2: "Diet"}
#
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
# try:
#     print("Select Client Name:")
#     for key, value in client_list.items():
#         print("Press", key, "for", value, "\n", end="")
#     client_name = int(input())
#
#     print("Selected Client :", client_list[client_name], "\n", end="")
#
#     print("Press 1 for Log")
#     print("Press 2 for Retrieve")
#     op = int(input())
#
#     if op == 1:
#         for key, value in log_list.items():
#             print("Press", key, "to lock", value, "\n", end="")
#         log_name = int(input())
#         print("Selected Job :", log_list[log_name])
#         f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "a")
#         k = 'y'
#         while (k != "n"):
#             print("Enter", log_list[log_name], "\n", end="")
#             mytext = input()
#             f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
#             k = input("ADD MORE ? y/n:")
#             continue
#         f.close()
#     elif op == 2:
#         for key, value in log_list.items():
#             print("Press", key, "to retrieve", value, "\n", end="")
#         lock_name = int(input())
#         print(client_list[client_name], "-", log_list[lock_name], "Report :", "\n", end="")
#         f = open(client_list[client_name] + "_" + log_list[lock_name] + ".txt", "rt")
#         contents = f.readlines()
#         for line in contents:
#             print(line, end="")
#         f.close()
#     else:
#         print("Invalid Input !!!")
# except Exception as e:
#     print("Wrong Input !!!")