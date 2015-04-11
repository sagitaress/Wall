__author__ = 'Faaiz'
from MemberStorage import *
from System import *


class SignupSystem():
    def __init__(self):
        self.storage = MemberStorage(self)
        System.directory = "SignupPage"

    def signup(self,username,password,first,last,email):
        if self.storage.checkSignup(username,password,first,last,email):
            System.directory = "LoginPage"
            System.notifyObservers()

    def addObserver(self,o):
        System.addObserver(o)

