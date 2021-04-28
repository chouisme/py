year = input("輸入年份")
month = input("輸入月份")
day = input("輸入日期")
data = year +month +day
sum = 0
for i in data:
    sum =sum +int(i)
if sum >10:
    c=str(sum)
    sum =0
    for a in c:
        sum = sum +int(a)
print(sum)