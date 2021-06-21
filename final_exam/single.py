#%%

import requests
import  pandas as pd
import  matplotlib.pyplot as plt 
font ={'family':'DFKai-SB','weight':'bold','size':'12'}
plt.rc('font',**font)                                
plt.rc('axes',unicode_minus=False)
head ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}



stock_id =input("輸入股票代碼")
response =requests.post("https://ww2.money-link.com.tw/TWStock/StockChart.aspx?SymId={}".format(stock_id),headers=head)
if response.status_code== 200:
    table_val = []
    url='https://ww2.money-link.com.tw/TWStock/StockChart.aspx?SymId={}'.format(stock_id)
    df_dict = []
    df=pd.read_html(url)[1]
    df_dict=df
    df_dict=df.drop(columns=[2,5])
    stock_dict ={'開盤:':[df_dict[1][0]],'昨收:':[df_dict[1][1]],'最高':[float(df_dict[4][0])],'買進':[float(df_dict[4][1])],'最低':[float(df_dict[7][0])],'賣出':[float(df_dict[7][1])]}
    df_stock =pd.DataFrame(stock_dict) 
    df_stock.plot.bar(title='股市',figsize=(10,5))
    print(df_dict)
    print('done')


  
  

 

#%%