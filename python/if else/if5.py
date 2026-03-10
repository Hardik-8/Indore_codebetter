#write a program to find the greatest number among three numbers
a=int(input("Enter first value "))
b=int(input("Enter second value "))
c=int(input("Enter third value "))
if(a>b and a>c):
    print("a is the greatest number")
if(b>a and b>c):
    print("b is the greatest number")
else:
    print("c is the greatest number")