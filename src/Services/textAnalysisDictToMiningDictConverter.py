from src.Services.utilityService import isChinese


#convert dictionaries from the text analysis format to FlashCardDeck format from the app 'hanzimining'

globalLineSeparator = "\n"

globalParagraphSeparator = "\n\n" # "<br/><br/>"

def addValueToDict(valueName, oldDict, newDict):
    if valueName in oldDict:
        newDict[valueName] = oldDict[valueName]
    return newDict


def doTokenList(tokenList, token, newList):
    punctuationSet = {",", ".", "。", "？", "?", ";", "!"}
    if len(tokenList) == 0:
        return newList
    elif tokenList[0] in punctuationSet: #not isChinese(tokenList[0]):
        punctuation = tokenList[0] + " "
        newList.append(punctuation)
        return doTokenList(tokenList[1:], token, newList)
    elif tokenList[0] == token:
        tokenWithBraces = " [" + token + "] "
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


def subcard(token, sharedData, index, pinyinList, tokenList, sentence):
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

    backsideAndSecondaryInfo = sharedData.split(globalParagraphSeparator)
    res = {
        "cardNumber": 0,
        "cardName": "sentenceNo:" + str(index + 1),
        "frontSide": " ".join(convertedPinyin),
        "backSide": tokentListToBacksideSentence(tokenList, token), # instead of just using token + sentence, i will try to join the tokentlist,
        "primaryInfo": backsideAndSecondaryInfo[0],
        "secondaryInfo": globalParagraphSeparator.join(backsideAndSecondaryInfo[1:]),
        "notableCards": [],
        "dateOfLastReview": "2000-01-01",
        "repetitionValue": 1,
        "repetitionHistory": [],
        "tags": generateTags
    }
    return res


def subcardForWholeSentence(sharedData, index, pinyinList, tokenList, sentence):
    # write a function that surrounds pinyin with curly
    generateTags = ["sentenceNo:" + str(index + 1), "onlySentence:" + str(index + 1)]
    backsideAndSecondaryInfo = sharedData.split(globalParagraphSeparator)
    res = {
        "cardNumber": 0,
        "cardName": "sentenceNo:" + str(index + 1),
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


def convertSentenceToCardOnlySimplified(sen, prevSen, nextSen, index, tokenList):
    output = sharedSentenceData(nextSen, prevSen, sen)
    cardList = [subcard(token, output, index, sen.get("pinyin"), sen.get("simplified"), sen.get("sentence")) for token in tokenList]
    cardForWholeSentence = subcardForWholeSentence(output, index, sen.get("pinyin"), sen.get("simplified"), sen.get("sentence"))
    cardList.append(cardForWholeSentence)
    return cardList

def sharedSentenceData(nextSen, prevSen, sen):
    output = ""
    tokenDataString = sentenceTokenDataOnlySimplified(sen, False)
    companionStr = ""
    if prevSen == None and not nextSen == None:
        companionStr = "next Sentence:" \
                       + globalLineSeparator \
                       + sentenceTokenDataOnlySimplified(nextSen, True)
    elif nextSen == None and not prevSen == None:
        companionStr = "previous Sentence:"\
                       + globalLineSeparator     \
                       + sentenceTokenDataOnlySimplified(prevSen, True)
    elif not nextSen == None and not prevSen == None:
        companionStr = "previous Sentence:"\
                       + globalLineSeparator  \
                       + sentenceTokenDataOnlySimplified(prevSen, True) \
                       + globalParagraphSeparator \
                       + "next Sentence:" \
                       + globalLineSeparator \
                       + sentenceTokenDataOnlySimplified(nextSen, True)
    else:
        return tokenDataString
    output = tokenDataString + globalParagraphSeparator + companionStr
    return output


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
    bclu = sen.get("bcluFrequency")
    Hsimp = sen.get("heisigSimplified")
    # Htrad = sen.get("heisigTraditional")
    tokenData = []
    for x in range(len(tokens)):
        generated = generateTokenDataOnlySimplified(tokens[x], pinyin[x], meaning[x], hsk[x], bclu[x], Hsimp[x])
        tokenData.append(generated)
    res = globalLineSeparator.join(tokenData)
    if not sentenceInFront == "":
        res = sentenceInFront + globalLineSeparator + res
    return res

def generateTokenDataOnlySimplified(token, pinyin, meaning, hsk, bclu, heisig):
    values = [token, pinyin, meaning, hsk, bclu, heisig]
    convNone = lambda i: str(i) if i else "nil"
    resultStr = [convNone(i) for i in values]
    result = resultStr[0] + " " + resultStr[1] + " " + resultStr[2] + globalLineSeparator + "heisig:" + resultStr[5] + " hsk:" + resultStr[3] + " bclu:"  + resultStr[4]
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

def convertSentencesToCardsSimplified(outputLines):
    uniqueTokens = getNestedUniqueList([x.get("simplified") for x in outputLines], [], len(outputLines), set())

    result = []
    for i in range(len(outputLines)):
        if i is 0:
            current = outputLines[i]
            next = outputLines[i+1] if len(outputLines) > i+1 else None
            card = convertSentenceToCardOnlySimplified(current, None, next, i, uniqueTokens[i])
            result.append(card)
        elif i is len(outputLines) - 1:
            current = outputLines[i]
            prev = outputLines[i-1]
            card = convertSentenceToCardOnlySimplified(current, prev, None, i, uniqueTokens[i])
            result.append(card)
        else:
            current = outputLines[i]
            prev = outputLines[i-1]
            next = outputLines[i+1] if len(outputLines) > i+1 else None
            card = convertSentenceToCardOnlySimplified(current, prev, next, i, uniqueTokens[i])
            result.append(card)
    return result

    #configurations
    #traditional data, simplified data, traditional first then simplified, simplified first then traditional
    # (how it is done depends on witch script the original script is in)
    #word cards only, sentencecards only, words and sentencecards
    #tags: the word cards, the sentencecards and the deck title will become tags

    #if no configs == only simplified data and both words and sentences

    #TODO: skal ordne text til simplified

def convertAnalysisDictToMiningDict(analysisDict):
    resultDict = {}
    resultDict = addValueToDict("deckName", analysisDict, resultDict)
    resultDict = addValueToDict("deckInfo", analysisDict, resultDict)
    resultDict = addValueToDict("script", analysisDict, resultDict)

    outputLines = getValueFromDictionary("output", analysisDict)
    if outputLines is None or outputLines is []:
        return resultDict
    else:
        cards = convertSentencesToCardsSimplified(outputLines)
        flatCArds = [element for innerList in cards for element in innerList]
        for x in range(len(flatCArds)):
            eachcard = flatCArds[x]
            eachcard["cardNumber"] = x + 1


        tagsList = getAllTagsFromCards(flatCArds)
        res = {tagsList[i]: tagsList[i] for i in range(len(tagsList))}
        resultDict["cards"] = flatCArds
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
