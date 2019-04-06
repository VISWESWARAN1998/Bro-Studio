# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from core.variable import Variable


class BuildML(QThread):

    def __init__(self, signal, X, y, model, model_name):
        QThread.__init__(self)
        self.signal = signal
        self.X = X
        self.y = y
        self.model = model
        self.model_name = model_name

    def run(self):
        self.signal.emit("Fitting")
        model = None
        if self.model == 0:
            model = LinearRegression()
        elif self.model == 1:
            model = LogisticRegression()
        elif self.model == 2:
            model = GaussianNB()
        elif self.model == 3:
            model = SVC()
        Variable.var_bucket[self.model_name] = model
        Variable.var_bucket[self.model_name].fit(Variable.var_bucket[self.X], Variable.var_bucket[self.y].ravel().tolist())
        self.signal.emit("Good job! Model has been trained successfully.")