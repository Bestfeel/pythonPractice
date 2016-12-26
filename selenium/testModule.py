# !/bin/env  python
# coding=utf-8


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


def getFun(driver, times, func):
    return WebDriverWait(driver, times).until(func)


def openBrower():
    '''

    :return:  webdriver handle
    '''
    return webdriver.Chrome()


def openUrl(handle, url):
    handle.get(url)


text_id = ""


def findElement(d, **args):
    if text_id in args:
        ele_login = getFun(d, 10, lambda d: d.find_element_by_link_text(args['text_id']))
        ele_login.click()


def main():
    pass


if __name__ == '__main__':
    main()
