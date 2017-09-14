# coding:utf-8
# 抽查员抽查流程

from time import sleep
from Projects.LABEL import pro_config as config
import framework.taf_logging as logger
from Projects.LABEL.UI.common import common


def stream_sample():

    _driver = common.diff_url_login(config.BASE_URL, 3)

    sleep(config.STIME)

    logger.write_debug(u"点击抽查，进入抽查管理页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[3]')

    logger.write_debug(u"点击新增抽查（流式），进入可抽查列表页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[1]/div')

    logger.write_debug(u"选择第一个任务，点击抽查")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]/a')
    common.find_by_id(_driver, 'new-sampling-job')

    logger.write_debug(u"放弃")
    common.find_by_id(_driver, "sampling-giveup")
    _driver.switch_to_alert().accept()
    sleep(config.STIME + 2)

    logger.write_debug(u"抽查驳回开始...")
    logger.write_debug(u"进入可抽查列表")
    _driver.get(config.BASE_URL + "spa/sample/sample-stream-available-jobs?sorts=&page=1&per_page=10&")
    sleep(config.STIME)
    logger.write_debug(u" 筛选出项目类型 （假脸识别）")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/select')

    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/select/option[12]')
    logger.write_debug(u"筛选出待抽查的数据...")
    logger.write_debug(u"点击抽查")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]/a')
    logger.write_debug(u"抽查个数选择")
    common.find_by_id(_driver, "reviewCount", send_keys_text="1", handle_type="send_keys")
    sleep(config.STIME+2)
    logger.write_debug(u"点击提交")
    common.find_by_xpath(_driver, '//*[@id="new-sampling-job"]')

    logger.write_debug(u"点击拒绝")
    common.find_by_id(_driver, "sampling-reject")
    _driver.switch_to_alert().accept()
    sleep(config.STIME)

    logger.write_debug(u"抽查通过开始...")
    logger.write_debug(u"进入可抽查列表")
    _driver.get(config.BASE_URL + "spa/sample/sample-stream-available-jobs?sorts=&page=1&per_page=10&")

    logger.write_debug(u" 筛选出项目类型 （假脸识别）")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/select')

    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/select/option[12]')

    logger.write_debug(u"筛选出待抽查的数据...")
    logger.write_debug(u"选择抽查")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]/a')

    logger.write_debug(u"抽查个数选择")
    # common.find_by_id(_driver, "reviewCount", send_keys_text="1", handle_type="send_keys")
    logger.write_debug(u"点击提交")
    common.find_by_xpath(_driver, '//*[@id="new-sampling-job"]')

    logger.write_debug(u"点击通过")
    common.find_by_id(_driver, "sampling-approve")
    _driver.switch_to_alert().accept()
    sleep(config.STIME)

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
