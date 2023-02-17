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

def vocabFromSentences(allItems, script):
    singleList = sum(allItems, [])
    onlyChinese = [x for x in singleList if utilityService.isChinese(x)]
    chineseSet = sorted(set(onlyChinese), key=lambda x: onlyChinese.index(x))
    hsk = []
    setToSimp = []
    if script == "traditional":
        setToSimp = [CedictParser.wordToSimplifiedFromTrad(x) for x in chineseSet]
        hsk = [HskParser.getHskLevel(x) for x in setToSimp]
    elif script == "simplified":
        setToSimp = [x for x in chineseSet]
        hsk = [HskParser.getHskLevel(x) for x in setToSimp]
    hsk1 = len([x for x in hsk if x == "hsk1"])
    hsk2 = len([x for x in hsk if x == "hsk2"])
    hsk3 = len([x for x in hsk if x == "hsk3"])
    hsk4 = len([x for x in hsk if x == "hsk4"])
    hsk5 = len([x for x in hsk if x == "hsk5"])
    hsk6 = len([x for x in hsk if x == "hsk6"])
    notHsk = len([x for x in hsk if x == ""])
    number = len(chineseSet)

    vocabText = ""
    vocabText = vocabText + "all words: " + str(number) + "\n"
    vocabText = vocabText + "hsk1: " + str(hsk1) + " of 150" + "\n"
    vocabText = vocabText + "hsk2: " + str(hsk2) + " of 151" + "\n"
    vocabText = vocabText + "hsk3: " + str(hsk3) + " of 300" + "\n"
    vocabText = vocabText + "hsk4: " + str(hsk4) + " of 600" + "\n"
    vocabText = vocabText + "hsk5: " + str(hsk5) + " of 1300" + "\n"
    vocabText = vocabText + "hsk6: " + str(hsk6) + " of 2500" + "\n"
    vocabText = vocabText + "non hsk: " + str(notHsk) + "\n" + "\n"
    vocabText = vocabText + '\n'.join(chineseSet)
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