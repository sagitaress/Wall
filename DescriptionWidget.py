__author__ = 'Faaiz'

from PySide.QtGui import *
from PySide.QtUiTools import*

class DescriptionWidget(QWidget):
    def __init__(self,par):
        QWidget.__init__(self,par)
        self.par = par
        loader=QUiLoader()
        self.dialog = loader.load("./descriptionWidget.ui",None)
        label = self.dialog.findChild(QLabel,"label")
        layout = QVBoxLayout()
        layout.addWidget(self.dialog)
        self.setLayout(layout)
        #self.dialog.clicked.connect(self.openProject)
