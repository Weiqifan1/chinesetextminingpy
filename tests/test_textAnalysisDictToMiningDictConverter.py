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
      "cardOrder": "chronological",
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
      #"cardOrder": "chronological",
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
        "cardOrder": "chronological",
        "text": "竹北市户政事. 务所日12日涌入。"
    }
    outputDict = src.Controllers.appController.postendpoint(jsondict)
    return outputDict

def createWikiSimpTestData():
    #中华人民共和国，简称中国[註 13][17][2]，是一个位於东亚的社会主义国家[18]，成立于1949年10月1日，
    jsondict = {
        "deckName": "jsonSimplifiedNews",
        "deckInfo": "simplifiedNewsInfo",
        "script": "simplified",
        "cardOrder": "chronological",
        "text": "中华人民共和国，简称中国[註 13][17][2]，是一个位於东亚的社会主义国家[18]，成立于1949年10月1日，"
    }
    outputDict = src.Controllers.appController.postendpoint(jsondict)
    return outputDict

def createWikiSimpTestData_byFrequency():
    #中华人民共和国，简称中国[註 13][17][2]，是一个位於东亚的社会主义国家[18]，成立于1949年10月1日，
    jsondict = {
        "deckName": "jsonSimplifiedNews",
        "deckInfo": "simplifiedNewsInfo",
        "script": "simplified",
        "cardOrder": "frequency",
        "text": "中华人民共和国，简称中国[註 13][17][2]，是一个位於东亚的社会主义国家[18]，成立于1949年10月1日，"
    }
    outputDict = src.Controllers.appController.postendpoint(jsondict)
    return outputDict

def createSmallTradTestData():
    jsondict = {
        "deckName": "jsonTraditionalNews",
        "deckInfo": "traditionalNewsInfo",
        "script": "traditional",
        "cardOrder": "chronological",
        "text": "竹北市戶政事. 務所日12日湧入。"
    }
    outputDict = src.Controllers.appController.postendpoint(jsondict)
    return outputDict

def createMoreComplexSimpTestData():
    jsondict = {
        "deckName": "jsonSimplifiedNews",
        "deckInfo": "simplifiedNewsInfo",
        "script": "simplified",
        "cardOrder": "chronological",
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
    assert res.get("tags") == {'onlySentence:2': 'onlySentence:2', 'sentenceNo:1': 'sentenceNo:1', 'onlySentence:1': 'onlySentence:1', 'jsonTraditionalNews': 'traditionalNewsInfo', 'firstInSentence': 'firstInSentence', 'sentenceNo:2': 'sentenceNo:2'}

    #four sentenceCards and
    firstCard = cards[0]

    assert firstCard.get("cardNumber") == 1
    assert firstCard.get("cardName") == "sentenceNo:1"
    assert firstCard.get("frontSide") == '[[Zhu2Bei3]] Shi4 Hu4 Zheng4Shi4 .'
    assert firstCard.get("backSide") == '[[竹北]] 市戶政事.'
    assert firstCard.get("primaryInfo") == trad_primary_example()
    assert firstCard.get("secondaryInfo") == trad_secondary_example()
    assert firstCard.get("tags") == ['sentenceNo:1', 'firstInSentence', 'jsonTraditionalNews']
    #assert firstCard.get("tokenblcu") == [None]

    #last four cards == front side is chinese character
    fifthCard = cards[4]
    assert fifthCard.get("cardNumber") == 5
    assert fifthCard.get("cardName") == 'sentenceNo:2'
    assert fifthCard.get("frontSide") == '[[Wu4]] Suo3 Ri4 12 Ri4 Yong3Ru4 。'
    assert fifthCard.get("backSide") == '[[務]] 所日12日湧入。'
    assert fifthCard.get("tags") == ['sentenceNo:2', 'firstInSentence', 'jsonTraditionalNews']
    #assert fifthCard.get("tokenblcu") == [None, 146, 947, 23396, None]

    assert cards[8].get("backSide") == '竹北市戶政事.'
    #assert cards[8].get("tokenblcu") == [12236]
    assert cards[9].get("backSide") == '務所日12日湧入。'
    #assert cards[9].get("tokenblcu") == [4450, 108, 29, None, 29, 12236, None]

def trad_primary_example():
    return """竹北 Zhu2Bei3 /Zhubei or Chupei city in Hsinchu County 新竹縣|新竹县[Xin1 zhu2 Xian4], northwest Taiwan/
heisig:728 竹 bamboo 420 北 north hsk:nil blcu:nil
市 Shi4 /market/city/CL:個|个[ge4]/
heisig:388 市 market hsk:nil blcu:146
戶 Hu4 /a household/door/family/
heisig:830 戶 door hsk:nil blcu:947
政事 Zheng4Shi4 /politics/government affairs/
heisig:363 政 politics 878 事 matter hsk:nil blcu:23396
. . .
heisig:nil hsk:nil blcu:nil"""

def trad_secondary_example():
    return """next Sentence:
務所日12日湧入。 
務 Wu4 /affair/business/matter/to be engaged in/to attend to/by all means/
heisig:934 務 tasks hsk:nil blcu:4450
所 Suo3 /actually/place/classifier for houses, small buildings, institutions etc/that which/particle introducing a relative clause or passive/CL:個|个[ge4]/
heisig:857 所 place hsk:hsk5 blcu:108
日 Ri4 /abbr. for 日本[Ri4 ben3], Japan/|/sun/day/date, day of the month/
heisig:12 日 day hsk:hsk2 blcu:29
12 12 12
heisig:nil hsk:nil blcu:nil
日 Ri4 /abbr. for 日本[Ri4 ben3], Japan/|/sun/day/date, day of the month/
heisig:12 日 day hsk:hsk2 blcu:29
湧入 Yong3Ru4 /to come pouring in/influx/
heisig:2378 湧 gush 638 入 enter hsk:nil blcu:12236
。 。 。
heisig:nil hsk:nil blcu:nil"""


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
    assert res.get("tags") == {'jsonSimplifiedNews': 'simplifiedNewsInfo', 'sentenceNo:2': 'sentenceNo:2', 'firstInSentence': 'firstInSentence', 'sentenceNo:1': 'sentenceNo:1', 'onlySentence:1': 'onlySentence:1', 'onlySentence:2': 'onlySentence:2'}

    #four sentenceCards and
    firstCard = cards[0]

    assert firstCard.get("cardNumber") == 1
    assert firstCard.get("cardName") == "sentenceNo:1"
    assert firstCard.get("frontSide") == '[[Zhu2Bei3]] Shi4 Hu4 Zheng4Shi4 .'
    assert firstCard.get("backSide") == '[[竹北]] 市户政事.'
    assert firstCard.get("tags") == ['sentenceNo:1', 'firstInSentence', 'jsonSimplifiedNews']

    #assert firstCard.get("tokenblcu") == [None]

    #last four cards == front side is chinese character
    fifthCard = cards[4]
    assert fifthCard.get("cardNumber") == 5
    assert fifthCard.get("cardName") == 'sentenceNo:2'
    assert fifthCard.get("frontSide") == '[[Wu4]] Suo3 Ri4 12 Ri4 Yong3Ru4 。'
    assert fifthCard.get("backSide") == '[[务]] 所日12日涌入。'
    assert fifthCard.get("tags") == ['sentenceNo:2', 'firstInSentence', 'jsonSimplifiedNews']

    #assert fifthCard.get("tokenblcu") == [None, 146, 947, 23396, None]

    assert cards[8].get("backSide") == '竹北市户政事.'
    #assert cards[8].get("tokenblcu") == [12236]
    assert cards[9].get("backSide") == '务所日12日涌入。'
    #assert cards[9].get("tokenblcu") == [4450, 108, 29, None, 29, 12236, None]

def test_convertDictionarySentenceToCard_targetSimnplified_wikidata():
    #configurations
    #traditional data, simplified data, traditional first then simplified, simplified first then traditional
    # (how it is done depends on witch script the original script is in)
    #word cards only, sentencecards only, words and sentencecards
    #tags: the word cards, the sentencecards and the deck title will become tags

    #if no configs == only simplified data and both words and sentences

    analysisDict = createWikiSimpTestData()
    output = analysisDict.get("output")
    allUniqueTokens = set()
    allUniqueTokens.update(output[0].get("tokens"))
    allUniqueTokens.update(output[1].get("tokens"))
    allUniqueTokens.update(output[2].get("tokens"))
    allUniqueTokens.update(output[3].get("tokens"))
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
    assert firstCard.get("frontSide") == '[[Zhong1Hua2Ren2Min2Gong4He2Guo2]] ，'
    assert firstCard.get("backSide") == '[[中华人民共和国]] ，'
    #assert firstCard.get("tokenblcu") == [3781]

    #last four cards == front side is chinese character
    fifthCard = cards[4]
    assert fifthCard.get("cardNumber") == 5
    assert fifthCard.get("cardName") == 'sentenceNo:3'
    assert fifthCard.get("frontSide") == '[[Shi4]] Yi1 GE Wei4 WU Dong1Ya4 DI She4Hui4Zhu3Yi4 Guo2Jia1 [18]，'
    assert fifthCard.get("backSide") == '[[是]] 一个位於东亚的社会主义国家[18]，'
    #assert fifthCard.get("tokenblcu") == [None]

    assert cards[8].get("backSide") == '是一个位 [[於]] 东亚的社会主义国家[18]，'
    #assert cards[8].get("tokenblcu") == [10]
    assert cards[9].get("backSide") == '是一个位於 [[东亚]] 的社会主义国家[18]，'
    #assert cards[9].get("tokenblcu") == [114]

def test_convertDictionarySentenceToCard_targetSimnplified_wikidata_byFrequency():
    #configurations
    #traditional data, simplified data, traditional first then simplified, simplified first then traditional
    # (how it is done depends on witch script the original script is in)
    #word cards only, sentencecards only, words and sentencecards
    #tags: the word cards, the sentencecards and the deck title will become tags

    #if no configs == only simplified data and both words and sentences

    analysisDict = createWikiSimpTestData_byFrequency()
    output = analysisDict.get("output")
    allUniqueTokens = set()
    allUniqueTokens.update(output[0].get("tokens"))
    allUniqueTokens.update(output[1].get("tokens"))
    allUniqueTokens.update(output[2].get("tokens"))
    allUniqueTokens.update(output[3].get("tokens"))
    #allUniqueTokens.update(output[2].get("tokens"))
    #allUniqueTokens.update(output[3].get("tokens"))
    chineseWords = set(filter(isChinese, allUniqueTokens))

    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    cards = res.get("cards")

    #number of cards == number of sentences + number of unique tokens containing chinese characters
    assert len(cards) == len(output) + len(chineseWords)
    expectedKeys = {'backSide', 'cardName', 'primaryInfo', 'notableCards', 'tags', 'frontSide', 'repetitionValue', 'dateOfLastReview', 'repetitionHistory', 'cardNumber', 'secondaryInfo'}
    allKeys = set().union(*(d.keys() for d in cards))
    assert allKeys == expectedKeys

    #four sentenceCards and
    firstCard = cards[0]

    assert firstCard.get("cardNumber") == 1
    assert firstCard.get("cardName") == 'sentenceNo:3'
    assert firstCard.get("frontSide") == 'Shi4 Yi1 GE Wei4 WU Dong1Ya4 [[DI]] She4Hui4Zhu3Yi4 Guo2Jia1 [18]，'
    assert firstCard.get("backSide") == '是一个位於东亚 [[的]] 社会主义国家[18]，'

    #last four cards == front side is chinese character
    fifthCard = cards[4]
    assert fifthCard.get("cardNumber") == 5
    assert fifthCard.get("cardName") == 'sentenceNo:4'
    assert fifthCard.get("frontSide") == 'Cheng2Li4 Yu2 1949 Nian2 10 Yue4 1 [[Ri4]] ，'
    assert fifthCard.get("backSide") == '成立于1949年10月1 [[日]] ，'

    assert cards[8].get("backSide") == '是一个 [[位]] 於东亚的社会主义国家[18]，'
    assert cards[9].get("backSide") == '是一个位於东亚的社会主义 [[国家]] [18]，'




