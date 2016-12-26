#!/bin/env  python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

a = np.arange(1, 10)
print(a)

plt.plot(a, a * 2, label="a")
plt.plot(a, a * 3, label="b")
plt.plot(a, a * 4, label="c")

#  loc  =1,2,3,4   分别代表 右上角,左上角,左下角,右下角

plt.legend(loc=0,title='testtitle',ncol=3)
plt.title('legend_test')

plt.show()
