#%%
import requests
import  pandas as pd
import  matplotlib.pyplot as plt 
font ={'family':'DFKai-SB','weight':'bold','size':'12'}
plt.rc('font',**font)                                
plt.rc('axes',unicode_minus=False)
in_head ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
url_in='https://ww2.money-link.com.tw/TWStock/TWStockMacroeconoic.aspx?mainOptionType=2&optionType=1'
res =requests.post(url_in,headers=in_head)
if res.status_code == 200:
    indicators=pd.read_html(url_in)[4]
    val_len=len(indicators.values)
    print(val_len)
    print(indicators.values[0][0])
    date=[]
    score=[]
    f_indicators=[]
    n_indicators=[]
    clame_check=[]
    buy_check=[]
    manerger=[]
    score_index=[]
    f_indicators_index=[]
    n_indicators_index=[]
    clame_check_index=[]
    buy_check_index=[]
    manerger_index=[]
    for i in range(0,23):
        date.append(indicators.values[i][0])
        score.append((indicators.values[i][1]))
        f_indicators.append(indicators.values[i][3])
        n_indicators.append(indicators.values[i][4])
        clame_check.append(indicators.values[i][5])
        buy_check.append(indicators.values[i][6])
        manerger.append(indicators.values[i][7])
    for i in range(0,23):
        ch_1=score[i]
        ch_2=f_indicators[i]
        ch_3 =n_indicators[i]
        ch_4 =clame_check[i]
        ch_5 =buy_check[i]
        ch_6 =manerger[i]
        if ch_1 =='-':
            ch_1=0
        if ch_2 =='-':
            ch_2=0
        if ch_3 =='-':
            ch_3=0  
        if ch_4 =='-':
            ch_4=0
        if ch_5 =='-':
            ch_5=0
        if ch_6 =='-':
            ch_6=0                      
        ch_1=float(ch_1)
        ch_2=float(ch_2)
        ch_3=float(ch_3)
        ch_4=float(ch_4)
        ch_5=float(ch_5)
        ch_6=float(ch_6)       
        score_index.append(ch_1)
        f_indicators_index.append(ch_2)
        n_indicators_index.append(ch_3)
        clame_check_index.append(ch_4)
        buy_check_index.append(ch_5)
        manerger_index.append(ch_6)

    in_inedex_sel = {'分數':score_index}
    df_in=pd.DataFrame(in_inedex_sel,index=date)
    df_in.plot.line(title="近期景氣分數",grid=True,figsize=(10,5))

    inedex_sel_2={"領先指標":f_indicators_index,'同時指標':n_indicators_index}
    df_2_in =pd.DataFrame(inedex_sel_2,index=date)
    df_2_in.plot.line(title='領先指標與同時指標',subplots=True,grid=True,figsize=(10,5))

    index_sel_3={'製造業營業氣候測驗點':clame_check_index,'臺灣製造業採購經理人指數':buy_check_index,'匯豐臺灣採購經理人指數':manerger_index}
    df_3_in=pd.DataFrame(index_sel_3,index=date)
    df_3_in.plot.box(title='各項指數',figsize=(10,5),grid=True)


    print('done')

  


 

#%%