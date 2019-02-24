#coding=utf-8

import sys
from PyQt4 import QtGui

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    trans = QtGui.QWidget()

    # 就这句就搞定了。。设置成0的话就是全透明，
    # 同时这个窗口也不会跟你交互了，要看不见又要交互，0.01吧。。
    # 我反正是这么干的。。简单粗暴。。。。
    trans.setWindowOpacity(0.01)

    trans.show()
    sys.exit(app.exec_())