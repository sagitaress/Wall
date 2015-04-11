__author__ = 'Faaiz'
import sys
import psycopg2
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from ProjectThumbnail import *
from Project import *
from WallObserver import*

class WallPage(QMainWindow,WallObserver):
    def __init__(self,system):
        QMainWindow.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        self.setWindowTitle("Wall")
        loader=QUiLoader()
        self.dialog = loader.load("./WallPage.ui",None)
        self.insideLayout = QGridLayout()
        self.setCentralWidget(self.dialog)
        self.name = self.dialog.findChild(QLabel,"name")
        self.thumbnailFrame = self.dialog.findChild(QFrame,"thumbnailFrame")
        self.projectArea = self.dialog.findChild(QScrollArea,"projectArea")
        self.projectArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.addProjectBt = self.dialog.findChild(QPushButton,"addProjectBt")

        self.addProjectBt.clicked.connect(self.addProject)

        widget = QWidget()
        widget.setLayout(self.insideLayout)
        self.projectArea.setWidget(widget)

        layout = QVBoxLayout(self.thumbnailFrame)
        layout.addWidget(self.projectArea)

        self.thumbnailFrame.setLayout(layout)
        #for i in range(20):
            #self.insideLayout.addWidget(ProjectThumbnail(self).getDialog(),i//3,i%3)

    def update(self, directory, error, wall, project):
        if directory == "WallPage":
            name = wall.owner.firstname+" "+ wall.owner.lastname
            self.name.setText(name)
            for i in range (len(wall.projects)):
                self.insideLayout.addWidget(ProjectThumbnail(self.system,self,wall.projects[i]),i//3,i%3)
            self.show()

    def addProject(self):
        self.system.addProject(Project("New Project"))

    def openProject(self,p):
        self.hide()
        self.system.openProject(p)