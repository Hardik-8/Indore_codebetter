#list of object 
class Student:
    def __init__(self,rollno=0,name=""):
        self.rollno=rollno
        self.name=name
        self.marks={"hindi":0,"eng":0,"phy":0}
    def input(self):
        self.rollno=int(input("enter rollno"))
        self.name=int(input("enter name"))
        self.marks["hindi"]=int(input("enter marks"))
        self.marks["eng"]=int(input("enter marks"))
        self.marks["phy"]=int(input("enter marks"))
    def display(self):
        print(self.rollno,",",self.name,",",self.marks,",",)

s1=Student(10,"hardik")
s1.marks={"hindi":90,"eng":80,"phy":70}
s1.display()

s2=Student(11,"rahul")
s2.marks={"hindi":80,"eng":70,"phy":60}
s2.display()
        
student=[s1,s2]
print(student)
print(s1)