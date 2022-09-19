import re
import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect
from PyQt5.QtCore import QSize

from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QTextFormat

from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

from Shyosai.ShyosaiWidgets import QLineNumberWidget


class ShyosaiWorkingAreaWidget(QWidget):

    def __init__(self):
        super(ShyosaiWorkingAreaWidget, self).__init__()

        base_layout = QVBoxLayout()
        working_layout = QHBoxLayout()

        tab_widget = QTabWidget()
        #TODO: remove empty widgets from tabs
        commit_tree_tab = tab_widget.addTab(QWidget(), 'Commit Tree')
        git_tab = tab_widget.addTab(QWidget(), 'Git')

        self.__text_area = QTextEdit()
        self.__line_number = QLineNumberWidget(self.__text_area)
        self.__text_area.textChanged.connect(self.__text_area_text_changed)

        working_layout.addWidget(tab_widget)
        working_layout.addWidget(self.__line_number)
        working_layout.addWidget(self.__text_area)
        
        base_layout.addLayout(working_layout)
        base_layout.addWidget(self.__text_area)
        self.setLayout(base_layout)

    def __text_area_text_changed(self):
        if self.__line_number:
            n = int(self.__text_area.document().lineCount())
            self.__line_number.changeLineCount(n)


class ShyosaiGUI(QMainWindow):

    def __init__(self)-> None:
        super(ShyosaiGUI, self).__init__()
        self.setWindowTitle('Shyosai')

        self.__initialize_menu_bar()
        working_area = ShyosaiWorkingAreaWidget()
        self.setCentralWidget(working_area)
        self.showMaximized()

    # Private

    def __initialize_menu_bar(self):
        menu_bar = QMenuBar()

        file_menu = menu_bar.addMenu('File')
        new_action = file_menu.addAction('New')
        open_action = file_menu.addAction('Open')
        open_dir_action = file_menu.addAction('Open Directory')
        recent_action = file_menu.addAction('Recent')
        file_menu.addSeparator()
        save_action = file_menu.addAction('Save')
        saveas_action = file_menu.addAction('Save As')
        file_menu.addSeparator()
        close_action = file_menu.addAction('Close')
        file_menu.addSeparator()
        quit_action = file_menu.addAction('Quit')

        edit_menu = menu_bar.addMenu('Edit')
        git_menu = menu_bar.addMenu('Git')

        self.setMenuBar(menu_bar)

    # Public


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_gui = ShyosaiGUI()
    app_gui.show()
    app.exec_()