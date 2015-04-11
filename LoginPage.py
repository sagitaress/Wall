__author__ = 'Faaiz'
from PySide.QtGui import *
from PySide.QtUiTools import*
from WallObserver import *


class LoginPage(QMainWindow,WallObserver):
    def __init__(self,system):
        QMainWindow.__init__(self,None)
        self.setWindowTitle("Login Page")
        loader=QUiLoader()
        self.system = system
        self.system.addObserver(self)
        self.dialog = loader.load("./LoginPage.ui",None)
        self.setMinimumSize(700, 600)
        self.setMaximumSize(700, 600)
        self.loginBt = self.dialog.findChild(QPushButton,"loginBt")
        self.signupBt = self.dialog.findChild(QPushButton,"signupBt")
        self.usernameText = self.dialog.findChild(QLineEdit,"usernameText")
        self.passwordText = self.dialog.findChild(QLineEdit,"passwordText")
        self.setCentralWidget(self.dialog)

        self.loginBt.clicked.connect(self.login)
        self.signupBt.clicked.connect(self.gotoSignupPage)
        self.show()

    def update(self, directory, error, wall, project):
        if directory == "LoginPage":
            self.show()

    def error(self):
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

    def login(self):
        self.system.login(self.usernameText.text(),self.passwordText.text())
        self.hide()

    def gotoSignupPage(self):
        self.system.gotoSignupPage()
        self.hide()