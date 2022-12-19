import sys

from git import Repo
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog


class CommitTextEdit(QWidget):

    def __init__(self, a_stParent:QWidget=None):
        super(CommitTextEdit, self).__init__(parent=a_stParent)
        self.__init_edits()

    def __init_edits(self):
        self.m_lutVBoxLayout = QVBoxLayout()
        self.m_lytEditsLayout = QHBoxLayout()
        self.m_lytEditsLayout_2 = QHBoxLayout()
        self.m_lytEditsLayout_3 = QHBoxLayout()

        self.text_edit = QLineEdit()
        self.description_label = QLabel('Description: ')
        self.description_label.setFixedWidth(60)
        self.m_lytEditsLayout.addWidget(self.description_label)
        self.m_lytEditsLayout.addWidget(self.text_edit)

        self.detail_label = QLabel('Details: ')
        self.detail_label.setFixedWidth(60)
        self.details_edit = QLineEdit()
        self.m_lytEditsLayout_2.addWidget(self.detail_label)
        self.m_lytEditsLayout_2.addWidget(self.details_edit)

        self.add_button = QPushButton('+')
        self.add_button.clicked.connect(self.__add_button_clicked)
        self.m_lutVBoxLayout.addLayout(self.m_lytEditsLayout)
        self.m_lutVBoxLayout.addLayout(self.m_lytEditsLayout_2)

        self.m_lytEditsLayout_3.addLayout(self.m_lutVBoxLayout)
        self.m_lytEditsLayout_3.addWidget(self.add_button)
        self.setLayout(self.m_lytEditsLayout_3)

    def __add_button_clicked(self):
        self.details_edit.setEnabled(False)
        self.text_edit.setEnabled(False)
        self.add_button.hide()

    def hide_add_button(self):
        self.add_button.hide()

    def show_add_button(self):
        self.add_button.show()

    def get_description_text(self):
        return self.text_edit.text()

    def get_details_text(self):
        return self.details_edit.text()


class GitCommitWidget(QWidget):

    def __init__(self, a_stParent:QWidget=None):
        super(GitCommitWidget, self).__init__(parent=a_stParent)
        self.layout = QVBoxLayout()
        self.m_repo = ""

        self.commit_title = QLineEdit()
        self.label_1 = QLabel("Fixed")
        self.label_2 = QLabel("Removed")
        self.label_3 = QLabel("Added")
        self.label_4 = QLabel("Note")

        self.text_edit_1 = QTextEdit()
        self.text_edit_2 = QTextEdit()
        self.text_edit_3 = QTextEdit()
        self.text_edit_4 = QTextEdit()
        self.button_push = QPushButton("Push")
        self.button_push.clicked.connect(self.__click)

        self.layout.addWidget(self.commit_title)
        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.text_edit_1)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.text_edit_2)
        self.layout.addWidget(self.label_3)
        self.layout.addWidget(self.text_edit_3)
        self.layout.addWidget(self.label_4)
        self.layout.addWidget(self.text_edit_4)
        self.layout.addWidget(self.button_push)
        self.setLayout(self.layout)
    
    def __click(self):
        commit = ""
        commit += self.commit_title.text()
        commit += "\nFixed \n"
        commit += self.text_edit_1.toPlainText() + "\n"
        commit += "\nRemoved \n"
        commit += self.text_edit_2.toPlainText() + "\n"
        commit += "\nAdded \n"
        commit += self.text_edit_3.toPlainText() + "\n"
        commit += "\nNoted \n"
        commit += self.text_edit_4.toPlainText() + "\n"
        commit += "\n"
        
        self.m_repo
        repo = Repo(self.m_repo)
        repo.git.execute("git add .")
        repo.git.execute("git commit -m \"{}\"".format(commit))
        repo.git.execute("git push origin main")
        # repo.execute("git commit -m \"{}\"".format(commit))

    def set_repo(self, repo):
        self.m_repo = repo

class MainWindow(QMainWindow):

    def __init__(self, a_stParent:QWidget=None):
        super(MainWindow, self).__init__(parent=a_stParent)
        self.setWindowTitle('Git Commit Test')
        self.setMinimumSize(600, 500)

        menuBar = QMenuBar()
        menu = menuBar.addMenu("File")
        act = menu.addAction("Open Repo", self.__open_dialog)
        self.setMenuBar(menuBar)

        self.work_area = GitCommitWidget()
        self.setCentralWidget(self.work_area)

    def __open_dialog(self):
        dir = QFileDialog.getExistingDirectory()
        dir.replace("\\", "/")
        dir.encode("utf-8")
        self.work_area.set_repo(dir)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = MainWindow()
    gui.show()
    app.exec_()