import pandas as pd

df = pd.DataFrame({
    "Name": ["Vignesh", "Arun", "Kumar"],
    "Marks": [85, 90, 75],
    "Age": [20, 22, 23],
    "City": ["Chennai", "Bangalore", "Delhi"]
})

df.loc["3"] = ["Santhosh", 88, 24, "Coimbatore"] # Adding a new row

df = df.drop("Age", axis=1) # Deleting a column

df = df.drop(2)

print(df.isnull()) # Checking for null values

df = df.dropna() # Deleting rows with null values

print(df)