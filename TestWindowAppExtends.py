import unittest
from PyQt4 import QtGui
import sys
from WindowAppExtends import PlainTextEdit, FindDialog


class TestPlainTextEdit(unittest.TestCase):
    def test_PlainTextEdit_init_method(self):
        txt = PlainTextEdit()
        self.assertIsInstance(txt, QtGui.QPlainTextEdit, msg='Wrong super class!')
        self.assertIsNone(txt.path, msg='Untitled Document path is not None!')
        txt = PlainTextEdit('/path/test/')
        self.assertIsNotNone(txt.path, msg='Document path is None!')


class TestFindDialog(unittest.TestCase):
    def test_TestFindDialog_init_method(self):
        """GUI manual testing!"""
        pass

    def test_TestFindDialog_new_find_method(self):
        """GUI manual testing!"""
        pass


def test():
    app = QtGui.QApplication(sys.argv)
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPlainTextEdit))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFindDialog))
    unittest.TextTestRunner(verbosity=2).run(suite)
    app.quit()
