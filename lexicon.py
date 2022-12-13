import json
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

pstemmer = PorterStemmer()

with open("airwars.json") as f:
    data = json.load(f)

allcontent = ""
for i in data:
    allcontent += i["title"]
    allcontent += i["content"]

listcontent = allcontent.split()

stops = set(stopwords.words('english'))

finallist = []

for word in listcontent:
    if word in stops:
        pass
    elif word in string.punctuation or word in ["-", '"']:
        pass
    else:
        if (pstemmer.stem(word) in finallist):
            pass
        else:
            finallist.append(pstemmer.stem(word))

finaldict = {}
count = 0
for i in finallist:
    finaldict[i] = count
    count += 1

with open("lexicon.json", 'w') as f:
    f.write(json.dumps(finaldict))