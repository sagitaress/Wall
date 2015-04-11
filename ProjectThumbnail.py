__author__ = 'Faaiz'
import sys
import psycopg2
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import*

class ProjectThumbnail(QWidget):
    def __init__(self,system,par,project):
        QWidget.__init__(self,par)
        self.system = system
        self.project = project
        self.par = par
        loader=QUiLoader()
        self.dialog = loader.load("./ProjectThumb.ui",None)
        label = self.dialog.findChild(QLabel,"label")
        label.setText(project.name)
        layout = QVBoxLayout()
        layout.addWidget(self.dialog)
        self.setLayout(layout)
        #self.dialog.clicked.connect(self.openProject)

    def openProject(self):
        self.par.openProject(self.project)

    def mousePressEvent(self, *args, **kwargs):
        self.openProject()