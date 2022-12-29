import json
import string
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords



def lexicon(file):
        
    pstemmer = PorterStemmer()

    with open(file) as f:
        data = json.load(f)

    allcontent = ""
    for i in data:
        #bcz we need titles and content from the files
        allcontent += i["title"]            
        allcontent += i["content"]            

    listcontent = allcontent.split()

    stops = set(stopwords.words('english'))

    finaldict = {}
    count = 0
    for word in listcontent:
        #performs stemming
        word = pstemmer.stem(word)  
        #removes punctuation and all the words like a, an, the etc        
        if word in stops or word in string.punctuation or word in ["-", '"']:   
            pass
        elif (word not in finaldict):
                finaldict[word] = count
                count += 1

    with open("lexicon.json", 'w') as f:
        f.write(json.dumps(finaldict))