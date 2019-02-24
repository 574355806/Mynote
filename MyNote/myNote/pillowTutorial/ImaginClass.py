#coding=utf-8

from PIL import Image

# im = Image.open("test.jpeg")
# im.show()
'''
ps：标准版本的show()方法不是很有效率，
因为它先将图像保存为一个临时文件，然后使用xv进行显示。
如果没有安装xv，该函数甚至不能工作。
但是该方法非常便于debug和test。
（windows中应该调用默认图片查看器打开）
'''
#im.show()


'''
format属性定义了图像的格式，如果图像不是从文件打开的，那么该属性值为None；
size属性是一个tuple，表示图像的宽和高（单位为像素）；
mode属性为表示图像的模式，常用的模式为：L为灰度图，RGB为真彩色，CMYK为pre-press图像。
'''
# print (im.format, im.size, im.mode)
'''
box = im.copy()
#4-tuple(left, upper, right, lower)
box = (100, 100, 400, 400)
#crop()方法可以从图片中提取一个子矩形
region = im.crop(box)
# region.save("ch_test.jpeg")
# print region.format, region.size, region.mode
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
'''

from PIL import Image
import glob, os

size = 128, 128

for infile in glob.glob("icon.png"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail", "JPEG")