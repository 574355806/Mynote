#coding=utf-8

"""
This program creates a menubar. The
menubar has one menu with an exit action.
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        #创建了有着自己图标和名字一个选项
        exitAction.setShortcut('Ctrl+Q')
        #给这个行为定义一个快捷键


        exitAction.setStatusTip('Exit application')
        #鼠标放在这个选项上时，可以在状态栏中显示出状态“Exit application”
        exitAction.triggered.connect(QtGui.qApp.quit)
        #当我们选择了这个选项时，一个触发信号(triggered signal)被发出了。
        #这个信号和QtGui.QApplication部件的quit()方法相联系(connect)，所以信号发出后，程序终止。

        self.statusBar()

        menubar = self.menuBar()
        #menuBar()方法创建了一个菜单栏

        fileMenu = menubar.addMenu('&File')
        #这里我们在菜单栏的基础上创建了一个file菜单

        fileMenu.addAction(exitAction)
        #在file菜单里添加了exit选项

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()