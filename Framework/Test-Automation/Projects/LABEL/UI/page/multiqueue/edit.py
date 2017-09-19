# coding:utf-8
# 标注员标注流程

import time
from time import sleep
from Projects.LABEL import pro_config as config
import framework.taf_logging as logger
from Projects.LABEL.UI.common import common


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
                            sleep(2)
                            common.find_by_xpath(_driver,
                                                 '//*[@id="singleImage"]/div[1]/div[3]/div/div[2]/label[2]/span')
                            common.find_by_id(_driver, 'clear-data1')
                            common.find_by_xpath(_driver, '/html/body/div[2]/div/div/div[3]/button[2]')
                            common.find_by_id(_driver, "next1")
                            units.append(unit_id)
                        if j == 1:
                            logger.write_debug(u"跳过unit %s" % unit_id)
                            common.find_by_id(_driver, 'skip1')
                            common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
                            units.append(unit_id)
                        if j == 2:
                            logger.write_debug(u"提交unit %s" % unit_id)
                            common.find_by_id(_driver, "next1")
                            units.append(unit_id)
                        if j == 3:
                            logger.write_debug(u"提交unit %s" % unit_id)
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


def edit_skip(work_flow_id, task_pool_id=config.TASK_POOL_ID, task_name=config.MULT_TASK_NAME):
    logger.write_debug(u"程序开始执行的时间为：%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "editor/flow-select")
    sleep(config.STIME)

    # 获取对应的标注工作流
    elements = _driver.find_elements_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr')
    l = len(elements)
    logger.write_debug(u"标注列表总共 %s 条数据" % l)

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
                if int(text_2) + int(text_3) >= 1:
                    _driver.find_element_by_xpath(
                        '//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[7]/a' % str(i)).click()
                    sleep(config.STIME)

                    job_id = common.get_text(_driver.find_element_by_id('job_id').text, 0)
                    unit_id = _driver.find_element_by_id("unit_id").text
                    logger.write_debug(u"标注的job为：%s, 跳过unit为：%s" % (job_id, unit_id))

                    logger.write_debug(u"1-查看在标注跳过前各统计数据")
                    logger.write_debug(u"1.1-查看任务池工作量统计页面在跳过前的标注个数")
                    before_edit_number = common.task_pool_statistic(_driver, task_pool_id, "4")
                    logger.write_debug(u"1.2-查看【从任务池进入多队列工作量统计】在标注跳过前的【标注个数，unit个数，跳过个数】")
                    before_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "4",
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.3-查看【工作流工作量统计】页面在标注跳过前的【标注次数】")
                    before_wf_edit_number = common.work_flow_statistic(_driver, task_pool_id, "4", work_flow_id)

                    logger.write_debug(u"1.4-查看【从工作流进入多队列工作量统计】页面在标注跳过前的【标注个数，unit个数，跳过个数】")
                    before_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "4", work_flow_id,
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.5-查看【工作量汇总统计】页面在跳过前的【标注总数】")
                    before_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"1.6-查看【老的用户工作量统计】页面在标注跳过前的【标注个数，unit个数，提交次数，跳过个数】")
                    before_user_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.7-查看【我的工作量总统计】页面在跳过前的【标注总数】")
                    before_my_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"1.8-查看【我的的用户工作量统计】页面在标注跳过前的【标注个数，unit个数，提交次数，跳过个数】")
                    before_my_user_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.9-查看任务池进度页面在跳过前的待检查总数")
                    before_to_check_number = common.progress_statistics(_driver, task_pool_id, "6")

                    logger.write_debug(u"1.10-查看项目列表页面在跳过前的待检查总数")
                    before_job_to_check_number = common.job_progress_statistic(_driver, job_id, "11")

                    logger.write_debug(u"点击跳过按钮")
                    common.find_by_id(_driver, 'skip1')
                    common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')

                    logger.write_debug(u"2-查看在标注跳过前各统计数据")
                    logger.write_debug(u"2.1-查看任务池工作量统计页面在跳过后的标注个数")
                    after_edit_number = common.task_pool_statistic(_driver, task_pool_id, "4")
                    logger.write_debug(u"2.2-查看【从任务池进入多队列工作量统计】在标注跳过后的【标注个数，unit个数，跳过个数】")
                    after_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "4",
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.3-查看【工作流工作量统计】页面在标注跳过后的【标注次数】")
                    after_wf_edit_number = common.work_flow_statistic(_driver, task_pool_id, "4", work_flow_id)

                    logger.write_debug(u"2.4-查看【从工作流进入多队列工作量统计】页面在标注跳过后的【标注个数，unit个数，跳过个数】")
                    after_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "4", work_flow_id,
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.5-查看【工作量汇总统计】页面在跳过后的【标注总数】")
                    after_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"2.6-查看【老的用户工作量统计】页面在标注跳过后的【标注个数，unit个数，提交次数，跳过个数】")
                    after_user_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.7-查看【我的工作量总统计】页面在跳过后的【标注总数】")
                    after_my_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"2.8-查看【我的的用户工作量统计】页面在标注跳过后的【标注个数，unit个数，提交次数，跳过个数】")
                    after_my_user_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.9-查看任务池进度页面在跳过后的待检查总数")
                    after_to_check_number = common.progress_statistics(_driver, task_pool_id, "6")

                    logger.write_debug(u"2.10-查看项目列表页面在跳过后的待检查总数")
                    after_job_to_check_number = common.job_progress_statistic(_driver, job_id, "11")

                    logger.write_debug(u"3-校验标注跳过后各统计数据的正确性")
                    common.check_statistic(u"3.1-标注跳过", u"任务池工作量统计", u"标注个数",
                                           before_edit_number, after_edit_number)
                    common.check_statistic(u"3.2.1-标注跳过", u"任务池进入的用户工作量统计", u"标注个数",
                                           before_tp_user_number[0], after_tp_user_number[0])
                    common.check_number(_driver, u"3.2.2-标注跳过", u"任务池进入的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_tp_user_number[1], before_tp_user_number[2],
                                        after_tp_user_number[1], after_tp_user_number[2])
                    common.check_statistic(u"3.3-标注跳过", u"工作流工作量统计", u"标注个数",
                                           before_wf_edit_number, after_wf_edit_number)
                    common.check_statistic(u"3.4.1-标注跳过", u"工作流进入的用户工作量统计", u"标注个数",
                                           before_wf_user_number[0], after_wf_user_number[0])
                    common.check_number(_driver, u"3.4.2-标注跳过", u"工作流进入的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_wf_user_number[1], before_wf_user_number[2],
                                        after_wf_user_number[1], after_wf_user_number[2])
                    common.check_statistic(u"3.5-标注跳过", u"老的工作量统计", u"标注个数",
                                           before_edit_total_number, after_edit_total_number)
                    common.check_statistic(u"3.6.1-标注跳过", u"老的工作量的用户工作量统计", u"标注个数",
                                           before_user_total_number[0], after_user_total_number[0])
                    common.check_statistic(u"3.6.2-标注跳过", u"老的工作量的用户工作量统计", u"提交总数",
                                           before_user_total_number[1], after_user_total_number[1])
                    common.check_number(_driver, u"3.6.3-标注跳过", u"老的工作量的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_user_total_number[2], before_user_total_number[3],
                                        after_user_total_number[2], after_user_total_number[3])
                    common.check_statistic(u"3.7-标注跳过", u"我的工作量统计", u"标注个数",
                                           before_my_edit_total_number, after_my_edit_total_number)
                    common.check_statistic(u"3.8.1-标注跳过", u"我的工作量的用户工作量统计", u"标注个数",
                                           before_my_user_number[0], after_my_user_number[0])
                    common.check_statistic(u"3.8.2-标注跳过", u"我的工作量的用户工作量统计", u"提交总数",
                                           before_my_user_number[1], after_my_user_number[1])
                    common.check_number(_driver, u"3.8.3-标注跳过", u"我的工作量的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_my_user_number[2], before_my_user_number[3],
                                        after_my_user_number[2], after_my_user_number[3])
                    common.check_statistic(u"3.9-标注跳过", u"任务池进度", u"待检查个数",
                                           before_to_check_number, after_to_check_number)
                    common.check_statistic(u"3.10-标注跳过", u"项目列表进度", u"待检查个数",
                                           before_job_to_check_number, after_job_to_check_number)

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


def edit_submit(work_flow_id, task_pool_id, task_name):
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "editor/flow-select")
    sleep(config.STIME)

    # 获取对应的标注工作流
    elements = _driver.find_elements_by_xpath('//*[@id="subjob-list-body"]/table/tbody/tr')
    l = len(elements)
    logger.write_debug(u"标注列表总共 %s 条数据" % l)

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
                if int(text_2) + int(text_3) >= 1:
                    _driver.find_element_by_xpath(
                        '//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[7]/a' % str(i)).click()
                    sleep(config.STIME)

                    job_id = common.get_text(_driver.find_element_by_id('job_id').text, 0)
                    unit_id = _driver.find_element_by_id("unit_id").text
                    logger.write_debug(u"提交unit：%s" % unit_id)

                    logger.write_debug(u"1-查看在标注提交前各统计数据")
                    logger.write_debug(u"1.1-查看任务池工作量统计页面在提交前的标注个数")
                    before_edit_number = common.task_pool_statistic(_driver, task_pool_id, "4")
                    logger.write_debug(u"1.2-查看【从任务池进入多队列工作量统计】在标注提交前的【标注个数，unit个数，跳过个数】")
                    before_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "4",
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.3-查看【工作流工作量统计】页面在标注提交前的【标注次数】")
                    before_wf_edit_number = common.work_flow_statistic(_driver, task_pool_id, "4", work_flow_id)

                    logger.write_debug(u"1.4-查看【从工作流进入多队列工作量统计】页面在标注提交前的【标注个数，unit个数，跳过个数】")
                    before_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "4", work_flow_id,
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.5-查看【工作量汇总统计】页面在提交前的【标注总数】")
                    before_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"1.6-查看【老的用户工作量统计】页面在标注提交前的【标注个数，unit个数，提交次数，跳过个数】")
                    before_user_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.7-查看【我的工作量总统计】页面在提交前的【标注总数】")
                    before_my_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"1.8-查看【我的的用户工作量统计】页面在标注提交前的【标注个数，unit个数，提交次数，跳过个数】")
                    before_my_user_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.9-查看任务池进度页面在提交前的待检查总数")
                    before_to_check_number = common.progress_statistics(_driver, task_pool_id, "6")

                    logger.write_debug(u"1.10-查看项目列表页面在提交前的待检查总数")
                    before_job_to_check_number = common.job_progress_statistic(_driver, job_id, "11")

                    logger.write_debug(u"标注提交")
                    common.find_by_id(_driver, 'next1')

                    logger.write_debug(u"2-查看在标注提交前各统计数据")
                    logger.write_debug(u"2.1-查看任务池工作量统计页面在提交后的标注个数")
                    after_edit_number = common.task_pool_statistic(_driver, task_pool_id, "4")
                    logger.write_debug(u"2.2-查看【从任务池进入多队列工作量统计】在标注提交后的【标注个数，unit个数，跳过个数】")
                    after_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "4",
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.3-查看【工作流工作量统计】页面在标注提交后的【标注次数】")
                    after_wf_edit_number = common.work_flow_statistic(_driver, task_pool_id, "4", work_flow_id)

                    logger.write_debug(u"2.4-查看【从工作流进入多队列工作量统计】页面在标注提交后的【标注个数，unit个数，跳过个数】")
                    after_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "4", work_flow_id,
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.5-查看【工作量汇总统计】页面在提交后的【标注总数】")
                    after_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"2.6-查看【老的用户工作量统计】页面在标注提交后的【标注个数，unit个数，提交次数，跳过个数】")
                    after_user_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.7-查看【我的工作量总统计】页面在提交后的【标注总数】")
                    after_my_edit_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '3')

                    logger.write_debug(u"2.8-查看【我的的用户工作量统计】页面在标注提交后的【标注个数，unit个数，提交次数，跳过个数】")
                    after_my_user_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '3', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.9-查看任务池进度页面在提交后的待检查总数")
                    after_to_check_number = common.progress_statistics(_driver, task_pool_id, "6")

                    logger.write_debug(u"2.10-查看项目列表页面在提交后的待检查总数")
                    after_job_to_check_number = common.job_progress_statistic(_driver, job_id, "11")

                    logger.write_debug(u"3-校验标注提交后各统计数据的正确性")
                    common.check_statistic(u"3.1-标注提交", u"任务池工作量统计", u"标注个数",
                                           before_edit_number, after_edit_number)
                    common.check_statistic(u"3.2.1-标注提交", u"任务池进入的用户工作量统计", u"标注个数",
                                           before_tp_user_number[0], after_tp_user_number[0])
                    common.check_number(_driver, u"3.2.2-标注提交", u"任务池进入的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_tp_user_number[1], before_tp_user_number[2],
                                        after_tp_user_number[1], after_tp_user_number[2])
                    common.check_statistic(u"3.3-标注提交", u"工作流工作量统计", u"标注个数",
                                           before_wf_edit_number, after_wf_edit_number)
                    common.check_statistic(u"3.4.1-标注提交", u"工作流进入的用户工作量统计", u"标注个数",
                                           before_wf_user_number[0], after_wf_user_number[0])
                    common.check_number(_driver, u"3.4.2-标注提交", u"工作流进入的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_wf_user_number[1], before_wf_user_number[2],
                                        after_wf_user_number[1], after_wf_user_number[2])
                    common.check_statistic(u"3.5-标注提交", u"老的工作量统计", u"标注个数",
                                           before_edit_total_number, after_edit_total_number)
                    common.check_statistic(u"3.6.1-标注提交", u"老的工作量的用户工作量统计", u"标注个数",
                                           before_user_total_number[0], after_user_total_number[0])
                    common.check_statistic(u"3.6.2-标注提交", u"老的工作量的用户工作量统计", u"提交总数",
                                           before_user_total_number[1], after_user_total_number[1])
                    common.check_number(_driver, u"3.6.3-标注提交", u"老的工作量的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_user_total_number[2], before_user_total_number[3],
                                        after_user_total_number[2], after_user_total_number[3])
                    common.check_statistic(u"3.7-标注提交", u"我的工作量统计", u"标注个数",
                                           before_my_edit_total_number, after_my_edit_total_number)
                    common.check_statistic(u"3.8.1-标注提交", u"我的工作量的用户工作量统计", u"标注个数",
                                           before_my_user_number[0], after_my_user_number[0])
                    common.check_statistic(u"3.8.2-标注提交", u"我的工作量的用户工作量统计", u"提交总数",
                                           before_my_user_number[1], after_my_user_number[1])
                    common.check_number(_driver, u"3.8.3-标注提交", u"我的工作量的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_my_user_number[2], before_my_user_number[3],
                                        after_my_user_number[2], after_my_user_number[3])
                    common.check_statistic(u"3.9-标注提交", u"任务池进度", u"待检查个数",
                                           before_to_check_number, after_to_check_number)
                    common.check_statistic(u"3.10-标注提交", u"项目列表进度", u"待检查个数",
                                           before_job_to_check_number, after_job_to_check_number)

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
