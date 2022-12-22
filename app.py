from flask import Flask, jsonify, request
from flask import render_template
import src.appController

app = Flask(__name__)


@app.route("/")
def hello_world():
    # return "hello owrld"
    return render_template("index.html")

@app.route("/newapi/<name>")
def hello_2(name):
    # return "hello owrld"
    return 'welcome %s' % name

@app.route('/user', methods = ['POST'])
def home():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        res = src.appController.postendpoint(json)
        return json
    else:
        return 'Content-Type not supported!'