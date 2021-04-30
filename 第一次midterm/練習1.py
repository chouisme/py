prime = input("請輸入正整數") 
number_list =list(str(prime))
number_list2 =[]
for c in range(0,len(number_list),1):
    prime_list = str()
    for d in range(c,len(number_list),1):
        prime_list = prime_list + number_list[d]
        prime_list = int(prime_list)
        prime_check = 0
        for check in range(2,prime_list-1,1):
            number_2 = prime_list % check
            if (number_2 == 0):
                prime_check = 1
        if (prime_check != 1):
            prime_list = int(prime_list)
            number_list3 = [prime_list]
            number_list2 = number_list2+number_list3
        prime_list =str(prime_list)
number_list2 = sorted(number_list2 ,reverse= True)
if len(number_list2)!=0:
    print("子字串中最大的質數值為 :",number_list2[0])
else:
    print("子字串中最大的質數值為 :NO prime found")