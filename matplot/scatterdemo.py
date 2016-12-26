#!/bin/env  python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


#  1000个样本值
N=1000
x=np.random.randn(N)
y=np.random.randn(N)

print(x)
plt.scatter(x,y,alpha=0.5,s=100,c='r')
plt.show()