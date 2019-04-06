# SWAMI KARUPPASWAMI THUNNAI

import os
import sqlite3
import pandas as pd
from PyQt5.QtCore import QThread
from core.variable import Variable


class LoadDataFrame(QThread):

    def __init__(self, status_signal, message_signal, file_location, file_type, file_args):
        """
        Constructor to initialize the instance variables.

        :param status_signal: Will send the status to the MainWidget.

        :param message_signal: Will open a message box.

        :param file_location: The location of the data-set.

        :param file_type: The type of the data-set; 0 for CSV; 1 for EXCEL; 2 FOR SQLite

        :param file_args: Custom arguments for complex file-types like databases and so on. This
        feature is less used now but on the further versions it's necessity is inevitable.
        """
        QThread.__init__(self)
        self.status_signal = status_signal
        self.file_location = file_location
        self.message_signal = message_signal
        self.file_type = file_type
        self.file_args = file_args
        self.data_frame = None

    def run(self):
        if not os.path.exists(self.file_location):
            self.message_signal.emit("Invalid file location: "+str(self.file_location))
            return None
        if self.file_type == 0:
            self.data_frame = pd.read_csv(self.file_location)
        elif self.file_type == 1:
            self.data_frame = pd.read_excel(self.file_location)
        elif self.file_type == 2:
            connection = sqlite3.connect(self.file_location)
            self.data_frame = pd.read_sql_query("select * from "+self.file_args[0], connection)
            connection.close()
        else:
            self.message_signal.emit("Invalid file type number")
        Variable.var_bucket["data_frame"] = self.data_frame
        self.status_signal.emit("Loaded!")





