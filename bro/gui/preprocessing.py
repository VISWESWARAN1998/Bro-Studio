# SWAMI KARUPPASWAMI THUNNAI

from PyQt5.QtWidgets import QTabWidget
from gui.preprocessing_widget.number import PreProcessingNumber
from gui.preprocessing_widget.fittransform import FitTransform
from gui.preprocessing_widget.text import TextWidget
from gui.preprocessing_widget.image import ImageWidget


class PreProcessing(QTabWidget):
    """
    Pre-processing tab
    """

    def __init__(self):
        super().__init__()
        self.addTab(PreProcessingNumber(), "Number")
        self.addTab(TextWidget(), "Text")
        self.addTab(ImageWidget(), "Image")
        self.addTab(FitTransform(), "sklearn Fit-Transform")