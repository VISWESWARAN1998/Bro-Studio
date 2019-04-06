# SWAMI KARUPPASWAMI THUNNAI

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTabWidget, QAction
from PyQt5.QtWidgets import QMessageBox
# Import all the necessary GUI widgets to display
from gui.data_frame import DataFrameWidget
from gui.variable_explorer.display_variable import DisplayVariableWidget
from gui.variable_explorer.df_viewer import DFViewerWidget
from gui.preprocessing import PreProcessing
from gui.ml import MLWidget


class BroWidget(QTabWidget):

    def __init__(self):
        super().__init__()
        self.addTab(DataFrameWidget(), "Data-Frame")
        self.addTab(PreProcessing(), "Pre-Processing")
        self.addTab(MLWidget(), "ML")


class BroWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # Widgets initialization
        self.display_variable_widget = None
        self.df_display_widget = None
        self.setWindowTitle("Bro Studio")
        self.setGeometry(300, 300, 800, 600)
        menu_bar = self.menuBar()
        # VARIABLE EXPLORER
        variable_explorer = menu_bar.addMenu("Variable Explorer")
        display_variable = QAction("Variable viewer", self)
        display_variable.triggered.connect(self.display_variable_triggered)
        display_variable.setShortcut("Alt+V")
        variable_explorer.addAction(display_variable)
        df_viewer = QAction("DF-Viewer", self)
        df_viewer.setShortcut("Alt+D")
        df_viewer.triggered.connect(self.display_df_triggered)
        variable_explorer.addAction(df_viewer)
        # HELP
        _help = menu_bar.addMenu("Help")
        about = QAction("About", self)
        about.triggered.connect(self.about_triggered)
        _help.addAction(about)
        self.setCentralWidget(BroWidget())

    def display_variable_triggered(self):
        self.display_variable_widget = DisplayVariableWidget()
        self.display_variable_widget.show()

    def display_df_triggered(self):
        self.df_display_widget = DFViewerWidget()
        self.df_display_widget.show()

    def about_triggered(self):
        QMessageBox.information(self, "Bro Studio", "Programmed with <3 by Visweswaran")


if __name__ == "__main__":
    bro_application = QApplication(sys.argv)
    bro_window = BroWindow()
    bro_window.show()
    sys.exit(bro_application.exec())