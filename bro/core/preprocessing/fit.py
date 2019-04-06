# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from core.variable import Variable


class Fit(QThread):

    def __init__(self, signal, sklearn_object, variable, var_type, rows, cols):
        QThread.__init__(self)
        self.signal = signal
        self.sklearn_object = sklearn_object
        self.variable = variable
        self.var_type = var_type
        # For n-dimensional numpy array
        self.rows = rows
        self.cols = cols

    def run(self):
        variable = Variable.var_bucket[self.variable]
        sklearn_object = Variable.var_bucket[self.sklearn_object]
        # Numpy array
        if self.var_type == 0:
            if self.rows == ":":
                if self.cols == ":":
                    Variable.var_bucket[self.sklearn_object] = sklearn_object.fit(variable[:, :])
                    self.signal.emit("Bro thread: Fitted to object")
                else:
                    self.cols = self.cols.split(",")
                    try:
                        self.cols = [int(i.strip()) for i in self.cols]
                    except ValueError:
                        self.signal.emit("Error converting to integers in one of the columns")
                        return None
                    except TypeError:
                        self.signal.emit("NPE > <*> :{")
                        return None
                    Variable.var_bucket[self.sklearn_object] = sklearn_object.fit(variable[:, self.cols])
                    self.signal.emit("Bro thread: Fitted to object")
        else:
            print("List")