# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QWidget, QTabWidget
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt5.QtWidgets import QMessageBox, QComboBox, QCheckBox
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from core.preprocessing.text.create_label_encoder import CreateLabelEncoder
from core.preprocessing.text.create_text_preprocessor import TextPreprocessorThread


class LabelEncoderWidget(QWidget):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.slot)
        self.create_variable_thread = None
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Label encoder will encode the label to numbers"))
        variable_layout = QHBoxLayout()
        variable_layout.addWidget(QLabel("Object name for label encoder: "))
        self.variable_name = QLineEdit()
        variable_layout.addWidget(self.variable_name)
        main_layout.addLayout(variable_layout)
        create_variable = QPushButton("CREATE VARIABLE")
        create_variable.clicked.connect(self.create_variable_clicked)
        main_layout.addWidget(create_variable)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(main_layout)

    @pyqtSlot(str)
    def slot(self, value):
        QMessageBox.information(self, "Bro Studio", value)

    def create_variable_clicked(self):
        variable_name = self.variable_name.text()
        if len(variable_name) == 0:
            self.signal.emit("Length of variable should be at-least one")
            return None
        self.create_variable_thread = CreateLabelEncoder(self.signal, variable_name)
        self.create_variable_thread.start()


class NLPWidget(QWidget):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.signal.connect(self.slot)
        self.create_variable_thread = None
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Choose your tokenizer: "))
        self.tokenizer = QComboBox()
        self.tokenizer.addItems([
            "word_tokenize",
            "TweetTokenizer (preferred)"
        ])
        main_layout.addWidget(self.tokenizer)
        self.keep_only_alphabets = QCheckBox("Remove non-alphabetic words (e.g Punctuation and symbols)")
        self.remove_stopwords = QCheckBox("Remove Stopwords")
        self.remove_user_data = QCheckBox("Remove Username and Hyper-Links")
        main_layout.addWidget(self.keep_only_alphabets)
        main_layout.addWidget(self.remove_stopwords)
        main_layout.addWidget(self.remove_user_data)
        main_layout.addWidget(QLabel("Choose your stemmer:"))
        self.stemmer = QComboBox()
        self.stemmer.addItems([
            "Porter Stemmer"
        ])
        main_layout.addWidget(self.stemmer)
        variable_layout = QHBoxLayout()
        variable_layout.addWidget(QLabel("Name for your pre-processor: "))
        self.variable_name = QLineEdit()
        variable_layout.addWidget(self.variable_name)
        main_layout.addLayout(variable_layout)
        create_variable = QPushButton("CREATE VARIABLE")
        create_variable.clicked.connect(self.create_variable_clicked)
        main_layout.addWidget(create_variable)
        main_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(main_layout)

    @pyqtSlot(str)
    def slot(self, value):
        QMessageBox.information(self, "Bro Studio", value)

    def create_variable_clicked(self):
        variable_name = self.variable_name.text()
        if len(variable_name) == 0:
            self.signal.emit("Variable name should be at-least one!")
            return None
        tokenizer = self.tokenizer.currentIndex()
        alphabets_only = self.keep_only_alphabets.isChecked()
        remove_stopwords = self.remove_stopwords.isChecked()
        remove_user_data = self.remove_user_data.isChecked()
        stemmer = self.stemmer.currentIndex()
        self.create_variable_thread = TextPreprocessorThread(self.signal, variable_name, tokenizer, alphabets_only,
                                                             remove_stopwords, remove_user_data, stemmer)
        self.create_variable_thread.start()


class PreprocessNumpyArray(QWidget):

    def __init__(self):
        super().__init__()


class TextWidget(QTabWidget):

    def __init__(self):
        super().__init__()
        self.addTab(LabelEncoderWidget(), "Label-Encoder")
        self.addTab(NLPWidget(), "NLP using NLTK")
        self.addTab(PreprocessNumpyArray(), "Apply pre-processing")