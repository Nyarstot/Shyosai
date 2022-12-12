import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

from Shyosai.Widgets.Timeline import Timeline
from Shyosai.Widgets.NumberedTextBrowser import NumberedTextBrowserWidget


class ShyosaiMainUIWidget(QWidget):

    def __init__(self, a_stParent=None)-> None:
        super(ShyosaiMainUIWidget, self).__init__(parent=a_stParent)


class ShyosaiMainWindow(QMainWindow):

    def __init__(self)-> None:
        super(ShyosaiMainWindow, self).__init__()
        self.setWindowTitle('Shyosai')


if __name__ == "__main__":
    appInstance = QApplication(sys.argv)
    appWindow = ShyosaiMainWindow()
    appWindow.show()
    appInstance.exec_()