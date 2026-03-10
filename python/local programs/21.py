#compound intrest 
P=float(input("enter Initial Principal Amount : "))
r=float(input("enter Annual Interest Rate : "))
n=float(input("enter Number of Times Interest is Compounded : "))
CI=P*(1+(r/100))**n-P
print("the area of copound intrest is :",CI)