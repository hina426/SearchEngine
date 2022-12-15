import json

with open("airwars.json") as f:
    articles = json.load(f)

docIDs = {}


count = 0


for article in articles:
    docIDs[article["id"]] = str(count)
    count += 1

with open("docIDs.json", "w") as f:
    f.write(json.dumps(docIDs))