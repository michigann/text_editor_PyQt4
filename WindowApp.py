from PyQt4 import QtGui
from WindowAppExtends import PlainTextEdit, FindDialog
import design
import os.path


# GUI controller
class WindowApp(QtGui.QMainWindow, QtGui.QFileDialog, design.Ui_MainWindow):
    # Initialisation and adding events to GUI elements
    def __init__(self, window_title='pyEdit'):
        super(WindowApp, self).__init__()
        self.setupUi(self)

        # actions_Tuple - elements to set/unset disabled
        self.actions_Tuple = (self.action_Save, self.action_Save_As, self.action_Close, self.action_Undo,
                              self.action_Redo, self.action_Cut, self.action_Copy, self.action_Paste,
                              self.action_Delete, self.action_Select_All, self.action_Find)
        self.set_action_disabled(True)

        # Adding triggered events to elements
        self.action_New.triggered.connect(self.new_file)
        self.action_Open.triggered.connect(self.open_file)
        self.action_Save.triggered.connect(self.save_file)
        self.action_Save_As.triggered.connect(self.save_file_as)
        self.action_Close.triggered.connect(self.remove_tab)
        self.action_Quit.triggered.connect(self.close)
        self.action_Undo.triggered.connect(lambda: self.tabWidget.currentWidget().undo())
        self.action_Redo.triggered.connect(lambda: self.tabWidget.currentWidget().redo())
        self.action_Cut.triggered.connect(lambda: self.tabWidget.currentWidget().cut())
        self.action_Copy.triggered.connect(lambda: self.tabWidget.currentWidget().copy())
        self.action_Paste.triggered.connect(lambda: self.tabWidget.currentWidget().paste())
        self.action_Delete.triggered.connect(lambda: self.tabWidget.currentWidget().textCursor().removeSelectedText())
        self.action_Select_All.triggered.connect(lambda: self.tabWidget.currentWidget().selectAll())
        self.action_Find.triggered.connect(self.text_find)

        # setting tabWidget option
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.tabCloseRequested.connect(self.remove_tab)
        self.tabWidget.currentChanged.connect(self.change_window_name)

        self.window_title = window_title
        self.setWindowTitle(self.window_title)

    # Create new tab
    def new_file(self):
        """
        Create new 'Untitled Document', needed to choose location during saving
        Method sets action_Tuple (0, 1, 2, 3, 4, 7, 9, 10) elements disabled
        :return: None
        """
        text_tab = PlainTextEdit()
        text_tab.cursorPositionChanged.connect(self.document_status)
        self.tabWidget.addTab(text_tab, 'Untitled Document')
        self.tabWidget.setCurrentWidget(text_tab)
        self.set_action_disabled(False, (0, 1, 2, 3, 4, 7, 9, 10))

    # This method changes window name to current document path
    def change_window_name(self):
        cw = self.tabWidget.currentWidget()
        if cw:
            if cw.path:
                self.setWindowTitle(cw.path + ' - ' + self.window_title)
            else:
                self.setWindowTitle('Untitled Document - ' + self.window_title)
        else:
            self.setWindowTitle(self.window_title)

    # Reading file to plainTextEdit element
    def open_file(self, file_path=None):
        """
        This method loads file content and adds its path to PlainTextEdit and creates new tab in tabWidget.
        If file_path == None then method runs the navigation window to open file
        If file_path != None then method creates the new file or old one is reading
        If directories in file_path does't exist or file_path is directory file can't be open or create
        Method sets actions_Tuple (0, 1, 2, 3, 4, 7, 9, 10) elements enable
        :param file_path: path to file when program has been run with args
        :return: boolean - operation status
        """
        if not file_path:
            file_path = QtGui.QFileDialog.getOpenFileName(self, 'Open')
            if not file_path:
                return False
        else:
            if os.path.isdir(file_path):
                print "Can't open '" + file_path + "' it's a directory."
                return False
            directory = '/'.join([i for i in file_path.split('/')[:-1]])
            if directory and not os.path.exists(directory):
                print "Can't open '"+file_path+"'"
                print "Directory '"+directory+"' does't exist."
                return False
            if not os.path.isfile(file_path):
                open(file_path, 'a').close()

        text_tab = PlainTextEdit(file_path)
        text_tab.cursorPositionChanged.connect(self.document_status)
        with open(file_path, 'r') as f:
            text_tab.setPlainText(f.read())
        file_name = file_path.split('/')[-1]
        self.tabWidget.addTab(text_tab, file_name)
        self.tabWidget.setCurrentWidget(text_tab)

        self.set_action_disabled(False, (0, 1, 2, 3, 4, 7, 9, 10))

        return True

    # Save current editing file
    def save_file(self):
        """
        Simple save method its write text from currentWidget to editing file
        If its new 'Untitled Document' file path need to choose
        :return: None
        """
        cw = self.tabWidget.currentWidget()
        if cw.path:
            with open(cw.path, 'w') as f:
                f.write(cw.toPlainText())
        else:
            self.save_file_as()

    # Save As - runs QFileDialog
    def save_file_as(self):
        """
        Opens QFileDialog to choose save location.
        Rename current tab name and change path to file in PlainTextEdit object.
        :return: None
        """
        file_path = QtGui.QFileDialog.getSaveFileName(self, 'Save As')
        if file_path:
            cw = self.tabWidget.currentWidget()
            cw.path = file_path
            ci, file_name = self.tabWidget.currentIndex(), file_path.split('/')[-1]
            self.tabWidget.setTabText(ci, file_name)
            self.setWindowTitle(file_path + ' - ' + self.window_title)

            with open(file_path, 'w') as f:
                f.write(cw.toPlainText())

    # Set actions_Tuple elements disabled/enabled
    def set_action_disabled(self, flag=True, which=None):
        """
        It sets elements disabled when flag==True else sets elements enabled
        :param flag: True - disabled / False - enabled
        :param which: iterable object - which elements to set if actions_Tuple is None set all
        :return: None
        """
        if which and iter(which):
            length = len(self.actions_Tuple)
            for i in which:
                if 0 <= i < length:
                    self.actions_Tuple[i].setDisabled(flag)
        else:
            for i in self.actions_Tuple:
                i.setDisabled(flag)

    # Remove current tab
    def remove_tab(self):
        """
        Its removes currentWidget - after clicking 'x' or 'Close'
        If there is not more tabs it sets all actions_Tuple elements disabled
        :return: None
        """
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        if not self.tabWidget.currentWidget():
            self.set_action_disabled(True)

    # It runs FindDialog
    def text_find(self):
        dialog = FindDialog(self.tabWidget.currentWidget())
        dialog.exec_()

    # Sets current line, col in label and disabled / enabled actions_Tuple (5, 6, 8) elements if text is selected
    def document_status(self):
        cw = self.tabWidget.currentWidget()
        if cw:
            cursor = cw.textCursor()
            string = 'Ln ' + str(cursor.blockNumber()+1) + ', ' + 'Col ' + str(cursor.columnNumber()+1)
            self.statusbar.showMessage(string)
            indexes = (5, 6, 8)
            if cursor.selectedText():
                self.set_action_disabled(False, indexes)
            else:
                self.set_action_disabled(True, indexes)


# Testing
if __name__ == '__main__':
    from TestWindowApp import test
    test()
