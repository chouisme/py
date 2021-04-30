x = int(input("輸入X座標"))
y = int(input("輸入Y座標"))
if (x == 0 and y == 0):
    print("該點位於原點")
elif(x == 0 and y >0):
    position =y*y
    print("該點位於上半平面Y軸上，離原點距離根號",position)
elif (x == 0 and y < 0):
    position = y*y
    print("該點位於下半平面Y軸上，離原點距離根號",position)
elif (x < 0 and y == 0):
    position =x*x
    print("該點位於左半平面X軸上，離原點距離根號",position)
elif (x>0 and y ==0):
    position = x*x
    print("該點位於右半平面X軸上，離原點距離根號",position)
elif (x>0 and y > 0 ):
    position = x*x+y*y
    print("該點位於第一象限，離原點距離根號",position)
elif(x < 0 and y > 0):
    position = x*x+y*y
    print("該點位於第二象限，離原點距離根號",position)
elif (x < 0 and y < 0):
    position = x*x+y*y
    print("該點位於第三象限，離原點距離根號",position)
else:
    position = x*x+y*y
    print("該點位於第四象限，離原點距離根號",position)
