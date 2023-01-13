import pytest
from src.libraryInterface import ChineseLibParser
from src.libraryInterface import CedictParser

def test_sentenceToTokens():
   ChineseLibParser.initChineseLibParser()
   sent = "记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相"
   basicTokens = ChineseLibParser.getTokensFromSimplifiedSentence(sent)
   assert basicTokens == ['记者', '在', '现场', '获悉', ',', '新', '成', '昆', '铁路', '将', '采用', '第', '三代', 'C', '型', "CR200J'", '复兴', '号', "'", '动车', '组', '值', '乘', ',', '这', '也', '是', '该', '车', '型', '首次', '正式', '亮相']

def test_simplified_parseWordByCedict_basicUnsplitWord():
   ChineseLibParser.initChineseLibParser()
   CedictParser.initCedictParser()
   cedict = CedictParser.getCedictSimpDict()
   word = '现场成昆铁路'
   tokens = ChineseLibParser.parseWordByCedict(word, "", [], cedict)
   assert tokens == ['现场', '成', '昆', '铁路']

def test_simplified_parseWordByCedict_stringWithNonHanCharacters():
   ChineseLibParser.initChineseLibParser()
   CedictParser.initCedictParser()
   cedict = CedictParser.getCedictSimpDict()
   word = '现场3$成昆铁路'
   tokens = ChineseLibParser.parseWordByCedict(word, "", [], cedict)
   assert tokens == ['现场', '3', '$', '成', '昆', '铁路']