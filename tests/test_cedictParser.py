import pytest
from src.libraryInterface import CedictParser

@pytest.fixture
def input_value():
   input = 39
   return input

def input_defaultjson():
   my_json_string = """{
       "text": "lykke"
   }"""
   return my_json_string

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 3

def test_appController_postendpoint():
   assert True

def test_initCedictParser():
    #given
    fileContent = CedictParser.readCedictContentFromCedictReader()
    #when
    CedictParser.initCedictParser(fileContent)
    trad = CedictParser.getCedictTradDict()
    simp = CedictParser.getCedictSimpDict()
    #then
    assert len(trad) == 119084 #keys = traditional character
    assert len(simp) == 117956 #keys = simplified character

    lai2bin1word = trad.get('來賓')
    assert len(lai2bin1word) == 2
    assert lai2bin1word[0].get('simplified') == '来宾'
    assert lai2bin1word[0].get('pinyin') == 'Lai2_Bin1'
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
    assert lai2bin1word[0].get('pinyin') == 'Lai2_Bin1'
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


