# !/bin/env  python
# coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.baidu.com')

# assert u'百度' in browser.title
#
# //*[@id="kw"] ,查找输入框,根据xpath

elem = browser.find_element_by_xpath('//*[@id="kw"]')

# 清空元素
elem.clear()
#  搜索seleniumhq,加上回车
elem.send_keys('seleniumhq' + Keys.RETURN)

# 点击事件
elem.click()
#  返回上一页
browser.back()

# browser.quit()
