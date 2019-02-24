#coding=utf-8

from PIL import ImageGrab
im = ImageGrab.grab(bbox=(10,10,510,510))
print im
im.save("2.png")