import os 
fp=open("C:\\py test\\mid\\1.txt","r",encoding="utf-8")
tmp =fp.readlines()
class Pru():
    def __init__(self):
        self.prud = []
a=Pru()
for i in tmp:
    a.prud.append(i)



