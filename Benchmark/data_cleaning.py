import csv, pandas as pd
df = pd.read_csv("Testing Data - Sheet1.csv")
print(df.head())

duplicate_values = list()
values = set()

for i in df["StackOverFlowID"]:
    if i in values: duplicate_values.append(i)
    else: values.add(i)
print(duplicate_values)
