import re
from src.Services import chineseTextHandlerService



def postendpoint(postinput):
    print("print start")
    sentences = []
    output = {"output": sentences}
    gettextdata = ""
    if "text" in postinput:
        gettextdata = postinput["text"]
    else:
        return output
    betterdata = re.sub("\s+", " ", gettextdata.strip())
    sentences = ""
    scriptvalue = ""
    if "script" in postinput:
        scriptvalue = postinput["script"]
    else:
        return {"output": []}
    if scriptvalue == "simplified":
        sentences = chineseTextHandlerService.textToTokensFromSimplified(betterdata)
    elif scriptvalue == "traditional":
        sentences = chineseTextHandlerService.textToTokensFromTraditional(betterdata)
    else:
        sentences = []
    output = {"output":sentences}
    return output


