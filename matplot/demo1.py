#!/bin/env  python
# coding=utf-8
__author__ = 'feel'

# import matplotlib.pyplot as plt
#
# plt.plot([1, 2, 3], [4, 5, 6])
#
# plt.show()
import numpy  as np
import matplotlib.pyplot as plt

# a = np.arange(1, 2, 4)
#
# x = np.arange(-5, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y, 'cx--')
#
# # plt.plot(x,'o')
# plt.savefig('a.png')
# plt.show()

# 0至5，每0.2一个点
t = np.arange(0., 5., 0.2)

# 同时绘制线性函数、平方函数、立方函数
plt.plot(t, t,    'r--',
         t, t**2, 'bs',
         t, t**3, 'g^')

plt.grid(True)
plt.show()