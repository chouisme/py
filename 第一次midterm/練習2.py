a = float(input("輸入所使用的度數:"))
if a<=120:
    summer = a*2.10
    Non_summer = a*2.10
    print("Summer_Month :",summer)
    print("Non_Sunmmer_month",Non_summer)
elif a>=121 and a<=330:
    summer = 120*2.10+(a-120)*3.02
    Non_summer = 120*2.10+(a-120)*2.68
    print("Summer_Month :",summer)
    print("Non_Sunmmer_month",Non_summer)
elif a>=331 and a <=500:
    summer = 120*2.10+210*3.02+(a-330)*4.39
    Non_summer =120*2.10+210*2.68+(a-330)*3.61
    print("Summer_Month :",summer)
    print("Non_Sunmmer_month",Non_summer)
elif a >=501 and a <=700:
    summer = 120*2.10 + 210*3.02 + 170*4.39 +(a-500)*4.97
    Non_summer = 120*2.10 + 210*2.68 + 170*3.61 +(a-500)*4.01
    print("Summer_Month :",summer)
    print("Non_Sunmmer_month",Non_summer)
else:
    summer = 120 *2.10 + 210*3.02 +170 * 4.39 + 200 *4.97 + (a-700)*5.63
    Non_summer =120 *2.10 + 210*2.68 +170 * 3.61 + 200 *4.01 + (a-700)*4.50
    print("Summer_Month :",summer)
    print("Non_Sunmmer_month",Non_summer)
    