# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_dialog.ui'
#
# Created: Tue May 31 18:42:40 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(460, 45)
        Dialog.setMinimumSize(QtCore.QSize(460, 45))
        Dialog.setMaximumSize(QtCore.QSize(460, 45))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(400, 30))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.findPrev_Button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.findPrev_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.findPrev_Button.setMaximumSize(QtCore.QSize(30, 30))
        self.findPrev_Button.setObjectName(_fromUtf8("findPrev_Button"))
        self.horizontalLayout_2.addWidget(self.findPrev_Button)
        self.findNext_Button = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.findNext_Button.setMinimumSize(QtCore.QSize(30, 30))
        self.findNext_Button.setMaximumSize(QtCore.QSize(30, 30))
        self.findNext_Button.setObjectName(_fromUtf8("findNext_Button"))
        self.horizontalLayout_2.addWidget(self.findNext_Button)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Find", None))
        self.findPrev_Button.setText(_translate("Dialog", "<", None))
        self.findNext_Button.setText(_translate("Dialog", ">", None))

