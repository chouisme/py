a = int(input("輸入組數"))
b=0
c=0
sumt =[]
total = 0
for i in range(a):
    a,b=input("第"+str(i+1)+"組：").split(" ")
    total = int(a)*250+int(b)*175
    sumt.append(total)

for  f in range(len(sumt)):
    print("第"+str(f+1)+"組應付："+str(sumt[f])+"元")

