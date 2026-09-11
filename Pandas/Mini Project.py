import pandas as pd

# Load the dataset
df = pd.read_csv("Student_data.csv")

print(df)
# Understand the Dataset

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

# First 3 students

print(df.head(3))

# Statistics

print(df.describe())

# Calculate average

df["Average"] = (
    df["Python"] +
    df["AI"] +
    df["ML"]
) / 3

print(df)

# Find high performers

high_performers = df[df["Average"] >= 80]

print(high_performers)

# Pass/Fail

df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

# Sort students

df = df.sort_values(
    "Average",
    ascending=False
)

print(df)

# Save Result

df.to_csv(
    "student_analysis.csv",
    index=False
)
