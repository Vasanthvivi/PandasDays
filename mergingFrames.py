import pandas as pd

# Define a dictionary containing employee data
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32], }

# Define a dictionary containing employee data
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data1)

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2)
print("table one")
print(df)
print()
print("table two")
print(df1)
print()

print("inner join")
res1 = pd.merge(df, df1, on=['key', 'key1'], how="inner")
print(res1)

print("right join")
res1 = pd.merge(df, df1, on=['key', 'key1'], how="right")
print(res1)

print("left join")
res1 = pd.merge(df, df1, on=['key', 'key1'], how="left")
print(res1)

print("outer join")
res1 = pd.merge(df, df1, on=['key', 'key1'], how="outer")
print(res1)
