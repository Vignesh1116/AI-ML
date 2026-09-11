import pandas as pd

df = pd.DataFrame({
    "Name": ["Vignesh", "Arun", "Kumar"],
    "Marks": [85, 90, 75],
    "Age": [20, 22, 23],
    "City": ["Chennai", "Bangalore", "Delhi"]
})

high = df[df["Marks"] >=80 ] # Filtering the data using Condition

sorted_df = df.sort_values("Marks") # Filtering using the sort

print(high)
print(sorted_df)

