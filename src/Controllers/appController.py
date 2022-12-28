import json
from chinese import ChineseAnalyzer
import re
from src.Services import chineseTextHandlerService

def postendpoint(postinput):
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    sentences = chineseTextHandlerService.textToTokens(betterdata)
    return sentences


