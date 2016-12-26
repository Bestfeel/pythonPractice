#!/bin/env  python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
#  绘制 均值为100 , 标准差为20 的 直方图
N = 100
sigma = 20

x = N + sigma * np.random.randn(1000)
print x
print(np.mean(x))

print(np.var(x))
print(np.std(x))

# normed  是否 标准化
plt.hist(x, bins=20, color='green', normed=False)

# plt.hist2d(x,x,bins=10)
plt.show()
