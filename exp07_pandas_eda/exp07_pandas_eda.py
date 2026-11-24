# Data Cleaning and Exploratory Data Analysis using Pandas
import pandas as pd
data = {
    "Name": ["Riya", "Arun", "Meera"],
    "Department": ["CSE", "ECE", "CSE"],
    "Attendance": [92, None, 88],
    "Mark": [86, 78, None]
}
df = pd.DataFrame(data)

print("--- Original Dataset ---")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())
# Missing value treatment
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())
# Remove duplicate records
df = df.drop_duplicates()
print("\n--- Cleaned Dataset ---")
print(df)
print("\n--- Descriptive Statistics ---")
print(df.describe())
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
