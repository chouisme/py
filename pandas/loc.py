#%%
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt  
font ={'family':'DFKai-SB','weight':'bold','size':'12'}
plt.rc('font',**font)                                
plt.rc('axes',unicode_minus=False)
fruits_dict = {'fruits':['apple','banana','cherry','dates','eggfruit'],'quantity':[5,10,8,3,7],'color':['red','yellow','red','brown','yellow']}
df = pd.DataFrame(fruits_dict)
df.columns=['水果','數量','顏色']
df['價格']=[30,40,50,60,70]
row ={'水果':'kiwi','數量':'2','顏色':'green','價格':200}
print(df.loc[0,'數量'])
                        #df.loc[0,'數量']取的該列特定欄的資料
print(df.loc[0,:])     
                        #df.loc[0,:]取的該列的所有資料
print(df.loc[:,'價格'])
                        #df.loc[:,'價格']取得該欄的所有資料
df.plot.bar()

#%%
