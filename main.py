import pandas as p

data = {
    "Name": ["nameone", "nametwo", "namethree", "namefour"],
    "status": ["running", "stopped", "running", "stopped"],
    "Id": [1, 2, 3, 4]
}
dataFrame = p.DataFrame(data)

# printing the series
print(dataFrame["Name"])

print("printing the first name from the DataFrame")
# getting the right data
print(dataFrame["Name"][0])

nameid = dataFrame.set_index('Name')

# customizing the index
print("customized index")
print(nameid)

print("indexing values using the loc")
# indexing
print(dataFrame.loc[[0, 1]])
# print( dataFrame.loc[0:1, "Name":"status"] )


# printing via customized rows
records = {
           'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
           'Age': [27, 24, 22, 32],
           'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
           'Qualification': ['Msc', 'MA', 'MCA', 'Phd']
          }
df = p.DataFrame(records)
print("New DataFrame")
print(df)
