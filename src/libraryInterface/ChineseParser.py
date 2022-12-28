from chinese import ChineseAnalyzer

def initChineseParser():
    global parser
    parser = ChineseAnalyzer()

def getSentences(inputTest):
    anal = parser.parse(inputTest)
    sent = anal.sentences()
    return sent

def getTokensFromSentence(sentence):
    tokenList = ' '.join(parser.parse(sentence).tokens()).split()
    return tokenList

def getTokenListFromSentence(sentence):
    res = parser.parse(sentence).tokens()
    return res

def getPinyinStringFromWord(text):
    pinyinStr = parser.parse(text).pinyin()
    return pinyinStr

def getPinyinFromSentence(sentence):
    basicPinyin = parser.parse(sentence).pinyin().split()
    return basicPinyin



