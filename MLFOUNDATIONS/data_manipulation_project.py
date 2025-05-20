"""
Complete Data Manipulation Script Project
This script demonstrates data loading, cleaning, transformation, aggregation, and export using pandas.
"""
import pandas as pd
import numpy as np

# 1. Data Loading
# For demonstration, we'll create a DataFrame. Replace this with pd.read_csv('yourfile.csv') for real data.
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi'],
    'Age': [25, 30, np.nan, 35, 28, 40, 22, 29],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F'],
    'Score': [85, 90, 78, 88, np.nan, 95, 80, 70],
    'City': ['NY', 'LA', 'NY', 'SF', 'LA', 'SF', 'NY', 'LA']
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# 2. Data Cleaning
# Fill missing Age with mean, Score with median
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Score'].fillna(df['Score'].median(), inplace=True)
print("\nAfter filling missing values:\n", df)

# 3. Data Transformation
# Add a new column: Pass/Fail based on Score
df['Result'] = np.where(df['Score'] >= 80, 'Pass', 'Fail')

# Convert 'Gender' to full form
df['Gender'] = df['Gender'].map({'F': 'Female', 'M': 'Male'})

# 4. Data Aggregation
# Group by City and calculate average Score and Age
city_stats = df.groupby('City').agg({'Score': 'mean', 'Age': 'mean', 'Name': 'count'}).rename(columns={'Name': 'Count'})
print("\nCity-wise statistics:\n", city_stats)

# 5. Sorting and Filtering
# Get top 3 scorers
top_scorers = df.sort_values(by='Score', ascending=False).head(3)
print("\nTop 3 scorers:\n", top_scorers[['Name', 'Score']])

# Filter: All females who passed
females_passed = df[(df['Gender'] == 'Female') & (df['Result'] == 'Pass')]
print("\nFemales who passed:\n", females_passed[['Name', 'Score']])

# 6. Export Results
df.to_csv('cleaned_data.csv', index=False)
city_stats.to_csv('city_stats.csv')
print("\nData exported to 'cleaned_data.csv' and 'city_stats.csv'.")
