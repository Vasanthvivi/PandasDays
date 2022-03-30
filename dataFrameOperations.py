import pandas as p
# DataFrame
import pandas as pd

data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
schema = p.DataFrame(data)
newRow = p.DataFrame( { "Name":['sample name'], 'Age':[22] } )
df = p.concat([ schema, newRow ]).reset_index(drop=True)
print(df)
# head method
print(df.head(4))
print(df.tail(3))
intdata = pd.Series([1,2,3,5])
print(type(intdata[0]))
strdata = pd.Series([1,2,3,5]).astype(str)
print(strdata)
print(type(strdata[0]))
# filtering
filteredData = df["Age"] >= 19
print("filetered data")
print(df[filteredData])
# print(schema)
# d = schema.drop([0,1], axis=0, inplace=True)
# print(schema)
