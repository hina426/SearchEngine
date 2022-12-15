import json
with open ("forwardindex.json") as f:
    forwardindex = json.load(f)


invertedindex = {}

for i in forwardindex:
    for wordID in forwardindex[i]:
        if wordID in invertedindex:
            invertedindex[wordID].append(i)
        else:
            invertedindex[wordID] = [i]







with open("invertedindex.json", "w") as f:
    f.write(json.dumps(invertedindex))