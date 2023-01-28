from src.resources import hskReader

def initBLCUDictionary():
    if 'blcuDictionary' in globals():
        pass
    else:
        global blcuDictionary
        blcuDictionary = hskReader.doReadDictionaryFromFile("BLCU_Cedict_Intersection")

def getBLCUdict():
    return blcuDictionary

def getBLCUfrequency(x):
    blcuDict = getBLCUdict()
    if x in blcuDict:
        #get only the frequency number
        return blcuDict.get(x)[1]
    else:
        return None
