from src.libraryInterface import ChineseParser
from src.libraryInterface import CedictParser

def sentenceToDict(sen):
    return sen

def textToTokensFromSimplified(text):
    ChineseParser.initChineseParser()
    test2 = ChineseParser.getSentencesFromLargeText(text)
    fileContent = CedictParser.readCedictContentFromCedictReader()
    CedictParser.initCedictParser(fileContent)
    result = [senToDictFromSimplified(x) for x in test2]
    return result

def isCharChinese(singleChar):
    #range of chinese punctuation in unicode
    myrange = range(12288, 12352)
    ordinal = ord(singleChar)
    if ordinal > 20000 and ordinal not in myrange:
        return True
    else:
        return False

def isChinese(firstElem):
    singleChars = [*firstElem]
    singleCharsSet = [isCharChinese(x) for x in singleChars]
    if True in singleCharsSet:
        return True
    else:
        return False

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



