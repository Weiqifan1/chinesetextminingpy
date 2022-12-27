import json
from chinese import ChineseAnalyzer
import re
from src.classes.ChineseParser import ChineseParser

def postendpoint(postinput):
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    chineseParser = ChineseParser()
    sentences = textToTokens(betterdata, chineseParser)
    return sentences

def sentenceToDict(sen):
    return sen

def textToTokens(text, chineseParser):
    test2 = chineseParser.getSentences(text)
    result = [senToDict(x, chineseParser) for x in test2]
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

def findSubtokenPairs(firstElem, remainElems, listOfCharsToPinyinTupples, chineseParser):
    pinyin = chineseParser.getPinyinStringFromWord(firstElem)
    pinyinSplit = pinyin.split()
    test = chineseParser.getTokensFromSentence(firstElem)

    if len(firstElem) == 0 and len(remainElems) == 0:
        return listOfCharsToPinyinTupples
    elif len(firstElem) == 0:
        return findSubtokenPairs(remainElems, firstElem, listOfCharsToPinyinTupples, chineseParser)
    elif len(pinyinSplit) > 1:
        lenOfSplit = len(test[0])
        shrinkFirstElemAgain = firstElem[:(lenOfSplit - len(firstElem))]
        lastSection = firstElem[(lenOfSplit - len(firstElem)):]
        return findSubtokenPairs(shrinkFirstElemAgain, lastSection + remainElems, listOfCharsToPinyinTupples, chineseParser)
    elif len(pinyin) > 0 and pinyin != firstElem:
        listOfCharsToPinyinTupples.append((firstElem, pinyin))
        return findSubtokenPairs(remainElems, "", listOfCharsToPinyinTupples, chineseParser)
    elif len(firstElem) == 1:
        listOfCharsToPinyinTupples.append((firstElem, firstElem))
        return findSubtokenPairs(remainElems, "", listOfCharsToPinyinTupples, chineseParser)
    else:
        shrinkFirstElem = firstElem[:-1]
        lastChar = firstElem[-1]
        return findSubtokenPairs(shrinkFirstElem, lastChar + remainElems, listOfCharsToPinyinTupples, chineseParser)

def cleanedToken(tokenPinyinTuple, chineseParser):
    firstElem = tokenPinyinTuple[0]
    secondElem = tokenPinyinTuple[1]
    if firstElem == secondElem and isChinese(firstElem):
        return findSubtokenPairs(firstElem, "", [], chineseParser)
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

def generatePinyinTokenPairs(sent, chineseParser):
    basicTokens = ' '.join(chineseParser.getTokenListFromSentence(sent)).split()
    basicPinyin = chineseParser.getPinyinStringFromWord(sent).split()
    mergedLists = list(zip(basicTokens, basicPinyin))
    cleanedMergedList = [cleanedToken(x, chineseParser) for x in mergedLists]
    result = flattenNestedList(cleanedMergedList, [])
    return result

def senToDict(sent, chineseParser):
    pinyinTokens = generatePinyinTokenPairs(sent, chineseParser)
    mydict = {
        "sentence": sent,
        "rawTokens": chineseParser.getTokenListFromSentence(sent),
        "wordToPinyinTuples": pinyinTokens
    }
    return mydict

