#!/bin/env  python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
# 如果使用相同的seed( )值，则每次生成的随即数都相同,如果不设置这个值，
# 则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
np.random.seed(1000)
# loc 为均值,scale 为  标准差
mu, sigma = 0, 1
data = np.random.normal(loc=mu, scale=sigma, size=(1000,4))

labels=['A','B','C','D']
#  whis  越大 , 虚线越长
plt.boxplot(data, sym='o', whis=1,labels=labels)
plt.show()
