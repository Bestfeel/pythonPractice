# !/bin/env  python
# coding=utf-8
import time

from selenium import webdriver

driver = webdriver.Chrome()

# 打开网址
driver.get('http://www.maiziedu.com')

#  login
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/a[2]').click()

# user ,passwd , maizi_test@139.com , abc123456

# user   //*[@id="id_account_l"]


#  在登入界面中,这里要注意的地方是,可能因为网络原因导致,上面的页面还没打开,所以先睡眠几秒

time.sleep(3)

user = driver.find_element_by_id('id_account_l')

user.clear()
accont = 'maizi_test@139.com'
pwd = 'abc123456'
user.send_keys(accont)

#
passwd = driver.find_element_by_id('id_password_l')
#
passwd.clear()
passwd.send_keys(pwd)

login = driver.find_element_by_xpath('//*[@id="login_btn"]')

login.click()
