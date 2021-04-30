list1 = input("輸入").split(" ")
list_len =  int(round(len(list1)/2))
dict1={}

list2=[]
for i in list1:
    if i in dict1:
        dict1[i]= dict1[i]+1
    else:
        dict1[i]=1
a = max(dict1.values())
dict1_new={v:k for k,v in dict1.items()}
if max(dict1.values()) > list_len:
    print("過半元素為",dict1_new[a])
else:
    print("過半元素為:NO")
    
        
    
