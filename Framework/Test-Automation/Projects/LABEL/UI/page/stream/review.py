# coding:utf-8
# 验收员验收流程

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def stream_review():

    _driver = common.diff_url_login(config.BASE_URL, 4)

    sleep(config.STIME)

    logger.write_debug(u"点击验收，进入验收管理页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[1]/div')
    # common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[2]')

    logger.write_debug(u"点击新增验收（流式），进入验收任务页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[5]/div')
    # common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[6]')

    logger.write_debug(u"选择第一个任务，点击验收")
    common.get_list(_driver, config.STREAM_REVIEW_TASK_NAME, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr',
                         u"验收", '/td[10]/a', '/td[2]')
    # common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[11]/a')
    # 填入验收的数量
    _driver.find_element_by_id("reviewCount").clear()
    sleep(config.STIME)
    common.find_by_id(_driver, 'reviewCount', "3", "send_keys")
    # 点击提交验收按钮
    common.find_by_id(_driver, 'new-review-commit')

    logger.write_debug(u"验收-驳回")
    common.find_by_id(_driver, "reject")

    common.find_by_id(_driver, "reason-btn")
    sleep(config.STIME + 2)

    # logger.write_debug(u"进入批驳...")
    # logger.write_debug(u"返回首页")
    # common.find_by_xpath(_driver, '//*[@id="navbar"]/div[2]/ul/li[1]/a')
    # logger.write_debug(u"点击任务管理，进入管理员页面")
    # common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[1]/div')
    # logger.write_debug(u"点击批驳验收，进入批驳列表")
    # common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[2]/div')
    # logger.write_debug(u"批驳按钮，进入批驳页面")
    # common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[2]/div[2]/table/tbody/tr/td[12]/a')
    # logger.write_debug(u"反对驳回")
    # common.find_by_id(_driver, 'reject')
    # common.find_by_id(_driver, 'reason-btn')
    # common.find_by_xpath(_driver, '/html/body/div[5]/div/div/div[3]/button[2]')
    # sleep(config.STIME + 2)

    # logger.write_debug(u"进入管理验收页面")
    # logger.write_debug(u"返回首页")
    # common.find_by_xpath(_driver, '//*[@id="navbar"]/div[2]/ul/li[1]')
    # logger.write_debug(u"点击验收，进入验收管理页面")
    # common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[2]/div')
    #
    # logger.write_debug(u" 筛选出项目类型 （假脸识别）")
    # common.find_by_xpath(_driver, '//*[@id="condition-area"]/select[1]')
    # common.find_by_xpath(_driver, '//*[@id="condition-area"]/select[1]/option[10]')
    #
    # logger.write_debug(u"筛选出验收中的数据...")
    # logger.write_debug(u"选择验收")
    # common.find_by_xpath(_driver, '//*[@id="condition-area"]/select[2]')
    # common.find_by_xpath(_driver, '//*[@id="condition-area"]/select[2]/option[2]')
    # logger.write_debug(u"点击提交")
    # common.find_by_xpath(_driver, '//*[@id="condition-area"]/button')

    logger.write_debug(u"放弃验收开始。。。")
    _driver.get(config.BASE_URL_VENDOR + "spa/review/stream-reviewable-jobs?page=1&per_page=10")
    sleep(config.STIME)
    logger.write_debug(u"选择第一个任务，点击验收")
    common.get_list(_driver, config.STREAM_REVIEW_TASK_NAME,
                         '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr',
                         u"验收", ']/td[10]/a', ']/td[2]')
    # 填入验收的数量
    _driver.find_element_by_id("reviewCount").clear()
    sleep(config.STIME)
    common.find_by_id(_driver, 'reviewCount', "2", "send_keys")
    # 点击提交验收按钮
    common.find_by_id(_driver, 'new-review-commit')

    logger.write_debug(u"点击放弃")
    common.find_by_id(_driver, 'giveup')
    _driver.switch_to_alert().accept()
    sleep(config.STIME + 2)

    logger.write_debug(u"验收通过开始。。。")
    _driver.get(config.BASE_URL_VENDOR + "spa/review/stream-reviewable-jobs?page=1&per_page=10")
    sleep(config.STIME)
    logger.write_debug(u"选择第一个任务，点击验收")
    common.get_list(_driver, config.STREAM_REVIEW_TASK_NAME,
                         '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr',
                         u"验收", '/td[10]/a', '/td[2]')
    # 填入验收的数量
    _driver.find_element_by_id("reviewCount").clear()
    sleep(config.STIME)
    common.find_by_id(_driver, 'reviewCount', "2", "send_keys")
    # 点击提交验收按钮
    common.find_by_id(_driver, 'new-review-commit')

    logger.write_debug(u"点击通过")
    common.find_by_id(_driver, "approve")
    _driver.switch_to_alert().accept()
    sleep(config.STIME)

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
