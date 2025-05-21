# Day 3: Pandas for Data Manipulation

Welcome to Day 3! Today you'll learn how to use Pandas for powerful data manipulation tasks. This includes mastering DataFrames and Series, reading/writing data, filtering, grouping, and building a Data Cleaner Tool.

## Contents
- [Day 3: Pandas for Data Manipulation](#day-3-pandas-for-data-manipulation)
  - [Contents](#contents)
    - [1. DataFrames and Series](#1-dataframes-and-series)
      - [Example:](#example)
    - [2. Reading and Writing Data](#2-reading-and-writing-data)
      - [Example:](#example-1)
    - [3. Filtering and Grouping](#3-filtering-and-grouping)
      - [Example:](#example-2)
    - [4. Data Cleaner Tool Project](#4-data-cleaner-tool-project)

---

### 1. DataFrames and Series
- **Series**: 1D labeled array (like a column)
- **DataFrame**: 2D labeled data structure (like a table)

#### Example:
```python
import pandas as pd
# Series
s = pd.Series([1, 2, 3], name='Numbers')
print(s)
# DataFrame
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
```

---

### 2. Reading and Writing Data
- Read CSV: `pd.read_csv('file.csv')`
- Write CSV: `df.to_csv('file.csv', index=False)`

#### Example:
```python
df = pd.read_csv('sample_data.csv')
df.to_csv('output.csv', index=False)
```

---

### 3. Filtering and Grouping
- **Filtering**: `df[df['col'] > value]`
- **Grouping**: `df.groupby('col').mean()`

#### Example:
```python
# Filtering
filtered = df[df['Age'] > 25]
# Grouping
grouped = df.groupby('City')['Salary'].mean()
```

---

### 4. Data Cleaner Tool Project
- See `data_cleaner.py` for starter code and instructions.

---

Happy Learning!
