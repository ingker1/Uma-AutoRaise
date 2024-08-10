#配合开发者模式获取屏幕像素点颜色

import os
from PIL import Image

a,b=(input().split(','))
a = int(a)
b = int(b)


# 获取屏幕截图
os.system("adb shell screencap -p /sdcard/screenshot.png")
os.system("adb pull /sdcard/screenshot.png")

# 打开图像并获取颜色
im = Image.open("screenshot.png")
rgb_im = im.convert('RGB')

#rv_im = im.crop(360, 300, 382, 300+40)

r, g, b = rgb_im.getpixel((a, b))
print(f"{r}, {g}, {b}")