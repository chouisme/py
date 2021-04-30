dict1={"a":1,"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"j":11,"q":12,"k":13}
while True: 
    list1 =list(input("輸入").split(" "))
    if len(list1)!=5:
        list1 =list(input("輸入").split(" "))
    else:
        break
a= 0
for i in list1:
    a= a+dict1[i]
print(a)
        
     