import re
from src.Services import chineseTextHandlerService
from src.Services import textAnalysisDictToMiningDictConverter

def texttovocab(postinput):
    res = postendpoint(postinput)
    allItems = list(map(lambda each: each["tokens"], res["output"]))
    vocabFromCards = chineseTextHandlerService.vocabFromSentences(allItems, res["script"])
    resultDict = {}
    resultDict["output"] = vocabFromCards
    return resultDict

def postendpoint(postinput):
    validated = validateTextToAnalysisDict(postinput)
    if not validated:
        return {"deckInfo": "text json is missing either of the following: [deckName, deckInfo, script, cardOrder, textType, text, vocab, sentencenames]"}
    print("print start")
    sentences = []
    sentencenames = []
    resultDict = {}
    resultDict["deckName"] = postinput["deckName"]
    resultDict["deckInfo"] = postinput["deckInfo"]
    resultDict["script"] = postinput["script"]
    resultDict["cardOrder"] = postinput["cardOrder"]

    if not "text" in postinput or not "script" in postinput:
        return resultDict
    gettextdata = postinput["text"]
    scriptvalue = postinput["script"]
    textType = postinput["textType"]

    if scriptvalue == "simplified":
        (sentences, sentencenames) = chineseTextHandlerService.textToTokensFromSimplified(gettextdata, textType)
    elif scriptvalue == "traditional":
        (sentences, sentencenames) = chineseTextHandlerService.textToTokensFromTraditional(gettextdata, textType)
    else:
        sentences = []
        sentencenames = []
    resultDict["output"] = sentences
    resultDict["vocab"] = postinput["vocab"]
    resultDict["sentencenames"] = sentencenames
    resultDict["textType"] = postinput["textType"]
    return resultDict

def postendpointToDeck(postnedpointOutput):
    validated = validateAnalysisDict(postnedpointOutput)
    if not validated:
        return {"deckInfo": "missing either of the following: [deckName, deckInfo, script, output, vocab, sentencenames]"}
    deck = textAnalysisDictToMiningDictConverter.convertAnalysisDictToMiningDict(postnedpointOutput)
    return deck

def validateTextToVocab(postinput):
    valid = True
    keylist = ["textVocab"]
    for x in keylist:
        if not x in postinput:
            valid = False
        if postinput.get(x) is None:
            valid = False
    return valid

def validateTextToAnalysisDict(postinput):
    valid = True
    keylist = ["deckName", "deckInfo", "script", "cardOrder", "textType", "text", "vocab", "sentencenames"]
    for x in keylist:
        if not x in postinput:
            valid = False
        if postinput.get(x) is None:
            valid = False
    return valid


def validateAnalysisDict(analysisDict):
    valid = True
    keylist = ["deckName", "deckInfo", "output", "script", "sentencenames"]
    for x in keylist:
        if not x in analysisDict:
            valid = False
        if analysisDict.get(x) is None:
            valid = False
    return valid


def addValueToDict(valueName, oldDict, newDict):
    if valueName in oldDict:
        newDict[valueName] = oldDict[valueName]
    return newDict

def getValueFromDictionary(key, dictionary):
    if key in dictionary:
        return dictionary[key]
    else:
        return None