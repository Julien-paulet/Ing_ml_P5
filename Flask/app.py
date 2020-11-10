# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from pickle import load
import pandas as pd

#Load pipeline
pipeline = load(open('pipeline.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    #Récupération de l'input user 
    ttle = request.form["title"]
    description = request.form["description"] 
    
    return render_template("results.html", SiteEnergyUse_ = SiteEnergyUse, TotalGHGEmissions_ = TotalGHGEmissions)

if __name__ == "__main__":
    app.run(debug=True)

