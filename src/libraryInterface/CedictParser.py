from pathlib import Path
import re
from src.resources import cedictReader


# def initChineseParser():
#     global parser
#     parser =
def cedictParserReadCedict():
    return cedictReader.readCedictFile()


def removeCommentLinesFromCedict(filelines):
    noComments = [x for x in filelines if not (x.startswith("# ") or x.startswith("#!"))]
    return noComments

def isCommentLine(cedictLine):
    if cedictLine[:2] == "# ":
        True
    elif cedictLine[:2] == "#!":
        True
    else:
        False



def lineToList(stringLine):
    firstSplit = stringLine.split(" ", 1)
    secondSplit = firstSplit[1].split("[", 1)
    thirdSplit = secondSplit[1].split("]", 1)

    #improve pinyin handling by joining strings
    #betterPinyin =

    return [firstSplit[0],
            secondSplit[0].strip(),
            thirdSplit[0],
            thirdSplit[1].strip()]


def testfunc(withoutComments):
    resultObj = map(lineToList, withoutComments)
    res = list(resultObj)
    return res


def createWordToInfoDictionary(cedictContent):
    filelines = cedictContent.split('\n')
    withoutComments = removeCommentLinesFromCedict(filelines)
    toNestedList = testfunc(withoutComments)
    return {"kin":"value"}

