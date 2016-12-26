#!/bin/env  python
# coding=utf-8
import matplotlib.pyplot as plt

# [u'dark_background', u'bmh', u'grayscale', u'ggplot', u'fivethirtyeight']

plt.style.use('ggplot')
print(plt.style.available)
fig = plt.figure()
#  add_subplot  的参数 221    ,22 表示 2x2 的图可绘制4张图, 1 表示 在第一个位置
ax1 = fig.add_subplot(221)  # 将当前绘图区域划分为2个子区域，并使用第一
ax1.plot([1, 2, 3], [1, 2, 3])

ax2 = fig.add_subplot(222)  # 使用第二个
ax2.plot([0, 1, 2], [0, 2, 1])

ax3 = fig.add_subplot(223)  # 使用第三个
ax3.plot([1, 2, 3], [3, 2, 1])
ax4 = fig.add_subplot(224)  # 使用第四个
ax4.plot([0, 1, 2], [0, 2, 1])
plt.show()
