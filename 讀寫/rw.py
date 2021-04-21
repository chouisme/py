import os
fp =open("C:\\py test\\a.txt","r")
tmp= fp.readlines()
for i in tmp:
    print(i)
a = tmp[0]
b = tmp[1]
c = tmp[2]
a1= a.split("\n")
a2=a1[0].split("/")
print(a2)
fp.close()