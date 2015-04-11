__author__ = 'Faaiz'
from MemberStorage import *
from System import *


class WallSystem():
    def __init__(self):
        self.storage = MemberStorage(self)

    def addProject(self,p):
        System.user.wall.addProject(p)
        System.notifyObservers()

    def openProject(self,p):
        System.directory = "ProjectPage"
        System.notifyObservers()

    def addObserver(self, o):
        System.addObserver(o)

