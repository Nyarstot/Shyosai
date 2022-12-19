from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDockWidget


class ShyosaiDockWidget(QDockWidget):

    def __init__(self, a_sTitle:str='', a_stParent:QWidget=None)-> None:
        super(ShyosaiDockWidget, self).__init__(parent=a_stParent)
        self.setWindowTitle(a_sTitle)
        self.__styleInitialize()

    # Private

    def __styleInitialize(self):
        self.__m_sStyle = ''
        self.setStyleSheet(self.__m_sStyle)
