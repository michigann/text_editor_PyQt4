from PyQt4 import QtGui
import find_dialog


# PlainTextEdit is class which extends QtGui.QPlainTextEdit and can store current editing file path.
class PlainTextEdit(QtGui.QPlainTextEdit):
    def __init__(self, path=None):
        super(PlainTextEdit, self).__init__()
        self.path = path


# FindDialog runs dialog to find words in QPlainTextEdit object
class FindDialog(QtGui.QDialog):
    # Showing dialog, checking text instance, initialisation, adding events
    def __init__(self, text):
        if not isinstance(text, QtGui.QPlainTextEdit):
            raise ValueError
        super(FindDialog, self).__init__()

        self.text = text
        self.ui = find_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.findPrev_Button.clicked.connect(lambda: self.text.find(self.to_find, QtGui.QTextDocument.FindBackward))
        self.ui.findNext_Button.clicked.connect(lambda: self.text.find(self.to_find))
        self.ui.plainTextEdit.textChanged.connect(self.new_find)
        self.to_find = ''

    # Runs if text to find is changed
    def new_find(self):
        self.to_find = self.ui.plainTextEdit.toPlainText()
        tc = self.text.textCursor()
        tc.clearSelection()
        self.text.setTextCursor(tc)
        flag = self.text.find(self.to_find)
        if not flag:
            self.text.find(self.to_find, QtGui.QTextDocument.FindBackward)


# Testing
if __name__ == '__main__':
    from TestWindowAppExtends import test
    test()
