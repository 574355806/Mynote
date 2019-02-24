#coding=utf-8

from PyQt4 import QtGui
im = QtGui.QPixmap.grabWindow(100,100,200,200)
im.save("117.jpeg")