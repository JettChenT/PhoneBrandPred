from matplotlib import pyplot as plt
import pandas as pd
from collections import defaultdict

def catg(lst):
    dct = defaultdict(int)
    for c in lst:
        dct[c]+=1
    ld,lc = [],[]
    for k in dct.keys():
        lc.append(k)
        ld.append(dct[k])
    return ld,lc

df = pd.read_csv("survey.processed.csv")
clm = "brand"
ccnt,ccrand = catg(df[clm])
# if "other" in ccrand:
#     n = ccrand.index("other")
#     ccnt.pop(n)
#     ccrand.pop(n)

fig, ax = plt.subplots(figsize=(6,6))
ax.pie(ccnt, labels = ccrand,autopct='%.0f%%')
ax.set_title(clm)
ax.legend(loc='best')
plt.show()
