#Write a program to accepts an amount in rupees (Hint Rs4567) and find out how many currency of Rs 2000 required. Also find remaining amount.
a=float(input("enter the money :"))
total=a//2000
tol=a%2000
print("the total money of 2000 note is  :",total)
print("the remaining is :",tol)