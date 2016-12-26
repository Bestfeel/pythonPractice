#!/bin/env  python
# coding=utf-8

import numpy as np

a = [4, 3]
#  在列的方向上重复2次,行重复3次
tile = np.tile(a, [2, 3])
print(tile)

