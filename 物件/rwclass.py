import os
lista =[]
fp =open("C:\\py test\\物件\\txt\\test.csv","r")
tmp = fp.readlines()

for c in range(56):
    a1 =tmp[int(c)]
    a2 = a1.split("?")
    lista.append(a2)
for x in range(56):    
    del lista[x][0]
print(lista[2])
del lista[0]
class Student:
    def __init__(self):
        self.name = []
        self.sid = []
        self.git = []
        self.oclass = []
students = Student()
for oss in range(55):
    students.oclass.append(lista[oss][0])
for sids in range(55):
    students.sid.append(lista[sids][1])
for ns in range(55):
    students.name.append(lista[ns][2])
for gt in range(55):
    students.git.append(lista[gt][3])
print(students.git[3])