# !/bin/env  python
# coding=utf-8
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


def getFun(driver, times, func):
    return WebDriverWait(driver, times).until(func)


driver = webdriver.Chrome()

# 打开网址
driver.get('http://www.maiziedu.com')

# 网页最大化
driver.maximize_window()

#  生成用户行为
elem = getFun(driver, 1, lambda driver: driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div[2]/ul/li[6]"))

#  将鼠标移动到该元素上

time.sleep(2)
ActionChains(driver).move_to_element(elem).perform()

time.sleep(1)
#  查找软件测试点击进入
driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[2]/ul/li[6]/a').click()

#  查看窗口句柄
hadles = driver.window_handles
print  hadles

# 窗口切换

driver.switch_to_window(hadles[0])
print  driver.current_url
print driver.current_window_handle
