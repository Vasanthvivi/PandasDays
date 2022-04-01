import pandas as pd
data = pd.read_csv("sampleData.csv")
# setting max rows as 5
print(data)
# renaming Height(inches) column name to Height
data.rename(columns={ "Height(inches)":"Height", "Weight(lbs)":"Weight" }, inplace=True)
print("after renaming applied")
print(data)
# renaming row wise using index
data.rename(index={ 0:"Captain", 1:"Vice Captain" }, inplace=True)
print(data)
# getting the captain values
print("Captain")
print(data.loc["Captain"])
# getting the vice captain values
print("Vice Captain")
print(data.loc["Vice Captain"])
print()
print()
# applying data axis names
data.rename_axis("Players",axis="rows", inplace=True)
data.rename_axis("Fields", axis="columns", inplace=True)
print(data)


