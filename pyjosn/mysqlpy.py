import pymysql
import  json

conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="ic",charset="utf8")
db1="hi"
db2 ="006"
conmon="'"
db1=str(db1)
print(db1)
cursor =conn.cursor(pymysql.cursors.DictCursor) #pymysql.cursors.DictCursor使傳回資料為字典型態
#cursor =conn.cursor()======>未指定傳回的資料型態
#cursor.execute("CREATE TABLE `ic`.`c109156112test`(`name` VARCHAR(10) NOT NULL , `id` VARCHAR(10) NOT NULL) ENGINE = InnoDB charset=utf8mb4 COLLATE utf8mb4_general_ci;")                             
                                                #用於下達SQL指令,新增資料庫

cursor.execute("INSERT INTO `c109156112test` (`name`,`id`) VALUES (%s,%s)",(db1,db2))#新增資料
#cursor.execute("DROP TABLE book;")                                                #刪除資料庫

cursor.execute("SELECT * FROM `c109156112test`;")
rows = cursor.fetchall()                                                           #將資料表內的data存取到row中
for i in rows:                                                                     #以迴圈的方式列印所有資料
    print(i)                            
data =[]
for i in rows:
    data.append(i)
print (data)
tmp = json.dumps(data,indent=1,ensure_ascii=False)                                 #dictionary====>byte or string,  ensure_ascii=False保留原本輸入的格式, indent=1排版(縮排)
print(tmp)


conn.commit()                                                                      #確認SQL指令是否執行
cursor.close()                                                                     #關閉通道以免誤佔port
conn.close()    
                              



