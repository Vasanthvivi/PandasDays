import pandas as pd
data = pd.read_csv("sampleData.csv")
teamGroups = data.groupby("Team")
print("Total teams ")
print(len(teamGroups.groups.keys()))
print("DET Team got {} members!".format(len(teamGroups.groups["DET"])))
# getting the data
print("getting the data using aggregation functions")
print( data.groupby(['Team']).Age.agg([len, min, max]) )
print("first data from the groupby object ")
print(teamGroups.groups["ANA"])
print("sorting values by Age")
print(data.sort_values(by="Age"))
print("sorting values using Name")
print(data.sort_values(by="Name"))
print("sorting in descending order")
print(data.sort_values(by="Age", ascending=False))
print("sorting in descending order using Name Series")
print(data.sort_values(by="Name", ascending=False))
print("sorting in ascending using multiple series such as Name and Age")
print(data.sort_values(by=["Age", "Name"]))






