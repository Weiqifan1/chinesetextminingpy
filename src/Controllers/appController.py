import re
from src.Services import chineseTextHandlerService
from src.Services import textAnalysisDictToMiningDictConverter


def postendpoint(postinput):
    validated = validateTextToAnalysisDict(postinput)
    if not validated:
        return {"deckInfo": "text json is missing either of the following: [deckName, deckInfo, script, text]"}

    print("print start")
    sentences = []
    output = {}
    resultDict = {}
    resultDict["deckName"] = postinput["deckName"] #addValueToDict("deckName", postinput, output)
    resultDict["deckInfo"] = postinput["deckInfo"]#addValueToDict("deckInfo", postinput, output)
    resultDict["script"] = postinput["script"]
    resultDict["cardOrder"] = postinput["cardOrder"]

    if not "text" in postinput or not "script" in postinput:
        return resultDict
    gettextdata = postinput["text"]
    scriptvalue = postinput["script"]

    betterdata = re.sub("\s+", " ", gettextdata.strip())
    sentences = ""
    if scriptvalue == "simplified":
        sentences = chineseTextHandlerService.textToTokensFromSimplified(betterdata)
    elif scriptvalue == "traditional":
        sentences = chineseTextHandlerService.textToTokensFromTraditional(betterdata)
    else:
        sentences = []
    resultDict["output"] = sentences
    return resultDict

def postendpointToDeck(postnedpointOutput):
    validated = validateAnalysisDict(postnedpointOutput)
    if not validated:
        return {"deckInfo": "missing either of the following: [deckName, deckInfo, script, output]"}
    deck = textAnalysisDictToMiningDictConverter.convertAnalysisDictToMiningDict(postnedpointOutput)
    return deck


def validateTextToAnalysisDict(postinput):
    valid = True
    keylist = ["deckName", "deckInfo", "script", "text"]
    for x in keylist:
        if not x in postinput:
            valid = False
        if postinput.get(x) is None:
            valid = False
    return valid


def validateAnalysisDict(analysisDict):
    valid = True
    keylist = ["deckName", "deckInfo", "output", "script"]
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

