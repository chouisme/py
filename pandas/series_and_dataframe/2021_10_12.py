from numpy import append
import pandas as pd


studentPerformance = pd.read_csv('pandas\series_and_dataframe\StudentsPerformance_modify.csv',index_col='ID',usecols=[0,6,7,8])
New_Sp = studentPerformance[:5].copy()


# print(studentPerformance)

# print(f"New_Sp is {New_Sp}")
# #drop
# drop = New_Sp.drop(['math score'],axis=1)

# print(f"drop New_Sp is {drop}")

# #del
# del New_Sp['math score']
# print(f"del New_Sp is {New_Sp}")

# #pop

# pop = New_Sp['reading score']

# print(f"pop New_Sp is {pop}") 
students = pd.Series(["steven","Jim","Amy","Wendy"])
score_math = pd.Series([60,70,80,90])
score_eng  = pd.Series([65,75,85,95])
df = pd.DataFrame({'name':students , 'math':score_math,'English':score_eng})
df  = df.set_index("name")
print(df)



students1 = pd.Series(["steven","Jim","Amy","Wendy"])
score_python = pd.Series([10,20,30,40])
score_chi =pd.Series([15,25,35,45])
df1 = pd.DataFrame({'name':students1 , 'python':score_python,'chinese':score_chi})
df1 = df1.set_index('name')
print(df1)

appended = df.append(df1)
print(appended)