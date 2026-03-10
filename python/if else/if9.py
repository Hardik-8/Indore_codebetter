a = int(input("Enter age: "))
if a <= 0:
    print("invalid")
elif a < 13:
    print("child")
elif a < 20:
    print("teen")
elif a < 60:
    print("young")
else:
    print("old")
