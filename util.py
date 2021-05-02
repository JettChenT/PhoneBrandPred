from config import *

def similar(a, b):
    accu = 0
    a = a.replace("("," ")
    a = a.replace(")"," ")
    b = b.replace("("," ")
    b = b.replace(")"," ")
    al = a.lower().split()
    bl = b.lower().split()
    for wa in al:
        for wb in bl:
            accu += wa==wb
    return accu


def getsim(brand):
    maxi = -1
    maxs = -1
    for i in range(len(Brands)):
        s = similar(brand,Brands[i])
        if s>maxs:
            maxs = s
            maxi = i
    if maxs<0.3:
        return -1
    return maxi

def psn(brand):
    n = getsim(brand)
    if n==-1:
        return "other"
    return Brands[n]

def get_br(brand):
    for i in range(len(Brands_cn)):
        if Brands_cn[i]==brand:
            return Brands[i]
    return "other"

def get_rs(rstr):
    res = [0]*len(reasons)
    rsns = rstr[:-1].split(";")
    for i in range(len(reasons)-1):
        if reasons[i] in rsns:
            res[i] = 1
    for r in rsns:
        if r not in reasons:
            res[-1]=1
    return res

def cn_get_br(n):
    if n==0:
        return "other"
    return Brands[int(n)-1]
