import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
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

from Shyosai.Utils.CssFileToStr import Css2String
from Shyosai.Widgets.ConsoleLogArea import Console
from Shyosai.Widgets.Timeline import GitGraphWidget
from Shyosai.Widgets.BaseWidgets import ShyosaiDockWidget
from Shyosai.Widgets.NumberedTextBrowser import NumberedTextBrowserWidget


class ShyosaiMainUIWidget(QWidget):

    def __init__(self, a_stParent=None)-> None:
        super(ShyosaiMainUIWidget, self).__init__(parent=a_stParent)
        self.__m_lytBaseLayout = QVBoxLayout()
        self.__m_lytWorkingLayout = QHBoxLayout()

        textBrowser = NumberedTextBrowserWidget()
        commitBrowser = NumberedTextBrowserWidget()
        splitter = QSplitter()

        splitter.addWidget(textBrowser)
        splitter.addWidget(commitBrowser)

        self.__m_lytWorkingLayout.addWidget(splitter)
        self.__m_lytBaseLayout.addLayout(self.__m_lytWorkingLayout)
        self.setLayout(self.__m_lytBaseLayout)


class ShyosaiMainWindow(QMainWindow):

    def __init__(self)-> None:
        super(ShyosaiMainWindow, self).__init__()
        self.setWindowTitle('Shyosai')

        self.__m_stMainUIWIdget = ShyosaiMainUIWidget()

        self.setCentralWidget(self.__m_stMainUIWIdget)

        self.__initializeMenuBar()
        self.__initializeDockWidgets()
        self.__styleInitialize()
        self.showMaximized()

    # Private

    def __initializeMenuBar(self):
        self.__m_stMenuBar = QMenuBar()

        fileMenu = self.__m_stMenuBar.addMenu('File')
        createRepoAction = fileMenu.addAction('Create Repository')
        openRepoAction = fileMenu.addAction('Open Repository')
        closeRepositoryAction = fileMenu.addAction('Close Repository')
        fileMenu.addSeparator()
        recentAction = fileMenu.addAction('Recent')
        quitAction = fileMenu.addAction('Quit')

        self.setMenuBar(self.__m_stMenuBar)

    def __initializeDockWidgets(self):
        consoleDock = ShyosaiDockWidget('Console Log')
        repoGraphDock = ShyosaiDockWidget('Tree View')

        graphView = GitGraphWidget('Shyosai', ['master', 'dev'])
        consoleLog = Console()

        consoleDock.setWidget(consoleLog)
        repoGraphDock.setWidget(graphView)

        self.addDockWidget(Qt.BottomDockWidgetArea, consoleDock)
        self.addDockWidget(Qt.BottomDockWidgetArea, repoGraphDock)

    def __styleInitialize(self):
        self.setStyleSheet(Css2String.read('Shyosai/Styles/test.css'))



if __name__ == "__main__":
    appInstance = QApplication(sys.argv)
    appWindow = ShyosaiMainWindow()
    appWindow.show()
    appInstance.exec_()