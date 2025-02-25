#!/usr/bin/python3
""" This script starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """ home method"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
