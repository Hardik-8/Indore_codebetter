a = int(input("Enter percentage: "))
if a < 0 and a > 101:
    print("invalid")
elif a < 45:
    print("3rd division")
elif a < 60:
    print("2nd division")
elif a < 101:
    print("1 st division")
else:
    print("Fail")

