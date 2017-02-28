#!/bin/env  python
# coding=utf-8

import multiprocessing
import os

'''
计数
'''


def add(num):
    print("pid:" + str(os.getpid()))


record = []

for i in range(5):
    process = multiprocessing.Process(target=add, name="node" + str(i) + "pid:" + str(os.getpid()), args=(i,))
    process.start()
    record.append(process)

for p in record:
    p.join()
