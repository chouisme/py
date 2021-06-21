#%%
import requests
import  pandas as pd
import  matplotlib.pyplot as plt 

check = input('輸入 1(查看股票),2(查看大盤)')
def in_sel():
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
if check=="1":
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
elif check == "2":

    all_head ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

    font ={'family':'DFKai-SB','weight':'bold','size':'12'}
    plt.rc('font',**font)                                
    plt.rc('axes',unicode_minus=False)

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
        in_sel()


        print('done')


    
#%%