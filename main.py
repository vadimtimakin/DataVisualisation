import pandas as pd 

df = pd.read_csv("/tmp/data/test.csv")
length = len(df)
df["age"] = [34 for _ in range(length)]
df.to_csv("/var/log/result.csv", index=False)
