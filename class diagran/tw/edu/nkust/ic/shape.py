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
        return pi*float(self.radius)*float(self.radius)

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "test"
    def __repr__(self):
        return "test"
    def __add__(self):
        return int(self.x)+int(self.y)
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_xy(self,cx,cy):
        self.x = cx
        self.y = cy
    def __mul__(self):
        return int(self.x)*int(self.y)

class Ret:
    def __init__(self,length=1,width=2):
        self.length = length
        self.width = width
    def set_length(self,leng):
        self.length = leng
    def get_length(self):
        return self.length
    def set_width(self,wid):
        self.width = wid
    def get_width(self):
        return self.width
