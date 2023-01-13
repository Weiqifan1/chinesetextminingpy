import re
from src.Services import chineseTextHandlerService

def postendpoint(postinput):
    print("print start")
    gettextdata = postinput["text"]
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    sentences = ""
    scriptvalue = ""
    if "script" in postinput:
        scriptvalue = postinput["script"]
    if scriptvalue == "simplified":
        sentences = chineseTextHandlerService.textToTokensFromSimplified(betterdata)
    elif scriptvalue == "traditional":
        sentences = chineseTextHandlerService.textToTokensFromTraditional(betterdata)
    else:
        sentences = []
    output = {"output":sentences}
    return output


