# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view/design.ui'
#
# Created: Tue May 31 22:14:40 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(705, 523)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        self.menu_Search = QtGui.QMenu(self.menubar)
        self.menu_Search.setObjectName(_fromUtf8("menu_Search"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName(_fromUtf8("action_New"))
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName(_fromUtf8("action_Open"))
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.action_Save_As = QtGui.QAction(MainWindow)
        self.action_Save_As.setObjectName(_fromUtf8("action_Save_As"))
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setObjectName(_fromUtf8("action_Close"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_Undo = QtGui.QAction(MainWindow)
        self.action_Undo.setObjectName(_fromUtf8("action_Undo"))
        self.action_Redo = QtGui.QAction(MainWindow)
        self.action_Redo.setObjectName(_fromUtf8("action_Redo"))
        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setObjectName(_fromUtf8("action_Cut"))
        self.action_Copy = QtGui.QAction(MainWindow)
        self.action_Copy.setObjectName(_fromUtf8("action_Copy"))
        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setObjectName(_fromUtf8("action_Paste"))
        self.action_Delete = QtGui.QAction(MainWindow)
        self.action_Delete.setObjectName(_fromUtf8("action_Delete"))
        self.action_Select_All = QtGui.QAction(MainWindow)
        self.action_Select_All.setObjectName(_fromUtf8("action_Select_All"))
        self.action_Find = QtGui.QAction(MainWindow)
        self.action_Find.setObjectName(_fromUtf8("action_Find"))
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.action_Save_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addAction(self.action_Quit)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addAction(self.action_Delete)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Select_All)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addSeparator()
        self.menu_Search.addAction(self.action_Find)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Search.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit", None))
        self.menu_Search.setTitle(_translate("MainWindow", "&Search", None))
        self.action_New.setText(_translate("MainWindow", "&New", None))
        self.action_New.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.action_Open.setText(_translate("MainWindow", "&Open", None))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.action_Save.setText(_translate("MainWindow", "&Save", None))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.action_Save_As.setText(_translate("MainWindow", "&Save As...", None))
        self.action_Save_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S", None))
        self.action_Close.setText(_translate("MainWindow", "&Close", None))
        self.action_Close.setShortcut(_translate("MainWindow", "Ctrl+W", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.action_Undo.setText(_translate("MainWindow", "&Undo", None))
        self.action_Undo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.action_Redo.setText(_translate("MainWindow", "&Redo", None))
        self.action_Redo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z", None))
        self.action_Cut.setText(_translate("MainWindow", "&Cut", None))
        self.action_Cut.setShortcut(_translate("MainWindow", "Ctrl+X", None))
        self.action_Copy.setText(_translate("MainWindow", "&Copy", None))
        self.action_Copy.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.action_Paste.setText(_translate("MainWindow", "&Paste", None))
        self.action_Paste.setShortcut(_translate("MainWindow", "Ctrl+V", None))
        self.action_Delete.setText(_translate("MainWindow", "&Delete", None))
        self.action_Select_All.setText(_translate("MainWindow", "&Select All", None))
        self.action_Select_All.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.action_Find.setText(_translate("MainWindow", "&Find", None))
        self.action_Find.setShortcut(_translate("MainWindow", "Ctrl+F", None))

