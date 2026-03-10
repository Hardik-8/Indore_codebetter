ls=[]

while True:
    print("\n\nTHIS IS TO GET THE MARKS OF A PARTIULAR OR A SINGLE STUDENT")
    print("Enter 1 TO ENTER ROLL_NO AND GET DETAILS")
    print("Enter 2 TO GET THE MARKSHEET")
    print("Enter 9 TO EXIT\n")

    y=int(input("Enter number :"))

    if y==9:
        break

    elif y==2:
        ls=[]
        n=int(input("Enter the number of student \n"))

        print("\n+------+----------+------+-------+------+--------+----------+")
        print("| Roll | Name     | PHY  | CHEM  | MATH | Total  | Percent  |")
        print("+------+----------+------+-------+------+--------+----------+")

        for i in range(1,n+1):
            print("\nenter",i,"record\n")
            q=int(input("Enter Roll_No : \n"))
            w=input("Enter your Name - \n:")

            P = int(input("Enter the marks of physics \n:"))
            C = int(input("Enter the marks of chemsitry \n:"))
            M = int(input("Enter the marks of maths \n:"))

            print("| Physics    |",P)
            print("| Chemistry  |",C)
            print("| Maths      |",M)

            tot=P+C+M
            c=(tot/300)*100
            print("| Roll | Name     | PHY  | CHEM  | MATH | Total  | Percent  |")
            print(q , w , P , C , M , tot ,c)
            print("+------+----------+------+-------+------+--------+----------+")
            if P<33 and C<33 and M<33:
                print("| Result | FAIL IN ALL SUBJECTS |")
            elif(P<33 and C<33) or (P<33 and M<33) or (C<33 and M<33):
                print("| Result | FAIL IN TWO SUBJECTS |")
            elif P<33 or C<33 or M<33:
                print("| Result | FAIL IN ONE SUBJECT  |")
            elif (P>33 and P<=100) and (C>33 and C<=100) and (M>33 and M<=100):
                print("| Result | PASS IN ALL SUBJECTS |")
                print("| Total Marks     |",tot)
                print("| Percentage      |",c)
            else:
                print("| Marks Error | Marks cannot be more than 100 |")

            s=[q, w, P, C, M, tot, c]
            ls.append(s)

    elif y==1:
        r = int(input("Enter Roll Number to Search: "))

        print("\n+------+----------+------+-------+------+--------+----------+")
        print("| Roll | Name     | PHY  | CHEM  | MATH | Total  | Percent  |")
        print("+------+----------+------+-------+------+--------+----------+")

        for i in ls:
            z=i[0]
            if z==r:
                print("\t",i[0] , i[1] , i[2] , i[3] , i[4] , i[5] , i[6] )
                print("+------+----------+------+-------+------+--------+----------+")
