from sklearn.feature_extraction.text import TfidfVectorizer
import re
import os
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


stop = stopwords.words('english')
porter = PorterStemmer()

#  clean my text data, tokenize the document
def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    text = re.sub(r'\d+', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
                           text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) \
                   + ' '.join(emoticons).replace('-', '')
    tokenized = [porter.stem(w) for w in text.split() if w not in stop]
    return tokenized
            
            
# construct a TfidfVectorizer

vect = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None,tokenizer=tokenizer)
