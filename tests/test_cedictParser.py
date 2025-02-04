import pytest
from src.libraryInterface import CedictParser

def test_wordToSimplifiedTrad():
    # when
    CedictParser.initCedictParser()
    nonChinese = CedictParser.wordToSimplifiedTrad(",")
    nullarg = CedictParser.wordToSimplifiedTrad(None)
    sim = CedictParser.wordToSimplifiedTrad('來賓')
    assert nonChinese == ","
    assert nullarg == ""
    assert sim == '来宾'

def test_wordToTraditionalSimp():
    # when
    CedictParser.initCedictParser()
    nonChinese = CedictParser.wordToTraditionalFromSimp(",")
    nullarg = CedictParser.wordToTraditionalFromSimp(None)
    sim = CedictParser.wordToTraditionalFromSimp('亩')
    assert nonChinese == ","
    assert nullarg == ""
    assert sim == '畝|畂|畆|畮'

def test_wordToMeaningSimp():
    # when
    CedictParser.initCedictParser()
    nonChinese = CedictParser.wordToMeaningSimp(",")
    nullarg = CedictParser.wordToMeaningSimp(None)
    sim = CedictParser.wordToMeaningSimp('亩')
    assert nonChinese == ","
    assert nullarg == ""
    assert sim == '/classifier for fields/unit of area equal to one fifteenth of a hectare/|/old variant of 畝|亩[mu3]/|/old variant of 畝|亩[mu3]/|/old variant of 畝|亩[mu3]/'


def test_wordToMeaningTrad():
    # when
    CedictParser.initCedictParser()
    nonChinese = CedictParser.wordToMeaningTrad(",")
    nullarg = CedictParser.wordToMeaningTrad(None)
    sim = CedictParser.wordToMeaningTrad('不是')
    assert nonChinese == ","
    assert nullarg == ""
    assert sim == '/fault/blame/|/no/is not/not/'

def test_wordToPinyinSimp():
    # when
    CedictParser.initCedictParser()
    nonChinese = CedictParser.wordToPinyinSimp(",")
    nullarg = CedictParser.wordToPinyinSimp(None)
    sim = CedictParser.wordToPinyinSimp('亩')
    assert nonChinese == ","
    assert nullarg == ""
    assert sim == "Mu3"

def test_wordToPinyinTrad():
    # when
    CedictParser.initCedictParser()
    nonChinese = CedictParser.wordToPinyinTrad(",")
    nullarg = CedictParser.wordToPinyinTrad(None)
    tra = CedictParser.wordToPinyinTrad('不是')
    assert nonChinese == ","
    assert nullarg == ""
    assert tra == "Bu2Shi5|Bu4Shi4"

def test_initCedictParser():
    #given
    #when
    CedictParser.initCedictParser()
    trad = CedictParser.getCedictTradDict()
    simp = CedictParser.getCedictSimpDict()
    #then
    assert len(trad) == 119084 #keys = traditional character
    assert len(simp) == 117956 #keys = simplified character

    test = [x for x in trad.values() if len(x) > 1]

    lai2bin1word = trad.get('來賓')
    assert len(lai2bin1word) == 2
    assert lai2bin1word[0].get('simplified') == '来宾'
    assert lai2bin1word[0].get('pinyin') == 'Lai2Bin1'
    assert lai2bin1word[0].get('meaning') == '/Laibin prefecture-level city in Guangxi/'
    assert lai2bin1word[1].get('meaning') == '/guest/visitor/'

    mu3Character = simp.get('亩')
    assert len(mu3Character) == 4
    assert mu3Character[0].get('traditional') == '畂'
    assert mu3Character[1].get('traditional') == '畆'
    assert mu3Character[2].get('traditional') == '畝'
    assert mu3Character[3].get('traditional') == '畮'
    assert mu3Character[2].get('simplified') == '亩'
    assert mu3Character[2].get('pinyin') == 'Mu3'
    assert mu3Character[2].get('meaning') == '/classifier for fields/unit of area equal to one fifteenth of a hectare/'

def test_cedictDictionariesFromRawFileContent():
    #given
    fileContent = CedictParser.readCedictContentFromCedictReader()
    filelines = fileContent.split('\n')
    #when
    withoutComments = CedictParser.removeCommentLinesFromCedict(filelines)
    finishedDictionaries = CedictParser.cedictDictionariesFromRawFileContent(fileContent)
    #then
    assert len(withoutComments) == 121426         #all lines in dictionary
    assert len(finishedDictionaries.get("traditionalDict")) == 119084 #keys = traditional characters
    assert len(finishedDictionaries.get("simplifiedDict")) == 117956 #keys = simplified characters

    trad = finishedDictionaries.get("traditionalDict")
    simp = finishedDictionaries.get("simplifiedDict")

    lai2bin1word = trad.get('來賓')
    assert len(lai2bin1word) == 2
    assert lai2bin1word[0].get('simplified') == '来宾'
    assert lai2bin1word[0].get('pinyin') == 'Lai2Bin1'
    assert lai2bin1word[0].get('meaning') == '/Laibin prefecture-level city in Guangxi/'
    assert lai2bin1word[1].get('meaning') == '/guest/visitor/'

    mu3Character = simp.get('亩')
    assert len(mu3Character) == 4
    assert mu3Character[0].get('traditional') == '畂'
    assert mu3Character[1].get('traditional') == '畆'
    assert mu3Character[2].get('traditional') == '畝'
    assert mu3Character[3].get('traditional') == '畮'
    assert mu3Character[2].get('simplified') == '亩'
    assert mu3Character[2].get('pinyin') == 'Mu3'
    assert mu3Character[2].get('meaning') == '/classifier for fields/unit of area equal to one fifteenth of a hectare/'


