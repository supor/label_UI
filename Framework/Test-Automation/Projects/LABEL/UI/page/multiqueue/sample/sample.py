# coding:utf-8
# 抽查员抽查流程

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def sample(work_flow_id):
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "spa/sample/task-flow-jobs")
    sleep(config.STIME)

    # 获取对应的抽查工作流
    elements = _driver.find_elements_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr')
    sleep(config.STIME)
    l = len(elements)
    logger.write_debug(u"抽查列表总共 %s 条数据" % l)

    if l != 0:
        for i in range(1, l + 1):
            # 工作流id定位文本值
            text_1 = _driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[1]' % str(i)).text
            # 待抽查数量文本值
            text_2 = _driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[5]' % str(i)).text

            # 匹配选择的工作流的操作按钮xpath
            if text_1 == work_flow_id:
                if int(text_2) >= 4:
                    _driver.find_element_by_xpath(
                        '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[6]/div/button/i' % str(i)).click()
                    sleep(2)
                    # total_text = common.get_text(_driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]').text, 0)
                    # sleep(config.STIME)
                    # if total_text == text_2:
                    #     logger.write_debug(u"共筛选出的抽查任务个数正确，个数为：%s" % total_text)
                    # else:
                    #     logger.write_error(u"共筛选出的抽查任务个数错误，显示为：%s, 应该是：%s" % (total_text, text_2))
                    logger.write_debug(u"抽查-放弃流程")
                    logger.write_debug(u"抽样出一个任务")
                    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]/input[1]').clear()
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/input[1]', "1", "send_keys")
                    logger.write_debug(u"点击开始抽查")
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/button')
                    sleep(1)
                    logger.write_debug(u"点击放弃")
                    common.find_by_id(_driver, "sampling-giveup")
                    _driver.switch_to_alert().accept()
                    sleep(config.STIME)

                    # logger.write_debug(u"获取待抽查总数")
                    # text_3 = _driver.find_element_by_xpath(
                    #     '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[5]' % str(i)).text
                    # sleep(config.STIME)
                    # if text_3 == text_2:
                    #     logger.write_debug(u"抽查放弃成功")
                    # else:
                    #     logger.write_error(u"放弃后的任务数没有被释放，放弃失败")
                    # # 校验抽查包 #TODO

                    logger.write_debug(u"抽查-驳回流程")
                    common.find_by_xpath(
                        _driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[6]/div/button/i' % str(i))
                    logger.write_debug(u"抽样出一个任务")
                    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]/input[1]').clear()
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/input[1]', "1", "send_keys")
                    logger.write_debug(u"点击开始抽查")
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/button')
                    logger.write_debug(u"显示所有的unit")
                    common.find_by_xpath(_driver, '//*[@id="main"]/div[3]/div[1]/div/div/form/div/select')
                    common.find_by_xpath(_driver, '//*[@id="main"]/div[3]/div[1]/div/div/form/div/select/option[1]')
                    common.find_by_xpath(_driver, '//*[@id="main"]/div[3]/div[1]/div/div/form/button')
                    logger.write_debug(u"获取unit_id")
                    reject_unit_id = _driver.find_element_by_xpath('//*[@id="image-panel"]/div[1]/div').get_attribute(
                        "id")
                    sleep(config.STIME + 1)
                    logger.write_debug(u"正在抽查驳回的unit_id为：%s" % reject_unit_id)
                    logger.write_debug(u"点击驳回按钮")
                    common.find_by_id(_driver, "sampling-reject")
                    _driver.switch_to_alert().accept()
                    sleep(config.STIME)

                    logger.write_debug(u"校验抽查驳回后的操作评论的正确性")
                    common.check_comment_after(_driver, reject_unit_id, u"抽查",
                                               config.USERNAME_VENDOR[0], u"驳回(笑脸)")

                    logger.write_debug(u"抽查-部分通过流程")
                    _driver.get(config.BASE_URL + "spa/sample/task-flow-jobs")
                    sleep(config.STIME)
                    common.find_by_xpath(
                        _driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[6]/div/button/i' % str(i))
                    logger.write_debug(u"抽样出一个任务")
                    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]/input[1]').clear()
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/input[1]', "2", "send_keys")
                    logger.write_debug(u"点击开始抽查")
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/button')
                    logger.write_debug(u"显示所有的unit")
                    common.select_all(_driver)
                    logger.write_debug(u"获取unit_id")
                    part_approve_unit_id = _driver.find_element_by_xpath(
                        '//*[@id="image-panel"]/div[1]/div').get_attribute("id")
                    sleep(config.STIME)
                    part_reject_unit_id = _driver.find_element_by_xpath(
                        '//*[@id="image-panel"]/div[2]/div').get_attribute("id")
                    sleep(config.STIME)
                    logger.write_debug(u"正在抽查部分通过的通过的unit_id为：%s， 驳回的unit_id为：%s" %
                                       (part_approve_unit_id, part_reject_unit_id))
                    logger.write_debug(u"把驳回的unit %s 标记为哭脸" % part_reject_unit_id)
                    _driver.find_element_by_xpath('//*[@id="%s"]/div[2]/img' % str(part_reject_unit_id)).click()
                    sleep(config.STIME)
                    logger.write_debug(u"点击部分通过按钮")
                    common.find_by_id(_driver, "sampling-partapprove")
                    _driver.switch_to_alert().accept()
                    sleep(config.STIME)

                    logger.write_debug(u"校验抽查部分通过后的操作评论的正确性")
                    logger.write_debug(u"校验部分通过的操作评论")
                    common.check_comment_after(_driver, part_approve_unit_id, u"抽查",
                                               config.USERNAME_VENDOR[0], u"通过(笑脸)")
                    logger.write_debug(u"校验部分驳回的操作评论")
                    common.check_comment_after(_driver, part_reject_unit_id, u"抽查",
                                               config.USERNAME_VENDOR[0], u"驳回(哭脸)")

                    logger.write_debug(u"抽查-通过流程")
                    _driver.get(config.BASE_URL + "spa/sample/task-flow-jobs")
                    sleep(config.STIME)
                    common.find_by_xpath(
                        _driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[6]/div/button/i' % str(i))
                    logger.write_debug(u"抽样出一个任务")
                    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]/input[1]').clear()
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/input[1]', "1", "send_keys")
                    logger.write_debug(u"点击开始抽查")
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/button')
                    logger.write_debug(u"显示所有的unit")
                    common.find_by_xpath(_driver, '//*[@id="main"]/div[3]/div[1]/div/div/form/div/select')
                    common.find_by_xpath(_driver, '//*[@id="main"]/div[3]/div[1]/div/div/form/div/select/option[1]')
                    common.find_by_xpath(_driver, '//*[@id="main"]/div[3]/div[1]/div/div/form/button')
                    logger.write_debug(u"获取unit_id")
                    approve_unit_id = _driver.find_element_by_xpath(
                        '//*[@id="image-panel"]/div/div[1]').get_attribute("id")
                    sleep(config.STIME)
                    logger.write_debug(u"正在抽查通过的unit_id为：%s" % approve_unit_id)
                    logger.write_debug(u"点击通过按钮")
                    common.find_by_id(_driver, "sampling-approve")
                    _driver.switch_to_alert().accept()

                    logger.write_debug(u"校验抽查通过的操作评论")
                    common.check_comment_after(_driver, approve_unit_id, u"抽查",
                                               config.USERNAME_VENDOR[0], u"通过(笑脸)")
                    sleep(3)
                    break
                else:
                    raise Exception(u"工作流 %s 可抽查的任务量不够，请抽查数据" % work_flow_id)
            else:
                if i != l:
                    continue
                else:
                    raise Exception(u"工作流 %s 无待抽查的数据，执行停止，请抽查数据" % work_flow_id)
    else:
        raise Exception(u"无待抽查的数据，执行停止,请抽查数据")

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
