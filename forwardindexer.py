import json
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

pstemmer = PorterStemmer()
forwardindex = {}

with open("airwars.json") as f:
    data = json.load(f)

with open("lexicon.json") as f:
    lexicon = json.load(f)

with open("docIDs.json") as f:
    docIDs = json.load(f)



for i in data:
    title = i["title"] + " " + i["content"]
    title = title.split()
    for word in title:
        if pstemmer.stem(word) in lexicon.keys():
            if docIDs[i["id"]] in forwardindex:
                forwardindex[docIDs[i["id"]]].append(lexicon[pstemmer.stem(word)])
            else:
                forwardindex[docIDs[i["id"]]] = [lexicon[pstemmer.stem(word)]]
        else:
            pass


with open("forwardindex.json", "w") as f:
    f.write(json.dumps(forwardindex))
