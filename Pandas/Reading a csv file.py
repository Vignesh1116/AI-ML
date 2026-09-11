import pandas as pd

df = pd.read_csv("students.csv")

print(df)

df.to_csv("cleaned_students.csv", index=False) # Saving the csv file 