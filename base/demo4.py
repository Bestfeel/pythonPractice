#!/bin/env  python
# coding=utf-8

import datetime
import threading


# 多线程
class MyThread(threading.Thread):
    def __init__(self, threadName, lock):
        self.lock = lock
        self.threadName = threadName
        '''
        注意此处比较调用父类初始化
        '''
        threading.Thread.__init__(self)

    def run(self):
        global g_num
        self.lock.acquire()
        for i in range(5):
            print(self.threadName + "--" + str(datetime.datetime.now()) + "......" + str(i))
            g_num += 1
            # threading._sleep(1)

        self.lock.release()


# 获取锁对象
lock = threading.Lock()

g_num = 0
for i in range(5):
    thread = MyThread("thread" + str(i), lock)
    thread.start()

threading._sleep(1)
print("计数:" + str(g_num))
