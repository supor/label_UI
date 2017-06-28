# -*- coding:utf-8 -*-
# 公共方法

from selenium import webdriver
from time import sleep
from Projects.LABEL import pro_config as config
from framework import taf_logging as logger
# # import framework.taf_logging as logger


def set_up():
    driver = webdriver.Chrome('D:\chromedriver')
    driver.maximize_window()
    return driver


def tear_down(driver):
    driver.quit()


def find_by_xpath(driver, xpath, send_keys_text="", handle_type="click"):

    if handle_type is "click":
        driver.find_element_by_xpath(xpath).click()
        sleep(config.STIME)
    else:
        driver.find_element_by_xpath(xpath).send_keys(send_keys_text)
        sleep(config.STIME)


def find_by_id(driver, id_xpath, send_keys_text="", handle_type="click"):
    if handle_type is "click":
        driver.find_element_by_id(id_xpath).click()
        sleep(config.STIME)
    else:
        driver.find_element_by_id(id_xpath).send_keys(send_keys_text)
        sleep(config.STIME)


def assert_url(driver, url, assert_text):
    if driver.current_url == config.BASE_URL + url:
        logger.write_debug(u"%s 页面跳转正确" % assert_text)
    else:
        logger.write_debug(u"%s 页面跳转不正确" % assert_text)


def login(username, passwd):

    # 登录
    driver = set_up()
    driver.get(config.BASE_URL)
    logger.write_debug(u"启动chrome浏览器...")
    sleep(config.STIME)
    logger.write_debug(u"点击主页的登录按钮")
    driver.find_element_by_xpath("//*[@id='navbar-collapse-1']/ul/li[5]/a").click()
    logger.write_debug(u"输入用户名")
    find_by_id(driver, 'username', username, "send_keys")
    logger.write_debug(u"输入密码")
    find_by_id(driver, 'password', passwd, "send_keys")
    logger.write_debug(u"点击登录按钮")
    find_by_id(driver, 'submit')

    assert_url(driver, "distribution", u"登录成功")

    return driver
