#coding=utf-8

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

def main():
    app = QApplication(sys.argv)
    btn = QPushButton("Hello Jakey!")
    btn.show()
    app.connect(btn, SIGNAL("clicked()"), app, SLOT("quit()"))
    app.exec_()
if __name__ == '__main__':
     main()