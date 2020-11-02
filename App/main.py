# -*- coding: utf-8 -*-
# Basic Imports
import numpy as np
import pickle

from flask import Flask, request, render_template, redirect


app = Flask(__name__)

# Reading 'insurance.ser', and storing in a variable
file = open("insurance.ser", "rb")
dtc = pickle.load(file)
file.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict_claim", methods=["POST"])
def predict_claim():
    age = request.form["age"]
    sex = request.form["sex"]
    bmi = request.form["bmi"]
    children = request.form["children"]
    smoker = request.form["smoker"]
    region = request.form["region"]
    charges = request.form["charges"]
    
    claim = dtc.predict(np.array([[age, sex, bmi, children, smoker, region, charges]]))
    # claim = dtc.predict(np.array[[int(age), int(sex), float(bmi), int(children), int(smoker), int(region), float(charges)]])
    return str(claim)

if __name__ == "__main__":
    app.run(debug=True)