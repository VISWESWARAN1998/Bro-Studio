# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtCore import QThread
from core.variable import Variable


class DisplayVariableThread(QThread):
    """
    This thread will send the available variables as signals for
    the GUI to display it.
    """

    def __init__(self, signal):
        """
        Constructor to initialize the instance variables.

        :param signal: The signal to be emitted for the GUI.
        """
        QThread.__init__(self)
        self.signal = signal

    def run(self):
        for variable in Variable.var_bucket:
            variable_name = variable
            variable_value = str(Variable.var_bucket[variable_name])
            variable_detail_list = list()
            variable_detail_list.append("Type: " + str(type(Variable.var_bucket[variable_name])))
            # If the attribute has size
            try:
                variable_detail_list.append("Size: "+str(len(Variable.var_bucket[variable_name])))
            except TypeError:
                pass
            variable_detail = ";\t".join(variable_detail_list)
            self.signal.emit([variable_name, variable_value, variable_detail])


