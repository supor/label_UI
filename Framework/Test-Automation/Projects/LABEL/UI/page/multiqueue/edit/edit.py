# coding:utf-8
# 标注员标注流程

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def edit(work_flow_id):
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 1)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "editor/flow-select")
    sleep(config.STIME)

    # 获取对应的标注工作流
    elements = _driver.find_elements_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr')
    l = len(elements)
    logger.write_debug(u"标注列表总共 %s 条数据" % l)

    units = []
    if l != 0:
        for i in range(1, l + 1):
            # 工作流id定位文本值
            text_1 = _driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[2]' % str(i)).text
            # 待标注数量文本值
            text_2 = _driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[5]' % str(i)).text
            # 标注中数量文本值
            text_3 = _driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[6]' % str(i)).text

            # 匹配选择的工作流的操作按钮xpath
            if text_1 == work_flow_id:
                if int(text_2) + int(text_3) >= 2:
                    _driver.find_element_by_xpath(
                        '//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[7]/a' % str(i)).click()
                    sleep(config.STIME)
                    for j in range(0, int(text_2) + int(text_3)):
                        unit_id = _driver.find_element_by_id("unit_id").text
                        if j == 0:
                            sleep(2)
                            logger.write_debug(u"重标并提交unit %s" % unit_id)
                            common.scroll(_driver)
                            sleep(2)
                            common.find_by_xpath(_driver,
                                                 '//*[@id="singleImage"]/div[1]/div[3]/div/div[2]/label[2]/span')

                            common.find_by_id(_driver, 'clear-data1')
                            common.find_by_xpath(_driver, '/html/body/div[2]/div/div/div[3]/button[2]')
                            common.find_by_id(_driver, "next1")
                            units.append(unit_id)
                        if j == 1:
                            logger.write_debug(u"跳过unit %s" % unit_id)
                            common.scroll(_driver)
                            common.find_by_id(_driver, 'skip1')
                            common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
                            units.append(unit_id)
                        if j == 2:
                            logger.write_debug(u"提交unit %s" % unit_id)
                            common.scroll(_driver)
                            common.find_by_id(_driver, "next1")
                            units.append(unit_id)
                        if j == 3:
                            logger.write_debug(u"提交unit %s" % unit_id)
                            common.scroll(_driver)
                            common.find_by_id(_driver, "next1")
                            units.append(unit_id)
                            break
                    break
                else:
                    raise Exception(u"工作流 %s 可标注的任务量不够，请检查数据" % work_flow_id)
            else:
                if i != l:
                    continue
                else:
                    raise Exception(u"工作流 %s 无待标注的数据，执行停止，请检查数据" % work_flow_id)
    else:
        raise Exception(u"无待标注的数据，执行停止,请检查数据")

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
    logger.write_debug(units)
    return units

