from flask import Flask, request
from flask import render_template
import src.Controllers.appController

app = Flask(__name__)


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


