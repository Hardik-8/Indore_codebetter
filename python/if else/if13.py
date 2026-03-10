#PCM marks
P = int(input("Enter the marks of physics :"))
C = int(input("Enter the marks of chemsitry :"))
M = int(input("Enter the marks of maths :"))
print("Physics:",P)
print("Chemistry:",C)
print("Maths:",M)
tot=P+C+M 
c=(tot/300)*100 
if P<33 and C<33 and M<33:
    print("fail in all")
elif(P<33 and C<33) or (P<33 and M<33) or (C<33 and M<33):
    print("fail in two subjects")
    if P<33 and C<33:
        print("fail in Physics and Chemistry")
    elif P<33 and M<33:
        print("fail in physics and Maths")
    else:
        print("fail in chemistry and maths")
elif P<33 or C<33 or M<33:
    print("fail in one subject")
    if P<33:
        print("fail in physics")
    elif C<33:
        print("Fail in chemistry")
    else:
        print("Fail in Maths")
elif (P>33 and P<=100) and (C>33 and C<=100) and (M>33 and M<=100):
    print("pass in all the subjects ")
    print("total marks are ",P+C+M) 
    print("total percentage are ",c)
    if c < 0 or c >=100:
        print("invalid")
    elif c >= 60:
        print("1st division")
    elif c >= 45:
        print("2nd division")
    elif c >= 33:
        print("3rd division")
    else:
        print("3rd")
else:
    print("marks cannot be more than 100")

