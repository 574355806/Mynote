#coding=utf-8

import sys
from PyQt4 import QtCore, QtGui
from edytor import Ui_notepad
from os.path import isfile
import codecs

class StartQt4(QtGui.QMainWindow):
    def __init__(self, parent=None, flags=0):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_notepad()
        self.ui.setupUi(self)
        ''' click点击 button_open 执行file_dialog'''
        QtCore.QObject.connect(self.ui.button_open, QtCore.SIGNAL("clicked()"), self.file_dialog)
        ''' click点击 button_save 执行file_save保存'''
        QtCore.QObject.connect(self.ui.button_save, QtCore.SIGNAL("clicked()"), self.file_save)
        ''' editor_window的内容发送改变时，执行enable_save函数，enable = true'''
        QtCore.QObject.connect(self.ui.editor_window, QtCore.SIGNAL("textChanged()"),self.enable_save )

    def file_dialog(self):
        response = False
        # buttton texts
        SAVE = 'Save'
        DISCARD = 'Discard'
        CANCEL =  'Cancel'

        # if we have changes then ask about them
        if self.ui.button_save.isEnabled() and self.filename:
            message = QtGui.QMessageBox(self)
            message.setText('What to do about unsaved changes ?')
            message.setWindowTitle('Notpad')
            message.setIcon(QtGui.QMessageBox.Question)
            message.addButton(SAVE, QtGui.QMessageBox.AcceptRole)
            message.addButton(DISCARD, QtGui.QMessageBox.DestructiveRole)
            message.addButton(CANCEL, QtGui.QMessageBox.RejectRole)
            message.setDetailedText('Unsaved changes in file: '+ str(self.filename))
            message.exec_()
            response = message.clickedButton().text()

        # save file
        if response == SAVE:
            self.file_save()
            self.ui.button_save.setEnabled(False)

        # descard changes
        elif response == DISCARD:
            self.ui.button_save.setEnabled(False)

        # if we didn't cancelled show the file dialogue

        if response != CANCEL:
            ''' 使用QFileDialog来选择文件'''
            fd = QtGui.QFileDialog(self)
            ''' 使用getOpenFileName()弹出一个文件选择框
            fd.getOpenFileName()用于返回我们选择文件的名字。如果没有选择文件的话，会得打一个空的文件名
            '''
            self.filename = fd.getOpenFileName()
            if isfile(self.filename):
                text = codecs.open(self.filename, 'r', 'utf-8').read()
                self.ui.editor_window.setPlainText(text)
                self.ui.button_save.setEnabled(False)
            '''文本没有被保存的时候，显示提示消息 —— 通过save是否被禁用得到文本是否被保存'''


    def file_save(self):
        if isfile(self.filename):
            file = codecs.open(self.filename, 'w', 'utf-8')
            file.write(unicode(self.ui.editor_window.toPlainText()))
            file.close()
            self.ui.button_save.setEnabled(False)
           
    def enable_save(self):
        self.ui.button_save.setEnabled(True)


if __name__ == "__main__":
     app = QtGui.QApplication(sys.argv)
     myapp = StartQt4()
     myapp.show()
     sys.exit(app.exec_())