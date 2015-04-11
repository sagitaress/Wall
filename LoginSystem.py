__author__ = 'Faaiz'
from System import *
from MemberStorage import *
from WallPage import *
from WallSystem import*


class LoginSystem():
    def __init__(self):
        self.storage = MemberStorage(self)
        System.directory = "LoginPage"

    def login(self,username,password):
        member = self.storage.checkLogin(username,password)
        if member != None:
            System.directory = "WallPage"
            System.user = member
            System.currentWall = System.user.wall
            System.notifyObservers()

    def gotoSignupPage(self):
        System.directory = "SignupPage"
        System.notifyObservers()

    def addObserver(self,o):
        System.addObserver(o)


