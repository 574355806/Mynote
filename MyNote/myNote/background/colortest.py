#coding=utf-8

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
def main():

    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.setWindowFlags(QtCore.Qt.CustomizeWindowHint)

    palette1 = QtGui.QPalette(w)
    palette1.setColor(w.backgroundRole(), QtGui.QColor('black'))   # 设置背景颜色



    # self.originalPixmap.scaled()  scaled()函数的声明const返回一个Qpixmap
        # QtCore.Qt.KeepAspectRatio 尽可能大的在一个给定的矩形大小缩放到一个矩形且保持长宽比。
        # QtCore.Qt.SmoothTransformation 平滑转换
    w.setPixmap(w.originalPixmap.scaled(w.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))



    w.setPalette(palette1)
    w.setWindowOpacity(0.5)



    w.resize(250, 150)
    w.move(500, 300)
    w.setWindowTitle('Simple')

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
