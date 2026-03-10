#function is used for code reusebility 
# write ones call multiple time 
# it is used in modularing programming concept
# an large prgroam is to be divided into its sub program and provide single solution form them is called modularing program .
# functions :
#     inbuilt
#     user define
    # syntax 
    #     def function_name(self,parameter1,2,3,4):
    #           pass 

# user define 
# `1. no written type without arguement function`
# `2.no written type with arguement fucntion `
# `3.return type without arguement`
# `4.return  type with arguement`
# variable ,arguement , parameter = these are all same but har jagah role alag alag hai 
# local and global hote hai 
# function ko hamko kisi aur fucntion me use krna ho to ham jab dusre fucntion ko call krte hai too ham uske ander argument ko pass krte hai  



def add(a,b):
    
    c=a+b
    print("sum is ",c)
add(a,b)


def subtract(a,b):
    d=a-b
    print("subtract is ",d)
subtract(a,b)
def multiply(a,b):
    print(a*b)
multiply(a,b)