""" 
Creating a Series by passing a list of values, letting pandas create a default integer index
"""

import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

""" Creating a DataFrame by passing a NumPy array """

dates = pd.date_range("20130101", periods=9)

# print((dates))
""" 
df = pd.DataFrame(np.random.randn(9, 4), index=dates, columns=list("ABCD"))
print(df)
"""
""" Creating a DataFrame by passing a dictionary of objects that can be converted into a series-like structure """


df2 = pd.DataFrame(
    {
        "A": pd.date_range("20130101", periods=9),
        "B": np.arange(9),
        "C": np.array([1.1] * 9, dtype="float64"),
        "D": np.array([3] * 9, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train","test", "train", "test", "train","Talismar"]),
    }, 
)

print(df2.dtypes)
name_cat = df2["E"].astype("category")
print(name_cat)