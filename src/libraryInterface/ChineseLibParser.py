import jieba
import re
from src.Services.utilityService import isChinese
from src.libraryInterface import CedictParser

def initChineseLibParser():
    print("start chinese")

def splitStringOnDelimiters(inputTest, paramList):
    stringlist = []
    newString = ""
    for elem in inputTest:
        elemUnicode = ord(elem)
        if elem in paramList:
            newString = newString + elem
            stringlist.append(newString)
            newString = ""
        else:
            newString = newString + elem
    return stringlist

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
    rawsens3 = splitStringOnDelimiters(inputTest, [".","。","，",","])
    stripSen = [x.strip() for x in rawsens3 if len(x) > 0]
    return stripSen

def getTokensFromTraditionalSentence(sent):
    # use cedict to find subtokens
    CedictParser.initCedictParser()
    cedict = CedictParser.getCedictTradDict()

    basic = jieba.cut(sent, cut_all=False)
    normal = " ".join(basic)
    parsed = normal.split()

    parsedByCedict = [parseWordByCedict(x, "", [], cedict) for x in parsed]
    flatList = flattenNestedList(parsedByCedict, [])
    joined = joinNonHanStrings(flatList, [])
    return joined

def getTokensFromSimplifiedSentence(sent):
    """
    :param sentence: a string consisting of a single chinese sentences or small string of text. Example:
     '昆铁路'
    :return: a list of words/tokens contained in the text. Example:
    ['昆', '铁路']
    """
    #use cedict to find subtokens
    CedictParser.initCedictParser()
    cedict = CedictParser.getCedictSimpDict()

    basic = jieba.cut(sent, cut_all=False)
    normal = " ".join(basic)
    parsed = normal.split()

    parsedByCedict = [parseWordByCedict(x, "", [], cedict) for x in parsed]
    flatList = flattenNestedList(parsedByCedict, [])
    joined = joinNonHanStrings(flatList, [])
    return joined


def joinNonHanStrings(flatList, newList):
    if len(flatList) == 0:
        return newList
    elif isChinese(flatList[0]) or len(flatList) == 1 or isChinese(flatList[1]):
        newList.append(flatList[0])
        shortened = flatList[1:]
        return joinNonHanStrings(shortened, newList)
    else:
        first = flatList[0]
        second = flatList[1]
        doubleShort = [first + second] + flatList[2:]
        return joinNonHanStrings(doubleShort, newList)

def parseWordByCedict(remainWord, restWord, parsedList, cedict):
    if remainWord == "" and restWord == "":
        return parsedList
    elif remainWord in cedict or len(remainWord) == 1:
        parsedList.append(remainWord)
        return parseWordByCedict(restWord, "", parsedList, cedict)
    else:
        init = remainWord[:-1]
        last = remainWord[-1:]
        newRestWord = last + restWord
        return parseWordByCedict(init, newRestWord, parsedList, cedict)

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

def sentencesFromOrdered2Line(text):
    # we split the text on double newLine. each trimmed block should now be 1 or 2 lines
    # if 1, then it is a front side. if 2, then the second is front line and the first is cardname
    doublenewline = re.compile(r"(\n{2})|(\n\r\n\r)").split(text)
    trimmedFirst = list(filter(lambda x: not x is None, doublenewline))
    trimmessecond = list(filter(lambda x: not x.isspace(), trimmedFirst))
    trimmesthrid = list([i for i in trimmessecond if i])#[x for x in doublenewline if not x.isspace()]
    nestedLines = [re.compile(r"\n").split(x) for x in trimmesthrid]
    doublenested = list(map(lambda x: [i.strip() for i in x if i], nestedLines))

    sent = []
    sentnames = []
    for item in doublenested:
        if len(item) > 1:
            sentnames.append(item[0])
            sent.append(item[1])
        else:
            sent.append(item[0])
            sentnames.append("")
    return (sent, sentnames)