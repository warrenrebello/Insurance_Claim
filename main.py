import numpy as np
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def mainPage():
    render_template("html.index")


if __name__ == "__main__":
    app.run(debug=True)