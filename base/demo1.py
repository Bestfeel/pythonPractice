#!/bin/env  python
# coding=utf-8

import time
from functools import wraps


def fun1(f):
    @wraps(f)
    def dec(*args, **kwargs):
        print ("装饰之前。。。。")
        f()
        print ("装饰之后。。。。。")

    return dec


@fun1
def myfun():
    print (time.localtime())


myfun()
