__author__ = 'Faaiz'
import sys
import psycopg2
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from WallObserver import *


class SignupPage(QMainWindow,WallObserver):
    def __init__(self,system):
        QMainWindow.__init__(self,None)
        self.setWindowTitle("SignupPage")
        self.system = system
        self.system.addObserver(self)
        loader=QUiLoader()
        self.dialog = loader.load("./SignupPage.ui",None)
        self.setMinimumSize(800, 600)
        self.setMaximumSize(800, 600)
        self.confirmButton = self.dialog.findChild(QPushButton,"confirmBt")
        self.usernameText = self.dialog.findChild(QLineEdit,"usernameText")
        self.passwordText = self.dialog.findChild(QLineEdit,"passwordText")
        self.confirmText = self.dialog.findChild(QLineEdit,"confirmText")
        self.firstnameText = self.dialog.findChild(QLineEdit,"firstnameText")
        self.lastnameText = self.dialog.findChild(QLineEdit,"lastnameText")
        self.emailText = self.dialog.findChild(QLineEdit,"emailText")
        self.confirmButton.clicked.connect(self.signup)
        self.setCentralWidget(self.dialog)

    def update(self, directory,error, wall, project):
        if directory == "SignupPage":
            self.show()

    def signup(self):
        username = self.usernameText.text()
        password = self.passwordText.text()
        confirm = self.confirmText.text()
        email = self.emailText.text()
        firstname = self.firstnameText.text()
        lastname = self.lastnameText.text()
        if password==confirm:
            self.hide()
            self.system.signup(username=username,password=password,first=firstname,last=lastname,email=email)
        else:
            dialog = QDialog(self)
            dialog.setWindowTitle("Passwords do not match")
            closeBt = QPushButton("Close")
            closeBt.clicked.connect(dialog.close)
            layout = QVBoxLayout()
            label = QLabel("Error: the two password given do not match")
            layout.addWidget(label)
            layout.addWidget(closeBt)
            dialog.setLayout(layout)
            dialog.setModal(True)
            dialog.show()
