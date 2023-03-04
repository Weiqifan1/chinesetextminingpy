from src.Services import utilityService
from src.libraryInterface import ChineseLibParser
from src.libraryInterface import CedictParser
from src.libraryInterface import HeisigParser
from src.libraryInterface import HskParser
from src.libraryInterface import BlcuParser
import re

def sentenceToDict(sen):
    return sen

def textToTokensFromSimplified(text, texttype):
    ChineseLibParser.initChineseLibParser()
    CedictParser.initCedictParser()
    HeisigParser.initHeisigParser()
    HskParser.initHskParser()
    BlcuParser.initBLCUDictionary()
    print("doneLoading")
    sentences = []
    sentn = []
    if texttype == "rawText":
        betterData = re.sub("\s+", " ", text.strip())
        sentences = ChineseLibParser.getSentencesFromLargeText(betterData)
        sentn = ["" for x in sentences]
    elif texttype == "ordered2Line":
        (sentences, sentnames) = ChineseLibParser.sentencesFromOrdered2Line(text)
        sentn = sentnames
    result = [senToDictFromSimplified(x) for x in sentences]
    return (result, sentn)

def textToTokensFromTraditional(text, texttype):
    ChineseLibParser.initChineseLibParser()
    CedictParser.initCedictParser()
    HeisigParser.initHeisigParser()
    HskParser.initHskParser()
    BlcuParser.initBLCUDictionary()
    print("doneLoading")
    sentences = []
    sentn = []
    if texttype == "rawText":
        betterData = re.sub("\s+", " ", text.strip())
        sentences = ChineseLibParser.getSentencesFromLargeText(betterData)
        sentn = ["" for x in sentences]
    elif texttype == "ordered2Line":
        (sentences, sentnames) = ChineseLibParser.sentencesFromOrdered2Line(text)
        sentn = sentnames
    result = [senToDictFromTraditional(x) for x in sentences]
    return (result, sentn)

def vocabFromSentencesRaw(allItems):
    singleList = sum(allItems, [])
    onlyChinese = [x for x in singleList if utilityService.isChinese(x)]
    chineseSet = sorted(set(onlyChinese), key=lambda x: onlyChinese.index(x))
    vocabText = ""
    vocabText = vocabText + '\n'.join(chineseSet)
    return vocabText

def getFirstWordFromConversion(param):
    #if a word can be converted to multiple words of the other system, then pick only the first word
    splitByHorizontal = param.split("|")
    return splitByHorizontal[0]

def infoToDict(character, hskinfo, bcluinfo, meaning, pinyin):
    resultdict = {}
    if bcluinfo is None:
        realFreq = 0
    else:
        realFreq = bcluinfo
    resultdict["character"] = character
    resultdict["hsk"] = hskinfo
    resultdict["frequency"] = realFreq
    resultdict["meaning"] = meaning
    resultdict["pinyin"] = pinyin
    return resultdict

def generateVocabDictionary(allItems, script):
    singleList = sum(allItems, [])
    onlyChinese = [x for x in singleList if utilityService.isChinese(x)]
    chineseSet = sorted(set(onlyChinese), key=lambda x: onlyChinese.index(x))
    hsk = []
    setToSimp = []
    if script == "traditional":
        setToSimp = [getFirstWordFromConversion(CedictParser.wordToSimplifiedFromTrad(x)) for x in chineseSet]
        for x, y in zip(chineseSet, setToSimp):
            eachitem = infoToDict(x, HskParser.getHskLevel(y), BlcuParser.getBLCUfrequency(y),
                                  CedictParser.wordToMeaningTrad(x), CedictParser.wordToPinyinTrad(x))
            hsk.append(eachitem)
    elif script == "simplified":
        setToSimp = [x for x in chineseSet]
        hsk = [
            infoToDict(x, HskParser.getHskLevel(x), BlcuParser.getBLCUfrequency(x), CedictParser.wordToMeaningSimp(x),
                       CedictParser.wordToPinyinSimp(x)) for x in setToSimp]

    hsk1 = [x for x in hsk if x["hsk"] == "hsk1"]
    hsk1 = sorted(hsk1, key=lambda d: d["frequency"])
    hsk2 = [x for x in hsk if x["hsk"] == "hsk2"]
    hsk2 = sorted(hsk2, key=lambda d: d["frequency"])
    hsk3 = [x for x in hsk if x["hsk"] == "hsk3"]
    hsk3 = sorted(hsk3, key=lambda d: d["frequency"])
    hsk4 = [x for x in hsk if x["hsk"] == "hsk4"]
    hsk4 = sorted(hsk4, key=lambda d: d["frequency"])
    hsk5 = [x for x in hsk if x["hsk"] == "hsk5"]
    hsk5 = sorted(hsk5, key=lambda d: d["frequency"])
    hsk6 = [x for x in hsk if x["hsk"] == "hsk6"]
    hsk6 = sorted(hsk6, key=lambda d: d["frequency"])
    notHsk = [x for x in hsk if x["hsk"] == ""]
    notHsk = sorted(notHsk, key=lambda d: d["frequency"])
    hsk = sorted(hsk, key=lambda d: d["frequency"])

    resultDict = {}
    resultDict["hsk"] = hsk
    resultDict["hsk1"] = hsk1
    resultDict["hsk2"] = hsk2
    resultDict["hsk3"] = hsk3
    resultDict["hsk4"] = hsk4
    resultDict["hsk5"] = hsk5
    resultDict["hsk6"] = hsk6
    resultDict["notHsk"] = notHsk
    return resultDict

def mergeDict(vocabDict):
    result = ""
    for x in vocabDict:
        char = x["character"]
        hsk = x["hsk"]
        freq = x["frequency"]
        mean = x["meaning"]
        pinyin = x["pinyin"]
        result = result + char + " " + hsk + " " + str(freq) + " " + pinyin + " " + mean + "\n"
    return result

def rawVocabFromSentences(allItems, script):
    chineseSet = generateVocabDictionary(allItems, script)
    result = ""
    hsk1 = [x["character"] for x in chineseSet["hsk1"]]
    hsk2 = [x["character"] for x in chineseSet["hsk2"]]
    hsk3 = [x["character"] for x in chineseSet["hsk3"]]
    hsk4 = [x["character"] for x in chineseSet["hsk4"]]
    hsk5 = [x["character"] for x in chineseSet["hsk5"]]
    hsk6 = [x["character"] for x in chineseSet["hsk6"]]
    notHsk = [x["character"] for x in chineseSet["notHsk"]]

    result = result + "\n".join(hsk1) + "\n" + "\n"
    result = result + "\n".join(hsk2) + "\n" + "\n"
    result = result + "\n".join(hsk3) + "\n" + "\n"
    result = result + "\n".join(hsk4) + "\n" + "\n"
    result = result + "\n".join(hsk5) + "\n" + "\n"
    result = result + "\n".join(hsk6) + "\n" + "\n"
    result = result + "\n".join(notHsk)
    return result

def vocabFromSentences(allItems, script):
    chineseSet = generateVocabDictionary(allItems, script)
    number = len(chineseSet["hsk"])

    vocabText = ""
    vocabText = vocabText + "all words: " + str(number) + "\n"
    vocabText = vocabText + "hsk1: " + str(len(chineseSet["hsk1"])) + " of 150" + "\n"
    vocabText = vocabText + "hsk2: " + str(len(chineseSet["hsk2"])) + " of 151" + "\n"
    vocabText = vocabText + "hsk3: " + str(len(chineseSet["hsk3"])) + " of 300" + "\n"
    vocabText = vocabText + "hsk4: " + str(len(chineseSet["hsk4"])) + " of 600" + "\n"
    vocabText = vocabText + "hsk5: " + str(len(chineseSet["hsk5"])) + " of 1300" + "\n"
    vocabText = vocabText + "hsk6: " + str(len(chineseSet["hsk6"])) + " of 2500" + "\n"
    vocabText = vocabText + "non hsk: " + str(len(chineseSet["notHsk"])) + "\n" + "\n"

    hsk1 = mergeDict(chineseSet["hsk1"])
    hsk2 = mergeDict(chineseSet["hsk2"])
    hsk3 = mergeDict(chineseSet["hsk3"])
    hsk4 = mergeDict(chineseSet["hsk4"])
    hsk5 = mergeDict(chineseSet["hsk5"])
    hsk6 = mergeDict(chineseSet["hsk6"])
    notHsk = mergeDict(chineseSet["notHsk"])

    vocabText = vocabText + hsk1 + "\n"
    vocabText = vocabText + hsk2 + "\n"
    vocabText = vocabText + hsk3 + "\n"
    vocabText = vocabText + hsk4 + "\n"
    vocabText = vocabText + hsk5 + "\n"
    vocabText = vocabText + hsk6 + "\n"
    vocabText = vocabText + notHsk
    return vocabText

def flattenNestedList(cleanedMergedList, outputList):
    if len(cleanedMergedList) == 0:
        return outputList
    elif type(cleanedMergedList[0]) is tuple:
        rest = cleanedMergedList[1:]
        outputList.append(cleanedMergedList[0])
        return flattenNestedList(rest, outputList)
    else:
        newList = outputList + cleanedMergedList[0]
        rest = cleanedMergedList[1:]
        return flattenNestedList(rest, newList)

def senToDictFromTraditional(sent):
    tokens = ChineseLibParser.getTokensFromTraditionalSentence(sent)
    simplified = [CedictParser.wordToSimplifiedFromTrad(x) for x in tokens]
    pinyinList = [CedictParser.wordToPinyinTrad(x) for x in tokens]
    meaningList = [CedictParser.wordToMeaningTrad(x) for x in tokens]
    heisigSimplified = [HeisigParser.getHeisigStringFromWordSimp(x) for x in simplified]
    heisigSimpInt = [HeisigParser.getHeisigIntsFromWordSimp(x) for x in simplified]
    heisigSimpIntFlatten = [*heisigSimpInt]
    heisigTraditional = [HeisigParser.getHeisigStringFromWordTrad(x) for x in tokens]
    heisigTradInt = [HeisigParser.getHeisigIntsFromWordTrad(x) for x in tokens]
    heisigTradIntFlatten = [*heisigTradInt]
    hskLevel = [HskParser.getHskLevel(x) for x in simplified]
    blcu = [BlcuParser.getBLCUfrequency(x) for x in simplified]
    mydict = {
        "sentence": sent,
        "tokens": tokens,
        "simplified": simplified,
        "traditional": tokens,
        "pinyin": pinyinList,
        "meaning": meaningList,
        "hskLevel": hskLevel,
        "blcuFrequency": blcu,
        "heisigSimplified": heisigSimplified,
        "heisigSimpInt": heisigSimpIntFlatten,
        "heisigTraditional": heisigTraditional,
        "heisigTradInt": heisigTradIntFlatten
    }
    return mydict

def senToDictFromSimplified(sent):
    tokens = ChineseLibParser.getTokensFromSimplifiedSentence(sent)
    traditional = [CedictParser.wordToTraditionalFromSimp(x) for x in tokens]
    pinyinList = [CedictParser.wordToPinyinSimp(x) for x in tokens]
    meaningList = [CedictParser.wordToMeaningSimp(x) for x in tokens]
    heisigSimplified = [HeisigParser.getHeisigStringFromWordSimp(x) for x in tokens]
    heisigSimpInt = [HeisigParser.getHeisigIntsFromWordSimp(x) for x in tokens]
    heisigSimpIntFlatten = [*heisigSimpInt]
    heisigTraditional = [HeisigParser.getHeisigStringFromWordTrad(x) for x in traditional]
    heisigTradInt = [HeisigParser.getHeisigIntsFromWordTrad(x) for x in traditional]
    heisigTradIntFlatten = [*heisigTradInt]
    hskLevel = [HskParser.getHskLevel(x) for x in tokens]
    blcu = [BlcuParser.getBLCUfrequency(x) for x in tokens]
    mydict = {
        "sentence": sent,
        "tokens": tokens,
        "simplified": tokens,
        "traditional": traditional,
        "pinyin": pinyinList,
        "meaning": meaningList,
        "hskLevel": hskLevel,
        "blcuFrequency": blcu,
        "heisigSimplified": heisigSimplified,
        "heisigSimpInt" : heisigSimpIntFlatten,
        "heisigTraditional": heisigTraditional,
        "heisigTradInt": heisigTradIntFlatten
    }
    return mydict