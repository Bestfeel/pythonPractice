#!/bin/env  python
# coding=utf-8
import matplotlib.pyplot as plt

labs = 'A', 'B', 'C', 'D'
faces = [14, 13, 54, 11]
#  expode
expode = [0, 0, 0.05, 0]
# 画图比例
plt.axes(aspect=1)
#  autopct 显示所占的比例值,expode   凸出显示
plt.pie(x=faces, explode=expode, labels=labs, autopct='%.0f%%')

# plt.pie(x=faces, labels=labs, autopct='%.0f%%')
plt.grid(True)
plt.show()
