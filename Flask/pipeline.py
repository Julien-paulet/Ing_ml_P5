#!/usr/bin/env python
# coding: utf-8

import csv
from lxml import html
import pandas as pd
import numpy as np
import nltk
import string
import re
from collections import defaultdict
from nltk.stem.snowball import EnglishStemmer

# # Loading stopwords
nltk.download('stopwords')
tokenizer = nltk.RegexpTokenizer(r'\w+')

# #Loading files
to_keep_ = open("to_keep.csv", 'r')
to_keep_ = csv.reader(to_keep_)
to_keep = list(to_keep_)
to_keep = [item for sublist in to_keep for item in sublist]

sw = open("sw.csv", 'r')
sw = csv.reader(sw)
sw = list(sw)
sw = [item for sublist in sw for item in sublist]


# # Building the pipeline

def pipe(title, body):
    body = title + ' ' + body
    body = title + ' ' + body
    body = html.fromstring(body).text_content()
    body = body.replace('\n', '')

    # There is still some html tags, let's remove them with a regex
    TAG_RE = re.compile(r'<[^>]+>')
    body = TAG_RE.sub('', body)
    print(body)
    # Init stemmer and tokenizer
    stemmer = EnglishStemmer()
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    # Remove stop words and keep only the good words
    token = tokenizer.tokenize(body.lower())
    desc = [stemmer.stem(w) for w in token if not w in sw and w in to_keep]
    
    return desc

