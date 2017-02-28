#!/bin/env  python
# coding=utf-8
from abc import abstractmethod, ABCMeta


class AbstractMyClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def show(self):
        print("show .....")


class SomeClass(AbstractMyClass):
    def show(self):
        print ("必须实现抽象方法")


def funSwitch(args):
    return {
        "name": "feel",
        "age": 20
    }[args]


print(funSwitch("name"))
