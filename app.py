from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    # return "hello owrld"
    return render_template("index.html")

@app.route("/newapi/<name>")
def hello_2(name):
    # return "hello owrld"
    return 'welcome %s' % name
