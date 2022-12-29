from docIDs import *
from forwardindexer import *
from invertedindex import *
from lexicon import lexicon as LEXICONCALL

from singleWordSearch import *

"""

with open("lexicon.json") as f:
    lexicon = json.load(f)

with open ("forwardindex.json") as f:
    forwardindex = json.load(f)

with open("invertedindex.json") as f:
    inverted_index = json.load(f)

LEXICONCALL(lexicon, "airwars.json")
forwardIndex(forwardindex, "airwars.json")
invertedIndex(inverted_index)

"""