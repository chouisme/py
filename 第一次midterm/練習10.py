n,m = input("輸入兩數 :").split(" ")
n= int(n)
m= int(m)
list1 =[]
for i in range(0,n,1):
    list2 =[]
    list2 = input("輸入矩正的值").split(" ")
    for  b in range(m ,m,1):
        del list2[m]
    list3 = [list2]
    list1 = list1+list3
for c in range(0,m,1):
    for d in range(0,n,1):
        print(list1[d][c],end =" ")
    print("\n")
    