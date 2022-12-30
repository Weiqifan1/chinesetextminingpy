from src.resources import cedictReader
import itertools

def initCedictParser(cedictContent):
    filelines = cedictContent.split('\n')
    withoutComments = removeCommentLinesFromCedict(filelines)
    resultObj = map(lineToList, withoutComments)
    res = list(resultObj)
    global traditionalDictionary
    traditionalDictionary = createCedictTradToInfoDict(res)
    global simplifiedDictionary
    simplifiedDictionary = createCedictSimpToInfoDict(res)

def getCedictTradDict():
    return traditionalDictionary

def getCedictSimpDict():
    return simplifiedDictionary

def readCedictContentFromCedictReader():
    return cedictReader.readCedictFile()

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
    tradDictList = [{key : list(group)} for key,group in tradIter]
    tradSuperDict = {}
    for d in tradDictList:
        tradSuperDict.update(d)

    simpIter = itertools.groupby(sortBySEcond, lambda x: x[1])
    simpDictList = [{key : list(group)} for key,group in simpIter]
    simpSuperDict = {}
    for d in simpDictList:
        simpSuperDict.update(d)
    return [tradSuperDict, simpSuperDict]

def createCedictTradToInfoDict(res):
    sortByFirst = sorted(res)
    tradIter = itertools.groupby(sortByFirst, lambda x: x[0])
    tradDictList = [{key: list(group)} for key, group in tradIter]
    tradSuperDict = {}
    for d in tradDictList:
        tradSuperDict.update(d)
    return tradSuperDict

def createCedictSimpToInfoDict(res):
    sortBySEcond = sorted(res, key=lambda x: x[1])
    simpIter = itertools.groupby(sortBySEcond, lambda x: x[1])
    simpDictList = [{key : list(group)} for key,group in simpIter]
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
    return "_".join(capitalize)

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



