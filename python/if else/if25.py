print("THIS IS CALL CENTER \n Enter 1 for prepaid services \n Enter 2 for post paid services \n Enter 3 for network problems \n Enter 9 for talking to an agent")
P = int(input("Enter the number shown above :"))
if P==1:
    print("Prepaid entered")
    print("press \n1.For recharge \n2.For data usage \n3.for OTT")
    d=int(input("enter a number for going forward "))
    print(d)
    if d==1:
        print("recharge plans are ....")
    elif d==2:
        print("data use is ....")
    else:
        print("ott are netflix , joihoststar ....")
elif P==2:
    print("Postpaid services ")
    print("press \n1.calling related \n2.SMS related \n3.international roaming ")
    e=int(input("enter a number for going forward "))
    print(e)
    if e==1:
        print("Calling plans are....")
    elif e==2:
        print("SMS  related plans are....")
    else :
        print("International roaming plans....")
elif P==3:
    print("Network Problem listed")
    f=input("enter the area ")
    print(f)
    if f=="satna" or f=="indore" or f=="rewa":
        print("these area are afected by the net and server is down")
    else:
        print("these area have stable net .Try to restart your mobile")
elif P==9:
    print("agent will join the call in some time just wait a while")
    print("agent here thanks for calling ")
else :
    print("invalid input entered")
