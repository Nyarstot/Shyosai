from PyQt5.QtCore import Qt

from PyQt5.QtGui import QFont
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QTextBrowser


class QLineNumberWidget(QTextBrowser):
    def __init__(self, parent=None)-> None:
        super(QLineNumberWidget, self).__init__()
        super().__init__()

        self.__line_count = parent.document().lineCount()
        self.__size = int(parent.font().pointSizeF())
        self.__styleInit()

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalScrollBar().setEnabled(False)
        self.verticalScrollBar().valueChanged.connect(self.__parentWidgetScrollChanged)

        self.__initializeLineCount()

    # Private

    def __parentWidgetScrollChanged(self, val):
        self.verticalScrollBar().setValue(val)

    def __initializeLineCount(self):
        for line in range(1, self.__line_count + 1):
            self.append(str(line))

    def __styleInit(self):
        self.__style = 'background: transparent;\
                        border: none;\
                        color: #AAA;\
                        font: {self.__size}pt;'
        self.setStyleSheet(self.__style)
        self.setFixedWidth(self.__size*5)

    # Public

    def changeLineCount(self, val):
        _max = max(self.__line_count, val)
        diff = val - self.__line_count
        if _max == self.__line_count:
            first_value = self.verticalScrollBar().value()
            for i in range(self.__line_count, self.__line_count + diff, -1):
                self.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
                self.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                self.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
                self.textCursor().removeSelectedText()
                self.textCursor().deletePreviousChar()
            last_value = self.verticalScrollBar().value()
            if abs(first_value - last_value) != 2:
                self.verticalScrollBar().setValue(first_value)
        else:
            for i in range(self.__line_count, self.__line_count + diff, 1):
                self.append(str(i + 1))
        self.__line_count = val

    def setValue(self, val):
        self.verticalScrollBar().setValue(val)

    def setFontSize(self, size:float):
        self.__size = int(size)
        self.__styleInit()
