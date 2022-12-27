import json
from chinese import ChineseAnalyzer
import re

def postendpoint(postinput):
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    analyzer = ChineseAnalyzer()
    sentences = textToTokens(betterdata, analyzer)
    return sentences

def sentenceToDict(sen):
    return sen

def textToTokens(text, analyserInp):
    anal = analyserInp.parse(text)
    test2 = anal.sentences()
    result = [senToDict(x, analyserInp) for x in test2]
    return result

def isCharChinese(singleChar):
    myrange = range(12288, 12352)
    ordinal = ord(singleChar)
    if ordinal > 20000 and ordinal not in myrange:
        return True
    else:
        return False
#12288 - 12351

def isChinese(firstElem):
    singleChars = [*firstElem]
    singleCharsSet = [isCharChinese(x) for x in singleChars]
    if True in singleCharsSet:
        return True
    else:
        return False

def findSubtokenPairs(firstElem, remainElems, analyserInp, listOfCharsToPinyinTupples):
    analysis = analyserInp.parse(firstElem)
    pinyin = analysis.pinyin()
    pinyinSplit = pinyin.split()
    test = analysis.tokens()

    if len(firstElem) == 0 and len(remainElems) == 0:
        return listOfCharsToPinyinTupples
    elif len(firstElem) == 0:
        return findSubtokenPairs(remainElems, firstElem, analyserInp, listOfCharsToPinyinTupples)
    elif len(pinyinSplit) > 1:
        lenOfSplit = len(test[0])
        shrinkFirstElemAgain = firstElem[:(lenOfSplit - len(firstElem))]
        lastSection = firstElem[(lenOfSplit - len(firstElem)):]
        return findSubtokenPairs(shrinkFirstElemAgain, lastSection + remainElems, analyserInp, listOfCharsToPinyinTupples)
    elif len(pinyin) > 0 and pinyin != firstElem:
        listOfCharsToPinyinTupples.append((firstElem, pinyin))
        return findSubtokenPairs(remainElems, "", analyserInp, listOfCharsToPinyinTupples)
    elif len(firstElem) == 1:
        listOfCharsToPinyinTupples.append((firstElem, firstElem))
        return findSubtokenPairs(remainElems, "", analyserInp, listOfCharsToPinyinTupples)
    else:
        shrinkFirstElem = firstElem[:-1]
        lastChar = firstElem[-1]
        return findSubtokenPairs(shrinkFirstElem, lastChar + remainElems, analyserInp, listOfCharsToPinyinTupples)

def cleanedToken(tokenPinyinTuple, analyserInp):
    firstElem = tokenPinyinTuple[0]
    secondElem = tokenPinyinTuple[1]
    if firstElem == secondElem and isChinese(firstElem):
        return findSubtokenPairs(firstElem, "",analyserInp, [])
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

def generatePinyinTokenPairs(sent, analyserInp):
    basicTokens = ' '.join(analyserInp.parse(sent).tokens()).split()
    basicPinyin = analyserInp.parse(sent).pinyin().split()
    mergedLists = list(zip(basicTokens, basicPinyin))
    cleanedMergedList = [cleanedToken(x, analyserInp) for x in mergedLists]
    result = flattenNestedList(cleanedMergedList, [])
    return result

def senToDict(sent, analyserInp):
    pinyinTokens = generatePinyinTokenPairs(sent, analyserInp)
    mydict = {
        "sentence": sent,
        "rawTokens": analyserInp.parse(sent).tokens(),
        "wordToPinyinTuples": pinyinTokens
    }
    return mydict

