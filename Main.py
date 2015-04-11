__author__ = 'Faaiz'

from WallSystem import *
from LoginSystem import *
from SignupSystem import *
from ProjectSystem import *
from WallPage import*
from LoginPage import *
from SignupPage import *
from ProjectPage import *
import sys


def main():
    app = QApplication(sys.argv)
    w = WallSystem()
    s = SignupSystem()
    l = LoginSystem()
    p = ProjectSystem()
    wp = WallPage(w)
    sp = SignupPage(s)
    lp = LoginPage(l)
    pp = ProjectPage(p)
    return app.exec_()

if __name__ == "__main__":
    main()