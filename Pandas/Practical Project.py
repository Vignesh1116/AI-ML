import pandas as pd

# 1. Load dataset
df = pd.read_csv("Student_data.csv")

# 2. Basic information
print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

# 3. Missing values
print("\nMissing values:")
print(df.isnull().sum())

# 4. Fill missing values for numeric columns
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Python"] = df["Python"].fillna(df["Python"].mean())
df["AI"] = df["AI"].fillna(df["AI"].mean())
df["ML"] = df["ML"].fillna(df["ML"].mean())

# 5. Remove duplicates
df = df.drop_duplicates()

# 6. Clean text column
df["Name"] = df["Name"].str.strip()

# 7. Create average mark
df["Average"] = (df["Python"] + df["AI"] + df["ML"]) / 3

# 8. Create result column
df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

# 9. Sort students by Average mark
df = df.sort_values("Average", ascending=False)

# 10. Display top 3 students
print("\nTop 3 Students:")
print(df.head(3))

# 11. Subject analysis
print("\nAverage Subject Marks:")
print(df[["Python", "AI", "ML"]].mean())

# 12. Save cleaned dataset
df.to_csv("cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully!")