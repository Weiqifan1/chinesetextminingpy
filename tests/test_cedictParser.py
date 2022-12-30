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

def test_cedictDictionariesFromRawFileContent():
    #given
    fileContent = CedictParser.readCedictContentFromCedictReader()
    filelines = fileContent.split('\n')
    #when
    withoutComments = CedictParser.removeCommentLinesFromCedict(filelines)
    finishedDictionaries = CedictParser.cedictDictionariesFromRawFileContent(fileContent)
    #then
    assert len(withoutComments) == 121426         #all lines in dictionary
    assert len(finishedDictionaries[0]) == 119084 #keys = traditional characters
    assert len(finishedDictionaries[1]) == 117956 #keys = simplified characters



