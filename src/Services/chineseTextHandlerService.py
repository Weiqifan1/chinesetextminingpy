from src.libraryInterface import ChineseLibParser
from src.libraryInterface import CedictParser
from src.libraryInterface import HeisigParser
from src.libraryInterface import HskParser
from src.libraryInterface import BcluParser

def sentenceToDict(sen):
    return sen

def textToTokensFromSimplified(text):
    print("dette er en print")
    ChineseLibParser.initChineseLibParser()
    print("chineselib har koert")
    # CedictParser.initCedictParser()
    # HeisigParser.initHeisigParser()
    #HskParser.initHskParser()
    # BcluParser.initBCLUDictionary()
    test2 = ChineseLibParser.getSentencesFromLargeText(text)
    result = [senToDictFromSimplified(x) for x in test2]
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

def senToDictFromSimplified(sent):
    tokens = ChineseLibParser.getTokensFromSentence(sent)
    # traditional = [CedictParser.wordToTraditionalSimp(x) for x in tokens]
    # pinyinList = [CedictParser.wordToPinyinSimp(x) for x in tokens]
    # meaningList = [CedictParser.wordToMeaningSimp(x) for x in tokens]
    # heisigSimplified = [HeisigParser.getHeisigStringFromWordSimp(x) for x in tokens]
    # heisigSimpInt = [HeisigParser.getHeisigIntsFromWordSimp(x) for x in tokens]
    # heisigSimpIntFlatten = [*heisigSimpInt]
    # heisigTraditional = [HeisigParser.getHeisigStringFromWordTrad(x) for x in traditional]
    # heisigTradInt = [HeisigParser.getHeisigIntsFromWordTrad(x) for x in traditional]
    # heisigTradIntFlatten = [*heisigTradInt]
    #hskLevel = [HskParser.getHskLevel(x) for x in tokens]
    # bclu = [BcluParser.getBCLUfrequency(x) for x in tokens]
    mydict = {
        "sentence": sent,
        "tokens": tokens,
        "simplified": tokens,
        # "traditional": traditional,
        # "pinyin": pinyinList,
        # "meaning": meaningList,
        #"hskLevel": hskLevel,
        # "bcluFrequency": bclu,
        # "heisigSimplified": heisigSimplified,
        # "heisigSimpInt" : heisigSimpIntFlatten,
        # "heisigTraditional": heisigTraditional,
        # "heisigTradInt": heisigTradIntFlatten
    }
    return mydict



