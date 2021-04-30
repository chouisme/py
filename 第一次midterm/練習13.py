list1 = list(input("輸入"))
list2 = list1
list2 = list2[len(list1)-1::-1]
if list1>=list2:
    print("YES")
else:
    print("NO")
    
