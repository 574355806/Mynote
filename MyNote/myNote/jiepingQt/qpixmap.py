#coding=utf-8

from PyQt4 import QtGui,QtCore

class MainFrom(QtGui.QWidget):
    def __init__(self):
        super(MainFrom, self).__init__()


        self.initUI()

    def initUI(self):


        self.grid = QtGui.QGridLayout()
        # button = QtGui.QPushButton("jietu",self).connect()
        #如何自定义信号、槽

        # self.grid.addWidget(button)



        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 设置总是在最前
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle(u'截图工具')
        self.setWindowIcon(QtGui.QIcon(':qq.ico'))

        self.show()


    # 截图
    def shootScreen(self):
        self.originalPixmap = QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())  # 获取 屏幕桌面截图
        self.show()


        # 保存截图图片
    def saveScreenshot(self):
        format = 'png'
        initialPath = QtCore.QDir.currentPath() + "/untitled." + format

        fileName = QtGui.QFileDialog.getSaveFileName(self, u"另存为",
                initialPath,
                "%s Files (*.%s)" % (format.upper(), format))
        if fileName:
            self.originalPixmap.save(fileName, format)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mf =MainFrom()
    mf.show()
    #QT5实现桌面截屏
    sys.exit(app.exec_())