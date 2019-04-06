# SWAMI KARUPPASWAMI THUNNAI

import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtWidgets import QProgressBar, QListWidget, QFileDialog
from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.preprocessing.image.preprocess import PreProcessImageThread


class ImageWidget(QWidget):

    signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.slot)
        self.image_thread = None
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Pre-process Image"))
        image_path_layout = QHBoxLayout()
        self.image_path = QLineEdit()
        image_path_layout.addWidget(self.image_path)
        choose_directory = QPushButton("CHOOSE IMAGES DIRECTORY")
        choose_directory.clicked.connect(self.preprocess)
        image_path_layout.addWidget(choose_directory)
        main_layout.addLayout(image_path_layout)
        options_layout = QHBoxLayout()
        self.should_resize = QCheckBox("resize")
        self.convert_grayscale = QCheckBox("grayscale")
        options_layout.addWidget(self.should_resize)
        options_layout.addWidget(self.convert_grayscale)
        main_layout.addLayout(options_layout)
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        main_layout.addWidget(self.progress)
        self.status_list = QListWidget()
        main_layout.addWidget(self.status_list)
        self.setLayout(main_layout)

    @pyqtSlot(dict)
    def slot(self, value):
        if value["percentage"] == 0:
            self.progress.setVisible(True)
            self.progress.setValue(0)
        elif value["percentage"] == 100:
            self.progress.setVisible(False)
        else:
            self.progress.setValue(value["percentage"])
            self.status_list.addItem(value["file"])

    def preprocess(self):
        directory = QFileDialog.getExistingDirectory(self, "Choose your images directory")
        self.image_path.setText(directory)
        if not os.path.exists(directory):
            QMessageBox.information(self, "Bro Studio", "Directory does not exists")
            return None
        should_resize = self.should_resize.isChecked()
        convert_grayscale = self.convert_grayscale.isChecked()
        if should_resize:
            width = QInputDialog.getInt(self, "Resize", "Enter the width")
            height = QInputDialog.getInt(self, "Resize", "Enter the height")
            width = width[0]
            height = height[0]
            print((width, height))
            self.image_thread = PreProcessImageThread(self.signal, directory, convert_grayscale, should_resize,
                                                      size=(width, height))
        else:
            self.image_thread = PreProcessImageThread(self.signal, directory, convert_grayscale, should_resize)
        self.image_thread.start()
