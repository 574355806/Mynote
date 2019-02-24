#coding=utf-8

import sys
from PyQt4 import QtCore, QtGui      #调用库函数
from secondtest import Ui_MainWindow
class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # QtCore.QObject.connect(self.ui.button_open,QtCore.SIGNAL("clicked()"), self.file_dialog)     #open按钮被点击后跳到自定义函数file_dialog
        # QtCore.QObject.connect(self.ui.button_save,QtCore.SIGNAL("clicked()"), self.file_save)

    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()    #getOpenFileName()函数   “打开”
        from os.path import isfile
        if isfile(self.filename):
            s = open(self.filename,'r').read()
            self.ui.editor_window.setPlainText(s)

    def file_save(self):
        fd =  QtGui.QFileDialog()
        self.filename =fd.getSaveFileName()       #getSaveFileName()函数     “另存为”
        fobj =open(self.filename,'w')
        fobj.write(self.ui.editor_window.toPlainText())
        fobj.close()
        self.ui.editor_window.setText('File saved!!')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())