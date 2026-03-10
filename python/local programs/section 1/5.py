#Write a program to accepts an amount in rupees (Hint Rs4567) and find out how many currency of Rs 2000 required. Also find remaining amount.
a=float(input("enter the money :"))


total=a//2000
tol=a%2000
print("the total marks are :",total)
print("the percentage is :",tol)