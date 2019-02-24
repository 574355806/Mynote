#coding=utf-8

from PIL import ImageDraw,Image
Im = Image.open("test.jpeg")
# drawObject = ImageDraw.Draw()
# drawObject.rectangle((200,200,500,500),outline = "red")
# drawObject.rectangle((250,300,450,400),fill = 128)

draw = ImageDraw.Draw(Im)
x=100
y=100
width=100
height=100
draw.line([(x,y),(x+width,y),(x+width,y+height),(x,y+width),(x,y)], width=3, fill="red")