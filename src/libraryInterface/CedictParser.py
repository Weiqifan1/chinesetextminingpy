from pathlib import Path

from src.resources import cedictReader


# def initChineseParser():
#     global parser
#     parser =


def createWordToInfoDictionary():
    #test = readCedict()
    # data = Path("resources")
    # file = data / "cedict20221227.txt"
    # f = open(file)
    # text = open("resources/cedict20221227.txt", "r")
    test = cedictReader.readCedictFile()
    return {"kin":"value"}

# def readCedict():
#     text = open("demofile.txt", "r")

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 3

