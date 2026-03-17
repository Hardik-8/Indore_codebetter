
class circle:
    def __init__(self):
        self.radius = 0
    def diameter(self):
     print(2*self.radius)
    def circumference(self):
     print(2*3.14*self.radius)
    def area(self):
     print(3.14*(self.radius**2))

c1=circle()
c1.radius=10
c1.diameter()
c1.circumference()
c1.area()