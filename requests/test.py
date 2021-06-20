import  requests
data = {'user':'no.1'}
r=requests.get("http://localhost/py/get.php",data)


print(r.content.decode("utf-8"))
if r.status_code == 200:
    print(r.content.decode("utf-8"))

data = {'lang':'tw','type':'2'}
r=requests.get("https://apis.youbike.com.tw/api/front/station/all",data)


print(r.content.decode("utf-8"))
if r.status_code == 200:
    print(r.content.decode("utf-8"))



for i in range(0,10):
    r=requests.get("https://www.google.co.jp/landing/motto/tabplay/{}.jpg".format(i))
    if r.status_code == 200:
        f=open(f'./requests/{i}.jpg','wb') #指定value到string(f'...' or "....".format(value))
        f.write(r.content)
        f.close()


data = {'_nc_cat':'107','ccb':'1-3','_nc_sid':'825194','_nc_cat':'107','_nc_ohc':'ABt10To6IQ0AX8-Ip7S','_nc_ht':'scontent.fkhh2-2.fna','oh':'a539823a32a993638d2af914682417dc','oe':'60D2FB95'}      
r=requests.get("https://scontent.fkhh2-2.fna.fbcdn.net/v/t1.6435-9/197596044_3680714838700531_3718044288367546156_n.jpg",data)
if r.status_code == 200:
    f=open('./requests/cat.jpg','wb') 
    f.write(r.content)
    f.close()
