import sys
sys.path.insert(0, 'C:/Users/winte/source/repos/Nyarstot/GitShyosai')

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView

from Shyosai.Utils.ShyosaiDateTime import ShyosaiDateTime


class GitGraphWidget(QTableWidget):

    def __init__(self, a_sBranches:list=[], a_stParent=None)->None:
        super(GitGraphWidget, self).__init__(a_stParent)
        self.__m_sBranches = a_sBranches

        self.setRowCount(1)
        self.setColumnCount(2)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setDefaultSectionSize(500)

        self.__m_stTimeline = Timeline(self.__m_sBranches)
        self.__m_stRepoInfo = RepoInfoItemWidget(a_sBranches=self.__m_sBranches)

        self.setCellWidget(0, 0, self.__m_stRepoInfo)
        self.setCellWidget(0, 1, self.__m_stTimeline)


class Timeline(QTableWidget):

    def __init__(self, a_sBranches:list=[], a_stParent=None)-> None:
        super(Timeline, self).__init__(a_stParent)
        self.__m_sBranches = a_sBranches

        # self.horizontalHeader().setDefaultSectionSize(1200)
        self.verticalHeader().setDefaultSectionSize(500)
        self.verticalHeader().setVisible(False)
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


class RepoInfoItemWidget(QTableWidget):

    def __init__(self, a_sRepoName:str='Untitled', a_sBranches:list=[], a_stParent=None):
        super(RepoInfoItemWidget, self).__init__(a_stParent)
        self.__m_sRepoName = a_sRepoName
        self.__m_sBranches = a_sBranches

        self.setColumnCount(1)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setFixedHeight(47)
        self.horizontalHeader().setStretchLastSection(True)
        self.setHorizontalHeaderItem(0, QTableWidgetItem(self.__m_sRepoName))

        self.__init_ui()

    def __init_ui(self):
        self.setRowCount(len(self.__m_sBranches))

        for i in range(self.rowCount()):
            item = QTableWidgetItem(self.__m_sBranches[i])
            item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.setItem(i, 0, item)


if __name__ == "__main__":
    branches = ['master', 'dev', 'old-state']
    app = QApplication(sys.argv)
    gui = GitGraphWidget(branches)
    gui.show()
    app.exec_()

