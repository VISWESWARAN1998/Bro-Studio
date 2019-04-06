# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QTabWidget, QWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtWidgets import QGridLayout, QComboBox, QMessageBox
from PyQt5.QtWidgets import QSpacerItem, QSizePolicy
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.preprocessing.number.missing_value.create_imputer import CreateImputer
from core.preprocessing.number.normalization.create_minmax_scaler import CreateMinMaxScaler


class MissingValueWidget(QWidget):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.missing_value_slot)
        self.create_imputer_thread = None
        main_layout = QVBoxLayout()
        imputer_init_layout = QHBoxLayout()
        imputer_init_layout.addWidget(QLabel("Variable Name for storing \"Imputer\" object:"))
        self.imputer_variable = QLineEdit()
        imputer_init_layout.addWidget(self.imputer_variable)
        main_layout.addLayout(imputer_init_layout)
        main_layout.addWidget(QLabel("Properties:"))
        imputer_properties = QGridLayout()
        imputer_properties.addWidget(QLabel("Missing Value:"), 0, 0)
        self.missing_value = QLineEdit("NaN")
        imputer_properties.addWidget(self.missing_value, 0, 1)
        imputer_properties.addWidget(QLabel("Strategy:"), 1, 0)
        self.strategy = QLineEdit("mean")
        imputer_properties.addWidget(self.strategy, 1, 1)
        imputer_properties.addWidget(QLabel("Axis:"), 2, 0)
        self.axis = QComboBox()
        self.axis.addItems(["0 - column wise", "1 - row wise"])
        imputer_properties.addWidget(self.axis, 2, 1)
        main_layout.addLayout(imputer_properties)
        create_imputer = QPushButton("CREATE IMPUTER")
        create_imputer.clicked.connect(self.create_imputer_clicked)
        main_layout.addWidget(create_imputer)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(main_layout)

    @pyqtSlot(str)
    def missing_value_slot(self, value):
        QMessageBox.information(self, "Bro", value)

    def create_imputer_clicked(self):
        var_name = self.imputer_variable.text()
        if len(var_name) == 0:
            self.signal.emit("Variable name should be of length 1")
            return None
        missing_value = self.missing_value.text()
        strategy = self.strategy.text()
        axis = self.axis.currentIndex()
        self.create_imputer_thread = CreateImputer(self.signal, var_name, missing_value,
                                                   strategy, axis)
        self.create_imputer_thread.start()


class Normalization(QWidget):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.scaler_slot)
        self.create_scaler_thread = None
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Normalize the array"))
        class_grid = QGridLayout()
        class_grid.addWidget(QLabel("MinMaxScaler object:"), 0, 0)
        self.scaler_object = QLineEdit()
        class_grid.addWidget(self.scaler_object, 0, 1)
        class_grid.addWidget(QLabel("Feature Minimum"), 1, 0)
        self.feature_minimum = QLineEdit()
        class_grid.addWidget(self.feature_minimum, 1, 1)
        class_grid.addWidget(QLabel("Feature Maximum"), 2, 0)
        self.feature_maximum = QLineEdit()
        class_grid.addWidget(self.feature_maximum, 2, 1)
        main_layout.addLayout(class_grid)
        create_scaler = QPushButton("CREATE SCALER")
        create_scaler.clicked.connect(self.create_scaler_clicked)
        main_layout.addWidget(create_scaler)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(main_layout)

    @pyqtSlot(str)
    def scaler_slot(self, value):
        QMessageBox.information(self, "Bro Studio", value)

    def create_scaler_clicked(self):
        variable_name = self.scaler_object.text()
        feature_minimum = self.feature_minimum.text()
        feature_maximum = self.feature_maximum.text()
        if len(variable_name) == 0:
            QMessageBox.information(self, "Error", "Length of variable should be atleast one")
        if len(feature_minimum) == 0:
            QMessageBox.information(self, "Error", "Feature minimum is missing")
        if len(feature_maximum) == 0:
            QMessageBox.information(self, "Error", "Feature maximum is missing")
        self.create_scaler_thread = CreateMinMaxScaler(self.signal, variable_name, feature_minimum, feature_maximum)
        self.create_scaler_thread.start()


class PreProcessingNumber(QTabWidget):

    def __init__(self):
        super().__init__()
        self.addTab(MissingValueWidget(), "Missing-Values")
        self.addTab(Normalization(), "Normalization")