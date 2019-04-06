# SWAMI KARUPPASWAMI THUNNAI

import re
from nltk.tokenize import word_tokenize, TweetTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


class TextPreProcessor:

    def __init__(self, tokenizer, remove_non_alphabets, should_remove_stopwords, remove_user_data, stemmer):
        """
        Constructor to initialize the instance variables.

        :param tokenizer: The tokenizer to use.

        :param remove_non_alphabets: True if we need to remove the non-alphabets.

        :param should_remove_stopwords: True if we need to remove the stopwords.

        :param remove_user_data: True if we need to remove username and http links.

        :param stemmer: The stemmer to use.
        """
        self.tokenizer = tokenizer
        self.remove_non_alphabets = remove_non_alphabets
        self.should_remove_stopwords = should_remove_stopwords
        self.remove_user_data = remove_user_data
        self.stemmer = stemmer

    def preprocess(self, text):
        tokens = None
        stemmer = None
        # Convert the text to lower case
        text = text.lower()
        if self.tokenizer == 0:
            tokens = word_tokenize(text=text)
        elif self.tokenizer == 1:
            tokenizer = TweetTokenizer()
            tokens = tokenizer.tokenize(text=text)
        # Remove stopwords
        if self.should_remove_stopwords:
            tokens = [token for token in tokens if token not in set(stopwords.words("english"))]
        # Remove punctuations
        if self.remove_non_alphabets:
            punc_remover = lambda word: re.sub("[^A-Za-z]", " ", word)
            tokens = list(map(punc_remover, tokens))
        # Perform stemming
        if self.stemmer == 0:
            stemmer = PorterStemmer()
        tokens = [stemmer.stem(token) for token in tokens]
        # Strip the words
        stripper = lambda word: word.strip()
        tokens = list(map(stripper, tokens))
        tokens = filter(None, tokens)
        processed_text = " ".join(tokens)
        return processed_text



