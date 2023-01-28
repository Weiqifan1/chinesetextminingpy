

def isChinese(firstElem):
    singleChars = [*firstElem]
    singleCharsSet = [isCharChinese(x) for x in singleChars]
    if True in singleCharsSet:
        return True
    else:
        return False

def isCharChinese(singleChar):
    #range of chinese punctuation in unicode
    myrange_1 = range(12288, 12352)
    myrange_2 = range(65281, 65518)
    totalrange = list(myrange_1) + list(myrange_2)
    #65281 _ 65518
    ordinal = ord(singleChar)
    if ordinal > 10000 and ordinal not in totalrange:
        return True
    else:
        return False