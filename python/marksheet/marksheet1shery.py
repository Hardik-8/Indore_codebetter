rec = []
num = int(input("enter how many student data do you want to save"))

for i in range(1,num+1):
    roll_no = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    marks1 = int(input("Enter physic marks : "))
    marks2 = int(input("Enter chemistry marks : "))
    marks3 = int(input("Enter maths marks : "))
    total = marks1+marks2+marks3
    per = total/3
    ls = [roll_no,name,marks1,marks2,marks3,total,per]
    rec.append(ls)


for x in rec[0]:
    print(x)

    

while True:
    option = int(input("""press 1 for check all records
press 2 for check who are passed in first division
press 3 for check who are passed in second division
press 4 for check who are passed in third division
press 5 for check who is failed in one subject
press 6 for check who is failed in two subject
press 7 for check who is failed in all subject
press 8 for exit"""))

    if option == 1:
        print("\nAll Records:")
        print(["Roll_no","Name","Phy","Chem","Math","Total","Percentage"])
        for x in rec:
            print(x)

    elif option == 2:
        print("\nFirst Division (>= 80%):")
        for x in rec:
            if x[6] >= 80:
                print(x)

    elif option == 3:
        print("\nSecond Division (>= 60% and < 79%):")
        for x in rec:
            if x[6] >= 60 and x[6] < 79:
                print(x)

    elif option == 4:
        print("\nThird Division (>= 33% and < 59%):")
        for x in rec:
            if x[6] >= 33 and x[6] < 59:
                print(x)

    elif option == 5:
        print("\nFailed in ONE subject:")
        for x in rec:
            fail = 0
            if x[2] < 33: 
                fail += 1
            if x[3] < 33: 
                fail += 1
            if x[4] < 33: 
                fail += 1

            if fail == 1:
                print(x)

    elif option == 6:
        print("\nFailed in TWO subjects:")
        for x in rec:
            fail = 0
            if x[2] < 33: 
                fail += 1
            if x[3] < 33: 
                fail += 1
            if x[4] < 33: 
                fail += 1

            if fail == 2:
                print(x)

    elif option == 7:
        print("\nFailed in ALL subjects:")
        for x in rec:
            if x[2] < 33 and x[3] < 33 and x[4] < 33:
                print(x)

    elif option == 8:
        print("Exiting program... Thank you 😄")
        break
    
        
    else:
        print("Invalid option Try again")



