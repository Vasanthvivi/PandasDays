# importing pandas module
import pandas as pd

# Define a dictionary containing employee data 
ddata1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
          'Age': [27, 24, 22, 32],
          'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
          'Qualification': ['Msc', 'MA', 'MCA', 'Phd'],
          'Mobile No': [97, 91, 58, 76]}

# Define a dictionary containing employee data 
ddata2 = {'Name': ['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'],
          'Age': [22, 32, 12, 52],
          'Address': ['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'],
          'Qualification': ['MCA', 'Phd', 'Bcom', 'B.hons'],
          'Salary': [1000, 2000, 3000, 4000]}

data1 = {
    "Name": ["jai", "princi", "gaurav"],
    "Age": [1, 2, 3]
}

data2 = {
    "Name": ["princi", "vivi", "com"],
    "Age": [2, 1, 3]
}

# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)

# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2)

# print(df, "\n\n", df1)

res2 = pd.concat([df, df1], axis=1, join='inner')

# print(res2)


dfone = pd.DataFrame([['a', 1], ['b', 2]], columns=["letter", "number"])
print(dfone)

dftwo = pd.DataFrame([['b', 2], ['c', 3]], columns=['letter', "number"])
print(dftwo)
# concatenating
res = pd.concat([dfone, dftwo], ignore_index=True)
print(res)

dfthree = pd.DataFrame([['c', 3, "cat"]], columns=["letter", "number", "animal"])
print(dfthree)

res = pd.concat([dfone, dfthree], join="inner", axis=0, ignore_index=True)
print(res)


# adding a series using cocat
dataone = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

dataoneTable = pd.DataFrame(dataone)
salaryData = pd.Series([ 1000, 2000, 3000, 6000 ], name="Salary")

res = pd.concat( [dataoneTable, salaryData], axis=1 )
print(res)

