len_check = True
while  True:
    a = int(input("輸入第一行正整數:"))
    b = list(input("第二行數列中的數字為:").split(" "))
    if a == len(b):
        break
    else:
        print("超出範圍")
dict1 ={}
for i in b:                #字典計數
    if i in dict1:         #判斷重複元素
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
dict1_new={v:k for k,v in dict1.items()}
check = False
count = len(dict1_new)
if count  == 1:
    check =True
if check == False:
    print("最大出現次數的數字為",dict1_new[max(dict1.values())])       
    print("出現次數為",max(dict1.values()))    
else:
    print("每個數字剛好都出現",max(dict1.values()),"次")

