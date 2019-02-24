#coding=utf-8

"""
This program centers a window
on the screen.
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        #用frameGeometry方法得到了主窗口的矩形框架qr

        cp = QtGui.QDesktopWidget().availableGeometry().center()
        #得到屏幕分辨率，并最终得到屏幕中间点的坐标cp

        qr.moveCenter(cp)
        #将矩形框架移至屏幕正中央，大小不变

        self.move(qr.topLeft())
        #将应用窗口移至矩形框架的左上角点，
        # 这样应用窗口就位于屏幕的中央了【注意部件的move都是左上角移动到某点】。


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()