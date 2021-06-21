#%%
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt  
s=pd.Series([1,3,5,7,9,6,8])                                                #產生數列,並且在左側產生索引(僅現一維)                                  
#print(s)
plt.plot(s)
fruits_dict = {'fruits':['apple','banana','cherry','dates','eggfruit'],'quantity':[5,10,8,3,7],'color':['red','yellow','red','brown','yellow']}
                                                                            #dataframe產生索引(自動產生)及欄標籤(字典內的key)，並且為二維的資料集
df = pd.DataFrame(fruits_dict)
#print(df)
df.columns=['水果','數量','顏色']                                                                           #更改dataframe的欄標籤
#print(df)
df.index=[1,2,3,4,5]                                                                                       #更改索引標籤
tmp=df[['水果','顏色']]                                                                                     #取其他dataframe任兩行組成dataframe
#print(tmp)
#tmp_2=df[0:2]                                                                                             #任取dataframe中的資料
#print(tmp_2)
#print(df.at[1,"水果"])                                                     
df['價格']=[30,40,50,60,70]                                                                                #新增欄位
row ={'水果':'kiwi','數量':'2','顏色':'green','價格':200}
df =df.append(row,ignore_index=True)                                                                       #新增資料,ignore_index(是否自動產生索引,預設為false)            
print(df)
df=df.drop(columns='水果')#df=df.drop(index=[1,4])                                                          #刪除欄
print(df)
#%%