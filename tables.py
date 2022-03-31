import pandas as pd
data = { "Bob":["i like this!", "it was awful"], "Sue":["Pretty good !", "Bland!"] }
table = pd.DataFrame(data, index=["Person A", "Person B"])
print(table)
newRow = pd.Series(["active","offline"])
table["status"] = newRow
print(table)
