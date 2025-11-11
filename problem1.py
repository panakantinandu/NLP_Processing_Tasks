import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "John enjoys playing football while Mary loves reading books in the library."

# Process the text
doc = nlp(text)

# Steps: Tokenize → Remove stopwords → Lemmatize → Keep only nouns and verbs
filtered_tokens = [
    token.lemma_ 
    for token in doc 
    if token.pos_ in ["NOUN", "VERB"] and token.text.lower() not in STOP_WORDS
]

print("Filtered tokens:", filtered_tokens)
