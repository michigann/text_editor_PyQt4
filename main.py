# PyQt4 and python2.7 application
from PyQt4 import QtGui
import sys
from WindowApp import WindowApp


def main():
    app = QtGui.QApplication(sys.argv)
    window = WindowApp()
    window.show()
    if len(sys.argv)>1:
        for file_name in sys.argv[1:]:
            window.open_file(file_name)
    else:
        window.new_file()
    app.exec_()

main()
