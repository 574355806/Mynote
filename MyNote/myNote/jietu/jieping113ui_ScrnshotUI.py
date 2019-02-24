#coding=utf-8

from PyQt4 import QtGui,QtCore
import sys

from PIL import ImageGrab
'''
简单截屏
'''

class ScrnshotUI(QtGui.QWidget):
    def __init__(self):
        super(ScrnshotUI, self).__init__()

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)#Qt.FramelessWindowHint
        self.ltPoint = self.tempPoint = self.rbPoint =QtCore.QPoint(0,0)
        self.ltRect = self.rtRect = self.lbRect = self.rbRect = self.pixmapRect = QtCore.QRect()
        self.grab = True



        #设置窗体为整个屏幕
        self.scrPix = ImageGrab.grab()
        self.scrPix.save("bground.jpeg")

        self.pixmap = QtGui.QPixmap("bground.jpeg")

        width, height = self.scrPix.size
        self.resize(width+5, height+5)

    def mousePressEvent(self, e):
        if (e.button() == QtCore.Qt.LeftButton and self.grab):
            self.ltPoint = e.pos()
            self.repaint()
        self.clickPoint = e.pos()
        self.oldPoint = self.clickPoint

    def mouseMoveEvent(self, e):

        self.p = e.pos()
        # 临时的point
        m_tempPoint=QtCore.QPoint(0,0)

        self.moveType = self.MoveType()
        # 左键点击移动事件
        if (e.button() == QtCore.Qt.LeftButton):
            if self.moveType == 'AREAGRAB':
                # 如果移动后的坐标大于矩形左上角的坐标
                if(self.isGrab( self.ltPoint, self.p)):
                    self.tempPoint = self.p
                    self.repaint();
            elif self.moveType == 'AREALEFTBOTTOM':
                # 封装右上角的坐标
                m_tempPoint.setX( self.tempPoint.x())
                m_tempPoint.setY( self.ltPoint.y());
                if(self.isGrabLeftBottom(self.p, m_tempPoint)):
                     self.ltPoint.setX(self.p.x());
                     self.tempPoint.setY(self.p.y());

            elif self.moveType ==  'AREALEFTTOP':
                if( self.isGrab(self.p,  self.tempPoint)):
                    self.ltPoint = self.p;
            elif self.moveType == 'AREARIGHTBOTTOM':
                if(self.isGrab( self.ltPoint, self.p)):
                    self.tempPoint = self.p
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


         # 鼠标未点击的时候移动
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
                self.setCursor(QtCore.Qt.SizeFDiagCursor);
                self.moveType = 'AREARIGHTBOTTOM';
            elif(self.pointInRect(self.p, self.pixmapRect)):
                self.setCursor(QtCore.Qt.SizeAllCursor)
                self.moveType = 'AREAMOVE';
            else:
                self.setCursor(QtCore.Qt.ArrowCursor);
                self.moveType = 'AREAGRAB';

        # 移动之后重绘
        self.repaint();

    def mouseReleaseEvent(self, e):

        if(e.button() == QtCore.Qt.LeftButton):
            self.rbPoint = self.tempPoint;
            #释放鼠标的时候截取选中的部分的图片
            pix = self.pixmap.copy(self.ltPoint.x(), self.ltPoint.y(), self.rbPoint.x() - self.ltPoint.x(), self.rbPoint.y() - self.ltPoint.y());
            savedPixmap = pix;
            #保存图片
            self.savePixmap();
            self.pixmapRect.setX(self.ltPoint.x());
            self.pixmapRect.setY(self.ltPoint.y());
            self.pixmapRect.setWidth(self.rbPoint.x() - self.ltPoint.x());
            self.pixmapRect.setHeight(self.rbPoint.y() - self.ltPoint.y());

            self.grab = False;
            #初始化桌面的宽高
            self.desktopWidth = self.pixmap.width();
            self.desktopHeight = self.pixmap.height();



         # 鼠标移动类型

    def savePixmap(self):
        #生成图片名称
        picName = "小万截图";
        #获取当前系统时间，用做伪随机数的种子
        time = QtCore.QTime.currentTime()
        QtCore.qsrand(time.msec() + time.second() * 1000);
        #随机字符串
        randStr=QtCore.QString
        randStr.setNum(QtCore.qrand());
        picName.append(randStr);
        picName.append(".jpg");
        QtCore.qDebug() << "picName:" << picName << "qrand:" << QtCore.qrand();
        self.savedPixmap.save(picName, "JPG");

    def MoveType(self):
        'AREAGRAB','AREAMOVE', 'AREALEFTTOP', 'AREALEFTBOTTOM',
        'AREARIGHTTOP', 'AREARIGHTBOTTOM'

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
        if qpoint.x()>qrect.x() and qpoint.x()<qrect.x() +qrect.width() and qpoint.y()>qrect.y() and qpoint.y() <qrect.y()+qrect.height():
            return True
        else:
            return False
    # 判断是否可以移动选取
    def isMove(self, ltPoint, rbPoint, moveX, moveY):
        if( (ltPoint.x() + moveX) < 0 or (ltPoint.y() + moveY) < 0
            or (rbPoint.x() + moveX) >= self.desktopWidth or (rbPoint.y() + moveY)
            >= self.desktopHeight) :
            return False
        return True

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)

        if( self.ltPoint == self.tempPoint or self.tempPoint == self.rbPoint and self.rbPoint == QtCore.QPoint(0, 0)):

            self.paintGradient(0, 0, self.rect().width(), self.rect().height(), painter);
            return

        print self.rect().width

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

def main():

    app = QtGui.QApplication(sys.argv)
    ui = ScrnshotUI()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()