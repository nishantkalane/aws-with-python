"""Snippet 48: Pandas: load a CSV and show the first five rows, column names and data types.

Pattern: pandas / data inspection
Complexity: O(n) to read the file

Needs pandas (pip install -r requirements.txt). Useful methods:
pd.read_csv(), df.head(), df.columns, df.dtypes, df.info().
(*.csv files are in .gitignore, so the demo uses an in-memory CSV.)

Interview answers
1. Logical correctness: Yes | I load the CSV into a DataFrame with
   pd.read_csv(). Then head() shows the first five rows, columns shows the
   column names and dtypes shows each column's data type.
2. Edge cases:
   - Valid CSV file
   - CSV with fewer than five rows
   - CSV with numeric and string columns
   - Empty CSV file (raises EmptyDataError)
   - Missing file (raises FileNotFoundError)
   - CSV containing missing values
3. Production ready: No | The basic inspection is correct, but production
   code should handle missing or malformed files, specify the encoding when
   needed and validate the expected columns.
"""


import pandas as pd


def inspect_csv(filename):
    df = pd.read_csv(filename)

    print("First five rows:")
    print(df.head())

    print("\nColumn names:")
    print(df.columns)

    print("\nData types:")
    print(df.dtypes)


# Demo with an in-memory CSV, so no data.csv file is needed.
# With a real file, call inspect_csv("data.csv").
import io

csv_text = """Name,Age,City
Amit,23,Pune
Rahul,24,Mumbai
Neha,22,Nagpur
"""

inspect_csv(io.StringIO(csv_text))
