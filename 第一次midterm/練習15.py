list1 = list(input("輸入一組四位數"))
if  len(list1) <4:
    list1 = list(input("輸入一組四位數"))
else:
    list1 = list(map(int,list1))
    for i in range(0,len(list1),1):
        list1[i]=(list1[i]+7)%10
    num_1 = list1[0]
    num_2 = list1[1]
    num_3 = list1[2]
    num_4 = list1[3]
list2 =[num_3,num_4,num_1,num_2]
print("加密後的數字為:",list2)


