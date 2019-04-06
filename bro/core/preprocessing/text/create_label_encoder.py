# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from core.variable import Variable
from sklearn.preprocessing import LabelEncoder


class CreateLabelEncoder(QThread):

    def __init__(self, signal, variable_name):
        QThread.__init__(self)
        self.signal = signal
        self.variable_name = variable_name

    def run(self):
        Variable.var_bucket[self.variable_name] = LabelEncoder()
        self.signal.emit("Bro thread: variable has been created!")


