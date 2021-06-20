import  json
import requests

data = {'lang':'tw','type':'2'}
r=requests.get("https://apis.youbike.com.tw/api/front/station/all",data)

#print(r.content.decode("utf-8"))
if r.status_code == 200:
    #print(r.content.decode("utf-8"))
    #json.loads string or byte ----> dictionary
    tmp = json.loads(r.content)
    #print (tmp['retCode'])      
    #print(tmp['retMsg'])
    #print(len(tmp['retVal']))
    #print(tmp["retVal"][0])

    #for i in tmp['retVal']:
    #    print(i)

    for i in range(0,1):
        a=i
        for key , value in tmp['retVal'][a].items(): #tmp['retVal'][0].items() 呼叫該字典裡的所有物件 
            print(key,"：",value)

    #for i in tmp['retVal']:
    #   for key , value in i .items():
    #       print(key,"：",value)

    #for i in tmp['retVal']:
    #    values=[]
    #    keys=[]
    #    for key , value in i.items():
    #        values.append(value)
    #        keys.append(key)
    #    print(values)
    #    print(keys)
    
    
    #keys =[i[0] for i in tmp['retVal'][0].items()] #i[0]為該串列內的第一個元素(key)
    #values=[i[1]for i in tmp['retVal'][0].items()] #i[1]為該串列內的第二個元素(value)
    #print(keys)
    #print(values)

    #totalval = []
    #for i in tmp['retVal']:
    #    values=[j[1] for j in i.items()]
    #    totalval.append(values)
    #print(totalval)

