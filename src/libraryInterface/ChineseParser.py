from chinese import ChineseAnalyzer

def initChineseParser():
    global parser
    parser = ChineseAnalyzer()

def getSentencesFromLargeText(inputTest):
    """
    :param inputTest: a string containing a chinese text. Example:
    "12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉,
    新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢,
    较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组,
    将全部用于新成昆铁路开行。"
    :return: a list of the sentences contained in the text. Example:
    ['12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验',
    "记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相",
    "据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间",
    "此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行"]
    """
    anal = parser.parse(inputTest)
    sent = anal.sentences()
    trimmedSen = [x.strip() for x in sent]
    return trimmedSen

def getTokensFromSentence(sent):
    """
    :param sentence: a string consisting of a single chinese sentences or small string of text. Example:
     '昆铁路'
    :return: a list of words/tokens contained in the text. Example:
    ['昆', '铁路']
    """
    basicTokens = ' '.join(parser.parse(sent).tokens()).split()
    basicPinyin = getPinyinStringFromSentence(sent).split()
    mergedLists = list(zip(basicTokens, basicPinyin))
    cleanedMergedList = [cleanedToken(x) for x in mergedLists]
    result = flattenNestedList(cleanedMergedList, [])
    final = [x for (x,y) in result]
    return final

def getTokenToPinyinTuplesFromSentence(sent):
    basicTokens = ' '.join(parser.parse(sent).tokens()).split()
    basicPinyin = getPinyinStringFromSentence(sent).split()
    mergedLists = list(zip(basicTokens, basicPinyin))
    cleanedMergedList = [cleanedToken(x) for x in mergedLists]
    result = flattenNestedList(cleanedMergedList, [])

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

def cleanedToken(tokenPinyinTuple):
    firstElem = tokenPinyinTuple[0]
    secondElem = tokenPinyinTuple[1]
    if firstElem == secondElem and isChinese(firstElem):
        return findSubtokenPairs(firstElem, "", [])  #findSubtokenPairs(firstElem, "", [])
    else:
        return tokenPinyinTuple

def findSubtokenPairs(firstElem, remainElems, listOfCharsToPinyinTupples):
    pinyin = getPinyinStringFromSentence(firstElem)
    pinyinSplit = pinyin.split()
    test = ' '.join(parser.parse(firstElem).tokens()).split()

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


def isChinese(firstElem):
    singleChars = [*firstElem]
    singleCharsSet = [isCharChinese(x) for x in singleChars]
    if True in singleCharsSet:
        return True
    else:
        return False

def isCharChinese(singleChar):
    #range of chinese punctuation in unicode
    myrange = range(12288, 12352)
    ordinal = ord(singleChar)
    if ordinal > 20000 and ordinal not in myrange:
        return True
    else:
        return False

def getPinyinStringFromSentence(text):
    """
    :param text: a string consisting of a single chinese sentences or small string of text. Example:
    '12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验'
    :return: a string of pinyin generated from the text. each ward is space separated. Example:
    '12 yuè 23 Rì ,   Zhōngguó tiělù Chéngdū jú 集团公司 zǔzhī méitǐ tíqián shìchéng Xīn 成昆铁路 ,   gǎnshòu jíjiāng dàolái de shíkōng 新体验'
    """
    pinyinStr = parser.parse(text).pinyin()
    return pinyinStr


