

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
a= Point()
d,e = input("enter：").split(" ")
a.set_xy(d,e)
print(a.get_x())
print(a.get_y())
print(a.__add__())
print(a.__mul__())