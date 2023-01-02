from operator import itemgetter
from src.resources import cedictReader
import itertools

def initCedictParser():
    if 'traditionalDictionary' in globals() and 'simplifiedDictionary' in globals():
        pass
    else:
        filelines = readCedictContentFromCedictReader().split('\n')
        withoutComments = removeCommentLinesFromCedict(filelines)
        resultObj = map(lineToList, withoutComments)
        res = list(resultObj)
        global traditionalDictionary
        traditionalDictionary = createCedictTradToInfoDict(res)
        global simplifiedDictionary
        simplifiedDictionary = createCedictSimpToInfoDict(res)
        global simplifyCedictPinyinWordList
        simplifyCedictPinyinWordList = {'的' : "De5"}

def getCedictTradDict():
    return traditionalDictionary

def getCedictSimpDict():
    return simplifiedDictionary

def wordToTraditionalSimp(word):
    simp = getCedictSimpDict()
    lookup = simp.get(word)
    res = doGetDctionaryContent(lookup, word, "traditional")
    return res

def wordToSimplifiedTrad(word):
    trad = getCedictTradDict()
    lookup = trad.get(word)
    res = doGetDctionaryContent(lookup, word, "simplified")
    return res

def wordToMeaningSimp(word):
    simp = getCedictSimpDict()
    lookup = simp.get(word)
    res = doGetDctionaryContent(lookup, word, "meaning")
    return res

def wordToMeaningTrad(word):
    trad = getCedictTradDict()
    lookup = trad.get(word)
    res = doGetDctionaryContent(lookup, word, "meaning")
    return res

def wordToPinyinSimp(word):
    simp = getCedictSimpDict()
    lookup = simp.get(word)
    changePinyin = simplifyCedictPinyinWordList.get(word)
    if changePinyin:
        res = changePinyin
    else:
        res = doGetDctionaryContent(lookup, word, "pinyin")
    return res

def wordToPinyinTrad(word):
    trad = getCedictTradDict()
    lookup = trad.get(word)
    changePinyin = simplifyCedictPinyinWordList.get(word)
    if changePinyin:
        res = changePinyin
    else:
        res = doGetDctionaryContent(lookup, word, "pinyin")
    return res

def doGetDctionaryContent(lookup, word, key):
    if lookup == None and word == None:
        return ""
    elif lookup == None:
        return word
    else:
        if word == '据' and key == "meaning":
            test = ""
        newLookup = sortListOfWordLookup(lookup)
        lookupList = [x.get(key) for x in newLookup]
        lookupSet = set(lookupList)
        if len(lookupSet) == 1:
            return lookupList[0]
        else:
            return "|".join(lookupList)

def sortListOfWordLookup(lookup):
    for x in range(len(lookup)):
        lookup[x]["length"] = len(lookup[x]["meaning"])
        lookup[x]["deprioritzeCariants"] = getVariantPrioritynumber(lookup[x]["meaning"])
    meaningLength = sorted(lookup, key=itemgetter('deprioritzeCariants', 'length'))
    return meaningLength

def getVariantPrioritynumber(param):
    if param.startswith("/old variant of"):
        return 4
    elif param.startswith("/variant of"):
        return 3
    elif param.startswith("/unofficial variant of"):
        return 2
    else:
        return 1
# /unofficial variant of 瞭[liao4]/|/(of eyes) bright/clear-sighted/to understand clearly/|/to finish/to achieve/variant of 瞭|了[liao3]/to understand clearly/|/(completed action marker)/(modal particle indicating change of state, situation now)/(modal particle intensifying preceding clause)/
def getMeaningLength(eachEntry):
    meaningString = eachEntry["meaning"]
    return len(meaningString)

def readCedictContentFromCedictReader():
    return cedictReader.readCedictFile()

def cedictListToDict(x):
    dict = {
            "traditional": x[0],
            "simplified": x[1],
            "pinyin": x[2],
            "meaning": x[3]}
    return dict

def getCedictSublistsToDict(group):
    nestedList = list(group)
    res = [cedictListToDict(x) for x in nestedList]
    return res

def cedictDictionariesFromRawFileContent(rawDictionaryContent):
    filelines = rawDictionaryContent.split('\n')
    withoutComments = removeCommentLinesFromCedict(filelines)
    resultObj = map(lineToList, withoutComments)
    res = list(resultObj)

    listOfTrad = [x[0] for x in res]
    tradset = set(listOfTrad)
    listOfSimp = [x[1] for x in res]
    simpset = set(listOfSimp)

    sortByFirst = sorted(res)
    sortBySEcond = sorted(res, key = lambda x: x[1])

    tradIter = itertools.groupby(sortByFirst, lambda x: x[0])
    tradDictList = [{key : getCedictSublistsToDict(group)} for key,group in tradIter]
    tradSuperDict = {}
    for d in tradDictList:
        tradSuperDict.update(d)

    simpIter = itertools.groupby(sortBySEcond, lambda x: x[1])
    simpDictList = [{key : getCedictSublistsToDict(group)} for key,group in simpIter]
    simpSuperDict = {}
    for d in simpDictList:
        simpSuperDict.update(d)
    return {"traditionalDict": tradSuperDict,
            "simplifiedDict": simpSuperDict}

def createCedictTradToInfoDict(res):
    sortByFirst = sorted(res)
    tradIter = itertools.groupby(sortByFirst, lambda x: x[0])
    tradDictList = [{key: getCedictSublistsToDict(group)} for key, group in tradIter]
    tradSuperDict = {}
    for d in tradDictList:
        tradSuperDict.update(d)
    return tradSuperDict

def createCedictSimpToInfoDict(res):
    sortBySEcond = sorted(res, key=lambda x: x[1])
    simpIter = itertools.groupby(sortBySEcond, lambda x: x[1])
    simpDictList = [{key : getCedictSublistsToDict(group)} for key,group in simpIter]
    simpSuperDict = {}
    for d in simpDictList:
        simpSuperDict.update(d)
    return simpSuperDict

def removeCommentLinesFromCedict(filelines):
    noComments = [x for x in filelines if not (x.startswith("# ") or x.startswith("#!"))]
    return noComments

def isCommentLine(cedictLine):
    if cedictLine[:2] == "# ":
        True
    elif cedictLine[:2] == "#!":
        True
    else:
        False


def createDisplayPinyinString(rawPinyin):
    pinyinList = rawPinyin.split()
    capitalize = [(x[0].upper() + x[1:]) for x in pinyinList]
    return "".join(capitalize)

def lineToList(stringLine):
    firstSplit = stringLine.split(" ", 1)
    secondSplit = firstSplit[1].split("[", 1)
    thirdSplit = secondSplit[1].split("]", 1)
    traditional = firstSplit[0]
    simplified = secondSplit[0].strip()
    rawPinyin = thirdSplit[0]
    meaning = thirdSplit[1].strip()
    betterPinyin = createDisplayPinyinString(rawPinyin)
    return [traditional,
            simplified,
            betterPinyin,
            meaning]



