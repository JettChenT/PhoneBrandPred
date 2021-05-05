from matplotlib import pyplot as plt
import pandas as pd
from collections import defaultdict

facters = ["ResMem","ResPric","ResStorage","ResOS","ResPub","ResScrRes","ResRefRate","ResScrSize","ResBattery"]
factnames = ["Memory","Pricing","Storage","OS","Publicity","Screen Resolution","Refresh Rate","Screen Size","Battery"]

df = pd.read_csv("survey.processed.csv")
fh = [df[facter].sum() for facter in facters]

plt.bar(factnames,fh)
plt.title("Important factors while purchasing mobile phone")
plt.xlabel("Factor")
plt.ylabel("Count")
plt.show()
