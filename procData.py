import pandas as pd
import numpy as np
from util import *

def proc_eng():
    EngData = pd.read_csv("surveyEng.csv")
    rList = []
    for obj in ['ID', 'Start time', 'Completion time', 'Email', 'Name',
           'What is your mobile phone brand?',
           'What is the name of your mobile phone model?',
           'Please enter the price of your phone(in USD)',
           'How satisfied are you about your phone?',
           'If you could have a phone of any brand you want, which brand would it be?',
           'What is the name of the your preferred phone model?',
           'What is the price of your preferred phone model?',
           'What factors are important to you whilst purchasing your phone?',
           'The amount of time you spend on your cell phone each day is approximately:'
    ]:
        if obj in Colm_eng.keys():
            rList.append(Colm_eng[obj])
        else:
            rList.append(obj)

    EngData.columns = rList
    EngData["brand"] = [psn(b) for b in EngData["brand"]]
    EngData["prefBrand"] = [psn(b) for b in EngData["prefBrand"]]

    fctrs = np.zeros((len(EngData),len(reasons)),dtype=np.int32)
    for i in range(len(EngData['factor'])):
        rsns = get_rs(EngData["factor"][i])
        fctrs[i] = rsns

    for i in range(len(reasons)):
        EngData[f"Res{ResCode[i]}"] = fctrs[:,i]

    for c in ["ID","Start time","Completion time","Email","Name","factor"]:
        EngData.drop(c,inplace=True,axis=1)

    EngData["sat"] = [satMap[s] for s in EngData["sat"]]
    EngData["st"] = [int(t[-7]) for t in EngData["st"]]
    return EngData

def proc_cn():
    data = pd.read_csv("surveyCN.csv")
    for c in ["序号", "提交答卷时间", "所用时间", "来源", "来源详情", "来自IP","8、(性能（CPU）)"]:
        if c in data.columns:
            data.drop(c, inplace=True, axis=1)
    data.columns = [Questions_cn[c] for c in data.columns]
    data = data.astype({'sat': 'int64'})
    data["brand"] = [cn_get_br(n) for n in data["brand"]]
    data.fillna(0,inplace=True)
    data["prefBrand"] = [cn_get_br(n) for n in data["prefBrand"]]
    data.drop("factor",inplace=True,axis=1)
    return data

EData = proc_eng()
CData = proc_cn()
TotalData = pd.concat([EData,CData],axis=0)
TotalData.to_csv("survey.processed.csv")
