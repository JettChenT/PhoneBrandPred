import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

price = pd.read_csv("price.prefmod.csv")
price = price.fillna(0)
df = pd.read_csv("survey.procmod.csv")

models = price["Model"]


def getMod(s):
    cmp = np.array([fuzz.ratio(s.lower(), s2.lower()) for s2 in models])
    res = models[np.argmax(cmp)]
    price.loc[price["Model"]==res,'Count']+=1
    return res


df["prefMod"] = [getMod(s) for s in df["prefMod"]]
df.to_csv("survey.procmod.csv",index=False)
price.to_csv("price.prefmod.csv",index=False)