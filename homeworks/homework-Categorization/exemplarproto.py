import string as str
import os
import numpy as np
import seaborn as sns
import pandas as pd
import math
from random import random, randint, shuffle, uniform
from scipy.optimize import fmin, brute

################################
# getcurve
################################
def getcurve(filename):
    prototypes = []
    low = []
    old = []
    high = []
    randoms = []
    mydata = readfile(filename)
    cond = mydata[-1][1]
    for line in mydata:
        if line[4] == 2 and len(line) == 9:
            if line[7] == 1:
                prototypes.append(line[5])
            if line[7] == 2:
                old.append(line[5])
            if line[7] == 3:
                high.append(line[5])
            if line[7] == 4:
                low.append(line[5])
            if line[7] == 5:
                randoms.append(line[5])
    return [
        np.average(prototypes),
        np.average(low),
        np.average(high),
        np.average(randoms),
        np.average(old),
        filename,
        cond,
    ]


def readfile(filename):
    results = []
    fp = open(filename, "r")
    for line in fp.readlines():
        myline = list(map(int, line.split(" ")[:-1]))
        results.append(myline[:])
    fp.close()
    return results


def get_all_filenames(directoryname):
    files = filter(
        lambda x: x[-4:] == ".dat" and x[0] != ".",
        os.listdir(os.path.join(".", directoryname)),
    )
    fn = map(lambda x: os.path.join(".", directoryname, x), files)
    # process each file and drop last 5 trials
    return list(fn)


def create_df(subjnum, cond, pattern):
    nobs = len(pattern)
    df = pd.DataFrame(
        {
            "Subject": [subjnum] * nobs,
            "Condition": [cond] * nobs,
            "Stimulus Type": ["Prototype", "Low", "High", "Random", "Old"],
            "Probability of Endorsement": pattern,
        }
    )
    return df


def get_human_results():
    allres = map(getcurve, get_all_filenames("data"))
    cat = []
    rec = []
    for patt in allres:
        if patt[-1] == 0:
            cat.append(create_df(patt[-2], "cat", patt[:-2]))
        else:
            rec.append(create_df(patt[-2], "rec", patt[:-2]))
    cat, rec = pd.concat(cat), pd.concat(rec)
    return pd.concat([cat, rec])


def getcurve_ll(filename):
    prototypes = []
    low = []
    old = []
    high = []
    randoms = []
    mydata = readfile(filename)
    cond = mydata[-1][1]
    for line in mydata:
        if line[4] == 2 and len(line) == 9:
            if line[7] == 1:
                prototypes.append(line[5])
            if line[7] == 2:
                old.append(line[5])
            if line[7] == 3:
                high.append(line[5])
            if line[7] == 4:
                low.append(line[5])
            if line[7] == 5:
                randoms.append(line[5])
    return [
        [sum(prototypes), sum(low), sum(high), sum(randoms), sum(old)],
        [len(prototypes), len(low), len(high), len(randoms), len(old)],
        filename,
        cond,
    ]


def get_human_results_ll():
    allres = list(map(getcurve_ll, get_all_filenames("data")))
    cat = []
    rec = []
    for patt in allres:
        if patt[-1] == 0:
            cat.append(create_df_ll(patt[-2], "cat", patt[0], patt[1]))
        else:
            rec.append(create_df_ll(patt[-2], "rec", patt[0], patt[1]))
    cat, rec = pd.concat(cat), pd.concat(rec)
    return pd.concat([cat, rec])


def create_df_ll(subjnum, cond, ss, ns):
    nobs = len(ss)
    df = pd.DataFrame(
        {
            "Subject": [subjnum] * nobs,
            "Condition": [cond] * nobs,
            "Stimulus Type": ["Prototype", "Low", "High", "Random", "Old"],
            "N_Yes": ss,
            "Total": ns,
        }
    )
    return df


################################
# unitdist:
# computes the euclidean distance between
# two dots
################################
def unitdist(x, y):
    x1 = np.array(x)
    y1 = np.array(y)
    return math.sqrt(sum(pow(x - y, 2.0)))


################################
# computeresponse
# computes the "activation" of each
# trace in memory
################################
def computeresponse(target, memory, c, k):
    res = []
    for mem in memory:
        res.append(
            math.log(
                1.0 + np.average(list(map(lambda x, y: unitdist(x, y), target, mem)))
            )
        )
    # print res
    resp = [math.exp(-c * x) for x in res]
    pofr = sum(resp) / (sum(resp) + k)
    return pofr


################################
# exemplar model
# stores all 10 study items in memory
# and computes the probability of endorsement
# for each item type
################################
def exemplarmodel(filename, c, k):
    data = readfile(filename)
    cond = data[-1][1]
    memory = []
    for line in data:
        if len(line) == 20 and line[1] == 2:
            memory.append(np.resize(line[2:], (9, 2)))
    # print(memory)

    # prototype items
    proto = []
    for line in data:
        if len(line) == 20 and line[1] == 1:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            proto.append(pofr)
    # print(np.average(proto))

    # old items
    old = []
    for line in data:
        if len(line) == 20 and line[1] == 2:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            old.append(pofr)
    # print "p of r", old
    # print(np.average(old))

    # new high items
    newhigh = []
    for line in data:
        if len(line) == 20 and line[1] == 3:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            newhigh.append(pofr)
    # print(np.average(newhigh))

    # new low items
    newlow = []
    for line in data:
        if len(line) == 20 and line[1] == 4:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            newlow.append(pofr)
    # print(np.average(newlow))

    # random items
    random = []
    for line in data:
        if len(line) == 20 and line[1] == 5:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            random.append(pofr)
    # print(np.average(random))

    return [
        np.average(proto),
        np.average(newlow),
        np.average(newhigh),
        np.average(random),
        np.average(old),
        filename,
        cond,
    ]


def get_exemplar_results(c_cat, k_cat, c_rec, k_rec):
    allres = {fn: readfile(fn) for fn in get_all_filenames("data")}
    cat = []
    rec = []
    for filename in allres.keys():
        if allres[filename][-1][1] == 0:
            res = exemplarmodel(filename, c_cat, k_cat)
            cat.append(create_df(filename, "cat", res[:-2]))
        else:
            res = exemplarmodel(filename, c_rec, k_rec)
            rec.append(create_df(filename, "rec", res[:-2]))
    cat, rec = pd.concat(cat), pd.concat(rec)
    return pd.concat([cat, rec])


################################
# prototype model
# stores an averate of the study items in memory
# and computes the probability of endorsement
# for each item type
################################
def prototypemodel(filename, c, k):
    data = readfile(filename)
    cond = data[-1][1]
    # average all the old items in memory
    memory = []
    for line in data:
        if len(line) == 20 and line[1] == 2:
            memory.append(line[2:])
    memory = [np.resize(list(map(np.average, np.transpose(np.array(memory)))), (9, 2))]

    # prototype items
    proto = []
    for line in data:
        if len(line) == 20 and line[1] == 1:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            proto.append(pofr)
    # print(np.average(proto))

    # old items
    old = []
    for line in data:
        if len(line) == 20 and line[1] == 2:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            old.append(pofr)
    # print "p of r", old
    # print(np.average(old))

    # new high items
    newhigh = []
    for line in data:
        if len(line) == 20 and line[1] == 3:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            newhigh.append(pofr)
    # print(np.average(newhigh))

    # new low items
    newlow = []
    for line in data:
        if len(line) == 20 and line[1] == 4:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            newlow.append(pofr)
    # print(np.average(newlow))

    # random items
    random = []
    for line in data:
        if len(line) == 20 and line[1] == 5:
            item = np.resize(line[2:], (9, 2))
            pofr = computeresponse(item, memory, c, k)
            random.append(pofr)
    # print(np.average(random))

    return [
        np.average(proto),
        np.average(newlow),
        np.average(newhigh),
        np.average(random),
        np.average(old),
        filename,
        cond,
    ]


def get_prototype_results(c_cat, k_cat, c_rec, k_rec):
    allres = {fn: readfile(fn) for fn in get_all_filenames("data")}
    cat = []
    rec = []
    for filename in allres.keys():
        if allres[filename][-1][1] == 0:
            res = prototypemodel(filename, c_cat, k_cat)
            cat.append(create_df(filename, "cat", res[:-2]))
        else:
            res = prototypemodel(filename, c_rec, k_rec)
            rec.append(create_df(filename, "rec", res[:-2]))
    cat, rec = pd.concat(cat), pd.concat(rec)
    return pd.concat([cat, rec])
