from matplotlib import pyplot as plt
import pandas as pd
from collections import defaultdict

def catg(lst):
    dct = defaultdict(int)
    for c in lst:
        dct[c]+=1
    l = []
    for k in dct.keys():
        l.append((dct[k],k))
    l.sort()
    l.reverse()
    lc = [k[1] for k in l]
    ld = [k[0] for k in l]
    return ld,lc

df = pd.read_csv("survey.processed.csv")
clm = "brand"
ccnt,ccrand = catg(df[clm])

fig, ax = plt.subplots(figsize=(6,6))
ax.pie(ccnt, labels = ccrand,autopct='%.0f%%')
ax.set_title(clm)
ax.legend(loc='best')
plt.show()
