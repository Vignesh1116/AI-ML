import pandas as pd

df = pd.DataFrame({
    "Name":["Vignesh","Santhosh","Kumar"],
    "Age":[20,22,23],
    "marks":[70,80,90]
},index=["1","2","3"])

print(df["Name"])   # Selecting one column

print(df[["Name","marks"]]) # select multiple column

print(df.iloc[0]) # Selecting one row using index position

print(df.iloc[[0,1]]) # Selecting multiple rows using index position

print(df.loc["1"]) # Selecting one row using index label

print(df.loc[["1","2"]]) # Selecting multiple rows using index label

