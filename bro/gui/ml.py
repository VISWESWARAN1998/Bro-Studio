# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QComboBox, QListWidget
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.ml.build_ml import BuildML


class MLWidget(QWidget):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.build_thread = None
        self.signal.connect(self.slot)
        main_layout = QVBoxLayout()
        variable_layout = QGridLayout()
        variable_layout.addWidget(QLabel("X"), 0, 0)
        self.x = QLineEdit()
        variable_layout.addWidget(self.x, 0, 1)
        variable_layout.addWidget(QLabel("y"), 1, 0)
        self.y = QLineEdit()
        variable_layout.addWidget(self.y, 1, 1)
        variable_layout.addWidget(QLabel("Model name:"), 2, 0)
        self.model_name = QLineEdit()
        variable_layout.addWidget(self.model_name, 2, 1)
        main_layout.addLayout(variable_layout)
        self.model = QComboBox()
        self.model.addItems(
            [
                "Linear Regression",
                "Logistic Regression",
                "Gaussian Naive Bayes",
                "Support Vector Classifier"
            ]
        )
        main_layout.addWidget(self.model)
        fit = QPushButton("FIT")
        fit.clicked.connect(self.fit_clicked)
        main_layout.addWidget(fit)
        self.process_display = QListWidget()
        main_layout.addWidget(self.process_display)
        self.setLayout(main_layout)

    @pyqtSlot(str)
    def slot(self, value):
        self.process_display.addItem(value)

    def fit_clicked(self):
        X = self.x.text()
        y = self.y.text()
        model_name = self.model_name.text()
        model = self.model.currentIndex()
        if len(X) == 0:
            self.signal.emit("length of X needs to be at-least one!")
        if len(y) == 0:
            self.signal.emit("length of y needs to be at-least one!")
        if len(model_name) == 0:
            self.signal.emit("Model name length invalid!")
        self.build_thread = BuildML(self.signal, X, y, model, model_name)
        self.build_thread.start()
