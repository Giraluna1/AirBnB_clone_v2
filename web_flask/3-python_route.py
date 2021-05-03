#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    " method response page1"
    return "Hello HBNB!"


@app.route('/hbnb')
def home2():
    " method response page2"
    return "HBNB"


@app.route('/c/<text>')
def home3(text=None):
    "This methos pass an argument"
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python")
@app.route('/python/(<text>)')
def home4(text="is cool"):
    "This method pass argument by default"
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
