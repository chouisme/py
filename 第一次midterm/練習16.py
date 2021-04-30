n,m = input("輸入兩數 :").split(" ")
n= int(n)
m= int(m)
while True:
    list1=list(input("輸入第一列數字").split(" "))
    list2=list(input("輸入第二列數字").split(" "))
    num1 = list1+list2
    num1 =list(map(int, num1))
    if len(list1)==m and len(list2)==m:
        break
    else:
        print("長度不夠")
a,b =input("輸入兩數 :").split(" ")
a= int(a)
b = int(b)
while True:
    list3 = list(input("輸入第一列數字").split(" "))
    list4 = list(input("輸入第二列數字").split(" "))
    num2 =list3+list4
    num2 =list(map(int, num2))
    if len(list3)==b and len(list4)==b:
        break
    else:
         print("長度不夠")
list5=[]
for i in range(0,n*m,1):
    list5.append(num1[i]+num2[i])
if m == n:
    for i in range(0,n-1,1):
        e= 0
        for d in range(0,m,1):
            print(list5[e],list5[e+1])
            e= e+2
else:
    print("無法相加")