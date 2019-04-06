# SWAMI KARUPPASWAMI THUNNAI

import os
import glob
import cv2
from PyQt5.QtCore import QThread


class PreProcessImageThread(QThread):

    def __init__(self, signal, directory, convert_grayscale, should_resize, size=None):
        """
        Constructor to initialize the instance variables.

        :param signal: The signal which is used to communicate to the GUI.

        :param directory: The directory of images.

        :param convert_grayscale: Should convert the image to gray-scale.

        :param should_resize: Should resize.

        :param size: If we need to resize then the size.
        """
        QThread.__init__(self)
        self.signal = signal
        self.directory = directory
        self.convert_grayscale = convert_grayscale
        self.should_resize = should_resize
        self.size = size

    def run(self):
        files = glob.glob(os.path.join(self.directory, "/*.*"))
        self.signal.emit(
            {
                "percentage": 0
            }
        )
        for count, file in enumerate(files):
            try:
                self.preprocess_file(file)
            except cv2.error as e:
                print(e)
            finally:
                completed_percentage = (count / len(files)) * 100
                self.signal.emit(
                    {
                        "percentage": completed_percentage,
                        "file": file
                    }
                )
        self.signal.emit(
            {
                "percentage": 100
            }
        )

    def preprocess_file(self, file):
        image = cv2.imread(file)
        if self.convert_grayscale:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        if self.should_resize:
            image = cv2.resize(image, self.size)
        cv2.imwrite(file, image)