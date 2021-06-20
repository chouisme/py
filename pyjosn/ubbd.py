import pymysql
import requests
import  json
data = {'lang':'tw','type':'2'}
r=requests.get("https://apis.youbike.com.tw/api/front/station/all",data)
tmp = json.loads(r.content)
conn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="ic",charset="utf8")
cursor =conn.cursor(pymysql.cursors.DictCursor)
val_list=[]
for i in tmp['retVal']:
    values = []
    for value in i.items(): 
        values.append(value)
    val_list.append(values)
list_len = len(val_list)-1

for i in range(0,list_len):
    cursor.execute("INSERT INTO `ub` (`country_code`,`area_code`,`type`,`status`,`station_on`,`name_tw`,`district_tw`,`address_tw`,`name_en`,`district_en`,`address_en`,`name_cn`,`district_cn`,`address_cn`,`parking_spaces`,`available_spaces`,`empty_spaces`,`forbidden_spaces`,`lat`,`lng`,`img`,`updated_at`,`time`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(val_list[i][0][1],val_list[i][1][1],val_list[i][2][1],val_list[i][3][1],val_list[i][4][1],val_list[i][5][1],val_list[i][6][1],val_list[i][7][1],val_list[i][8][1],val_list[i][9][1],val_list[i][10][1],val_list[i][11][1],val_list[i][12][1],val_list[i][13][1],val_list[i][14][1],val_list[i][15][1],val_list[i][16][1],val_list[i][17][1],val_list[i][18][1],val_list[i][19][1],val_list[i][20][1],val_list[i][21][1],val_list[i][22][1]))
conn.commit()                                                                      
cursor.close()                                                                     
conn.close() 