import pandas as pd

# Day 3: Pandas for Data Manipulation
# Practice Notebook

# 1. DataFrames and Series
print('--- Series Example ---')
series = pd.Series([10, 20, 30], name='SampleSeries')
print(series)

print('\n--- DataFrame Example ---')
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})
print(df)

# 2. Reading and Writing Data
print('\n--- Reading CSV ---')
sample_df = pd.read_csv('sample_data.csv')
print(sample_df)

print('\n--- Writing CSV ---')
sample_df.to_csv('output_sample.csv', index=False)
print('Data written to output_sample.csv')

# 3. Filtering and Grouping
print('\n--- Filtering: Age > 25 ---')
filtered = sample_df[sample_df['Age'] > 25]
print(filtered)

print('\n--- Grouping: Mean Salary by City ---')
grouped = sample_df.groupby('City')['Salary'].mean()
print(grouped)
