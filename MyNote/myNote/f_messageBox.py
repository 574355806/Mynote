#coding=utf-8

"""
This program shows a confirmation
message box when we click on the close
button of the application window.
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()


    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message',
                                           "Are you sure to quit?", QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        #QtGui.QMessageBox.question()方法的第二个参数是出现在标题栏的标题，
        # 第三个参数是消息框显示的对话内容，
        # 第四个参数是出现在消息框的按钮的组合【用或( | )连接】，
        # 最后一个参数是默认按钮，即消息框刚跳出来的时候按enter键就可以执行的按钮


        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()