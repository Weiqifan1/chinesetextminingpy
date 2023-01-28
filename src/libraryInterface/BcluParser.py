from src.resources import hskReader

def initBCLUDictionary():
    if 'bcluDictionary' in globals():
        pass
    else:
        global bcluDictionary
        bcluDictionary = hskReader.doReadDictionaryFromFile("BCLU_Cedict_Intersection")

def getBCLUdict():
    return bcluDictionary

def getBCLUfrequency(x):
    bcluDict = getBCLUdict()
    if x in bcluDict:
        #get only the frequency number
        return bcluDict.get(x)[1]
    else:
        return None
