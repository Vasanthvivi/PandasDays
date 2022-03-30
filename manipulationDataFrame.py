# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Define a dictionary containing employee data
data2 = {'Name': ['Abhi', 'Jai', 'Dhiraj', 'Hitesh'],
         'Age': [17, 27, 12, 52],
         'Address': ['Nagpur', 'Nagpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'Msc', 'Bcom', 'B.hons']}


# Convert the dictionary into DataFrame
df = pd.DataFrame(data1, index=[0, 1, 2, 3])

# Convert the dictionary into DataFrame
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])

# DataFrames we got
print("Data Frame one")
print(df)
print("Data Frame two")
print(df1)


# concatenating data Frames

dataFrame = [df, df1]
# print(pd.concat(dataFrame))

# inner join of dataFrames
print("Inner join of Data Frame")
print(pd.concat(dataFrame, axis=1, sort=False, join="inner"))

