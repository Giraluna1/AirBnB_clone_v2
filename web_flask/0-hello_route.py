#!/usr/bin/python3
""" """
from flask import Flask

app = Flask(__name__)
strict_slashes = False


@app.route('/')
def home():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
