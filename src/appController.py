import json
from chinese import ChineseAnalyzer
import re

from src.classes import ChineseParser


#from src.classes.ChineseParser import ChineseParser



def postendpoint(postinput):
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    ChineseParser.initChineseParser()
    sentences = textToTokens(betterdata)
    return sentences

def sentenceToDict(sen):
    return sen

def textToTokens(text):
    test2 = ChineseParser.getSentences(text)
    result = [senToDict(x) for x in test2]
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

def findSubtokenPairs(firstElem, remainElems, listOfCharsToPinyinTupples):
    pinyin = ChineseParser.getPinyinStringFromWord(firstElem)
    pinyinSplit = pinyin.split()
    test = ChineseParser.getTokensFromSentence(firstElem)

    if len(firstElem) == 0 and len(remainElems) == 0:
        return listOfCharsToPinyinTupples
    elif len(firstElem) == 0:
        return findSubtokenPairs(remainElems, firstElem, listOfCharsToPinyinTupples)
    elif len(pinyinSplit) > 1:
        lenOfSplit = len(test[0])
        shrinkFirstElemAgain = firstElem[:(lenOfSplit - len(firstElem))]
        lastSection = firstElem[(lenOfSplit - len(firstElem)):]
        return findSubtokenPairs(shrinkFirstElemAgain, lastSection + remainElems, listOfCharsToPinyinTupples)
    elif len(pinyin) > 0 and pinyin != firstElem:
        listOfCharsToPinyinTupples.append((firstElem, pinyin))
        return findSubtokenPairs(remainElems, "", listOfCharsToPinyinTupples)
    elif len(firstElem) == 1:
        listOfCharsToPinyinTupples.append((firstElem, firstElem))
        return findSubtokenPairs(remainElems, "", listOfCharsToPinyinTupples)
    else:
        shrinkFirstElem = firstElem[:-1]
        lastChar = firstElem[-1]
        return findSubtokenPairs(shrinkFirstElem, lastChar + remainElems, listOfCharsToPinyinTupples)

def cleanedToken(tokenPinyinTuple):
    firstElem = tokenPinyinTuple[0]
    secondElem = tokenPinyinTuple[1]
    if firstElem == secondElem and isChinese(firstElem):
        return findSubtokenPairs(firstElem, "", [])
    else:
        return tokenPinyinTuple

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

def generatePinyinTokenPairs(sent):
    basicTokens = ' '.join(ChineseParser.getTokenListFromSentence(sent)).split()
    basicPinyin = ChineseParser.getPinyinStringFromWord(sent).split()
    mergedLists = list(zip(basicTokens, basicPinyin))
    cleanedMergedList = [cleanedToken(x) for x in mergedLists]
    result = flattenNestedList(cleanedMergedList, [])
    return result

def senToDict(sent):
    pinyinTokens = generatePinyinTokenPairs(sent)
    mydict = {
        "sentence": sent,
        "rawTokens": ChineseParser.getTokenListFromSentence(sent),
        "wordToPinyinTuples": pinyinTokens
    }
    return mydict

