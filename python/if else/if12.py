P = int(input("Enter Basic Salary :"))
c=(P*20)/100
d=(P*80)/100
e=(P*25)/100
f=(P*90)/100
g=(P*30)/100
h=(P*95)/100
if P<=10000:
    print("the gross salary is",P+c+d)
elif P<=20000:
    print("Your gross salary is",P+e+f)
else:
    print("Your gross salary is",P+g+h)