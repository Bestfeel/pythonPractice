# !/bin/env  python
# coding=utf-8

import pytesseract

from PIL import Image

#  mac 下安装   sudo port install tesseract

image = Image.open('aa.png')
print image

# vcode = pytesseract.image_to_string(image, config='-psm 7')


vcode = pytesseract.image_to_string(image)

print (vcode)
print  len('ZBW‘')
