#coding=utf-8

from PyQt4 import QtGui,QtCore

class hello:
    def __init__(self):
        self.a = 0
        self.helloforyou()


    def helloforyou(self):
        self.a=11

    def hellohello(self):
        return self.a

if __name__ == '__main__':
    hlo = hello()
    print hlo.hellohello()
