__author__ = 'Faaiz'
from ClickableLabel import *
from WallObserver import *
from DescriptionWidget import *
from SourcecodeWidget import *
from CommentsWidget import *
from PhotosWidget import *


class ProjectPage(QMainWindow,WallObserver):
    def __init__(self,system):
        QMainWindow.__init__(self,None)
        self.setWindowTitle("SignupPage")
        self.system = system
        self.system.addObserver(self)
        loader=QUiLoader()
        self.dialog = loader.load("./projectPage.ui",None)
        self.descriptionBt = self.dialog.findChild(QLabel,"descriptionLabel")
        self.sourcecodeBt = self.dialog.findChild(QLabel,"sourcecodeLabel")
        self.photosBt = self.dialog.findChild(QLabel,"photosLabel")
        self.commentsBt = self.dialog.findChild(QLabel,"commentsLabel")
        self.info = self.dialog.findChild(QScrollArea,"info")
        self.infoLayout = QGridLayout()
        self.info.setLayout(self.infoLayout)
        self.widget = QWidget(None)
        self.infoLayout.addWidget(self.widget)
        self.setCentralWidget(self.dialog)

        clickable(self.descriptionBt).connect(self.descriptionTab)
        clickable(self.commentsBt).connect(self.commentsTab)
        clickable(self.photosBt).connect(self.photosTab)
        clickable(self.sourcecodeBt).connect(self.sourcecodeTab)

    def update(self, directory, error, wall, project):
        if "ProjectPage" in directory:
            self.infoLayout.removeWidget(self.widget)
            self.widget.setParent(None)
            if directory == "ProjectPage/description":
                self.widget = DescriptionWidget(par=self)
            elif directory == "ProjectPage/sourcecode":
                self.widget = SourcecodeWidget(par=self)
            elif directory == "ProjectPage/photos":
                self.widget = PhotosWidget(par=self)
            elif directory == "ProjectPage/comments":
                self.widget = CommentsWidget(par=self)
            self.infoLayout.addWidget(self.widget)
            self.show()

    def sourcecodeTab(self):
        self.system.sourcecodeTab()

    def descriptionTab(self):
        self.system.descriptionTab()

    def photosTab(self):
        self.system.photosTab()

    def commentsTab(self):
        self.system.commentsTab()


