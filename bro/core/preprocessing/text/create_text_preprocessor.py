# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from core.preprocessing.text.text_preprocessor import TextPreProcessor
from core.variable import Variable


class TextPreprocessorThread(QThread):

    def __init__(self, signal, variable_name, tokenizer, remove_non_alphabets, should_remove_stopwords, remove_user_data, stemmer):
        QThread.__init__(self)
        self.signal = signal
        self.variable_name = variable_name
        self.tokenizer = tokenizer
        self.remove_non_alphabets = remove_non_alphabets
        self.should_remove_stopwords = should_remove_stopwords
        self.remove_user_data = remove_user_data
        self.stemmer = stemmer

    def run(self):
        Variable.var_bucket[self.variable_name] = TextPreProcessor(self.tokenizer, self.remove_non_alphabets,
                                                        self.should_remove_stopwords, self.remove_user_data,
                                                        self.stemmer)
        self.signal.emit("Bro Thread: Preprocessor has been created!")
