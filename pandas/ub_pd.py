#%%
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt  
import  requests
import requests
import  json

font ={'family':'DFKai-SB','weight':'bold','size':'12'}
                                                        #字體設定

plt.rc('font',**font)                                
                                                        # **font 可變的參數
plt.rc('axes',unicode_minus=False)




data = {'lang':'tw','type':'2'}
r=requests.get("https://apis.youbike.com.tw/api/front/station/all",data)
ub = json.loads(r.content)
df = pd.DataFrame.from_dict(ub['retVal'])
#print(df)
print(df.loc[1746,:])
print(df['area_code'].value_counts())
                                                                            #計算該欄位中各值出現的次數
#print(df.loc[:,"area_code"].value_counts())
                                            
ktmp = df[df['area_code']=="12"]
#print(ktmp)
stationtatle = ktmp.groupby("district_tw").count()[['country_code']]
                                                                            #列印特定欄位的總數
#stationtatle = ktmp.groupby("district_tw").count()
                                                                            #列印所有欄位的總數
                                                                     
stationtatle['country_code'].plot.pie(title="高雄市區域",figsize=(10,10),y="area_code",autopct="%1.1f%%")
                                                                            #autopct="%1.1f%%" 計算每部分佔全部的百分比
tt =stationtatle.sort_values(by='country_code')    
                                                                            #以小到大排序   
tt['country_code'].plot.pie(title="高雄市區域",figsize=(10,10),y="area_code",autopct="%1.1f%%")
#%%