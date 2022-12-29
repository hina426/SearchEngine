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

print(len(forward_index), "Docs")



def perform_search(query):
               
    docs = []
    for word in query.split(" "):
      stem = ps.stem(word)    #rootword
      if(stem not in lexicon): continue
      docs.append(inverted_index[str(lexicon[stem])])

    results = {}
    for docsW in docs:
      for doc in docsW:

        if(doc in results):
          results[doc] += docsW[doc]
        else:
          results[doc] = docsW[doc]

    sorted_d = sorted(results.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in sorted_d[:10]:
      res.append(docIDs[i[0]])
    return res








