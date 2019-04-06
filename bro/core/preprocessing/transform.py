# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from core.variable import Variable
import numpy as np


class Transform(QThread):

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
                    result = sklearn_object.transform(variable[:, :])
                    if result.shape != Variable.var_bucket[self.variable][:, self.cols].shape:
                        result = np.reshape(result, Variable.var_bucket[self.variable][:, self.cols].shape)
                    Variable.var_bucket[self.variable][:, self.cols] = result
                    self.signal.emit("Bro thread: Transformed!")
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
                    result = sklearn_object.transform(variable[:, self.cols])
                    if result.shape != Variable.var_bucket[self.variable][:, self.cols].shape:
                        result = np.reshape(result, Variable.var_bucket[self.variable][:, self.cols].shape)
                    Variable.var_bucket[self.variable][:, self.cols] = result
                    self.signal.emit("Bro thread: Transformed!")

        else:
            print("List")