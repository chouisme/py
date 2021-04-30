number =  list(str(input("輸入一串數字")))
number_list =  []

for i in range(0 , len(number),1):
    number_list.append(int(number[i]))
Max_list = sorted(number_list ,reverse=True)
Min_list = sorted(number_list)
Max_list_new = [str(x) for x in Max_list]
Min_list_new = [str(y) for y in Min_list]
for i  in Max_list:
    Max=int("".join(Max_list_new))
for c in Min_list:
    Min = int("".join(Min_list_new))
print("最大值數列與最小值數列差值為 :",Max-Min)


    