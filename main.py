# How to drop all Rows in a Pandas DataFrame in Python

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl'],
    'salary': [175.1, 180.2, 190.3],
})

print(df)

print('-' * 50)

df.drop(df.index, inplace=True)

print(df)