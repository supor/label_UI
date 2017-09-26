# coding:utf-8
# 检查员检查流程

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config
from Projects.LABEL.UI.page.multiqueue.edit.edit import edit


def check(work_flow_id):
    units = edit(work_flow_id)
    # units = [u'6186', u'6187', u'6188', u'6189']
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 2)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "checker/flow-select")
    sleep(config.STIME)

    # 获取对应的检查工作流
    elements = _driver.find_elements_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr')
    l = len(elements)
    logger.write_debug(u"检查列表总共 %s 条数据" % l)

    if l != 0:
        for i in range(1, l + 1):
            # 工作流id定位文本值
            text_1 = _driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[2]' % str(i)).text
            # 待检查数量文本值
            text_2 = _driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[5]' % str(i)).text
            # 检查中数量文本值
            text_3 = _driver.find_element_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[6]' % str(i)).text

            # 匹配选择的工作流的操作按钮xpath
            if text_1 == work_flow_id:
                if int(text_2) + int(text_3) >= 4:
                    _driver.find_element_by_xpath(
                        '//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[7]/a' % str(i)).click()
                    sleep(2)
                    for j in range(0, int(text_2) + int(text_3)):
                        unit_id = _driver.find_element_by_id("unit_id").text
                        if unit_id not in units:
                            # common.check_comments(_driver, unit_id, u"标注", config.USERNAME_VENDOR[1], u"通过")
                            logger.write_debug(u"提交unit %s" % unit_id)
                            common.scroll(_driver)
                            common.find_by_id(_driver, "next2")
                        if unit_id == units[0]:
                            logger.write_debug(u"标注通过的unit %s" % unit_id)
                            common.check_comments(_driver, unit_id, u"标注", config.USERNAME_VENDOR[1], u"通过")
                            logger.write_debug(u"测试检查-通过")
                            logger.write_debug(u"提交unit %s" % unit_id)
                            common.scroll(_driver)
                            common.find_by_id(_driver, 'next2')
                        if unit_id == units[1]:
                            logger.write_debug(u"标注跳过的unit %s" % unit_id)
                            common.check_comments(_driver, unit_id, u"标注", config.USERNAME_VENDOR[1], u"跳过", u"跳过")
                            logger.write_debug(u"测试检查-驳回")
                            logger.write_debug(u"驳回unit %s" % unit_id)
                            common.scroll(_driver)
                            common.find_by_id(_driver, 'reject2')
                            common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
                        if unit_id == units[2]:
                            logger.write_debug(u"标注通过的unit %s" % unit_id)
                            common.check_comments(_driver, unit_id, u"标注", config.USERNAME_VENDOR[1], u"通过")
                            logger.write_debug(u"测试检查-修改")
                            common.scroll(_driver)
                            common.find_by_xpath(_driver,
                                                 '//*[@id="singleImage"]/div[1]/div[3]/div/div[2]/label[2]/span')
                            # 标注为假脸
                            common.find_by_xpath(_driver, '//*[@id="opt-area-check"]/div[2]/div[1]/button[2]')
                            # 点击修改
                            common.scroll(_driver)
                            common.find_by_id(_driver, "updateData")
                            common.find_by_xpath(_driver, '/html/body/div[3]/div/div/div[3]/button')
                            logger.write_debug(u"提交unit %s" % unit_id)
                            common.find_by_id(_driver, 'next2')
                        if unit_id == units[3]:
                            logger.write_debug(u"标注通过的unit %s" % unit_id)
                            common.check_comments(_driver, unit_id, u"标注", config.USERNAME_VENDOR[1], u"通过")
                            logger.write_debug(u"测试检查-修改为跳过")
                            common.scroll(_driver)
                            common.find_by_xpath(_driver, '//*[@id="opt-area-check"]/div[2]/div[1]/button[2]')
                            # 点击跳过
                            common.find_by_id(_driver, "updateSkip")
                            common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
                            common.find_by_xpath(_driver, '/html/body/div[3]/div/div/div[3]/button')
                            logger.write_debug(u"提交unit %s" % unit_id)
                            common.find_by_id(_driver, 'next2')
                            break

                    break
                else:
                    raise Exception(u"工作流 %s 可检查的任务量不够，请检查数据" % work_flow_id)
            else:
                if i != l:
                    continue
                else:
                    raise Exception(u"工作流 %s 无待检查的数据，执行停止，请检查数据" % work_flow_id)
    else:
        raise Exception(u"无待检查的数据，执行停止,请检查数据")

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)








