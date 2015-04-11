__author__ = 'Faaiz'


class System():
    observers = []
    user = None
    directory = "WallPage"
    error = ""
    currentWall = None
    currentProject = None

    @staticmethod
    def addObserver(o):
        System.observers.append(o)

    @staticmethod
    def notifyObservers():
        for i in System.observers:
            i.update(System.directory,System.error,System.currentWall, System.currentProject)