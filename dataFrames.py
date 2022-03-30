import pandas as pd
import numpy as np
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
nameKeys = pd.Series(data["Name"])
df = pd.DataFrame(data)
print("getting data via loc first argument is how many rows and second argument is how many columns")
names = df.loc[:2, ["Name"]]
print(names)
print()
# concatenating series
seriesOne = df["Age"]
seriesTwo = pd.Series([1, 2, 3, 4, 5])
print("first series")
print(seriesOne)
print()
print("second series")
print(seriesTwo)

# concatenatedSeries = seriesTwo.

# dictionary of lists
dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# putting data
backupData = dict
dataFrame = pd.DataFrame(dict)
# dataFrame.dropna(inplace=True)
dTypesBakcup = dataFrame.dtypes
dataFrame["First Score"] = dataFrame["First Score"].astype(str)
dataFrame["Second Score"] = dataFrame["Second Score"].astype(str)
print("before conversion")
print(dTypesBakcup)
print("after conversion")
print(dataFrame.dtypes)
print()
print("as a list by pandas.Series")
print(df["Name"].tolist())
print()
deletedNameSeries = df.drop([0], axis=0)
print(deletedNameSeries)
