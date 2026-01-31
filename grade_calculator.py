import pandas as pd

# Excel file name (exact ga mee file name)
file_name = "Grade_Calculator_Sample.xlsx"

# Read Excel file
df = pd.read_excel(file_name)

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

# Apply grade calculation
df["Grade"] = df["Marks"].apply(calculate_grade)

# Save result back to same Excel file
df.to_excel(file_name, index=False)

print("Student grades calculated successfully!")
