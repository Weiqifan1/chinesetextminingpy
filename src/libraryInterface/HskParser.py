from operator import itemgetter
from src.resources import hskReader
import itertools

def initHskParser():
    if 'hskSimpDictionary' in globals():
        pass
    else:
        hskContent = hskReader.readHskFiles()

        keyList = [x for x in hskContent.keys()]
        allstrings = [getStringSet(hskContent.get(x), x) for x in keyList]
        res = {}
        for x in allstrings:
            res.update(x)
        global hskSimpDictionary
        hskSimpDictionary = res

def initBCLUDictionary():
    if 'bcluDictionary' in globals():
        pass
    else:
        global bcluDictionary
        bcluDictionary = hskReader.doReadDictionaryFromFile("BCLU_Cedict_Intersection")

def getHskSimpDict():
    return hskSimpDictionary

def getBCLUdict():
    return bcluDictionary

def getStringSet(param, hskLevel):
    splitString = set(param.split("，"))
    return {hskLevel : splitString}


def hskListToDict(x):
    dict = {
            "level": int(x[5][-1]),
            "freq" : x[6]}
    return dict

def getHSKSublistsToDict(group):
    nestedList = list(group)
    res = [hskListToDict(x) for x in nestedList]
    return res

def getHskLevel(x):
    simpDict = getHskSimpDict()
    allkeys = simpDict.keys()
    for key in allkeys:
        if x in simpDict.get(key):
            return key
    return ""


def getBCLUfrequency(x):
    bcluDict = getBCLUdict()
    if x in bcluDict:
        #get only the frequency number
        return bcluDict.get(x)[1]
    else:
        return None