class cricle:
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        f=3.14*(self.radius**2)
        print(f)
    def getv(self):
            a=3.14*self.radius*2
            print(a)
r=int(input("enter:-"))
c1=cricle(r)
c1.getarea()
c1.getv()


