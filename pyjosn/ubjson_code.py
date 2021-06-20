import pymysql
import requests
import  json
data = {'lang':'tw','type':'2'}
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="ic",charset="utf8")
r=requests.get("https://apis.youbike.com.tw/api/front/station/all",data)
tmp = json.loads(r.content)
cursor =conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT * FROM `ub`;")
rows = cursor.fetchall()                                                                                     
data =[]
for i in rows:
    data.append(i)
tmp = json.dumps(data,indent=1,ensure_ascii=False)                                
print(tmp)
conn.commit()                                                                      
cursor.close()                                                                    
conn.close()   