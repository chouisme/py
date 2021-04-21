ans = input("請輸入答案")
a = list(ans)
g =input("請輸入數值")
b = list(g)
acounter = 0
bcounter = 0
length = len(a)
for i in range(0,length):
    if a[i] == b[i]:
        acounter +=1
    if a[i] != b[i] and b[i] in a:
        bcounter +=1
print(acounter,"A",bcounter,"B")


