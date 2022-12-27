import json
from chinese import ChineseAnalyzer
import re

def postendpoint(postinput):
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    analyzer = ChineseAnalyzer()

    sentences = textToTokens(betterdata, analyzer)



    anal = analyzer.parse(betterdata)
    test2 =  anal.sentences()
    hello = [x.strip(' ') for x in test2]
    tokens = [analyzer.parse(x).tokens() for x in hello]


    return hello

def sentenceToDict(sen):

    return sen

def textToTokens(text, analyserInp):
    anal = analyserInp.parse(text)
    test2 = anal.sentences()
    #for sent in test2:
    #    sentdic
    #[analyserInp.parse(x).tokens() for x in test2]

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


def findSubtokenPairs(firstElem, analyserInp):
    #write logic to handle untranslated text, such as names

    return firstElem


def cleanedToken(tokenPinyinTuple, analyserInp):
    firstElem = tokenPinyinTuple[0]
    secondElem = tokenPinyinTuple[1]

    if firstElem == secondElem and isChinese(firstElem):
        return findSubtokenPairs(firstElem, analyserInp)
    else:
        return tokenPinyinTuple



def generatePinyinTokenPairs(sent, analyserInp):
    basicTokens = ' '.join(analyserInp.parse(sent).tokens()).split()
    basicPinyin = analyserInp.parse(sent).pinyin().split()

    mergedLists = list(zip(basicTokens, basicPinyin))
    #list(map(list.__add__, basicTokens, basicPinyin))

    cleanedMergedList = [cleanedToken(x, analyserInp) for x in mergedLists]

    return cleanedMergedList


def senToDict(sent, analyserInp):
    pinyinTokens = generatePinyinTokenPairs(sent, analyserInp)

    mydict = {
        "sentence": sent,
        "tokens": analyserInp.parse(sent).tokens(),
        "pinyin": pinyinTokens
    }
    return mydict

