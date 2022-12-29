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


    docID = 0

    for i in data:
        title = i["title"]
        title = title.split()
        docIDs[docID] = i["title"]
        for word in title:
            word = pstemmer.stem(word)
            if word in lexicon.keys():
                if docID in forwardindex:
                    if lexicon[word] in forwardindex[docID]:
                        forwardindex[docID][lexicon[word]] += 5
                    else:
                        forwardindex[docID][lexicon[word]] = 5
                else:
                    forwardindex[docID] = {lexicon[word] : 5}

        title = i["content"]
        title = title.split()
        for word in title:
            word = pstemmer.stem(word)
            if word in lexicon.keys():
                if docID in forwardindex:
                    if lexicon[word] in forwardindex[docID]:
                        forwardindex[docID][lexicon[word]] += 1
                    else:
                        forwardindex[docID][lexicon[word]] = 1
                else:
                    forwardindex[docID] = {lexicon[word] : 1}

        docID += 1

    with open("docIDs.json", "w") as f:
        f.write(json.dumps(docIDs))

    with open("forwardindex.json", "w") as f:
        f.write(json.dumps(forwardindex))
