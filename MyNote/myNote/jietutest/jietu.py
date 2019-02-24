#coding=utf-8

import sys,time
import os.path
from PyQt4 import QtGui, QtCore, QtWebKit

class PageShotter(QtGui.QWidget):
    def __init__(self, url, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.url = url

    def shot(self):
        webView = QtWebKit.QWebView(self)
        webView.load(QtCore.QUrl(self.url))
        self.webPage = webView.page()
        self.connect(webView, QtCore.SIGNAL("loadFinished(bool)"), self.savePage)

    def savePage(self, finished):
        if finished:
            print "开始截图！"
            size = self.webPage.mainFrame().contentsSize()
            print "页面宽：%d，页面高：%d" % (size.width(), size.height())
            self.webPage.setViewportSize(QtCore.QSize(size.width() + 16, size.height()))
            img = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
            painter = QtGui.QPainter(img)
            self.webPage.mainFrame().render(painter)
            painter.end()
            fileName = "shot.png"
            if img.save(fileName):
                filePath = os.path.join(os.path.dirname(__file__), fileName)
                print "截图完毕：%s" % filePath
            else:
                print "截图失败"
        else:
            print "网页加载失败！"
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    shotter = PageShotter("https://www.jd.com/")
    shotter.shot()
    sys.exit(app.exec_())