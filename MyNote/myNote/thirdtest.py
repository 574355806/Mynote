#coding=utf-8

import sys
from PyQt4 import QtGui

def main():

    app = QtGui.QApplication(sys.argv)
    #每一个PyQt4应用都必须创建一个应用(application)对象
    #其中的sys.argv参数是由命令行参数组成的列表(list)

    w = QtGui.QWidget()
    #QtGui.QWidget是PyQt4所有用户接口对象中的基础类库
    #我们把没有父对象的部件(widget)叫做窗口(window)


    w.resize(250, 150)  #宽 高
    w.move(500, 300)    #左边界距离  上边界距离
    w.setWindowTitle('Simple')

    w.show()
    #部件先在内存(memory)中被创建，之后再被显示到屏幕上。

    sys.exit(app.exec_())
    #sys.exit()调用保证程序完全退出

if __name__ == '__main__':
    main()
