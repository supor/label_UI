# coding:utf-8
# 检查员检查流程

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def stream_check():

    _driver = common.diff_url_login(config.BASE_URL, 2)

    sleep(config.STIME)

    logger.write_debug(u"点击检查，进入检查员管理页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[1]/div')

    logger.write_debug(u"点击流式检查，进入检查任务列表页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[4]/div')

    logger.write_debug(u"选择第一个任务，点击开始检查按钮")
    common.get_list(_driver, config.STREAM_CHECK_TASK_NAME, '//*[@id="subjob-list-body"]/table/tbody/tr', u"检查",
                         '/td[3]/a', '/td[1]')
    # common.find_by_xpath(_driver, '//*[@id="subjob-list-body"]/table/tbody/tr/td[3]/a')
    sleep(config.STIME+2)

    logger.write_debug(u"开始检查操作...")

    logger.write_debug(u"修改-修改")
    common.find_by_xpath(_driver, '//*[@id="opt-area-check"]/div[2]/div[1]/button[2]')
    common.find_by_id(_driver, "updateData")
    common.find_by_xpath(_driver, '/html/body/div[3]/div/div/div[3]/button')

    logger.write_debug(u"通过")
    common.find_by_id(_driver, "next2")
    sleep(config.STIME+2)

    logger.write_debug(u"修改-跳过")
    common.find_by_xpath(_driver, '//*[@id="opt-area-check"]/div[2]/div[1]/button[2]')
    common.find_by_id(_driver, "updateSkip")
    common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
    common.find_by_xpath(_driver, '/html/body/div[3]/div/div/div[3]/button')
    common.find_by_id(_driver, "next2")
    sleep(config.STIME + 2)

    logger.write_debug(u"驳回")
    common.find_by_id(_driver, 'reject2')
    common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
    sleep(config.STIME+2)

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
