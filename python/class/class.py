class rectangle:
    def __init__(self):
        #ye hai properties 
        self.length=0
        self.breadth=0
    def display(self):
        print(self.length,self.breadth)
    def area(self):
        a=self.length*self.breadth
        print("Area ",a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print("Parimeter",p)

r1=rectangle()
r1.display()
r1.length=10
r1.breadth=3
r1.area()
r1.perimeter()
r1.display()


