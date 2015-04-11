__author__ = 'Faaiz'

from MemberStorage import *
from System import *

class ProjectSystem():
    def __init__(self):
        self.storage = MemberStorage(self)

    def descriptionTab(self):
        if System.directory == "ProjectPage/description":
            return
        System.directory = "ProjectPage/description"
        System.notifyObservers()

    def photosTab(self):
        if System.directory == "ProjectPage/photos":
            return
        System.directory = "ProjectPage/photos"
        System.notifyObservers()

    def sourcecodeTab(self):
        if System.directory == "ProjectPage/sourcecode":
            return
        System.directory = "ProjectPage/sourcecode"
        System.notifyObservers()

    def commentsTab(self):
        if System.directory == "ProjectPage/comments":
            return
        System.directory = "ProjectPage/comments"
        System.notifyObservers()

    def addObserver(self,o):
        System.addObserver(o)

