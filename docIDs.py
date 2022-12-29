import json


def docIDs(docTable, file):
        
    with open(file) as f:
        articles = json.load(f)

    docIDs = docTable
    count = len(docTable)


    for article in articles:
        docIDs[article["id"]] = str(count)
        count += 1

    with open("docIDs.json", "w") as f:
        f.write(json.dumps(docIDs))