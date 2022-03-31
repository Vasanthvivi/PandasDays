import pandas as pd
data = pd.read_csv("sampleData.csv")
# using the iloc method
print(data.iloc[:3, [0,1]])
# using the loc method
print(data.loc[:3, ["Name","Team"]])
# getting last 5 data
print(data.iloc[-5:])
# getting first three data
print(data.iloc[ [0,1,2], [0]])
# describe method defines the dimensions of the data we have got
# print(data.describe())
# setting the index via set_index
print(data.set_index("Name"))
# filtering data persons from age between 20 and 25
condition = (data.Age > 20.00) & (data.Age < 22.00)
print(data.loc[condition])
# getting the DET Team persons only using isin
condition = data["Team"].isin(["DET"])
print(data.loc[condition])
data["critic"] = "everyone"
print(data)