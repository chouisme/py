b =[87,80,3,33]
lnegth = len(b)
for c in range(0,lnegth):
    for i in range(0,lnegth-c-1,1):
        if b[i]>b[i+1]:
            tmp =b[i]
            b[i]=b[i+1]
            b[i+1]=tmp
print(b)
# "-c" 比較完成的數值不列入比較
#tmp = b[0] 交換
#b[0]=b[1]
#b[1]=tmp