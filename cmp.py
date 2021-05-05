import pandas as pd
df1 = pd.read_csv("survey.processed.csv")
df2 = pd.read_csv("survey.benny.csv")
print(df1.compare(df2))
