import  pandas as pd 
import  numpy as np
from pandas.core.arrays import categorical
df_catgorical = pd.DataFrame({'A':np.arange(6),"B":list('aabbca')})
cat = pd.CategoricalDtype(categories=['a','b','c'])
df_catgorical['B'] = df_catgorical['B'].astype(cat)
print(df_catgorical)
print(df_catgorical.index)
print(df_catgorical.columns)


df_catgorical = df_catgorical.set_index('B')
print(df_catgorical)
print(df_catgorical.index)
print(df_catgorical.columns)

#serch the data in category 'a'
print(df_catgorical.loc["a"])