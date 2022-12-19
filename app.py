from flask import Flask
from flask import render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello_world():
    # return "hello owrld"
    return render_template("index.html")

class Video(Resource):
    def newapi(self):
        # return "hello owrld"
        return ""



api.add_resource(Video, '/newapi')