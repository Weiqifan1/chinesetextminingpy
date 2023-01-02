from src.libraryInterface import ChineseParser
from src.libraryInterface import CedictParser

def sentenceToDict(sen):
    return sen

def textToTokensFromSimplified(text):
    ChineseParser.initChineseParser()
    CedictParser.initCedictParser()
    test2 = ChineseParser.getSentencesFromLargeText(text)
    result = [senToDictFromSimplified(x) for x in test2]
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

def senToDictFromSimplified(sent):
    tokens = ChineseParser.getTokensFromSentence(sent)
    traditional = [CedictParser.wordToTraditionalSimp(x) for x in tokens]
    pinyinList = [CedictParser.wordToPinyinSimp(x) for x in tokens]
    meaningList = [CedictParser.wordToMeaningSimp(x) for x in tokens]
    mydict = {
        "sentence": sent,
        "tokens": tokens,
        "simplified": tokens,
        "traditional": traditional,
        "pinyin": pinyinList,
        "meaning": meaningList
    }
    return mydict



