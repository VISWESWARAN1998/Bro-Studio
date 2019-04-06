# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from core.variable import Variable


class DFViewer(QThread):

    def __init__(self, signal):
        QThread.__init__(self)
        self.signal = signal

    def run(self):
        if "data_frame" not in Variable.var_bucket:
            return None
        data_frame = Variable.var_bucket["data_frame"]
        # Emit the column names
        column_name_list = list(data_frame)
        self.signal.emit(column_name_list)
        for row in data_frame.itertuples():
            row_value = list(row)
            row_value = row_value[1:]
            self.signal.emit(row_value)

