#6. Write a program to find the greatest of four numbers entered by the user. 
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
d=int(input("Enter fourth number "))
if(a>b and a>c and a>d):
    print("a is the greatest number")
if(b>a and b>c and b>d):
    print("b is the greatest number")
if(c>a and c>b and c>d):
    print("c is the greatest number")
else:
    print("d is the greatest number")