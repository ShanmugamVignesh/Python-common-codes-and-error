import pandas as pd

# Load the Excel file
file_path = 'data generate/random_data.xlsx'  # Replace with your file path
df = pd.read_excel(file_path)

# Display the first few rows of the dataframe
print(df.head())
