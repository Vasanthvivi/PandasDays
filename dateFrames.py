import pandas as pd

data = pd.date_range('1/1/2011', periods=5)
print(data)
print(type(data))
print("now what is the timestamp")
print(pd.tslib.Timestamp.now())
