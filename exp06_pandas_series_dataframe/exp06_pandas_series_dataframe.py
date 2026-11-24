# Pandas Series and DataFrame
import pandas as pd
marks = pd.Series([85, 91], index=["A", "B"])
print("--- Pandas Series ---")
print(marks)
data = {
    "RollNo": [201, 202],
    "Name": ["Riya", "Arun"],
    "Department": ["CSE", "ECE"],
    "Mark": [85, 91]
}
df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)
print("\nAverage Mark:", round(df["Mark"].mean(), 2))
print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
