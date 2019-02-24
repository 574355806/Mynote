#coding=utf-8

from PyQt4 import QtGui,QtCore
import sys

'''
简单截屏
'''

from PIL import ImageGrab

class Tool(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Tool, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)#Qt.CustomizeWindowHint
        self.initUI()

    def initUI(self):
        self.saveAction = QtGui.QAction(QtGui.QIcon('ss2.png'), 'Save', self)
        self.saveAction.setShortcut('Ctrl+S')

        self.exitAction = QtGui.QAction(QtGui.QIcon('ss2.png'), 'Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')

        self.resize(100, 10)

class MyScrnshot(QtGui.QWidget):
    def __init__(self):
        super(MyScrnshot, self).__init__()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)#Qt.FramelessWindowHint

class ScrnshotUI(QtGui.QWidget):
    def __init__(self):
        super(ScrnshotUI, self).__init__()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)#Qt.FramelessWindowHint
        self.myscreen = MyScrnshot()
        self.initUI()

    def initUI(self):


        #设置窗体为整个屏幕
        desktop = QtGui.QApplication.desktop()
        rect = desktop.availableGeometry()
        self.setGeometry(rect)
        # screen = ImageGrab.grab()
        # width, height = screen.size
        # self.setGeometry(0, 0, width, height)

        #设置窗体背景为黑色透明
        palette1 = QtGui.QPalette(self)
        palette1.setColor(self.backgroundRole(), QtGui.QColor('black'))   # 设置背景颜色
        self.setPalette(palette1)
        self.setWindowOpacity(0.01)

        self.show()

    #重制事件句柄  （事件句柄，可以理解为事件处理程序）
    def keyPressEvent(self, e):
        #在这个例子中，重制了keyPressEvent()这个事件句柄
        #如果按下了Esc键，应用就会终止。

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:
            self.x1 = e.x()
            self.y1 = e.y()

    def mouseMoveEvent(self, e):

        self.x2 = e.x()
        self.y2 = e.y()
        self.myscreen.setGeometry(self.x1, self.y1,(self.x2-self.x1),(self.y2-self.y1))

        # palette2 = QtGui.QPalette()
        # palette2.setColor(self.myscreen.backgroundRole(), QtGui.QColor('write'))   # 设置背景颜色
        # self.myscreen.setPalette(palette2)
        self.myscreen.setWindowOpacity(0.1)
        self.myscreen.setStyleSheet("border:1px solid red;")
        self.myscreen.show()

    def mouseReleaseEvent(self, e):
        if e.button() == QtCore.Qt.LeftButton:

            self.myscreen.show()
            global im
            im = ImageGrab.grab(bbox=(self.x1-1,self.y1-1,self.x2-1,self.y2-1))

            self.tool = Tool()
            # 为工具栏图标添加事件
            self.tool.saveAction.triggered.connect(self.saveFile)
            self.tool.exitAction.triggered.connect(QtGui.qApp.quit)
            self.tool.toolbar = self.tool.addToolBar('Save')
            self.tool.toolbar.addAction(self.tool.saveAction)
            # self.tool.toolbar = self.tool.addToolBar('Exit')
            self.tool.toolbar.addAction(self.tool.exitAction)
            self.tool.show()

    def saveFile(self):
        file_path =  str(QtGui.QFileDialog.getSaveFileName(self,'save file',"saveFile" ,"jpeg files (*.jpeg);;all files(*.*)")) ####
        my_file_path = ''
        for i in file_path:
            if i == '/':
                my_file_path+='\\\\'
            else:
                my_file_path+=i
        try:
            im.save(my_file_path)
        except ValueError:
            print 'error'

        sys.exit()


def main():

    app = QtGui.QApplication(sys.argv)
    ui = ScrnshotUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()