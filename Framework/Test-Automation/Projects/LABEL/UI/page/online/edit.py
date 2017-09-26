# coding:utf-8
# 标注员标注流程

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def edit():

    _driver = common.diff_url_login(config.BASE_URL, 1)
    # _driver = common.diff_url_login(config.BASE_URL, 1)
    sleep(config.STIME)
    _driver.get("https://www.zzcrowd.com/editor/flow-select")
    common.find_by_xpath(_driver, '//*[@id="subjob-list-body"]/table/tbody/tr[1]/td[6]/a')
    for i in range(19077):
        common.find_by_id(_driver, 'next1')
        logger.write_debug(u"第%s个任务已标注完成" % i)

    # logger.write_debug(u"点击标注，进入标注员管理页面")
    # common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div/div')
    # logger.write_debug(u"点击流式标注，进入流式标注任务列表页面")
    # common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[5]/div')
    #
    # logger.write_debug(u"点击第一个任务的开始标注按钮")
    # common.find_by_xpath(_driver, '//*[@id="subjob-list-body"]/table/tbody/tr[1]/td[3]/a')
    #
    # logger.write_debug(u"开始标注...")
    # logger.write_debug(u"提交")
    # common.find_by_id(_driver, "next1")
    #
    # logger.write_debug(u"跳过")
    # common.find_by_id(_driver, "skip1")
    # common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
    # common.find_by_id(_driver, "next1")
    #
    # logger.write_debug(u"重标")
    # common.find_by_id(_driver, "clear-data1")
    # common.find_by_xpath(_driver, '/html/body/div[2]/div/div/div[3]/button[2]')
    # common.find_by_id(_driver, "next1")
    #
    # logger.write_debug(u"关闭浏览器")
    # common.tear_down(_driver)
