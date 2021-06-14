import math
class cal2:
    def setdata(self,radius):
        self.radius = radius
    def area(self):
            area = math.pi *(radius**2)
            self.area = area
    def display(self):
                print('area of circle is :{:.2f}'.format(self.area))

radius = int(input("enter a radius of the circle :"))
obj = cal2()
obj.setdata(radius)
obj.area()
obj.display()