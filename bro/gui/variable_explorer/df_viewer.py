# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.variable_explorer.df_viewer import DFViewer


class DFViewerWidget(QWidget):

    signal = pyqtSignal(list)
    head_added = False

    def __init__(self):
        super().__init__()
        self.signal.connect(self.df_slot)
        main_layout = QVBoxLayout()
        self.df = QTableWidget()
        main_layout.addWidget(self.df)
        self.setLayout(main_layout)
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("DFViewer")
        self.df_thread = DFViewer(self.signal)
        self.df_thread.start()

    @pyqtSlot(list)
    def df_slot(self, value):
        # Check if the head of the data-frame is added or not
        if self.head_added is False:
            self.head_added = True
            self.df.setColumnCount(len(value))
            self.df.setHorizontalHeaderLabels(value)
            return None
        row_count = self.df.rowCount()
        self.df.setRowCount(row_count+1)
        for index, data in enumerate(value):
            self.df.setItem(row_count, index, QTableWidgetItem(str(data)))

