import sys
sys.path.insert(0, 'C:/Users/winte/source/repos/Nyarstot/GitShyosai')

from PyQt5.QtCore import QSize

from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView

from Shyosai.Utils.ShyosaiDateTime import ShyosaiDateTime


class ShyosaiTimeline(QTableWidget):

    def __init__(self, a_sBranches:list=[], a_stParent=None)-> None:
        super(ShyosaiTimeline, self).__init__(a_stParent)
        self.__m_sBranches = a_sBranches

        # self.horizontalHeader().setDefaultSectionSize(1200)
        self.verticalHeader().setDefaultSectionSize(500)
        self.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.setShowGrid(False)

        self.__draw_timeline()

    def __draw_timeline(self):
        date_handler = ShyosaiDateTime()
        current_year = date_handler.current_year()

        self.setRowCount(1)
        self.setColumnCount(13)

        for i in range(0, self.columnCount()):
            month_num = ((i + 1) % 12) if ((i + 1) % 12 != 0) else 12
            month_name = date_handler.get_month_name(month_num)
            month_timeline = MonthItemWidget(current_year, month_num, self.__m_sBranches, a_stParent=self)

            self.setHorizontalHeaderItem(i, QTableWidgetItem(month_name))
            self.setColumnWidth(i, month_timeline.total_column_width())
            self.setCellWidget(0, i, month_timeline)


class MonthItemWidget(QTableWidget):

    def __init__(self, a_nYear:int=0, a_nMonthNumber:int=0, a_sBranches:list=[], a_stParent=None)->None:
        super(MonthItemWidget, self).__init__(a_stParent)
        self.__m_stDateHandler = ShyosaiDateTime()
        self.m_nYear = a_nYear
        self.m_nMonthNumber = a_nMonthNumber
        self.m_sMontName = self.__m_stDateHandler.get_month_name(a_nMonthNumber)
        self.m_nDayCount = self.__m_stDateHandler.days_in_month(a_nYear, a_nMonthNumber)
        self.m_sBranches = a_sBranches

        self.horizontalHeader().setDefaultSectionSize(1)
        self.verticalHeader().setVisible(False)

        self.__draw_timeline()

    def __draw_timeline(self):
        self.setRowCount(len(self.m_sBranches))
        self.setColumnCount(self.m_nDayCount)

    def total_column_width(self):
        total_width = 2
        for i in range(self.columnCount()):
            total_width += self.columnWidth(i)
        return total_width


class InfoItemWidget(QTableWidget):

    def __init__(self, a_sBranches:list=[], a_stParent=None):
        super(InfoItemWidget, self).__init__(a_stParent)
        self.__m_sBranches = a_sBranches

    def __draw_timeline(self):
        self.setRowCount(len(self.__m_sBranches))
        self.setColumnCount(1)


if __name__ == "__main__":
    branches = ['master', 'dev', 'old-state']
    app = QApplication(sys.argv)
    gui = ShyosaiTimeline(branches)
    gui.show()
    app.exec_()
