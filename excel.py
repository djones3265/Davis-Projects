import pandas as pd

# Replace 'your_file.xlsx' with the actual filename of your Excel file
filename = 'Book1.xlsx'

# Replace 'sheet_name' with the name of the sheet you want to analyze (optional)
sheet_name = None  # If unspecified, reads the first sheet

# Read the Excel file into a Pandas DataFrame
df = pd.read_excel(filename, sheet_name=sheet_name)

# Get maximum values in each column
max_values = df.max(axis=0)

# Print the maximum values
print("Maximum values in each column:")
print(max_values)