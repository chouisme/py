from math import pi


class Circle:
    def __init__(self,radius=1.0):
        self.radius=radius
    def __str__(self):
        return "test-"+str(self.radius)
    def __repr__(self):
        return "test"
    def get_radius(self):
        return self.radius
    def set_radius(self,tmp):
        self.radius = tmp
    def get_area(self):
        return pi*self.radius*self.radius

a=Circle()

#tmp = input("enter：")
#a.set_radius(tmp)
print(a.get_area())
#print(a.__str__())
#print(a.get_radius())

