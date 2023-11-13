class shape:
    def area (self):
        pass
class rectangle(shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        import math
        return math.pi*self.radius**2
rectangle=rectangle(5,4)
circle=circle(3)
print("Area of the rectangle:-",rectangle.area())
print("Area of the circle:-",circle.area())