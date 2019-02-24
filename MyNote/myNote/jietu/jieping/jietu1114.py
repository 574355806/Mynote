#coding=utf-8

from PyQt4 import QtGui,QtCore
import sys

from PIL import ImageGrab
'''
简单截屏
'''

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


class ScrnshotUI(QtGui.QWidget):
    def __init__(self):
        super(ScrnshotUI, self).__init__()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ltPoint = self.tempPoint = self.rbPoint =QtCore.QPoint(0,0)
        self.ltRect = QtCore.QRect()
        self.rtRect = QtCore.QRect()
        self.lbRect = QtCore.QRect()
        self.rbRect = QtCore.QRect()
        self.pixmapRect = QtCore.QRect()
        self.grab = True

        #设置窗体为整个屏幕
        self.scrPix = ImageGrab.grab()
        self.scrPix.save("bground.jpeg")

        self.pixmap = QtGui.QPixmap("bground.jpeg")

        width, height = self.scrPix.size
        self.resize(width, height)

    def mousePressEvent(self, e):
        if (e.button() == QtCore.Qt.LeftButton and self.grab):
            self.ltPoint = e.pos()
            self.repaint()
        self.clickPoint = e.pos()
        self.oldPoint = self.clickPoint

    def mouseMoveEvent(self, e):
        self.tempPoint = QtCore.QPoint(e.x(), e.y())
        if(self.tempPoint.x()<self.ltPoint.x() or self.tempPoint.y() < self.ltPoint.y()):
            QtGui.QMessageBox.critical(self,u'提示',
                             u'请从右上角开始截屏操作')
        else:
            self.repaint()


    def mouseReleaseEvent(self, e):
        # self.rbPoint = QtCore.QPoint(e.x(), e.y())
        # self.repaint()
         if(e.button() == QtCore.Qt.LeftButton):
            self.rbPoint = self.tempPoint;
            #释放鼠标的时候截取选中的部分的图片
            pix = self.pixmap.copy(self.ltPoint.x(), self.ltPoint.y(), self.rbPoint.x() - self.ltPoint.x(), self.rbPoint.y() - self.ltPoint.y());
            self.savedPixmap = pix;
            #保存图片
            # self.savedPixmap.save("hello.png")
            self.pixmapRect.setX(self.ltPoint.x());
            self.pixmapRect.setY(self.ltPoint.y());
            self.pixmapRect.setWidth(self.rbPoint.x() - self.ltPoint.x());
            self.pixmapRect.setHeight(self.rbPoint.y() - self.ltPoint.y());

            self.grab = False;
            #初始化桌面的宽高
            self.desktopWidth = self.pixmap.width();
            self.desktopHeight = self.pixmap.height();


            self.tool = Tool()
             # 为工具栏图标添加事件
            self.tool.saveAction.triggered.connect(self.saveFile)
            self.tool.exitAction.triggered.connect(self.close)
            self.tool.exitAction.triggered.connect(self.tool.close)
            self.tool.toolbar = self.tool.addToolBar('Save')
            self.tool.toolbar.addAction(self.tool.saveAction)
            self.tool.toolbar.addAction(self.tool.exitAction)
            self.tool.move(e.x(), e.y())
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
            self.savedPixmap.save(my_file_path)
        except ValueError:
            print 'error'
        self.tool.close()
        self.close()



    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

        if( self.ltPoint == self.tempPoint or self.tempPoint == self.rbPoint and self.rbPoint == QtCore.QPoint(0, 0)):

            self.paintGradient(0, 0, self.rect().width(), self.rect().height(), painter);
            return

#     矩形上方的渐变
        self.paintGradient(0, 0, self.rect().width(), self.ltPoint.y(), painter);
#     矩形左边的渐变
        self.paintGradient(0, self.ltPoint.y(), self.ltPoint.x(), self.rect().height(), painter);
#     矩形正下方的渐变
        self.paintGradient(self.ltPoint.x(), self.tempPoint.y(), self.tempPoint.x() - self.ltPoint.x(), self.rect().height(), painter);
#     矩形右边的渐变
        self.paintGradient(self.tempPoint.x(), self.ltPoint.y(),self.rect().width(), self.rect().height(), painter);
    # 保存画笔的状态
        painter.save();
# #     绘制矩形边界
        self.paintBorder(self.ltPoint, self.tempPoint, painter);
        painter.restore();
#     画四个顶点的矩形
        self.paintStretchRect(self.ltPoint, self.tempPoint, painter);
    # 根据坐标绘制渐变
    def paintGradient(self, x1, y1, width, height, painter):
        grad = QtGui.QLinearGradient(x1, y1, width, height)
        grad.setColorAt(0.0, QtGui.QColor(0, 0, 0, 100));
        painter.fillRect(x1, y1, width, height, grad);

        # 绘制边框
    def paintBorder(self, ltPoint, rbPoint, painter):
        pen = QtGui.QPen()
        pen.setColor(QtCore.Qt.blue)
        pen.setWidth(1)
        painter.setPen(pen)
        # 画左边界
        painter.drawLine(ltPoint.x(), ltPoint.y(), ltPoint.x(), rbPoint.y());
        # 画上边界
        painter.drawLine(ltPoint.x(), ltPoint.y(), rbPoint.x(), ltPoint.y());
        # 画右边界
        painter.drawLine(rbPoint.x(), ltPoint.y(), rbPoint.x(), rbPoint.y());
        # 画下边界
        painter.drawLine(ltPoint.x(), rbPoint.y(), rbPoint.x(), rbPoint.y());
    def paintStretchRect(self, ltPoint, rbPoint, painter):
        # 每个矩形算6的长度
        # 左上角
        self.ltRect.setX(ltPoint.x() - 3);
        self.ltRect.setY(ltPoint.y() - 3);
        self.ltRect.setWidth(6);
        self.ltRect.setHeight(6);
        # 右上角
        self.rtRect.setX(rbPoint.x() - 3);
        self.rtRect.setY(ltPoint.y() - 3);
        self.rtRect.setWidth(6);
        self.rtRect.setHeight(6);
        # 左下角
        self.lbRect.setX(ltPoint.x() - 3);
        self.lbRect.setY(rbPoint.y() - 3);
        self.lbRect.setWidth(6);
        self.lbRect.setHeight(6);
        # 右下角
        self.rbRect.setX(rbPoint.x() - 3);
        self.rbRect.setY(rbPoint.y() - 3);
        self.rbRect.setWidth(6);
        self.rbRect.setHeight(6);
        # 绘制用于拉伸的矩形
        brush = QtGui.QBrush(QtCore.Qt.blue)
        painter.fillRect(self.ltRect, brush);
        painter.fillRect(self.lbRect, brush);
        painter.fillRect(self.rtRect, brush);
        painter.fillRect(self.rbRect, brush);

    #重制事件句柄  （事件句柄，可以理解为事件处理程序）
    def keyPressEvent(self, e):
        #在这个例子中，重制了keyPressEvent()这个事件句柄
        #如果按下了Esc键，应用就会终止。

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

