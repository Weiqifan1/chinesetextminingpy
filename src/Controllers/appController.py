
import re
from src.Services import chineseTextHandlerService

def postendpoint(postinput):
    print("print start")
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    sentences = chineseTextHandlerService.textToTokensFromSimplified(betterdata)
    return sentences


