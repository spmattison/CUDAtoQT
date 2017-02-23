# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:29:59 2017

@author: AL1
"""

from PyQt4 import QtGui
import sys

import TestUI

class TestApp(QtGui.QMainWindow, TestUI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
    
def main():
    app = QtGui.QApplication(sys.argv)
    form = TestApp()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()