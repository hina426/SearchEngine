import json


def invertedIndex(inv):
        
    with open ("forwardindex.json") as f:
        forwardindex = json.load(f)


    invertedindex = inv

    #loops over the document ids
    for i in forwardindex:
        for wordID in forwardindex[i]:
            if wordID in invertedindex:
                invertedindex[wordID][i] = forwardindex[i][wordID]
            else:
                invertedindex[wordID] = {i : forwardindex[i][wordID]}

    print(len(invertedindex), " words in inverted index")
    

    with open("invertedindex.json", "w") as f:
        f.write(json.dumps(invertedindex))