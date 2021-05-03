""" This script starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


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
@app.route("/python/<text>")
def home4(text="is cool"):
    "This method pass argument by default"
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def home5(n):
    "This methos pass an int argument"
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def home6(n):
    """
    This methos display a HTML page if n is int
    - H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def home7(n):
    """
    display a HTML page only if n is an integer
    - H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
