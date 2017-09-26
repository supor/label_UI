# coding:utf-8
# 检查员检查流程-检查跳过

from time import sleep
import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def check_skip(work_flow_id, task_pool_id=config.TASK_POOL_ID, task_name=config.MULT_TASK_NAME, sample="false"):
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
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
                if int(text_2) + int(text_3) >= 1:
                    _driver.find_element_by_xpath(
                        '//*[@id="subjob-list-body"]/table/tbody/tr[%s]/td[7]/a' % str(i)).click()
                    sleep(config.STIME)

                    job_id = common.get_text(_driver.find_element_by_xpath(
                        '//*[@id="display-panel"]/ol/li[3]/span').text, 0)
                    logger.write_debug(u"检查提交的项目id为：%s" % job_id)
                    sleep(config.STIME)
                    unit_id = _driver.find_element_by_id("unit_id").text
                    logger.write_debug(u"提交unit %s" % unit_id)

                    logger.write_debug(u"1-查看在检查跳过通过前各统计数据")
                    logger.write_debug(u"1.1-查看任务池工作量统计页面在跳过通过前的检查个数")
                    before_check_number = common.task_pool_statistic(_driver, task_pool_id, "7")
                    logger.write_debug(u"1.2-查看【从任务池进入多队列工作量统计】在检查跳过通过前的【检查个数，unit个数，跳过个数】")
                    before_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "7",
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.3-查看【工作流工作量统计】页面在检查跳过通过前的【检查次数】")
                    before_wf_check_number = common.work_flow_statistic(_driver, task_pool_id, "7", work_flow_id)

                    logger.write_debug(u"1.4-查看【从工作流进入多队列工作量统计】页面在检查跳过通过前的【检查个数，unit个数，跳过个数】")
                    before_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "7", work_flow_id,
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.5-查看【工作量汇总统计】页面在跳过通过前的【检查总数】")
                    before_check_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '6')

                    logger.write_debug(u"1.6-查看【老的用户工作量统计】页面在检查跳过通过前的【检查个数，unit个数，提交次数，跳过个数】")
                    before_user_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '6', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.7-查看【我的工作量总统计】页面在跳过通过前的【检查总数】")
                    before_my_check_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '6')

                    logger.write_debug(u"1.8-查看【我的的用户工作量统计】页面在检查跳过通过前的【检查个数，unit个数，提交次数，跳过个数】")
                    before_my_user_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '6', config.USERNAME_VENDOR[0])

                    if sample == "false":
                        logger.write_debug(u"1.9-查看任务池进度页面在检查跳过通过前的待验收总数")
                        before_to_next_number = common.progress_statistics(_driver, task_pool_id, "10")

                        logger.write_debug(u"1.10-查看项目列表页面在检查跳过前的待验收总数")
                        before_job_to_next_number = common.job_progress_statistic(_driver, job_id, "13")
                    else:
                        logger.write_debug(u"1.9-查看任务池进度页面在检查跳过通过前的待抽查总数")
                        before_to_next_number = common.progress_statistics(_driver, task_pool_id, "8")

                        logger.write_debug(u"1.10-查看项目列表页面在检查跳过前的待抽查总数")
                        before_job_to_next_number = common.job_progress_statistic(_driver, job_id, "12")

                    logger.write_debug(u"检查-修改为跳过")
                    common.scroll(_driver)
                    common.find_by_xpath(_driver, '//*[@id="opt-area-check"]/div[2]/div[1]/button[2]')
                    # 点击跳过
                    common.find_by_id(_driver, "updateSkip")
                    common.find_by_xpath(_driver, '//*[@id="reason-dialog"]/div/div[2]/button')
                    common.find_by_xpath(_driver, '/html/body/div[3]/div/div/div[3]/button')
                    common.find_by_id(_driver, 'next2')

                    logger.write_debug(u"2-查看检查跳过通过后的各统计数据")
                    logger.write_debug(u"2.1-查看任务池工作量统计页面在跳过通过后的检查个数")
                    after_check_number = common.task_pool_statistic(_driver, task_pool_id, "7")
                    logger.write_debug(u"2.2-查看【从任务池进入多队列工作量统计】在检查跳过通过后的【检查个数，unit个数，跳过个数】")
                    after_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "7",
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.3-查看【工作流工作量统计】页面在检查跳过通过后的【检查次数】")
                    after_wf_check_number = common.work_flow_statistic(_driver, task_pool_id, "7", work_flow_id)

                    logger.write_debug(u"2.4-查看【从工作流进入多队列工作量统计】页面在检查跳过通过后的【检查个数，unit个数，跳过个数】")
                    after_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "7", work_flow_id,
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.5-查看【工作量汇总统计】页面在跳过通过后的【检查总数】")
                    after_check_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '6')

                    logger.write_debug(u"2.6-查看【老的用户工作量统计】页面在检查跳过通过后的【检查个数，unit个数，提交次数，跳过个数】")
                    after_user_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '6', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"2.7-查看【我的工作量总统计】页面在跳过通过后的【检查总数】")
                    after_my_check_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '6')

                    logger.write_debug(u"2.8-查看【我的的用户工作量统计】页面在检查跳过通过后的【检查个数，unit个数，提交次数，跳过个数】")
                    after_my_user_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '6', config.USERNAME_VENDOR[0])
                    if sample == "false":
                        logger.write_debug(u"2.9-查看任务池进度页面在检查跳过通过后的待验收总数")
                        after_to_next_number = common.progress_statistics(_driver, task_pool_id, "10")

                        logger.write_debug(u"2.10-查看项目列表页面在检查跳过后的待验收总数")
                        after_job_to_next_number = common.job_progress_statistic(_driver, job_id, "13")
                    else:
                        logger.write_debug(u"2.9-查看任务池进度页面在检查跳过通过后的待抽查总数")
                        after_to_next_number = common.progress_statistics(_driver, task_pool_id, "8")

                        logger.write_debug(u"2.10-查看项目列表页面在检查跳过后的待抽查总数")
                        after_job_to_next_number = common.job_progress_statistic(_driver, job_id, "12")

                    logger.write_debug(u"3-校验检查跳过通过后各统计数据的正确性")
                    common.check_statistic(u"3.1-检查跳过通过", u"任务池工作量统计", u"检查个数",
                                           before_check_number, after_check_number)
                    common.check_statistic(u"3.2.1-检查跳过通过", u"任务池进入的用户工作量统计", u"检查个数",
                                           before_tp_user_number[0], after_tp_user_number[0])
                    common.check_number(_driver, u"3.2.2-检查跳过通过", u"任务池进入的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_tp_user_number[1], before_tp_user_number[2],
                                        after_tp_user_number[1], after_tp_user_number[2])
                    common.check_statistic(u"3.3-检查跳过通过", u"工作流工作量统计", u"检查个数",
                                           before_wf_check_number, after_wf_check_number)
                    common.check_statistic(u"3.4.1-检查跳过通过", u"工作流进入的用户工作量统计", u"检查个数",
                                           before_wf_user_number[0], after_wf_user_number[0])
                    common.check_number(_driver, u"3.4.2-检查跳过通过", u"工作流进入的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_wf_user_number[1], before_wf_user_number[2],
                                        after_wf_user_number[1], after_wf_user_number[2])
                    common.check_statistic(u"3.5-检查跳过通过", u"老的工作量统计", u"检查个数",
                                           before_check_total_number, after_check_total_number)
                    common.check_statistic(u"3.6.1-检查跳过通过", u"老的工作量的用户工作量统计", u"检查个数",
                                           before_user_total_number[0], after_user_total_number[0])
                    common.check_statistic(u"3.6.2-检查跳过通过", u"老的工作量的用户工作量统计", u"提交总数",
                                           before_user_total_number[1], after_user_total_number[1])
                    common.check_number(_driver, u"3.6.3-检查跳过通过", u"老的工作量的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_user_total_number[2], before_user_total_number[3],
                                        after_user_total_number[2], after_user_total_number[3])
                    common.check_statistic(u"3.7-检查跳过通过", u"我的工作量统计", u"检查个数",
                                           before_my_check_total_number, after_my_check_total_number)
                    common.check_statistic(u"3.8.1-检查跳过通过", u"我的工作量的用户工作量统计", u"检查个数",
                                           before_my_user_number[0], after_my_user_number[0])
                    common.check_statistic(u"3.8.2-检查跳过通过", u"我的工作量的用户工作量统计", u"提交总数",
                                           before_my_user_number[1], after_my_user_number[1])
                    common.check_number(_driver, u"3.8.3-检查跳过通过", u"我的工作量的用户工作量统计",
                                        unit_id, u"unit", u"跳过",
                                        before_my_user_number[2], before_my_user_number[3],
                                        after_my_user_number[2], after_my_user_number[3])
                    common.check_statistic(u"3.9-检查跳过通过", u"任务池进度", u"待抽查/验收个数",
                                           before_to_next_number, after_to_next_number)
                    common.check_statistic(u"3.10-检查跳过通过", u"项目列表进度", u"待抽查/待验收个数",
                                           before_job_to_next_number, after_job_to_next_number)

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
