#%%

import requests
import  pandas as pd
import  matplotlib.pyplot as plt 


font ={'family':'DFKai-SB','weight':'bold','size':'12'}
plt.rc('font',**font)                                
plt.rc('axes',unicode_minus=False)
all_head ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}



response =requests.post("https://ww2.money-link.com.tw/TWStock/TWStockMarket.aspx?optionType=2#SubMain",headers=all_head)
if response.status_code == 200:
    url ='https://ww2.money-link.com.tw/TWStock/TWStockMarket.aspx?optionType=2#SubMain'
    listed_tatble=pd.read_html(url)[4]
    listed_tatble_index={}
    listed_tatble_val=listed_tatble
    emerging_tatble=pd.read_html(url)[5]
    a=4
    index_text=['融資張數','融券張數','融資金額(萬)']
    for i in range(0,3):
        listed_tatble_index={'本日餘額':[listed_tatble.loc[0][a]/100,listed_tatble.loc[1][a],listed_tatble.loc[2][a]],'前日餘額':[listed_tatble.loc[0][a+1]/100,listed_tatble.loc[1][a+1],listed_tatble.loc[2][a+1]],'餘額增減':[listed_tatble.loc[0][a+2],listed_tatble.loc[1][a+2],float(listed_tatble.loc[2][a+2]*1000)]}
    for i in range(0,3):
        emerging_tatble_index={'本日餘額':[emerging_tatble.loc[0][a]/100,emerging_tatble.loc[1][a],emerging_tatble.loc[2][a]],'前日餘額':[emerging_tatble.loc[0][a+1]/100,emerging_tatble.loc[1][a+1],emerging_tatble.loc[2][a+1]],'餘額增減':[emerging_tatble.loc[0][a+2],emerging_tatble.loc[1][a+2],float(emerging_tatble.loc[2][a+2]*1000)]}

    df_listed = pd.DataFrame(listed_tatble_index,index=index_text)
    df_emerging=pd.DataFrame(emerging_tatble_index,index=index_text)
    df_listed.plot.barh(title="上市大盤信用交易",subplots=True,figsize=(10,5))
    df_emerging.plot.barh(title="上櫃大盤信用交易",subplots=True,figsize=(10,5))
    print('done')

  


 

#%%