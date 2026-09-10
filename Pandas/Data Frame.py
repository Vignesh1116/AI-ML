import pandas as pd

data = {
    "Name":["Vignesh","Santhosh","Kumar"],
    "Age":[23,22,21],
    "marks":[80,90,80]
}

df = pd.DataFrame(data)

print(df)

print(df.head(2)) # First 5 rows(default) , we can specify the number