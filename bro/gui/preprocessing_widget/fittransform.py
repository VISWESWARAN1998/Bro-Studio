# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QInputDialog, QMessageBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.variable import Variable
from core.preprocessing.fit import Fit
from core.preprocessing.transform import Transform


class FitTransform(QWidget):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.fit_transform_slot)
        self.fit_thread = None
        self.transform_thread = None
        main_layout = QVBoxLayout()
        variable_grid = QGridLayout()
        variable_grid.addWidget(QLabel("sklearn object:"), 0, 0)
        self.sklearn_object = QLineEdit()
        variable_grid.addWidget(self.sklearn_object, 0, 1)
        variable_grid.addWidget(QLabel("Variable Affected:"), 1, 0)
        self.variable_affected = QLineEdit()
        variable_grid.addWidget(self.variable_affected, 1, 1)
        main_layout.addLayout(variable_grid)
        fit_transform_layout = QHBoxLayout()
        fit = QPushButton("FIT")
        fit.clicked.connect(self.fit_clicked)
        transform = QPushButton("TRANSFORM")
        transform.clicked.connect(self.transform_clicked)
        fit_transform_layout.addWidget(fit)
        fit_transform_layout.addWidget(transform)
        main_layout.addLayout(fit_transform_layout)
        self.setLayout(main_layout)

    @pyqtSlot(str)
    def fit_transform_slot(self, value):
        QMessageBox.information(self, "Bro", value)

    def fit_clicked(self):
        sklearn_object = self.sklearn_object.text()
        variable_affected = self.variable_affected.text()
        if len(sklearn_object) == 0:
            return None
        if len(variable_affected) == 0:
            return None
        if variable_affected not in Variable.var_bucket:
            return None
        if sklearn_object not in Variable.var_bucket:
            return None
        if str(type(Variable.var_bucket[variable_affected])) == "<class 'numpy.ndarray'>":
            rows = QInputDialog.getText(self, "Row", "Enter the rows in csv format. Put : for all rows")
            cols = QInputDialog.getText(self, "Column", "Enter the columns in csv format. Put : for all columns")
            rows = rows[0]
            cols = cols[0]
            self.fit_thread = Fit(self.signal, sklearn_object, variable_affected, 0, rows, cols)
            self.fit_thread.start()

    def transform_clicked(self):
        sklearn_object = self.sklearn_object.text()
        variable_affected = self.variable_affected.text()
        if len(sklearn_object) == 0:
            return None
        if len(variable_affected) == 0:
            return None
        if variable_affected not in Variable.var_bucket:
            return None
        if sklearn_object not in Variable.var_bucket:
            return None
        if str(type(Variable.var_bucket[variable_affected])) == "<class 'numpy.ndarray'>":
            rows = QInputDialog.getText(self, "Row", "Enter the rows in csv format. Put : for all rows")
            cols = QInputDialog.getText(self, "Column", "Enter the columns in csv format. Put : for all columns")
            rows = rows[0]
            cols = cols[0]
            self.transform_thread = Transform(self.signal, sklearn_object, variable_affected, 0, rows, cols)
            self.transform_thread.start()

