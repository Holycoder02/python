"""
syntax: pd.merge(df1, df2, on="column_name", how="type of join")
types of join:
1. inner join: it will return only the common rows between the two dataframes based on the specified column.
2. left join: it will return all the rows from the left dataframe and the matching rows
3. right join: it will return all the rows from the right dataframe and the matching rows from the left dataframe.
4. outer join: it will return all the rows from both dataframes, filling in NaN for missing values where there is no match.
5. cross join: it will return the Cartesian product of the two dataframes, combining each row of the first dataframe with every row of the second dataframe.
6. self join: it is a special case of join where a dataframe is joined with itself. it is used to compare rows within the same dataframe based on a common column.
7. anti join: it will return the rows from the left dataframe that do not have a match in the right dataframe based on the specified column.
8. semi join: it will return the rows from the left dataframe that have a match in
the right dataframe based on the specified column, but it will not include the columns from the right dataframe in the result.
"""

import pandas as pd

#Customer DataFrame
df_customer = pd.DataFrame({
    'CustomerID': [1,2,3],
    'Name': ['Ramesh', 'Sureesh', 'Kalpesh']
})

#Order DataFrame
df_order = pd.DataFrame({
    'CustomerID': [1,2,4],
    'OrderID': [101, 102, 103]

})

#merge
df_merged = pd.merge(df_customer, df_order, on='CustomerID', how='inner')
print('Inner Join')
print(df_merged)

"""
# left join
df_merged = pd.merge(df_customer, df_order, on='CustomerID', how='left')
print('Left Join')
print(df_merged)

# right join
df_merged = pd.merge(df_customer, df_order, on='CustomerID', how='right')
print('Right Join')
print(df_merged)

# outer join
df_merged = pd.merge(df_customer, df_order, on='CustomerID', how='outer')
print('Outer Join')
print(df_merged)

# cross join
df_merged = pd.merge(df_customer, df_order, how='cross')
print('Cross Join')
print(df_merged)

# self join
df_merged = pd.merge(df_customer, df_customer, on='CustomerID', how='inner')
print('Self Join')
print(df_merged)

# anti join
df_merged = pd.merge(df_customer, df_order, on='CustomerID', how='left', indicator=True)
df_anti_join = df_merged[df_merged['_merge'] == 'left_only'].drop(columns=['OrderID', '_merge'])
print('Anti Join')
print(df_anti_join)

# semi join
df_merged = pd.merge(df_customer, df_order, on='CustomerID', how='inner')
df_semi_join = df_merged.drop(columns=['OrderID'])
print('Semi Join')
print(df_semi_join)

# Note: The above code snippets for different types of joins are commented out. You can uncomment them one by one to see the results for each type of join.

"""