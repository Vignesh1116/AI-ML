import pandas as pd

df = pd.DataFrame(
    {
        "Name": ["Vignesh", "Arun", "Kumar"],
        "Marks": [85, 90, 75]
    },
    index=["S1", "S2", "S3"]
)
 
df["Subject"] = ["Maths", "Science", "English"] #  add a new column

print(df)

df["Marks"] = df["Marks"] + 5  # add a value to all the rows in a column

print(df)
