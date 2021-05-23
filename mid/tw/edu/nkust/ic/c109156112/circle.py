from math import pi


class Circle:
    def __init__(self,radius=1.0):
        self.radius=radius
    def __str__(self):
        return "test-"+str(self.radius)
    def __repr__(self):
        return "test"
    def get_area(self):
        return pi*self.radius*self.radius
