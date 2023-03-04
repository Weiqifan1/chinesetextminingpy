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

@app.route('/texttovocabinfo', methods = ['POST'])
def textToVocabInfo():
    content_type = request.headers.get('Content-Type')
    print("appstart chr")
    if (content_type == 'application/json'):
        json = request.json
        res = src.Controllers.appController.texttovocabinfo(json)
        return res
    else:
        return 'Content-Type not supported!'

@app.route('/texttovocabraw', methods = ['POST'])
def textToVocabRaw():
    content_type = request.headers.get('Content-Type')
    print("appstart chr")
    if (content_type == 'application/json'):
        json = request.json
        res = src.Controllers.appController.texttovocabraw(json)
        return res
    else:
        return 'Content-Type not supported!'