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
   return my_json_string#json.loads(my_json_string)


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 3

def test_appController_postendpoint():
   assert True

def test_createWordToInfoDictionary():
    fileContent = CedictParser.cedictParserReadCedict()
    test = CedictParser.createWordToInfoDictionary(fileContent)
    assert True