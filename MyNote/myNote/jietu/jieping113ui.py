#coding=utf-8

from PyQt4 import QtGui,QtCore
import sys

'''
鼠标位置获得不到
'''

from PIL import ImageGrab


# class Position(QtCore.QObject):
#
#     position = QtCore.pyqtSignal()

class ScrnshotUI(QtGui.QMainWindow):
    def __init__(self):
        super(ScrnshotUI, self).__init__()
        self.initUI()

    def initUI(self):

        scrnshotButton = QtGui.QPushButton("ScreenShot", self)
        scrnshotButton.move(15, 10)
        exitButton = QtGui.QPushButton("exit", self)
        exitButton.move(130, 10)

        scrnshotButton.clicked.connect(self.screenShot)
        exitButton.clicked.connect(QtGui.qApp.quit)


        self.labelMousePos = QtGui.QLabel();
        self.labelMousePos.setText(self.tr(""))
        self.labelMousePos.setFixedWidth(100)

        self.sBar = self.statusBar()
        self.sBar.addPermanentWidget(self.labelMousePos)




        self.setGeometry(500, 400, 1000, 60)
        self.setWindowTitle('ss')
        self.setWindowIcon(QtGui.QIcon("ss2.png"))
        self.show()

    #重制事件句柄  （事件句柄，可以理解为事件处理程序）
    def keyPressEvent(self, e):
        #在这个例子中，重制了keyPressEvent()这个事件句柄
        #如果按下了Esc键，应用就会终止。

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


    #自定义槽
    def screenShot(self):
        sender = self.sender()
        im = ImageGrab.grab(bbox=(10,10,510,510))
        im.save("2.png")
        self.statusBar().showMessage(sender.text() + ' ok')







    def mousePressEvent(self, e): # real signature unknown
        str="("+QtCore.QString.number(e.x())+","+QtCore.QString.number(e.y())+")"
        if e.button() == QtCore.Qt.LeftButton:
            self.sBar.showMessage(QtCore.QString.number(e.x())+","+QtCore.QString.number(e.y()))
            self.x1 = QtCore.QString.number(e.x())
            self.y1 = QtCore.QString.number(e.y())
            print self.x1,self.y1

    def mouseReleaseEvent(self, e): # real signature unknown
        str="("+QtCore.QString.number(e.x())+","+QtCore.QString.number(e.y())+")"
        if e.button() == QtCore.Qt.LeftButton:
            self.labelMousePos.setText(QtCore.QString.number(e.x())+","+QtCore.QString.number(e.y()))
            self.x2 = QtCore.QString.number(e.x())
            self.y2 = QtCore.QString.number(e.y())
            print self.x2,self.y2
            im = ImageGrab.grab(bbox=(float(self.x1)+500,float(self.y1)+400,float(self.x2)+500,float(self.y2)+400))
            im.save("new.png")


def main():

    app = QtGui.QApplication(sys.argv)
    ui = ScrnshotUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()