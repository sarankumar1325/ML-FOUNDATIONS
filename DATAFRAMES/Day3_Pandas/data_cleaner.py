"""
Data Cleaner Tool
----------------
A simple script to clean CSV data using pandas.

Features:
- Remove duplicates
- Handle missing values (drop or fill)
- Save cleaned data to a new file

Instructions:
1. Place your CSV file in this folder.
2. Update the 'input_file' variable below.
3. Run this script.
"""
import pandas as pd

# === USER SETTINGS ===
input_file = 'sample_data.csv'  # Change to your file
output_file = 'cleaned_data.csv'

# === LOAD DATA ===
df = pd.read_csv(input_file)
print('Original Data:')
print(df.head())

# === REMOVE DUPLICATES ===
df = df.drop_duplicates()

# === HANDLE MISSING VALUES ===
# Option 1: Drop rows with any missing values
# df = df.dropna()

# Option 2: Fill missing values (example: fill with 0)
# df = df.fillna(0)

# === SAVE CLEANED DATA ===
df.to_csv(output_file, index=False)
print(f'Cleaned data saved to {output_file}')
