"""Snippet 50: Pandas: group a DataFrame by city and find the average purchase amount per city.

Pattern: pandas / groupby aggregation
Complexity: Data-dependent (roughly O(n))

Related methods: groupby(), mean(), sum(), count() (non-missing), agg()
(several aggregations at once).

Interview answers
1. Logical correctness: Yes | I group the DataFrame by the City column and
   select Purchase_Amount. Then I apply mean() to get the average purchase
   amount for each city.
2. Edge cases:
   - Multiple purchases from the same city
   - Only one purchase per city
   - Empty DataFrame
   - Missing city values (those rows are dropped by groupby)
   - Missing purchase amounts (skipped by mean)
   - Non-numeric purchase amounts
3. Production ready: Yes, for valid DataFrame inputs | groupby() and mean()
   are an efficient aggregation. I'd validate the column names and numeric
   data types, and decide how missing city and purchase values should be
   handled.
"""


import pandas as pd


def average_purchase_by_city(df):
    result = df.groupby("City")["Purchase_Amount"].mean()

    return result


data = {
    "City": ["Pune", "Mumbai", "Pune", "Mumbai", "Nagpur"],
    "Purchase_Amount": [1000, 2000, 3000, 4000, 1500]
}

df = pd.DataFrame(data)

print(average_purchase_by_city(df))
# City
# Mumbai    3000.0
# Nagpur    1500.0
# Pune      2000.0
