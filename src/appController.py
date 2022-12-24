import json
from chinese import ChineseAnalyzer
import re

def postendpoint(postinput):
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())

    analyzer = ChineseAnalyzer()
    anal = analyzer.parse(betterdata)
    test2 =  anal.sentences()
    hello = [x.strip(' ') for x in test2]
    return hello





