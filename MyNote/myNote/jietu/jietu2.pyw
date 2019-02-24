#coding=utf-8

import  ctypes
import os

def capture():
    try:
        dll = ctypes.cdll.LoadLibrary("PrScrn.dll")
    except Exception:
        print ('Dll load error!')
        return
    else:
        try:
            dll.PrScrn(0)
        except Exception:
            print ('Sth wrong in capture!')
            return

def main():
    capture()

if __name__ == "__main__":
    main()

