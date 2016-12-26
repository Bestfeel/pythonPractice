#!/bin/env  python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

a=np.arange(1,20,1)

y1=a*a
y2=np.log(a)
plt.plot(a,y1)

#  添加另一个刻度

plt.twinx()

plt.plot(a,y2,'r-')
plt.show()
