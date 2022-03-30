import pandas as pd
# Define a dictionary containing employee data
data1 = {
        'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']
        }
dataFrameone = pd.DataFrame(data1)
print("Data Set One")
print(dataFrameone)
print("Age and Name datas from the dataset")
print(dataFrameone[ ["Name", "Age"] ])
print("age greater than 30 people are")
print(dataFrameone[ dataFrameone["Age"] >= 30 ])
print("adding an extra row")
extraRow = pd.DataFrame({
    "Name":["new person"], "Age":[22], "Address":["new address"], "Qualification":["new person qualification"]
}, index=[8])
df = pd.DataFrame(pd.concat([dataFrameone, extraRow]).reset_index(drop=True))
print(df)
print("adding one column in the integer position one[1]")
# adding a column

# build column value
status = pd.Series([ 1,2,3,4,5,6,7,8,9])

# add the column using insert of the DataFrame method
dataFrameone.insert(1, "status", status)
print(dataFrameone)
# grouping data using names

namesGroup = dataFrameone.groupby("Name")
print("grouped by names")
print(namesGroup)
# getting the first value from the group
# print(namesGroup.first())
for a,b in namesGroup:
    print(type(a))
    print(a)
    print(type(b))
    print(b)
    print()
# getting each object from the groups

# grouping by name and Age
grp = df.groupby(['Name', 'Qualification'])
print( grp.get_group(('Jai', 'Msc')) )


