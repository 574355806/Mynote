#coding=utf-8

from PyQt4 import QtGui,QtCore
import sys

'''
简单截屏
'''

from jietu1114 import ScrnshotUI

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.jietuBtn = QtGui.QPushButton('jieping', self)
        self.jietuBtn.clicked.connect(self.jietu)
        self.resize(300, 300)
        self.show()

    def jietu(self):
        # self.hide()
        self.screen = ScrnshotUI()
        self.screen.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


