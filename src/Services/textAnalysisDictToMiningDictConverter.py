from operator import itemgetter

from src.Services.utilityService import isChinese
import functools

globalLineSeparator = "\n"
globalParagraphSeparator = "\n\n" # "<br/><br/>"

def addValueToDict(valueName, oldDict, newDict):
    if valueName in oldDict:
        newDict[valueName] = oldDict[valueName]
    return newDict


def doTokenList(tokenList, token, newList):
    punctuationSet = {",", ".", "。", "？", "?", ";", "!", "、"}
    if len(tokenList) == 0:
        return newList
    elif tokenList[0] in punctuationSet: #not isChinese(tokenList[0]):
        punctuation = tokenList[0] + " "
        newList.append(punctuation)
        return doTokenList(tokenList[1:], token, newList)
    elif tokenList[0] == token:
        tokenWithBraces = " [[" + token + "]] "
        newList.append(tokenWithBraces)
        return doTokenList(tokenList[1:], token, newList)
    else:
        other = tokenList[0]
        newList.append(other)
        return doTokenList(tokenList[1:], token, newList)



def tokentListToBacksideSentence(tokenList, token):
    resultString = doTokenList(tokenList, token, [])
    joinedString = "".join(resultString)
    return joinedString


def formatAmbigousPinyin(rawPinyin):
    if not "|" in rawPinyin:
        return rawPinyin
    else:
        spl = rawPinyin.split("|")
        bolden = spl[0].upper()
        last = bolden[-1]
        noNum = bolden[:-1] if last.isnumeric() else bolden
        return noNum


def subcard(token, sharedData, index, pinyinList, tokenList, sentence, blcu, deckName, deckInfo, sentencename, textType):
    #write a function that surrounds pinyin with curly
    firstCardInSentece = False
    convertedPinyin = []
    for x in range(len(pinyinList)):
        tok = tokenList[x]
        rawPinyin = pinyinList[x]
        pin = formatAmbigousPinyin(rawPinyin)
        if tok == token:
            convertedPinyin.append("[[" + pin + "]]")
            if x == 0:
                firstCardInSentece = True
        else:
            convertedPinyin.append(pin)

    generateTags = ["sentenceNo:" + str(index + 1)]
    if firstCardInSentece:
        generateTags.append("firstInSentence")
    generateTags.append(deckName)
    generateTags.append(token)

    backsideAndSecondaryInfo = sharedData.split(globalParagraphSeparator)
    cardName = "sentenceNo:" + str(index + 1)
    if textType == "ordered2Line":
        cardName = sentencename
    res = {
        "tokenblcu": [blcu],
        "cardNumber": 0,
        "cardName": cardName,
        "frontSide": (" ".join(convertedPinyin)).strip(),
        "backSide": (tokentListToBacksideSentence(tokenList, token)).strip(), # instead of just using token + sentence, i will try to join the tokentlist,
        "primaryInfo": backsideAndSecondaryInfo[0],
        "secondaryInfo": globalParagraphSeparator.join(backsideAndSecondaryInfo[1:]),
        "notableCards": [],
        "dateOfLastReview": "2000-01-01",
        "repetitionValue": 1,
        "repetitionHistory": [],
        "tags": generateTags
    }
    return res


def subcardForWholeSentence(sharedData, index, pinyinList, tokenList, sentence, blcu, deckName, deckInfo, senHasUniqueWord, sentencename, textType):
    # write a function that surrounds pinyin with curly
    generateTags = ["sentenceNo:" + str(index + 1), "onlySentence"]
    if senHasUniqueWord:
        generateTags.append("hasUniqueWord")
    generateTags.append(deckName)
    for elem in tokenList:
        if isChinese(elem):
            generateTags.append(elem)
    backsideAndSecondaryInfo = sharedData.split(globalParagraphSeparator)
    cardName = "sentenceNo:" + str(index + 1)
    if textType == "ordered2Line":
        cardName = sentencename
    res = {
        "tokenblcu": blcu,
        "cardNumber": 0,
        "cardName": cardName,
        "frontSide": " ".join(pinyinList),
        "backSide": sentence,
        "primaryInfo": backsideAndSecondaryInfo[0],
        "secondaryInfo": globalParagraphSeparator.join(backsideAndSecondaryInfo[1:]),
        "notableCards": [],
        "dateOfLastReview": "",
        "repetitionValue": 1,
        "repetitionHistory": [],
        "tags": generateTags
    }
    return res


def convertSentenceToCardOnlySimplified(sen, prevSen, nextSen, index, tokenList, blcu, lineblcu, deckName, deckInfo, vocab, sentencenames, textType):
    output = sharedSentenceData(nextSen, prevSen, sen, "simplified")
    cardList = []
    senHasUniqueWord = False
    for i in range(len(tokenList)):
        eachWord = tokenList[i]
        #sentName = sentencenames[i]
        if eachWord not in vocab:
            senHasUniqueWord = True
            cardtemp = subcard(eachWord, output, index, sen.get("pinyin"), sen.get("simplified"), sen.get("sentence"), blcu.get(eachWord), deckName, deckInfo, sentencenames, textType)
            cardList.append(cardtemp)
    cardForWholeSentence = subcardForWholeSentence(output, index, sen.get("pinyin"), sen.get("simplified"), sen.get("sentence"), lineblcu, deckName, deckInfo, senHasUniqueWord, sentencenames, textType)
    cardList.append(cardForWholeSentence)
    return cardList

def convertSentenceToCardOnlyTraditional(sen, prevSen, nextSen, index, tokenList, blcu, lineblcu, deckName, deckInfo, vocab, sentencenames, textType):
    output = sharedSentenceData(nextSen, prevSen, sen, "traditional")
    cardList = []
    senHasUniqueWord = False
    for i in range(len(tokenList)):
        eachWord = tokenList[i]
        #sentName = sentencenames[i]
        if eachWord not in vocab:
            senHasUniqueWord = True
            cardtemp = subcard(eachWord, output, index, sen.get("pinyin"), sen.get("traditional"), sen.get("sentence"), blcu.get(eachWord), deckName, deckInfo, sentencenames, textType)
            cardList.append(cardtemp)
    cardForWholeSentence = subcardForWholeSentence(output, index, sen.get("pinyin"), sen.get("traditional"), sen.get("sentence"), lineblcu, deckName, deckInfo, senHasUniqueWord, sentencenames, textType)
    cardList.append(cardForWholeSentence)
    return cardList

def sharedSentenceData(nextSen, prevSen, sen, script):
    if script == "simplified":
        output = ""
        tokenDataString = sentenceTokenDataOnlySimplified(sen, False)
        companionStr = ""
        if prevSen == None and not nextSen == None:
            companionStr = "next Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlySimplified(nextSen, True)
        elif nextSen == None and not prevSen == None:
            companionStr = "previous Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlySimplified(prevSen, True)
        elif not nextSen == None and not prevSen == None:
            companionStr = "previous Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlySimplified(prevSen, True) \
                           + globalParagraphSeparator \
                           + "next Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlySimplified(nextSen, True)
        else:
            return tokenDataString
        output = tokenDataString + globalParagraphSeparator + companionStr
        return output
    elif script == "traditional":
        output = ""
        tokenDataString = sentenceTokenDataOnlyTraditional(sen, False)#sentenceTokenDataOnlySimplified(sen, False)
        companionStr = ""
        if prevSen == None and not nextSen == None:
            companionStr = "next Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlyTraditional(nextSen, True)
        elif nextSen == None and not prevSen == None:
            companionStr = "previous Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlyTraditional(prevSen, True)
        elif not nextSen == None and not prevSen == None:
            companionStr = "previous Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlyTraditional(prevSen, True) \
                           + globalParagraphSeparator \
                           + "next Sentence:" \
                           + globalLineSeparator \
                           + sentenceTokenDataOnlyTraditional(nextSen, True)
        else:
            return tokenDataString
        output = tokenDataString + globalParagraphSeparator + companionStr
        return output
    else:
        return None

def sentenceTokenDataOnlyTraditional(sen, includeSentenceInFront):
    tokens = sen.get("tokens")
    sentenceInFront = ""
    if includeSentenceInFront:
        sentenceInFront = tokentListToBacksideSentence(tokens, "")
    # simplified = sen.get("simplified")
    # traditional = sen.get("traditional")
    pinyin = sen.get("pinyin")
    meaning = sen.get("meaning")
    hsk = sen.get("hskLevel")
    blcu = sen.get("blcuFrequency")
    #Hsimp = sen.get("heisigSimplified")
    Htrad = sen.get("heisigTraditional")
    tokenData = []
    for x in range(len(tokens)):
        generated = generateTokenDataOnly(tokens[x], pinyin[x], meaning[x], hsk[x], blcu[x], Htrad[x])
        tokenData.append(generated)
    res = globalLineSeparator.join(tokenData)
    if not sentenceInFront == "":
        res = sentenceInFront + globalLineSeparator + res
    return res
def sentenceTokenDataOnlySimplified(sen, includeSentenceInFront):
    tokens = sen.get("tokens")
    sentenceInFront = ""
    if includeSentenceInFront:
        sentenceInFront = tokentListToBacksideSentence(tokens, "")
    # simplified = sen.get("simplified")
    # traditional = sen.get("traditional")
    pinyin = sen.get("pinyin")
    meaning = sen.get("meaning")
    hsk = sen.get("hskLevel")
    blcu = sen.get("blcuFrequency")
    Hsimp = sen.get("heisigSimplified")
    # Htrad = sen.get("heisigTraditional")
    tokenData = []
    for x in range(len(tokens)):
        generated = generateTokenDataOnly(tokens[x], pinyin[x], meaning[x], hsk[x], blcu[x], Hsimp[x])
        tokenData.append(generated)
    res = globalLineSeparator.join(tokenData)
    if not sentenceInFront == "":
        res = sentenceInFront + globalLineSeparator + res
    return res

def generateTokenDataOnly(token, pinyin, meaning, hsk, blcu, heisig):
    values = [token, pinyin, meaning, hsk, blcu, heisig]
    convNone = lambda i: str(i) if i else "nil"
    resultStr = [convNone(i) for i in values]
    result = resultStr[0] + " " + resultStr[1] + " " + resultStr[2] + globalLineSeparator + "heisig:" + resultStr[5] + " hsk:" + resultStr[3] + " blcu:"  + resultStr[4]
    return result

def getNestedUniqueList(listOfTokens, newList, length, setToCompare):
    if len(newList) == length:
        return newList
    else:
        currentTokens = listOfTokens[0]
        filtered = list(filter(lambda a: a not in setToCompare and isChinese(a), currentTokens))
        newFiltered = []
        for x in filtered:
            if not x in newFiltered:
                newFiltered.append(x)
        updatedListOfTokens = listOfTokens[1:]
        newList.append(newFiltered)
        setToCompare.update(currentTokens)
        return getNestedUniqueList(updatedListOfTokens, newList, length, setToCompare)

def convertSentencesToCardsSimplified(outputLines, deckName, deckInfo, vocab, sentencenames, textType):
    tokenFReqMap = getTokenFreqMap(outputLines)
    uniqueTokens = getNestedUniqueList([x.get("simplified") for x in outputLines], [], len(outputLines), set())

    result = []
    for i in range(len(outputLines)):
        if i is 0:
            current = outputLines[i]
            next = outputLines[i+1] if len(outputLines) > i+1 else None
            card = convertSentenceToCardOnlySimplified(current, None, next, i, uniqueTokens[i], tokenFReqMap, current.get("blcuFrequency"), deckName, deckInfo, vocab, sentencenames[i], textType)
            result.append(card)
        elif i is len(outputLines) - 1:
            current = outputLines[i]
            prev = outputLines[i-1]
            card = convertSentenceToCardOnlySimplified(current, prev, None, i, uniqueTokens[i], tokenFReqMap, current.get("blcuFrequency"), deckName, deckInfo, vocab, sentencenames[i], textType)
            result.append(card)
        else:
            current = outputLines[i]
            prev = outputLines[i-1]
            next = outputLines[i+1] if len(outputLines) > i+1 else None
            card = convertSentenceToCardOnlySimplified(current, prev, next, i, uniqueTokens[i], tokenFReqMap, current.get("blcuFrequency"), deckName, deckInfo, vocab, sentencenames[i], textType)
            result.append(card)
    return result

    #configurations
    #traditional data, simplified data, traditional first then simplified, simplified first then traditional
    # (how it is done depends on witch script the original script is in)
    #word cards only, sentencecards only, words and sentencecards
    #tags: the word cards, the sentencecards and the deck title will become tags

    #if no configs == only simplified data and both words and sentences

    #TODO: skal ordne text til simplified

def convertSentencesToCardsTraditional(outputLines, deckName, deckInfo, vocab, sentencenames, textType):
    tokenFReqMap = getTokenFreqMap(outputLines)
    uniqueTokens = getNestedUniqueList([x.get("traditional") for x in outputLines], [], len(outputLines), set())
    result = []

    for i in range(len(outputLines)):
        if i is 0:
            current = outputLines[i]
            next = outputLines[i + 1] if len(outputLines) > i + 1 else None
            #createUniquetokens to blcu map
            card = convertSentenceToCardOnlyTraditional(current, None, next, i, uniqueTokens[i], tokenFReqMap, current.get("blcuFrequency"), deckName, deckInfo, vocab, sentencenames[i], textType)
            result.append(card)
        elif i is len(outputLines) - 1:
            current = outputLines[i]
            prev = outputLines[i - 1]
            card = convertSentenceToCardOnlyTraditional(current, prev, None, i, uniqueTokens[i], tokenFReqMap, current.get("blcuFrequency"), deckName, deckInfo, vocab, sentencenames[i], textType)
            result.append(card)
        else:
            current = outputLines[i]
            prev = outputLines[i - 1]
            next = outputLines[i + 1] if len(outputLines) > i + 1 else None
            card = convertSentenceToCardOnlyTraditional(current, prev, next, i, uniqueTokens[i], tokenFReqMap, current.get("blcuFrequency"), deckName, deckInfo, vocab, sentencenames[i], textType)
            result.append(card)
    return result


def getTokenFreqMap(outputLines):
    tokenJoinedList = sum([x.get("tokens") for x in outputLines], [])
    freqlist = sum([x.get("blcuFrequency") for x in outputLines], [])
    tokenFReqMap = {}
    for key in tokenJoinedList:
        for value in freqlist:
            tokenFReqMap[key] = value
            freqlist.remove(value)
            break
    return tokenFReqMap


def sortBlcu(blcuList):
    #write code that removes None
    noNone = [x for x in blcuList if x is not None]
    #write code that sorts the list
    sortedList = list(reversed(sorted(noNone)))
    return sortedList


def getBlcu1IsLarger(blcu1, blcu2):
    if blcu1 == []:
        return False
    if blcu2 == []:
        return True
    head1, *tail1 = blcu1
    head2, *tail2 = blcu2
    if head1 > head2:
        return True
    elif head2 > head1:
        return False
    return getBlcu1IsLarger(tail1, tail2)

def sortDictsByBlcuTuple(item1, item2):
    blcu1 = item1[0]
    blcu2 = item2[0]
    if blcu1 == blcu2:
        return 0
    blcu1IsLarger = getBlcu1IsLarger(blcu1, blcu2)
    if blcu1IsLarger:
        return 1
    return -1

def flatCardsWithNumbers(flatCArds, param):
    if param == "chronological":
        multitokenCards = list(filter(lambda a: len(a.get("tokenblcu")) > 1, flatCArds))
        singleTokenCards = list(filter(lambda a: len(a.get("tokenblcu")) < 2, flatCArds))
        resultToNumber = singleTokenCards + multitokenCards

        for x in range(len(resultToNumber)):
            eachcard = resultToNumber[x]
            eachcard["cardNumber"] = x + 1
        return resultToNumber
    elif param == "frequency":
        #multitokens
        multitokenCards = list(filter(lambda a : len(a.get("tokenblcu")) > 1, flatCArds))
        #write code that create a tupple. left side is sorted list of blcu, right side is dict
        rawMultiTupple = [(sortBlcu(y.get("tokenblcu")), y) for y in multitokenCards]
        oldStyleComparator = functools.cmp_to_key(sortDictsByBlcuTuple)
        sortedMultiTupple = sorted(rawMultiTupple, key=oldStyleComparator)#sortDictsByBlcuTuple(rawMultiTupple)

        #single tokens
        singleTokenCards = list(filter(lambda a : len(a.get("tokenblcu")) < 2, flatCArds))
        notHasBlcu = list(filter(lambda a : a.get("tokenblcu") == [None], singleTokenCards))
        hasBlcu = list(filter(lambda a : a.get("tokenblcu") != [None], singleTokenCards))
        hasBlcu_sorted = hasBlcu
        hasBlcu_sorted.sort(key = lambda a : a.get("tokenblcu")[0])

        finalMultiple = list(map(lambda a: a[1], sortedMultiTupple))
        finalResult = hasBlcu_sorted + notHasBlcu + finalMultiple

        for x in range(len(finalResult)):
            eachcard = finalResult[x]
            eachcard["cardNumber"] = x + 1
        return finalResult
    else:
        return flatCArds

def getInfoForTag(tag):
    return "noInfo"

def convertAnalysisDictToMiningDict(analysisDict):
    resultDict = {}
    resultDict = addValueToDict("deckName", analysisDict, resultDict)
    resultDict = addValueToDict("deckInfo", analysisDict, resultDict)
    resultDict = addValueToDict("script", analysisDict, resultDict)

    outputLines = getValueFromDictionary("output", analysisDict)
    if outputLines is None or outputLines is []:
        return resultDict
    else:
        cards = {}
        if analysisDict["script"] == "simplified":
            cards = convertSentencesToCardsSimplified(outputLines,
                                                      analysisDict.get("deckName"),
                                                      analysisDict.get("deckInfo"),
                                                      analysisDict.get("vocab"),
                                                      analysisDict.get("sentencenames"),
                                                      analysisDict.get("textType"))
        elif analysisDict["script"] == "traditional":
            cards = convertSentencesToCardsTraditional(outputLines,
                                                       analysisDict.get("deckName"),
                                                       analysisDict.get("deckInfo"),
                                                       analysisDict.get("vocab"),
                                                       analysisDict.get("sentencenames"),
                                                       analysisDict.get("textType"))

        flatCArds = [element for innerList in cards for element in innerList]
        #flatCArds = [card.strip() for card in flatCArdsRaw]

        cardsWithNumbers = flatCardsWithNumbers(flatCArds, analysisDict.get("cardOrder"))

        tagsList = getAllTagsFromCards(cardsWithNumbers)
        tagsList.sort()
        res = {tagsList[i]: getInfoForTag(tagsList[i]) for i in range(len(tagsList))}
        res.update({analysisDict.get("deckName"): analysisDict.get("deckInfo")})
        finalCards = list(map(lambda a: {key:val for key, val in a.items() if key != "tokenblcu"}, cardsWithNumbers))
        resultDict["cards"] = finalCards#cards#finalCards#list(map(lambda a: a.update({"cardNumber": a["cardNumber"] + )) ))
        resultDict["tags"] = res
        resultDict["settings"] = {}
        return resultDict

def getAllTagsFromCards(flatCArds):
    alltags = [x.get("tags") for x in flatCArds if x.get("tags")]
    flattenTags = set([element for innerList in alltags for element in innerList])
    return list(flattenTags)

def getValueFromDictionary(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        return None
