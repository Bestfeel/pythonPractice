#!/bin/env  python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 11)

plt.plot(x, x * x)

# 添加注释
plt.annotate('this is the  bottom', xy=(0, 1), xytext=(0, 20),
             arrowprops=dict(facecolor='g', frac=0.2, headwidth=20, width=15))

plt.show()
