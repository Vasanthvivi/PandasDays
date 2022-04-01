import pandas as pd
data = pd.read_csv("sampleData.csv")
statusData = pd.read_csv("statusSample.csv")
data.rename(columns={ "Weight(lbs)":"Weight" }, inplace=True)
data.rename(columns={ "Height(inches)":"Height" }, inplace=True)
data.rename_axis("Fields", axis="rows", inplace=True)
data.rename_axis("Players", axis="columns", inplace=True)
statusData["status"] = "active"
combinedData = pd.concat([ data, statusData ])
print(combinedData)
print("")
data.set_index()
