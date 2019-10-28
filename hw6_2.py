import pandas as pd
df = pd.read_csv("complete.csv")
result = df.query("price > 100 and price < 150")
result.to_csv("hw6_2.csv")
