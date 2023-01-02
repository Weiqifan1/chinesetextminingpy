from src.resources import heisigReader

def readHeisigContentFromHeisigReader():
    return heisigReader.readHeisigFile()

def initHeisigParser():
    if 'simplifiedHeisig' in globals() and "traditionalHeisig" in globals() and "kanjiHeisig" in globals():
        pass
    else:
        raw = readHeisigContentFromHeisigReader()
        rawFile = raw.split("\n")
        shorterList = [x.split(',')[0:10] for x in rawFile if len(x.split(',')) > 1]
        tradHanzi = [{x[3]: {"ordinal": int(x[0]), "char": x[3], "meaning": x[7]}}
                     for x in shorterList if x[0].isdigit()]
        simpHanzi = [{x[4]: {"ordinal": int(x[1]), "char": x[4], "meaning": x[8]}}
                     for x in shorterList if x[1].isdigit()]
        kanji = [{x[5]: {"ordinal": int(x[2]), "char": x[5], "meaning": x[9]}}
                 for x in shorterList if x[2].isdigit()]

        finalTrad = {}
        finalSimp = {}
        finalKanji = {}
        for x in tradHanzi:
            finalTrad.update(x)
        for x in simpHanzi:
            finalSimp.update(x)
        for x in kanji:
            finalKanji.update(x)
        global simplifiedHeisig
        simplifiedHeisig = finalSimp
        global traditionalHeisig
        traditionalHeisig = finalTrad
        global kanjiHeisig
        kanjiHeisig = finalKanji

def getHeisigSimpDict():
    return simplifiedHeisig

def getHeisigTradDict():
    return traditionalHeisig

def getHeisigKanjiDict():
    return kanjiHeisig









