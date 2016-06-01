import unittest
from PyQt4 import QtGui
import os
import shutil
import sys
from WindowApp import WindowApp
from WindowAppExtends import PlainTextEdit


class TestWindowApp(unittest.TestCase):
    def __init__(self, init_test):
        super(TestWindowApp, self).__init__(init_test)
        self.test_dir = '/tmp/test_dir/'
        self.test_file = '/tmp/test_dir/test_file.txt'
        self.test_file_content = 'test1\ntest2\ntest3test4test5\nlast_line!'

    def setUp(self):
        self.window = WindowApp()
        os.mkdir(self.test_dir)

    def tearDown(self):
        self.window = None
        shutil.rmtree(self.test_dir)

    def test_new_file_method(self):
        w = self.window
        w.new_file()
        cw = w.tabWidget.currentWidget()
        self.assertIsInstance(cw, PlainTextEdit, msg='New tab is not QtGui.QPlainTextEdit instance!')
        for i in (0, 1, 2, 3, 4, 7, 9, 10):
            self.assertTrue(w.actions_Tuple[i].isEnabled(), msg='actions_Tuple['+str(i)+'] element is disabled!')

    def test_open_file_method(self):
        print ''
        w, test_dir, test_file, test_file_content = self.window, self.test_dir, self.test_file, self.test_file_content

        with open(test_file, 'a') as f:
            f.write(test_file_content)

        # Not existing dir cases
        print 'Not existing dir cases:'
        self.assertFalse(w.open_file(test_dir), msg=test_dir+' is a directory not file!')
        self.assertFalse(w.open_file(test_dir+'test/file'), msg='path '+test_dir+'/test/'+' does not exist!')
        # Existing file case
        self.assertTrue(w.open_file(test_file), msg='file '+test_file+' exists but cant open!')
        cw = w.tabWidget.currentWidget()
        self.assertIsInstance(cw, PlainTextEdit, msg='New tab is not QtGui.QPlainTextEdit instance!')
        self.assertEqual(cw.path, test_file, msg='Bad file path!')
        ci = w.tabWidget.currentIndex()
        self.assertEqual(w.tabWidget.tabText(ci), 'test_file.txt', msg='Different file and tab name!')
        self.assertEqual(cw.toPlainText(), test_file_content, msg='text in file and window is different!')
        for i in (0, 1, 2, 3, 4, 7, 9, 10):
            self.assertTrue(w.actions_Tuple[i].isEnabled(), msg='actions_Tuple['+str(i)+'] element is disabled!')
        # Not existing file case
        self.assertTrue(w.open_file(test_dir+'new_file.txt'), msg='new_file.txt in existing path is not created!')
        self.assertNotEqual(cw, w.tabWidget.currentWidget(), msg='currentWidget doesnt change after open new!')
        cw = w.tabWidget.currentWidget()
        self.assertIsInstance(cw, PlainTextEdit, msg='New tab is not QtGui.QPlainTextEdit instance!')
        self.assertEqual(cw.path, test_dir+'new_file.txt', msg='Bad file path!')
        ci = w.tabWidget.currentIndex()
        self.assertEqual(w.tabWidget.tabText(ci), 'new_file.txt', msg='Different file and tab name!')
        self.assertEqual(cw.toPlainText(), '', msg='new file is not empty!')
        for i in (0, 1, 2, 3, 4, 7, 9, 10):
            self.assertTrue(w.actions_Tuple[i].isEnabled(), msg='actions_Tuple['+str(i)+'] element is disabled!')

    def test_save_file_method(self):
        w, test_dir, test_file, test_file_content = self.window, self.test_dir, self.test_file, self.test_file_content
        open(test_file, 'a').close()

        w.open_file(test_file)
        w.tabWidget.currentWidget().setPlainText(test_file_content)
        w.save_file()
        with open(test_file, 'r') as f:
            content = f.read()
        self.assertEqual(test_file_content, content, msg='Save error: different between text in tab and in file!')

    def test_save_file_as_method(self):
        """GUI manual testing!"""
        pass

    def test_set_action_disabled_method(self):
        w = self.window
        w.set_action_disabled(True)
        for i in w.actions_Tuple:
            self.assertFalse(i.isEnabled(), msg='some actions_Tuple element is enabled!')
        w.set_action_disabled(False)
        for i in w.actions_Tuple:
            self.assertTrue(i.isEnabled(), msg='some actions_Tuple element is disabled!')

        tpl = (0, 1, 2, 3, 4, 7, 9, 10)
        w.set_action_disabled(True, tpl)
        for i in tpl:
            self.assertFalse(w.actions_Tuple[i].isEnabled(), msg='actions_Tuple[' + str(i) + '] element is enabled!')
        w.set_action_disabled(False, tpl)
        for i in tpl:
            self.assertTrue(w.actions_Tuple[i].isEnabled(), msg='actions_Tuple[' + str(i) + '] element is disabled!')
        self.assertRaises(TypeError, w.set_action_disabled, True, 1, msg='No raises exception if arg2 not iterable')

        try:
            w.set_action_disabled(True, (1, 1000))
        except IndexError:
            raise AssertionError('IndexError raised!')

    def test_remove_tab_method(self):
        w = self.window
        w.new_file()
        w.open_file(self.test_file)
        cw = w.tabWidget.currentWidget()
        w.remove_tab()
        self.assertNotEqual(cw, w.tabWidget.currentWidget(), msg='currentWidget was not changed after remove tab')
        w.remove_tab()
        cw = w.tabWidget.currentWidget()
        self.assertIsNone(cw, msg='currentWidget not None after delete last tab')
        for i in w.actions_Tuple:
            self.assertFalse(i.isEnabled(), msg='some actions_Tuple element is enabled!')

    def test_text_find_method(self):
        """GUI manual testing!"""
        pass

    def test_document_status_method(self):
        """GUI manual testing!"""
        pass


def test():
    app = QtGui.QApplication(sys.argv)
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestWindowApp))
    unittest.TextTestRunner(verbosity=2).run(suite)
    app.quit()
