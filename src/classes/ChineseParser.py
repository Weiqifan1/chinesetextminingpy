from chinese import ChineseAnalyzer

class ChineseParser:
    def __init__(self):
        self.chineseLib = ChineseAnalyzer()

    def getSentences(self, inputTest):
        anal = self.chineseLib.parse(inputTest)
        sent = anal.sentences()
        return sent

    def getTokensFromSentence(self, sentence):
        tokenList = ' '.join(self.chineseLib.parse(sentence).tokens()).split()
        return tokenList

    def getTokenListFromSentence(self, sentence):
        res = self.chineseLib.parse(sentence).tokens()
        return res

    def getPinyinStringFromWord(self, text):
        pinyinStr = self.chineseLib.parse(text).pinyin()
        return pinyinStr

    def getPinyinFromSentence(self, sentence):
        basicPinyin = self.chineseLib.parse(sentence).pinyin().split()
        return basicPinyin



