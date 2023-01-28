from src.libraryInterface import ChineseLibParser
from src.libraryInterface import CedictParser
from src.libraryInterface import HeisigParser
from src.libraryInterface import HskParser
from src.libraryInterface import BlcuParser

def sentenceToDict(sen):
    return sen

def textToTokensFromSimplified(text):
    ChineseLibParser.initChineseLibParser()
    CedictParser.initCedictParser()
    HeisigParser.initHeisigParser()
    HskParser.initHskParser()
    BlcuParser.initBLCUDictionary()
    print("doneLoading")
    test2 = ChineseLibParser.getSentencesFromLargeText(text)
    result = [senToDictFromSimplified(x) for x in test2]
    return result

def textToTokensFromTraditional(text):
    ChineseLibParser.initChineseLibParser()
    CedictParser.initCedictParser()
    HeisigParser.initHeisigParser()
    HskParser.initHskParser()
    BlcuParser.initBLCUDictionary()
    print("doneLoading")
    test2 = ChineseLibParser.getSentencesFromLargeText(text)
    result = [senToDictFromTraditional(x) for x in test2]
    return result

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



