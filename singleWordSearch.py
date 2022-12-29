import json
from nltk.stem import PorterStemmer


ps = PorterStemmer()

with open("lexicon.json") as f:
    lexicon = json.load(f)

with open("forwardindex.json") as f:
    forward_index = json.load(f)

with open("invertedindex.json") as f:
    inverted_index = json.load(f)
  
with open("docIDs.json") as f:
    docIDs = json.load(f)



def perform_search(query):
               
    query = ps.stem(query)    #rootword
    # Look up the postings lists for each token in the inverted index
    # for word in query.split("")
    docs = inverted_index[str(lexicon[query])]
    sorted_d = sorted(docs.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in sorted_d:
      res.append(docIDs[i[0]])
    return res













"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def search():
    # Perform the search and retrieve the results
    results = perform_search()
    # Render the search template and pass the results to it
    return render_template('search.html', results=results)

if __name__ == '__main__':
    app.run()


...................................................................

<html>
  <head>
    <title>My Search Engine</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <header>
      <h1>My Search Engine</h1>
      <form action="/" method="post">
        <input type="text" name="query" placeholder="Search...">
        <button type="submit">Search</button>
      </form>
    </header>
    <main>
      {% if results %}
      <ul>
        {% for result in results %}
        <li>{{ result }}</li>
        {% endfor %}
      </ul>
      {% else %}
      <p>No results found.</p>
      {% endif %}
    </main>
  </body>
</html>


.....................................

<!-- search.html -->
<html>
  <head>
    <title>My Search Engine</title>
    <link rel="stylesheet" href="/static/style.css">
  </head>
  <body>
    <header>
      <h1>My Search Engine</h1>
      <form action="/" method="post">
        <input type="text" name="query" placeholder="Search...">
        <button type="submit">Search</button>
      </form>
    </header>
    <main>
      {% if results %}
      <ul>
        {% for result in results %}
        <li>{{ result }}</li>
        {% endfor %}
      </ul>
      {% else %}
      <p>No results found.</p>
      {% endif %}
    </main>
  </body>
</html>


................

# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Get the search query from the form submission
        query = request.form['query']
        # Perform the search and retrieve the results
        results = perform_search(query)
        # Render the search template and pass the results to it
        return render_template('search.html', results=results)
    else:
        # Render the search template with no results
        return render_template('search.


................

Preprocess the search query and the documents in the dataset to extract relevant data and normalize it, such as lowercasing the text and removing stop words.
For each document in the dataset, calculate the frequency of each term in the search query in the document. You can use a dictionary to store the term frequencies for each document.
For each document, calculate a score based on the term frequencies and the positions of the terms in the document. You can give higher weight to terms that appear more frequently or closer to the beginning of the document.
Sort the documents by their scores in descending order.


from collections import defaultdict
import re

def rank_results(query, documents):
    # Preprocess the query and documents
    query = preprocess(query)
    docs = [preprocess(doc) for doc in documents]
    
    # Calculate the term frequencies for each document
    term_freqs = []
    for query in :
        freq = defaultdict(int)
        for term in query:
            freq[term] += doc.count(term)
        term_freqs.append(freq)
    
    # Calculate the scores for each document
    scores = []
    for i, doc in enumerate(docs):
        score = 0
        for j, term in enumerate(







"""