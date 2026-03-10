rec = []
n = int(input("Enter how many student data you want to save: "))

for i in range(n):
    print("\nEnter student", i+1, "details")
    roll = int(input("Roll No: "))
    name = input("Name: ")
    phy = int(input("Physics Marks: "))
    chem = int(input("Chemistry Marks: "))
    math = int(input("Maths Marks: "))
    total = phy + chem + math
    per = (total / 300) * 100
    rec.append([roll, name, phy, chem, math, total, per])

while True:
    print("""
1. Show ALL records
2. First Division (>=60%)
3. Second Division (>=45%)
4. Third Division (>=33%)
5. Failed in ONE subject
6. Failed in TWO subjects
7. Failed in ALL subjects
8. Search student by Roll No / Exit
""")

    ch = int(input("Enter choice: "))

    if ch == 1:
        print("\nRoll Name Phy Chem Math Total %")
        for x in rec:
            print(x)

    elif ch == 2:
        print("\nFirst Division:")
        for x in rec:
            if x[6] >= 60:
                print(x)

    elif ch == 3:
        print("\nSecond Division:")
        for x in rec:
            if 45 <= x[6] < 60:
                print(x)

    elif ch == 4:
        print("\nThird Division:")
        for x in rec:
            if 33 <= x[6] < 45:
                print(x)

    elif ch == 5:
        print("\nFailed in ONE subject:")
        for x in rec:
            fail = 0
            if x[2] < 33: fail += 1
            if x[3] < 33: fail += 1
            if x[4] < 33: fail += 1
            if fail == 1:
                print(x)

    elif ch == 6:
        print("\nFailed in TWO subjects:")
        for x in rec:
            fail = 0
            if x[2] < 33: fail += 1
            if x[3] < 33: fail += 1
            if x[4] < 33: fail += 1
            if fail == 2:
                print(x)

    elif ch == 7:
        print("\nFailed in ALL subjects:")
        for x in rec:
            if x[2] < 33 and x[3] < 33 and x[4] < 33:
                print(x)

    elif ch == 8:
        r = int(input("Enter Roll No to search (0 to exit): "))
        if r == 0:
            print("end")
            break
        found = False 
        for x in rec:
            if x[0] == r:
                print("\nMarksheet:")
                print("Roll:", x[0])
                print("Name:", x[1])
                print("Physics:", x[2])
                print("Chemistry:", x[3])
                print("Maths:", x[4])
                print("Total:", x[5])
                print("Percentage:", x[6])
                found = True
        if not found:
            print("Roll No not found ❌")

    else:
        print("Invalid choice ❌")
