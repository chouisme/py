a,b =input("請輸入通話費形式和通話時間").split(",")
cost = float(a)
time = float(b)
price = 0
if cost == 186:
    price = time * 0.09
    if price/cost >1:
        price = time *0.09*0.8
    elif price/cost <=1 and price !=cost:
        price = time *0.09*0.9
    else:
        price = cost
elif cost == 386:
    price = time * 0.08
    if price / cost > 1:
        price = time *0.08*0.7
    elif price/cost <=1 and price !=cost:
        price = time *0.08*0.8
    else:
        price = cost   
elif cost == 586:
    price = time * 0.07
    if price/cost >1:
        price = time *0.07*0.6
    elif price/cost <=1 and price !=cost:
        price = time *0.07*0.7
    else:
        price = cost   
elif cost == 986:
    price = time * 0.06
    if price/cost >1:
        price = time *0.06*0.5
    elif price/cost <=1 and price !=cost:
        price = time *0.06*0.6
    else:
        price = cost
else:
    print("查無此月費")
print("通話費為 : ",round(price))