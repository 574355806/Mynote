#coding=utf-8

"""
This example shows an icon
in the titlebar of the window.
"""

import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        #将部件定位并设定了它的大小【其实就是resize和move的混合函数】
        #前两个参数是部件相对于父元素的x，y坐标【这里其实是个窗口(window)，没有父元素,所以是屏幕上的x，y坐标。】，后两个参数是部件的宽和高

        self.setWindowTitle('Icon')

        self.setWindowIcon(QtGui.QIcon("icon.png"))

        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()