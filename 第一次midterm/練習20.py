a=[[0]*3 for i in range(3)]
b=[]
p={}
add = 0

for i in range(3):
    for c in range(3):
        a[i][c]=int(input("輸入："))
        b.append(a[i][c])
        p[a[i][c]]=str(i+1)+","+str(c+1)
b.sort(reverse=True)
for j in range(3):
    add = add + b[j]
print("位置為"+"("+str(p[b[0]])+")"+","+"("+str(p[b[1]])+")"+","+"("+str(p[b[2]])+")")
print("最大值為："+str(add))


