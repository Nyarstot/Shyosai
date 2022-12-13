from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextBrowser


class Console(QTextEdit):

    def __init__(self, a_stParent=None)-> None:
        super(Console, self).__init__(parent=a_stParent)
        self.setReadOnly(True)