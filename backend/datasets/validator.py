import pandas as pd

df = pd.read_csv("conditions/conditions.csv")

print(f"Total Conditions: {len(df)}")

print(df.head())