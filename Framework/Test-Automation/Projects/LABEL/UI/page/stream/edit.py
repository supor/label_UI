# coding:utf-8
# 标注员标注流程

from time import sleep
from Projects.LABEL import pro_config as config
import framework.taf_logging as logger
from Projects.LABEL.UI.common import common


def stream_edit():

    _driver = common.diff_url_login(config.BASE_URL_VENDOR, 1)
    sleep(config.STIME)

    logger.write_debug(u"点击标注，进入标注员管理页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[1]/div')
    logger.write_debug(u"点击流式标注，进入流式标注任务列表页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[5]/div')

    logger.write_debug(u"点击第一个任务的开始标注按钮")
    # //*[@id="subjob-list-body"]/table/tbody/tr[1]/td[1]
    common.get_list(_driver, config.STREAM_EDIT_TASK_NAME, '//*[@id="subjob-list-body"]/table/tbody/tr', u"标注",
                         '/td[3]/a', '/td[1]')
    # common.find_by_xpath(_driver, '//*[@id="subjob-list-body"]/table/tbody/tr[1]/td[3]/a')
    sleep(2)
    logger.write_debug(u"开始标注...")
    logger.write_debug(u"提交")
    common.find_by_id(_driver, "next1")

    logger.write_debug(u"跳过")
    common.find_by_id(_driver, "skip1")
    common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
    common.find_by_id(_driver, "next1")

    logger.write_debug(u"重标")
    common.find_by_id(_driver, "clear-data1")
    common.find_by_xpath(_driver, '/html/body/div[2]/div/div/div[3]/button[2]')
    common.find_by_id(_driver, "next1")

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
