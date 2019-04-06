# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QComboBox, QPushButton
from PyQt5.QtWidgets import QFileDialog, QTextEdit, QInputDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.df.load_df import LoadDataFrame
from core.df.assign_variable import VarFromDfCols


class DataFrameWidget(QWidget):

    status_signal = pyqtSignal(str)
    message_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.status_signal.connect(self.status_slot)
        self.message_signal.connect(self.message_slot)
        self.df_load_thread = None
        self.df_assign_thread = None
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('<b style="color:green">GUI interface to '
                                     'access pandas data-frame</b>'))
        select_file_layout = QHBoxLayout()
        select_file_layout.addWidget(QLabel("Choose File: "))
        self.file_location = QLineEdit()
        select_file_layout.addWidget(self.file_location)
        self.file_type = QComboBox()
        self.file_type.addItems(["CSV", "EXCEL", "SQLITE"])
        select_file_layout.addWidget(self.file_type)
        select_file = QPushButton("SELECT FILE")
        select_file.clicked.connect(self.load_df_clicked)
        select_file_layout.addWidget(select_file)
        main_layout.addLayout(select_file_layout)
        self.status = QLabel()
        main_layout.addWidget(self.status)
        main_layout.addWidget(QLabel("Column Names: "))
        self.column_name = QTextEdit()
        main_layout.addWidget(self.column_name)
        variable_layout = QHBoxLayout()
        variable_layout.addWidget(QLabel("Variable Name: "))
        self.variable_name = QLineEdit()
        variable_layout.addWidget(self.variable_name)
        save_variable = QPushButton("SAVE VARIABLE")
        save_variable.clicked.connect(self.save_variable_clicked)
        variable_layout.addWidget(save_variable)
        main_layout.addLayout(variable_layout)
        self.setLayout(main_layout)

    def load_df_clicked(self):
        file_type = self.file_type.currentIndex()
        file_location = QFileDialog.getOpenFileName(self, "Choose your data-frame")
        file_location = file_location[0]
        self.file_location.setText(file_location)
        args = []
        if file_type == 2:
            table_name = QInputDialog.getText(self, "Bro", "Enter the table name")
            args.append(table_name)
        self.df_load_thread = LoadDataFrame(self.status_signal, self.message_signal, file_location, file_type, args)
        self.df_load_thread.start()

    @pyqtSlot(str)
    def status_slot(self, value):
        self.status.setText(value)

    @pyqtSlot(str)
    def message_slot(self, value):
        QMessageBox.information(self, "Bro", value)

    def save_variable_clicked(self):
        variable_name = self.variable_name.text()
        if len(variable_name) == 0:
            QMessageBox.information(self, "Bro", "Minimum 1 character for variable name!")
            return None
        columns = self.column_name.toPlainText().split("\n")
        columns = [column.strip() for column in columns]
        columns = list(filter(None, columns))
        if len(columns) == 0:
            QMessageBox.information(self, "Bro", "Minimum 1 column needed")
            return None
        self.df_assign_thread = VarFromDfCols(self.status_signal, self.message_signal,
                                              variable_name, columns)
        self.df_assign_thread.start()



