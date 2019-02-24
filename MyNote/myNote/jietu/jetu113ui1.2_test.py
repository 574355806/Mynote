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


class ScrnshotUI(QtGui.QWidget):
    def __init__(self):
        super(ScrnshotUI, self).__init__()
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)#Qt.FramelessWindowHint


        self.ltPoint = self.tempPoint = self.rbPoint =QtCore.QPoint(0,0)


        self.grab = True
        # global desktopWidth, desktopHeight

        #设置窗体为整个屏幕ImageGrab.grab()save("bground.jpeg")
        # self.pixmap = QtGui.QApplication.primaryScreen().grabWindow(0);
        # screen =
        width, height = self.pixmap.size
        self.setGeometry(0, 0, width, height)

        #设置窗体背景为黑色透明
        palette1 = QtGui.QPalette(self)
        self.setAutoFillBackground(True)
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("bground.jpeg")))   # 设置背景图片
        self.setPalette(palette1)
        self.show()


    #重制事件句柄  （事件句柄，可以理解为事件处理程序）
    def keyPressEvent(self, e):
        #在这个例子中，重制了keyPressEvent()这个事件句柄
        #如果按下了Esc键，应用就会终止。

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, e):
        if (e.button() == QtCore.Qt.LeftButton and self.grab):
            self.ltPoint = e.pos()
            self.repaint()
        self.clickPoint = e.pos()
        self.oldPoint = self.clickPoint


    def mouseMoveEvent(self, e):
        print self.ltPoint
        self.p = e.pos()
        # 临时的point
        m_tempPoint=QtCore.QPoint(0,0)
        self.moveType = self.MoveType()
        # 左键点击移动事件
        if (e.button() == QtCore.Qt.LeftButton and self.grab):
            if self.moveType == 'AREAGRAB':
                # 如果移动后的坐标大于矩形左上角的坐标
                if(self.isGrab( self.ltPoint, self.p)):
                    tempPoint = self.p
                    # repaint();
            elif self.moveType == 'AREALEFTBOTTOM':
                # 封装右上角的坐标
                m_tempPoint.setX( self.tempPoint.x())
                m_tempPoint.setY( self.ltPoint.y());
                if(self.isGrabLeftBottom(self.p, m_tempPoint)):
                     self.ltPoint.setX(self.p.x());
                     self.tempPoint.setY(self.p.y());

            elif self.moveType ==  'AREALEFTTOP':
                if( self.isGrab(self.p,  self.tempPoint)):
                    ltPoint = self.p;
            elif self.moveType == 'AREARIGHTBOTTOM':
                if(self.isGrab( self.ltPoint, self.p)):
                    tempPoint = self.p
            elif self.moveType == 'AREARIGHTTOP':
                # 封装左下角的坐标
                m_tempPoint.setX( self.ltPoint.x());
                m_tempPoint.setY( self.tempPoint.y());
                if(self.isGrabLeftBottom(m_tempPoint, self.p)):
                     self.ltPoint.setY(self.p.y());
                     self.tempPoint.setX(self.p.x());
            elif self.moveType == 'AREAMOVE':
                # 记录此时移动的距离
                moveX = self.p.x() -  self.oldPoint.x();
                moveY = self.p.y() -  self.oldPoint.y();
                # 整个选取移动的时候两个点的坐标都要移动
                if(self.isMove( self.ltPoint,  self.tempPoint, moveX, moveY)):
                     self.ltPoint.setX( self.ltPoint.x() + moveX);     #左上角的x坐标
                     self.ltPoint.setY( self.ltPoint.y() + moveY);     #左上角的y坐标
                     self.tempPoint.setX( self.tempPoint.x() + moveX); #右下角的x坐标
                     self.tempPoint.setY( self.tempPoint.y() + moveY); #右下角的y坐标
                    #将此时的移动坐标记录
                     self.oldPoint = self.p;


         # //鼠标未点击的时候移动
        else:
            # 根据鼠标移动的位置该表鼠标的样式
            if(self.pointInRect(self.p, self.ltRect)):
                self.setCursor(QtCore.Qt.SizeFDiagCursor)
                self.moveType = 'AREALEFTTOP';
            elif(self.pointInRect(self.p, self.rtRect)):
                self.setCursor(QtCore.Qt.SizeBDiagCursor)
                self.moveType = 'AREARIGHTTOP';
            elif(self.pointInRect(self.p, self.lbRect)):
                self.setCursor(QtCore.Qt.SizeBDiagCursor);
                self.moveType = 'AREALEFTBOTTOM';
            elif(self.pointInRect(self.p, self.rbRect)):
                self.setCursor(QtCore.Qt.SizeBDiagCursor);
                self.moveType = 'AREARIGHTBOTTOM';
            elif(self.pointInRect(self.p, self.pixmap)):
                self.setCursor(QtCore.Qt.SizeAllCursor)
                self.moveType = 'AREAMOVE';
            else:
                self.setCursor(QtCore.Qt.ArrowCursor);
                self.moveType = 'AREAGRAB';

        # 移动之后重绘
        self.repaint();





    def mouseReleaseEvent(self, e):
        self.tempPoint = QtCore.QPoint(e.x(), e.y())
        self.repaint();


    def saveFile(self):
        file_path =  str(QtGui.QFileDialog.getSaveFileName(self,'save file',"saveFile" ,"jpeg files (*.jpeg);;all files(*.*)")) ####
        my_file_path = ''
        for i in file_path:
            if i == '/':
                my_file_path+='\\\\'
            else:
                my_file_path+=i
        try:
             self.pixmap.save(my_file_path)
        except ValueError:
            print 'error'
        sys.exit()

    def paintEvent(self, QPaintEvent):
        self.painter = QtGui.QPainter(self)
        self.painter.drawPixmap(0, 0, self.pixmap)

        if( self.ltPoint == self.tempPoint or self.tempPoint == self.rbPoint and self.rbPoint == QtCore.QPoint(0, 0)):
            self.paintGradient(0, 0, self.rect().width(), self.rect().height(), self.painter);
            return

#     //矩形上方的渐变
        self.paintGradient(0, 0, self.rect().width(), self.ltPoint.y(), self.painter);
#     //矩形左边的渐变
        self.paintGradient(0, self.ltPoint.y(), self.ltPoint.x(), QPaintEvent.rect().height(), self.painter);
#     //矩形正下方的渐变
        self.paintGradient(self.ltPoint.x(), self.tempPoint.y(), self.tempPoint.x() - self.ltPoint.x(), QPaintEvent.rect().height(), self.painter);
#     //矩形右边的渐变
        self.paintGradient(self.tempPoint.x(), self.ltPoint.y(),QPaintEvent.rect().width(), QPaintEvent.rect().height(), self.painter);
#     //保存画笔的状态
        self.painter.save();
#     绘制矩形边界
        self.paintBorder(self.ltPoint, self.tempPoint, self.painter);
        self.painter.restore();
#     画四个顶点的矩形
        self.paintStretchRect(self.ltPoint, self.tempPoint, self.painter);
# #


    # pixmap的setter方法
    def setPixmap(self, pixmap):
        pass

    # # 根据传过来坐标得到线性渐变对象，并设置颜色
    # def getLinearGadient(self, x, y, width, height):
    #     grad = QtGui.QLinearGradient(x, y, width, height);
    #     grad.setColorAt(0.0, QtGui.QColor(0, 0, 0, 100));
    #     return grad;

    # 根据坐标绘制渐变
    def paintGradient(self, x1, y1, width, height, painter):
        grad = QtGui.QLinearGradient(x1, y1, width, height)
        grad.setColorAt(0.0, QtGui.QColor(0, 0, 0, 100));
        painter.fillRect(x1, y1, width, height, grad);











    # 绘制边框
    def paintBorder(self, ltPoint, rbPoint):
        pen = QtGui.QPen.setColor(QtCore.Qt.blue)
        pen.setWidth(1)
        self.painter.setPen(pen)
        # 画左边界
        self.painter.drawLine(self.ltPoint.x(), self.ltPoint.y(), self.ltPoint.x(), self.rbPoint.y());
        # 画上边界
        self.painter.drawLine(ltPoint.x(), ltPoint.y(), rbPoint.x(), ltPoint.y());
        # 画右边界
        self.painter.drawLine(self.rbPoint.x(), self.ltPoint.y(), self.rbPoint.x(), self.rbPoint.y());
        # 画下边界
        self.painter.drawLine(self.ltPoint.x(), self.rbPoint.y(), self.rbPoint.x(), self.rbPoint.y());
    # 绘制边框上的四个可拉伸的小正方形













    def paintStretchRect(self, ltPoint, rbPoint):
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
        self.painter.fillRect(self.ltRect, brush);
        self.painter.fillRect(self.lbRect, brush);
        self.painter.fillRect(self.rtRect, brush);
        self.painter.fillRect(self.rbRect, brush);











    # 保存截取到的图片
    def savePixmap(self):
        pass
    # 判断左上角和右下角之间的坐标是否能够用来选取
    def isGrab(self, p1, p2):
        if( p2.x() > p1.x() and p2.y() > p1.y()):
            return True;
        return False;
    # 判断左下角与右上角之间的坐标
    def isGrabLeftBottom(self, p1, p2):
        if( self.p.x() < p2.x() and self.p.y() > p2.y()):
            return True;
        return False;
    # 判断点是否在矩形里面
    def pointInRect(self, qpoint, qrect):
        pass

    # 判断是否可以移动选取
    def isMove(self, ltPoint, rbPoint, moveX, moveY):
        if( (ltPoint.x() + moveX) < 0 or (ltPoint.y() + moveY) < 0
            or (rbPoint.x() + moveX) >= self.desktopWidth or (rbPoint.y() + moveY)
            >= self.desktopHeight) :
            return False
        return True

    # 鼠标移动类型
    def MoveType(self):
        'AREAGRAB','AREAMOVE', 'AREALEFTTOP', 'AREALEFTBOTTOM',
        'AREARIGHTTOP', 'AREARIGHTBOTTOM'















