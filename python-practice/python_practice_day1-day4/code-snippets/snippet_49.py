"""Snippet 49: Pandas: count missing values per column and remove duplicate rows.

Pattern: pandas / data cleaning
Complexity: Data-dependent (drop_duplicates is roughly O(n))

isnull().sum() counts missing values; drop_duplicates() removes duplicate
rows; dropna() removes rows or columns with missing values; fillna() replaces
them.

Interview answers
1. Logical correctness: Yes | I use isnull().sum() to count missing values
   for each column. Then drop_duplicates() removes duplicate rows and I
   return the cleaned DataFrame.
2. Edge cases:
   - DataFrame with duplicate rows
   - DataFrame without duplicates
   - DataFrame with missing values
   - DataFrame where all rows are duplicates
   - Empty DataFrame
   - Missing values but no duplicate rows
3. Production ready: Yes, for basic duplicate removal | The operations are
   correct and Pandas handles them efficiently. I'd still clarify whether
   duplicates should be judged on all columns or selected ones, and whether
   missing values should be removed or imputed.
"""


import pandas as pd


def clean_dataframe(df):
    print("Missing values:")
    print(df.isnull().sum())

    df = df.drop_duplicates()

    return df


data = {
    "Name": ["Amit", "Rahul", "Amit", "Neha"],
    "Age": [23, 24, 23, None],
    "City": ["Pune", "Mumbai", "Pune", "Nagpur"]
}

df = pd.DataFrame(data)

cleaned_df = clean_dataframe(df)

print("\nCleaned DataFrame:")
print(cleaned_df)
