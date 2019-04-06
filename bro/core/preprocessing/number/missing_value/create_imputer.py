# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from sklearn.preprocessing import Imputer
from core.variable import Variable


class CreateImputer(QThread):
    """
    This class will create the imputer object.

    Import: from sklearn.preprocessing import Imputer
    """

    def __init__(self, signal, var_name, missing_value, strategy, axis):
        """
        Constructor the initialize the instance variables.

        :param signal: The signal will help to communicate from QThread to GUI.

        :param var_name: The name of the imputer object.

        :param missing_value: Missing value place holder.

        :param strategy: Mean, Median, Most Frequent

        :param axis: 0 => column wise, 1 => row wise
        """
        QThread.__init__(self)
        self.signal = signal
        self.var_name = var_name
        self.missing_value = missing_value
        self.strategy = strategy
        self.axis = axis

    def run(self):
        Variable.var_bucket[self.var_name] = Imputer(missing_values=self.missing_value, strategy=self.strategy,
                                                     axis=self.axis)
        self.signal.emit("Bro Thread: Imputer object has been created")
