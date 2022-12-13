import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import QAbstractItemModel

from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication

class DirviewWidget(QTreeView):

    def __init__(self, a_stParent:QWidget=None)-> None:
        super(DirviewWidget, self).__init__(parent=a_stParent)
        self.items = []

        for i in 'abc':
            self.items.append(ShyosaiGitDirviewNode(i))
            self.items[-1].addChild(ShyosaiGitDirviewNode(['g', 'e', 'f']))
            self.items[-1].addChild(ShyosaiGitDirviewNode(['d', 'c', 'z']))

        self.tw = QTreeView()
        self.tw.setModel(ShyosaiDirviewItemModel(self.items))


class ShyosaiGitDirviewNode(object):

    def __init__(self, a_stData:list)-> None:
        self.__m_sData = a_stData

        if type(a_stData) == tuple:
            self.__m_sData = list(a_stData)
        if type(a_stData) is str or not hasattr(a_stData, '__getitem__'):
            self.__m_sData = [a_stData]

        self.__m_nColumnCount = len(self.__m_sData)
        self.__m_stChildrens = []
        self.__m_stParent = None
        self.__m_nRow = 0

    # Public

    def data(self, a_nColumn:int):
        if a_nColumn >= 0 and a_nColumn < len(self.__m_sData):
            return self.__m_sData[a_nColumn]

    def columnCount(self)-> int:
        return self.__m_nColumnCount

    def childCount(self)-> int:
        return len(self.__m_stChildrens)

    def child(self, a_nRow:int):
        if a_nRow >= 0 and a_nRow < self.childCount():
            return self.__m_stChildrens[a_nRow]

    def parent(self):
        return self.__m_stParent

    def row(self):
        return self.__m_nRow

    def addChild(self, a_stChild):
        a_stChild.__m_stParent = self
        a_stChild.__m_nRow = len(self.__m_stChildrens)
        self.__m_stChildrens.append(a_stChild)
        self.__m_nColumnCount = max(a_stChild.columnCount(), self.__m_nColumnCount)


class ShyosaiDirviewItemModel(QAbstractItemModel):

    def __init__(self, a_stNodes:list, a_stParent:QWidget=None)-> None:
        super(ShyosaiDirviewItemModel, self).__init__(parent=a_stParent)
        self.__m_stRoot = ShyosaiGitDirviewNode(None)
        for node in a_stNodes:
            self.__m_stRoot.addChild(node)

    def rowCount(self, a_stIndex:QModelIndex)-> int:
        if a_stIndex.isValid():
            return a_stIndex.internalPointer().childCount()
        return self.__m_stRoot.childCount()

    def addChild(self, a_stNode, a_stParent):
        if not a_stParent or not a_stParent.isValid():
            parent = self.__m_stRoot
        else:
            parent = a_stParent.internalPointer()
        parent.addChild(a_stNode)

    def index(self, a_nRow:int, a_nColumn:int, a_stParent=None):
        if not a_stParent or not a_stParent.isValid():
            parent = self.__m_stRoot
        else:
            parent = a_stParent.internalPointer()

        if not QAbstractItemModel.hasIndex(self, a_nRow, a_nColumn, a_stParent):
            return QModelIndex()

        child = parent.child(a_nRow)
        if child:
            return QAbstractItemModel.createIndex(self, a_nRow, a_nColumn, child)
        else:
            return QModelIndex()

    def parent(self, a_stIndex:QModelIndex)-> QModelIndex:
        if a_stIndex.isValid():
            parent = a_stIndex.internalPointer().parent()
            if parent:
                return QAbstractItemModel.createIndex(self, parent.row(), 0, parent)
        return QModelIndex()

    def columnCount(self, a_stIndex:QModelIndex)-> int:
        if a_stIndex.isValid():
            return a_stIndex.internalPointer().columnCount()
        return self.__m_stRoot.columnCount()

    def data(self, a_stIndex:QModelIndex, a_stRole):
        if not a_stIndex.isValid():
            return None
        node = a_stIndex.internalPointer()
        if a_stRole == Qt.DisplayRole:
            return node.data(a_stIndex.column())
        return None


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mt = DirviewWidget()
    mt.tw.show()
    app.exec_()