# !/bin/env  python
# coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


driver.get('http://site.gizwits.com/zh-cn/developer/product')
cookie1 = {'name': 'CNZZDATA1259661796',
           'value': '1818071549-1472107878-http%253A%252F%252Fsite.gizwits.com%252F%7C1472107878'}
driver.add_cookie(cookie1)
driver.add_cookie({'name': 'Hm_lvt_3787e6b3b29a084fde41f22828d89b7d', 'value': '1472110051'})
driver.add_cookie({'name': 'Hm_lvt_c4c9e1db84e605270799d6222c5c44c8', 'value': '1472110051'})
driver.add_cookie({'name': '__referer', 'value': 'site.gizwits.com'})
driver.add_cookie({'name': 'csrftoken', 'value': 'xxxxxxxxxx'})
driver.add_cookie({'name': 'django_language', 'value': 'zh-cn'})
driver.add_cookie({'name': 'sessionid', 'value': 'xxxxxxxxxx'})
driver.get('http://site.gizwits.com/zh-cn/developer/product')