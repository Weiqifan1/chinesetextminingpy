

def isChinese(firstElem):
    singleChars = [*firstElem]
    singleCharsSet = [isCharChinese(x) for x in singleChars]
    if True in singleCharsSet:
        return True
    else:
        return False

def isCharChinese(singleChar):
    #range of chinese punctuation in unicode
    myrange = range(12288, 12352)
    ordinal = ord(singleChar)
    if ordinal > 10000 and ordinal not in myrange:
        return True
    else:
        return False