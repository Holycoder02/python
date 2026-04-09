import pandas as pd 

data = {
    "Name": ["Ram", "Shyam", "Hari"],
    "Age": [25, 30, 35],
    "City": ["Nagpur", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df)

#    Name  Age    City
#0    Ram   25  Nagpur
#1  Shyam   30  Mumbai
#2   Hari   35   Delhi

# for instance you can see the output it gave but i don't want to remove the numbers from there for that we'll see

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
# Hence, you can see the output,csv file is created without the inddex numbers.
