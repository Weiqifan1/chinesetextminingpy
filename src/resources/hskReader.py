
from pathlib import Path
import json
from src.libraryInterface import CedictParser
from src.resources import hskReader

def doReadHsk(title):
    base_path = Path(__file__).parent
    pathString = "../resources/" + title + ".txt"
    finpath = (base_path / pathString).resolve()
    loktest = open(finpath, "r", encoding="utf8").read()
    return loktest

def doWriteDictionaryToFile(file, title):
    pathString = title + ".json"
    out_file = open(pathString, "w", encoding="utf8")
    json.dump(file, out_file)
    out_file.close()


def doReadDictionaryFromFile(title):
    pathString = "../resources/" + title + ".json"
    base_path = Path(__file__).parent
    finpath = (base_path / pathString).resolve()
    #pathString = title + ".json"
    retdict = {}
    with open(finpath, "r") as f:
        jsonstr = f.read()
        retdict = json.loads(jsonstr)
    f.close()
    return retdict

def readbclu():
    fullBclu = doReadHsk("BLCU2018freqcorpus")
    return fullBclu

def readHskFiles():
    hsk1 = doReadHsk("hsk1raw")
    hsk2 = doReadHsk("hsk2raw")
    hsk3 = doReadHsk("hsk3raw")
    hsk4 = doReadHsk("hsk4raw")
    hsk5 = doReadHsk("hsk5raw")
    hsk6 = doReadHsk("hsk6raw")
    return {"hsk1" : hsk1,
            "hsk2" : hsk2,
            "hsk3" : hsk3,
            "hsk4" : hsk4,
            "hsk5" : hsk5,
            "hsk6" : hsk6}

def createBCLU_cedict_intersection():
    # create, save, and read a dictionary that is the intersection of
    # BCC (BLCU Chinese Corpus)  https://www.plecoforums.com/threads/word-frequency-list-based-on-a-15-billion-character-corpus-bcc-blcu-chinese-corpus.5859/
    # and the cedict open dictionary.
    # this code requires that bclu corpus get downloaded and saved under resources as BLCU2018freqcorpus.txt
    CedictParser.initCedictParser()
    simp = CedictParser.getCedictSimpDict()
    wort = simp.get("附赘悬疣")

    # create a dictionary based on bclu_corpus
    fullBclu = hskReader.readbclu()
    lines = (fullBclu[1:]).split("\n")
    nested = [x.split("\t") for x in lines]

    filterDublicates = remove_duplicatesAndAddIndex(nested, simp)
    last10elem = filterDublicates[-10:]
    bcludict = list_to_dict(filterDublicates)
    readfile = hskReader.doReadDictionaryFromFile("BCLU_Cedict_Intersection")

def list_to_dict(lst):
  result = {}
  for sublist in lst:
    result[sublist[0]] = sublist
  return result

def remove_duplicatesAndAddIndex(lst, dict):
  keys = set()
  result = []
  index = 1
  value = ""
  for sublist in lst:
    if sublist[0] not in keys and sublist[0] in dict:
      value = [sublist[0], index, sublist[1]]
      keys.add(sublist[0])
      result.append(value)
      index = index + 1
  return result
