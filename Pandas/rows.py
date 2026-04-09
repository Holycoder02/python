#head() tail()

#head() 5
# tail(n) 5
# if you don't pass any values then, bydefault it will show the first and last (5) rows of the dataframe
# only integer values are allowed in head() and tail() functions


import pandas as pd 
df = pd.read_json("output.json")

print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))