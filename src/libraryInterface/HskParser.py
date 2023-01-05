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

def init_bcluDictionary():
    if 'bcluDictionary' in globals():
        pass
    else:
        readfile = hskReader.doReadDictionaryFromFile("BCLU_Cedict_Intersection")
        return readfile

def getHskSimpDict():
    return hskSimpDictionary

def getHskTradDict():
    return hskTradDictionary

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

def createHskNestedList(hskContent):


    return hskContent


