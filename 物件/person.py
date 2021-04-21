class Head:
    def __init__(self,size):
        self.size = size
class Body:
    def __init__(self,vol):
        self.vol = vol
class Hand:
    def __init__(self,length):
        self.length=length
class Leg:
    def __init__(self,width):
        self.width =width
class People:
    def __init__(self,hd,bd,rh,lh,rl,ll):
        self.hd = hd
        self.bd = bd
        self.rh = rh
        self.lh = lh
        self.rl = rl
        self.ll = ll

lee = People(Head(60),Body(50),Hand(30),Hand(30),Leg(40),Leg(40))
print(lee.bd.vol)
print(lee.ll.width)



class Eng:
    def __init__(self,cc):
        self.cc = cc
class wheel:
    def __init__(self,size):
        self.size =size
class Car:
    def __init__(self,eg,w1,w2,w3,w4):
        self.eg = eg
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4
t1 = Car(Eng(2000),wheel(50),wheel(50),wheel(50),wheel(50))
print(t1.w4.size)
print(t1.eg.cc)