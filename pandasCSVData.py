import pandas as pd
df = pd.read_csv("sampleData.csv", index_col="Name")
print(pd.get_option("display.max_columns"))
pd.set_option("display.max_columns", 0)
# print(df.head(10))

# print the schema columns
# print(df.columns)

# print the whole table
# print(df)

# getting the data through customized indexes
print(df.loc["AdamDonachie"])

# getting data via series or columns
# print(df["Position"])
