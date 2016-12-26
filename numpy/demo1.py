#!/bin/env  python
# coding=utf-8

import numpy as np

a = np.random.randint(0, 100, 20)

print(a)

np.savetxt('test.out', a, delimiter=',')

b=np.loadtxt('test.out',delimiter=',')

print(np.sort(b))
print(np.max(b))
print(np.min(b))
print(np.average(b))
print(np.var(b)) #方差
print(np.std(b)) #  标准差