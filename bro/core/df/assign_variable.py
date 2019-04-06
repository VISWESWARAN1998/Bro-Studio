# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from core.variable import Variable


class VarFromDfCols(QThread):
    """
    This class is used to create variables from pandas data-frame columns.
    """

    def __init__(self, status_signal, message_signal, var_name, column_names):
        QThread.__init__(self)
        self.status_signal = status_signal
        self.message_signal = message_signal
        self.var_name = var_name
        self.column_names = column_names

    def run(self):
        if "data_frame" not in Variable.var_bucket:
            self.message_signal.emit("No variable named: data_frame")
            return None
        data_frame = Variable.var_bucket["data_frame"]
        try:
            column_values = data_frame[self.column_names].values
            Variable.var_bucket[self.var_name] = column_values
            self.status_signal.emit("Assigned the value!")
        except KeyError:
            self.message_signal.emit("Column not found in data frame. Please check the names.")
