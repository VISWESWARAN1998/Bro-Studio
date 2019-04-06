# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.variable_explorer.display_variable import DisplayVariableThread


class DisplayVariableWidget(QWidget):

    display_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        self.display_signal.connect(self.display_slot)
        main_layout = QVBoxLayout()
        self.variable_table = QTableWidget()
        self.variable_table.setColumnCount(3)
        self.variable_table.setHorizontalHeaderLabels(("Name", "Value", "Details"))
        self.variable_table.setColumnWidth(0, 300)
        self.variable_table.setColumnWidth(1, 300)
        self.variable_table.setColumnWidth(2, 600)
        main_layout.addWidget(self.variable_table)
        self.setLayout(main_layout)
        self.setWindowTitle("Variable viewer")
        self.setGeometry(300, 300, 1200, 400)
        self.display_variable_thread = DisplayVariableThread(self.display_signal)
        self.display_variable_thread.start()

    @pyqtSlot(list)
    def display_slot(self, value):
        row_count = self.variable_table.rowCount()
        self.variable_table.setRowCount(row_count+1)
        self.variable_table.setItem(row_count, 0, QTableWidgetItem(value[0]))
        self.variable_table.setItem(row_count, 1, QTableWidgetItem(value[1]))
        self.variable_table.setItem(row_count, 2, QTableWidgetItem(value[2]))

