# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from sklearn.preprocessing import MinMaxScaler
from core.variable import Variable


class CreateMinMaxScaler(QThread):

    def __init__(self, signal, variable_name, feature_minimum, feature_maximum):
        QThread.__init__(self)
        self.signal = signal
        self.variable_name = variable_name
        self.feature_minimum = feature_minimum
        self.feature_maximum = feature_maximum

    def run(self):
        try:
            self.feature_minimum = int(self.feature_minimum)
            self.feature_maximum = int(self.feature_maximum)
        except ValueError:
            self.signal.emit("Bro Thread: Feature values are not integer")
            return None
        except TypeError:
            self.signal.emit("Bro Thread: Feature value NPE :<{")
            return None
        Variable.var_bucket[self.variable_name] = MinMaxScaler(
            feature_range=(self.feature_minimum, self.feature_maximum)
        )
        self.signal.emit("Bro thread: variable has been created!")
