import pandas as pd

data = {
    "Name":["Vignesh","Santhosh","Kumar"],
    "Age":[23,22,21],
    "marks":[80,90,80]
}

df = pd.DataFrame(data)

print(df)

print(df.head(2)) # First 5 rows(default) , we can specify the number

print(df.tail(2)) # Last rows(default) , we can specify the number

print(df.shape) # rows, columns

print(df.columns) # columns

print(df.dtypes) # data types

print(df.info()) # structure of the dataset

print(df.describe()) # statistical summary