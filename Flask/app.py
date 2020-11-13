# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from pickle import load
import pandas as pd
import numpy as np
from pipeline import pipe

#Load pipeline
tfidf = load(open('tfidf', 'rb'))
model = load(open('model', 'rb'))
mb = load(open('mb', 'rb'))

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    #Récupération de l'input user 
    title = request.form["title"]
    description = request.form["description"]
    cleaned = pipe(title, description)
    cleaned = tfidf.transform(cleaned)
    result = mb.inverse_transform(model.predict(cleaned))[0]
    result = [i for i in result if i != '']
    if result:
        result = result
    else:
        result = 'No match found'
    
    return render_template("results.html", results=result, title=title, description=description)

if __name__ == "__main__":
    app.run(debug=True)

