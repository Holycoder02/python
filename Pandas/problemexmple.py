import pandas as pd

#df = pd.read_json("output.json")

#print('Displaying the info of data set')

#print(df.info())


data = {
    "Name": ["Alice", "bob", "charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

print('Displaying the info of the data set')
print(df.info())
