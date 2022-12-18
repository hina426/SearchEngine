import json
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords



def forwardIndex(file):

    pstemmer = PorterStemmer()
    forwardindex = {}

    with open(file) as f:
        data = json.load(f)

    with open("lexicon.json") as f:
        lexicon = json.load(f)

    with open("docIDs.json") as f:
        docIDs = json.load(f)



    for i in data:
        title = i["title"] + " " + i["content"]
        title = title.split()
        for word in title:
            word = pstemmer.stem(word)
            if word in lexicon.keys():
                if docIDs[i["id"]] in forwardindex:
                    forwardindex[docIDs[i["id"]]].append(lexicon[word])
                else:
                    forwardindex[docIDs[i["id"]]] = [lexicon[word]]


    with open("forwardindex.json", "w") as f:
        f.write(json.dumps(forwardindex))
