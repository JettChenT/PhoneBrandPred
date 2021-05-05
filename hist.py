from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
# from collections import defaultdict

# def catg(lst):
#     dct = defaultdict(int)
#     for c in lst:
#         dct[c]+=1
#     l = []
#     for k in dct.keys():
#         l.append((dct[k],k))
#     l.sort()
#     l.reverse()
#     lc = [k[1] for k in l]
#     ld = [k[0] for k in l]
#     return ld,lc

df = pd.read_csv("survey.processed.csv")
clm = "st"
# ccnt,cct = catg(df[clm])
# plt.bar(cct,ccnt)
plt.hist(df[clm]-1)
plt.title("Phone time usage")
plt.xlabel("Time (in hours)")
plt.ylabel("Number of people")
plt.xticks(np.arange(10))
plt.show()