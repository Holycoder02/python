"""
vertically (row-wise)
horizontally (column-wise)

pd.concat([df1, df2], axis=0, ignore_index=True) - it will concatenate the two dataframes vertically (row-wise) and reset the index.
pd.concat([df1, df2], axis=1) - it will concatenate the two

dataframes horizontally (column-wise) based on the index. if the index is not the same then it will fill the missing values with NaN.


"""

#vertical concatenation
import pandas as pd

df_Region1 = pd.DataFrame({
    'CustomerID': [1,2],
    'Name': ['Ramesh', 'Sureesh']
})

df_Region2 = pd.DataFrame({
    'CustomerID': [3,4],
    'Name': ['Kalpesh', 'Suresh']
})

#concatenate vertically
df_concat = pd.concat([df_Region1, df_Region2], ignore_index=True)
print(df_concat)

#horizontal concatenation
df_concat = pd.concat([df_Region1, df_Region2], axis= 1, ignore_index=True)
print(df_concat)