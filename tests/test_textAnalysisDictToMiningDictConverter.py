import pytest
import src.Services.textAnalysisDictToMiningDictConverter as Converter
import src.Controllers.appController
from src.Services.utilityService import isChinese


def input_jsonSimpNews():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   cntext = """12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行。"""
   jsondict = {
      "deckName": "jsonSimplifiedNews",
      "deckInfo": "simplifiedNewsInfo",
      "tags": {"tag1": "tagVal1"},
      "script": "simplified",
      "text": cntext
   }
   return jsondict

def input_jsonSimpNews_missingField():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   cntext = """12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行。"""
   jsondict = {
      #"deckName": "jsonSimplifiedNews",
      #"deckInfo": "simplifiedNewsInfo",
      #"tags": {"tag1": "tagVal1"},
      "script": "simplified",
      "text": cntext
   }
   return jsondict

def createFaultyTestData():
    news = input_jsonSimpNews_missingField()
    outputDict = src.Controllers.appController.postendpoint(news)
    return outputDict

def createTestData():
    news = input_jsonSimpNews()
    outputDict = src.Controllers.appController.postendpoint(news)
    return outputDict

def createSmallSimpTestData():
    jsondict = {
        "deckName": "jsonSimplifiedNews",
        "deckInfo": "simplifiedNewsInfo",
        "script": "simplified",
        "text": "竹北市户政事. 务所日12日涌入。"
    }
    outputDict = src.Controllers.appController.postendpoint(jsondict)
    return outputDict

def createSmallTradTestData():
    jsondict = {
        "deckName": "jsonTraditionalNews",
        "deckInfo": "traditionalNewsInfo",
        "script": "traditional",
        "text": "竹北市戶政事. 務所日12日湧入。"
    }
    outputDict = src.Controllers.appController.postendpoint(jsondict)
    return outputDict

def createMoreComplexSimpTestData():
    jsondict = {
        "deckName": "jsonSimplifiedNews",
        "deckInfo": "simplifiedNewsInfo",
        "script": "simplified",
        "text": "中世纪时犹太学者为希伯来语的4字神名标。"
    }
    outputDict = src.Controllers.appController.postendpoint(jsondict)
    return outputDict


def test_convertAnalysisDictToMiningDict_missingValue():
    analysisDict = createFaultyTestData()
    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    assert res["deckInfo"] == 'text json is missing either of the following: [deckName, deckInfo, script, text]'

    #assert not "cards" in res
    #assert not "deckName" in res
    #assert not "deckInfo" in res
    #assert not "tags" in res

def test_convertAnalysisDictToMiningDict_doesntTestCards():
    analysisDict = createTestData()
    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    deckName = res.get("deckName")
    assert deckName == "jsonSimplifiedNews"
    deckInfo = res.get("deckInfo")
    assert deckInfo == "simplifiedNewsInfo"
    cards = res["cards"]
    assert len(cards) == 85
    firstCard = cards[0]
    assert not firstCard == None

def test_convertDictionarySentenceToCard_targetSimplied():
    analysisDict = createSmallSimpTestData()
    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    output = res.get("cards")
    assert len(output) == 10

def test_convertDictionarySentenceToCard_targetTraditional_shortText():
    analysisDict = createSmallTradTestData()
    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    output = res.get("cards")
    assert len(output) == 10

def test_convertDictionarySentenceToCard_targetSimplied_moreComplex():
    analysisDict = createMoreComplexSimpTestData()
    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    output = res.get("cards")
    assert len(output) == 12

def test_convertDictionarySentenceToCard_targetTraditional():
    #configurations
    #traditional data, simplified data, traditional first then simplified, simplified first then traditional
    # (how it is done depends on witch script the original script is in)
    #word cards only, sentencecards only, words and sentencecards
    #tags: the word cards, the sentencecards and the deck title will become tags

    #if no configs == only simplified data and both words and sentences

    analysisDict = createSmallTradTestData()
    output = analysisDict.get("output")
    allUniqueTokens = set()
    allUniqueTokens.update(output[0].get("tokens"))
    allUniqueTokens.update(output[1].get("tokens"))
    #allUniqueTokens.update(output[2].get("tokens"))
    #allUniqueTokens.update(output[3].get("tokens"))
    chineseWords = set(filter(isChinese, allUniqueTokens))

    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    cards = res.get("cards")

    #number of cards == number of sentences + number of unique tokens containing chinese characters
    assert len(cards) == len(output) + len(chineseWords)

    #four sentenceCards and
    firstCard = cards[0]

    assert firstCard.get("cardNumber") == 1
    assert firstCard.get("cardName") == "sentenceNo:1"
    assert firstCard.get("frontSide") == '[[Zhu2Bei3]] Shi4 Hu4 Zheng4Shi4 .'
    assert firstCard.get("backSide") == '[[竹北]] 市戶政事.'
    assert firstCard.get("tokenbclu") == [None]


    #last four cards == front side is chinese character
    fifthCard = cards[4]
    assert fifthCard.get("cardNumber") == 5
    assert fifthCard.get("cardName") == 'sentenceNo:1'
    assert fifthCard.get("frontSide") == 'Zhu2Bei3 Shi4 Hu4 Zheng4Shi4 .'
    assert fifthCard.get("backSide") == '竹北市戶政事.'
    assert fifthCard.get("tokenbclu") == [None, 146, 947, 23396, None]

    assert cards[8].get("backSide") == '務所日12日 [[湧入]] 。'
    assert cards[8].get("tokenbclu") == [12236]
    assert cards[9].get("backSide") == '務所日12日湧入。'
    assert cards[9].get("tokenbclu") == [4450, 108, 29, None, 29, 12236, None]


def test_convertDictionarySentenceToCard_targetSimnplified():
    #configurations
    #traditional data, simplified data, traditional first then simplified, simplified first then traditional
    # (how it is done depends on witch script the original script is in)
    #word cards only, sentencecards only, words and sentencecards
    #tags: the word cards, the sentencecards and the deck title will become tags

    #if no configs == only simplified data and both words and sentences

    analysisDict = createSmallSimpTestData()
    output = analysisDict.get("output")
    allUniqueTokens = set()
    allUniqueTokens.update(output[0].get("tokens"))
    allUniqueTokens.update(output[1].get("tokens"))
    #allUniqueTokens.update(output[2].get("tokens"))
    #allUniqueTokens.update(output[3].get("tokens"))
    chineseWords = set(filter(isChinese, allUniqueTokens))

    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    cards = res.get("cards")

    #number of cards == number of sentences + number of unique tokens containing chinese characters
    assert len(cards) == len(output) + len(chineseWords)

    #four sentenceCards and
    firstCard = cards[0]

    assert firstCard.get("cardNumber") == 1
    assert firstCard.get("cardName") == "sentenceNo:1"
    assert firstCard.get("frontSide") == '[[Zhu2Bei3]] Shi4 Hu4 Zheng4Shi4 .'
    assert firstCard.get("backSide") == '[[竹北]] 市户政事.'
    assert firstCard.get("tokenbclu") == [None]

    #last four cards == front side is chinese character
    fifthCard = cards[4]
    assert fifthCard.get("cardNumber") == 5
    assert fifthCard.get("cardName") == 'sentenceNo:1'
    assert fifthCard.get("frontSide") == 'Zhu2Bei3 Shi4 Hu4 Zheng4Shi4 .'
    assert fifthCard.get("backSide") == '竹北市户政事.'
    assert fifthCard.get("tokenbclu") == [None, 146, 947, 23396, None]

    assert cards[8].get("backSide") == '务所日12日 [[涌入]] 。'
    assert cards[8].get("tokenbclu") == [12236]
    assert cards[9].get("backSide") == '务所日12日涌入。'
    assert cards[9].get("tokenbclu") == [4450, 108, 29, None, 29, 12236, None]









