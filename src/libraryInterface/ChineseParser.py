from chinese import ChineseAnalyzer

def initChineseParser():
    global parser
    parser = ChineseAnalyzer()

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
    anal = parser.parse(inputTest)
    sent = anal.sentences()
    trimmedSen = [x.strip() for x in sent]
    return trimmedSen

def getTokensFromSentence(sentence):
    """
    :param sentence: a string consisting of a single chinese sentences or small string of text. Example:
     '昆铁路'
    :return: a list of words/tokens contained in the text. Example:
    ['昆', '铁路']
    """
    tokenList = ' '.join(parser.parse(sentence).tokens()).split()
    return tokenList

def getPinyinStringFromSentence(text):
    """
    :param text: a string consisting of a single chinese sentences or small string of text. Example:
    '12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验'
    :return: a string of pinyin generated from the text. each ward is space separated. Example:
    '12 yuè 23 Rì ,   Zhōngguó tiělù Chéngdū jú 集团公司 zǔzhī méitǐ tíqián shìchéng Xīn 成昆铁路 ,   gǎnshòu jíjiāng dàolái de shíkōng 新体验'
    """
    pinyinStr = parser.parse(text).pinyin()
    return pinyinStr


