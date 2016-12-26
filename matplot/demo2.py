#!/bin/env  python
# coding=utf-8
from pylab import *

N = 5

index = np.arange(N)
y = np.array([1, 44, 2, 54, 12])

leftLenght = 0.5
# plt.bar(left=index, height=y, color='yellow', width=0.5)

#  画重叠图
# plt.bar(left=index + leftLenght, height=y, color='red', width=0.5)

# plt.plot(index,y,'r-')

plt.barh(bottom=index,width=y)

plt.show()
