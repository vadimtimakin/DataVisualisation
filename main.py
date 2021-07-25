import pandas as pd 

df = pd.DataFrame()
length = 100
df["age"] = [34 for _ in range(length)]
df.to_csv("/var/log/result.csv", index=False)
