# 🔰 Search Engine

Welcome to the Search Engine project! This project is a simple search engine implemented using HTML, CSS, Python, and the Flask framework.

# [Project Live Here ↗](https://github.com/hina426/SearchEngine)

### Project Goals 🔅

1. Forward index
2. Inverted index
3. Single word searching
4. Multi word searching
5. Ranking results based on frequency and position
6. Dynamic Content Addition
7. System scalability
8. Using GIT for team collaboration
9. System Interface

## Table of contents 

- [Features](#Features)
- [Setup and Usage](#Setup-and-Usage)
- [Implementation](#Implementation)
- [Technologies](#Technologies)
- [Acknowledgements](#Acknowledgements)
- [Feedback](#Feedback)

## Features

- Forward indexing
- Inverted indexing
- Lexicon
- Single and multi-word search
- Page Rank algorithm
- Scalability

## Setup and Usage

To get started with the project, follow these steps:

Clone the repository

Afterward get following libraries:

1-Punkt Tokenizer Model
2-Stopwords Corpus

By typing: 

import nltk

nltk.download()

To use the search engine, simply type your search query into the search bar and press the "Search" button. The search engine will return a list of relevant results based on your query.

## Implementation

The search engine uses the following algorithms:

#### Forward indexing: 
This algorithm is used to map documents to words.

#### Inverted indexing: 
This algorithm is used to create a reverse index of the documents, mapping each word to the list of documents it appears in.

#### Lexicon: 
This is a list of all the unique words in the documents, used for efficient searching.

#### Single and multi-word search: 
The search engine supports both single and multi-word searches, allowing users to search for multiple words at once.

#### Page Rank algorithm:
This algorithm is used to rank the documents based on their importance and relevance to the search query.

#### Scalability: 
The search engine has been designed to scale to large amounts of data and handle a high volume of search queries.


## Technologies

This project is built using the following frameworks:

- HTML for the structure of the web page
- CSS for the styling of the web page
- Python for the backend logic and implementation of the search engine
- Flask for the web framework


## Acknowledgements

- [The Anatomy of a Large Scale Hypertextual Web Search Engine](https://snap.stanford.edu/class/cs224w-readings/Brin98Anatomy.pdf)

## Feedback

If you have any feedback, please reach out to me at hnaeem.bscs21seecs@seecs.edu.pk
