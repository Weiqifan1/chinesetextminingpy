from flask import Flask, request
from flask import render_template
import src.Controllers.appController
from flask_cors import CORS
#import flask-cors from flask-cors

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    # return "hello world"
    return render_template("index.html")

@app.route("/newapi/<name>", methods = ['GET'])
def hello_2(name):
    # return "hello world"
    return 'welcome %s' % name

@app.route('/user', methods = ['POST'])
def home():
    content_type = request.headers.get('Content-Type')
    print("appstart chr")
    if (content_type == 'application/json'):
        json = request.json
        res = src.Controllers.appController.postendpoint(json)
        return res
    else:
        return 'Content-Type not supported!'



#endpoint which convert a text to a mining deck
#http://localhost/texttodeck    POST
#body:
#{
#      "deckName": "jsonSimplifiedNews",
#         "deckInfo": "simplifiedNewsInfo",
#         "script": "simplified",
#         "text": "竹北市戶政事務所12日湧入大量人潮，碼牌抽到1297號，多是為辦遷入戶籍作業。"
# }
@app.route('/texttodeck', methods = ['POST'])
def textToDeck():
    content_type = request.headers.get('Content-Type')
    print("appstart chr")
    if (content_type == 'application/json'):
        json = request.json
        res = src.Controllers.appController.postendpoint(json)
        resToDeck = src.Controllers.appController.postendpointToDeck(res)
        return resToDeck
    else:
        return 'Content-Type not supported!'
    #["deckName", "deckInfo", "output", "script"]

@app.route('/texttovocab', methods = ['POST'])
def textToVocab():
    content_type = request.headers.get('Content-Type')
    print("appstart chr")
    if (content_type == 'application/json'):
        json = request.json
        res = src.Controllers.appController.texttovocab(json)
        return res
    else:
        return 'Content-Type not supported!'
    #["deckName", "deckInfo", "output", "script"]

