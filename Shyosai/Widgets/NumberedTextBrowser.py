from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFontMetricsF

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextBrowser


class NumberedTextBrowserWidget(QWidget):

    def __init__(self, a_stParent=None)-> None:
        super(NumberedTextBrowserWidget, self).__init__(parent=a_stParent)
        self.__m_lytWidgetLayout = QHBoxLayout()

        self.__m_stTextArea = QTextEdit()
        self.__m_stNumberLine = NumberLine(self.__m_stTextArea)

        self.__m_stTextArea.textChanged.connect(self.__textChanged)

        self.__m_lytWidgetLayout.addWidget(self.__m_stNumberLine)
        self.__m_lytWidgetLayout.addWidget(self.__m_stTextArea)
        self.setLayout(self.__m_lytWidgetLayout)

    # Private

    def __calcTabDistance(self):
        font = self.__m_stTextArea.font()
        fontMetric = QFontMetricsF(font)
        spaceWidth = fontMetric.width(' ')
        self.__m_stTextArea.setTabStopDistance(spaceWidth*4)

    def __textChanged(self):
        if self.__m_stNumberLine:
            currLineCount = int(self.__m_stTextArea.document().lineCount())
            self.__m_stNumberLine.changeLineCount(currLineCount)

    # Public

    def document(self):
        return self.__m_stTextArea.document()


class NumberLine(QTextBrowser):

    def __init__(self, a_stParent=None)-> None:
        super(NumberLine, self).__init__(parent=a_stParent)

        self.__m_nLineCount = a_stParent.document().lineCount()
        self.__m_nFontSize = int(a_stParent.font().pointSizeF())

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalScrollBar().setEnabled(False)

        self.verticalScrollBar().valueChanged.connect(self.__parentWidgetScrollChanged)

        self.__styleInitialize()
        self.__initializeLineCount()


    # Private

    def __parentWidgetScrollChanged(self, a_Value):
        self.verticalScrollBar().setValue(a_Value)

    def __initializeLineCount(self):
        for line in range(1, self.__m_nLineCount + 1):
            self.append(str(line))

    def __styleInitialize(self):
        self.__m_Style = 'background: transparent;\
                          border: none;\
                          color: #AAA;\
                          font: {self.__m_nFontSize}pt;'
        self.setStyleSheet(self.__m_Style)
        self.setFixedWidth(self.__m_nFontSize*5)

    # Public

    def changeLineCount(self, a_nValue:int):
        _max = max(self.__m_nLineCount, a_nValue)
        diff = a_nValue - self.__m_nLineCount
        if _max == self.__m_nLineCount:
            firstValue = self.verticalScrollBar().value()
            for i in range(self.__m_nLineCount, self.__m_nLineCount + diff, -1):
                self.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
                self.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                self.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
                self.textCursor().removeSelectedText()
                self.textCursor().deletePreviousChar()
            lastValue = self.verticalScrollBar().value()
            if abs(firstValue - lastValue) != 2:
                self.verticalScrollBar().setValue(firstValue)
        else:
            for i in range(self.__m_nLineCount, self.__m_nLineCount + diff, 1):
                self.append(str(i + 1))
        self.__m_nLineCount = a_nValue

    def setValue(self, a_Value):
        self.verticalScrollBar().setValue(a_Value)

    def setFontSize(self, a_nSize:int):
        self.__m_nFontSize = int(a_nSize)
        self.__styleInitialize()

