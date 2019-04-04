from flask import Flask
import flask

print(flask.__version__)


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
