class Car:
    def __init__(self,brand,cc):
        self.brand=brand
        self.cc=cc
t1 = Car("toyota",2000)
t2 = Car("BMW",2500)
t3 = Car("Honda",1200)
print(t2.cc)
print(t2.brand)
swap = t2
t2 = t3
t3 = swap
print(t2.cc)
print(t2.brand)