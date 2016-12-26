#!/bin/env  python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

a=np.arange(1,20)
print(a)
plt.figure()
plt.subplot(121)
plt.plot(a,a)
plt.subplot(122)
plt.plot(a,a*a)




plt.show()