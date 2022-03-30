import pandas as pd
import numpy as np

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function
df.isnull()

#without filling the null values
print(df)

print("checking the values through the isnull function()")
# checking the null values using isnull
print(df.isnull())

# getting the rows contain atleast one null value using drop function
print(df.dropna())

# with filling the null values using fillna method
print("editing the values using inplace parameter value True")
df.fillna(0, inplace=True)
print(df)

# iterating over rows
iterCollection = df.iterrows()
print(type(iterCollection))
for i,j in iterCollection:
        print(j.loc["First Score"])
        print(type(j))

# getting data from the DataFrame
datas = list(df)
print(datas)

for i in datas:
        print( df[i][2] )

# # between in DataFrame
# print("using the between")
# print(df.loc[0:]["First Score"])
