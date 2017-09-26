# coding:utf-8
# 小组长批驳流程

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def refute(review_unit_id, leader_n, review_number, sample_proportion, reject_number, part_approve, refute_handle):
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, leader_n)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "spa/manager/task-flow/review-job?page=1&per_page=10&state=1")
    sleep(config.STIME+1)

    # 获取对应的待批驳验收包
    elements = _driver.find_elements_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr')
    sleep(config.STIME)
    l = len(elements)
    logger.write_debug(u"验收列表总共 %s 条数据" % l)

    if l != 0:
        for i in range(1, l + 1):
            # 验收包名称（id）
            text_1 = _driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[1]' % str(i)).text

            # 匹配选择的工作流的操作按钮xpath
            if text_1 == review_unit_id:
                # 验收总数
                text_2 = _driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[4]' % str(i)).text
                # 抽样（比例）
                text_3 = _driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[5]' % str(i)).text
                # 驳回（哭脸）
                text_4 = _driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[6]' % str(i)).text
                # 是否是部分通过
                text_5 = _driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[7]' % str(i)).text
                # 当前状态
                text_6 = _driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[8]' % str(i)).text

                logger.write_debug(u"开始校验待批驳数据的正确性")
                common.check_text(review_number, text_2, u"验收总数")
                common.check_text(sample_proportion, text_3, u"抽样(比例)")
                common.check_text(reject_number, text_4, u"驳回(哭脸)")
                common.check_text(part_approve, text_5, u"是否部分通过")
                common.check_text(text_6, u"待批驳", u"当前状态")

                logger.write_debug(u"点击批驳按钮进入批驳页面")
                common.find_by_xpath(_driver,
                                     '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[9]/a' % str(i))
                sleep(config.STIME + 0.5)
                logger.write_debug(u"批驳操作")
                if refute_handle == u"同意驳回":
                    logger.write_debug(u"批驳-同意驳回")
                    common.find_by_id(_driver, "approve")
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '/html/body/div[4]/div/div/div[3]/button[2]')
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '/html/body/div[4]/div/div/div[3]/button[2]')
                    sleep(config.STIME)

                if refute_handle == u"反对驳回":
                    logger.write_debug(u"批驳-反对驳回")
                    common.find_by_id(_driver, "reject")
                    sleep(config.STIME)
                    common.find_by_id(_driver, "reason-btn")
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '/html/body/div[5]/div/div/div[3]/button[2]')

                break

            else:
                if i != l:
                    continue
                else:
                    raise Exception(u"待批驳的验收包%s不存在，执行停止，请确认数据" % review_unit_id)
    else:
        raise Exception(u"无待批驳的数据，执行停止,请确认数据")

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)


