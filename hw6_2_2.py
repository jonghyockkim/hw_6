import pandas as pd
df = pd.read_csv("complete.csv")
result = df.query("price > 50 and price < 100")
result.to_csv("hw6_2_affordable.csv")
