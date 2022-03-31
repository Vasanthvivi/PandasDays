import pandas as pd
schema = pd.read_csv("sampleData.csv", index_col=["Name"], usecols=["Name", "Team", "Position"])
print(schema.head(5))
# filtering
print(schema.loc[ ["AdamDonachie","KevinMillar"], ["Team", "Position"] ])