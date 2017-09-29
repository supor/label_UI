# coding:utf-8
# 验收员验收流程-验收部分通过

import time
from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config
from Projects.LABEL.UI.page.multiqueue.review.refute import refute


def review_part_approve(work_flow_id, task_pool_id=config.TASK_POOL_ID, task_name=config.MULT_TASK_NAME):
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "spa/review/task-flow-jobs?sorts=&page=1&per_page=10&continuable=1#1")
    sleep(config.STIME)

    # 获取对应的验收任务池
    elements = _driver.find_elements_by_xpath('//*[@id="beginReview"]/div/div[2]/table/tbody/tr')
    sleep(config.STIME)
    l = len(elements)
    logger.write_debug(u"验收列表总共 %s 条数据" % l)
    if l == 0:
        raise Exception(u"无待验收的数据，执行停止,请确认数据")
    else:
        for i in range(1, l + 1):
            # 任务池id定位文本值
            text_1 = _driver.find_element_by_xpath(
                '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[1]' % str(i)).text
            # 待验收数量文本值
            text_2 = _driver.find_element_by_xpath(
                '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[5]' % str(i)).text

            # 匹配选择的工作流的操作按钮xpath
            if text_1 != task_pool_id:
                if i != l:
                    continue
                else:
                    raise Exception(u"任务池 %s 无待验收的数据，执行停止，请确认数据" % task_pool_id)
            else:
                if int(text_2) < 2:
                    raise Exception(u"任务池 %s 可验收的任务量不够，请确认数据" % task_pool_id)
                else:
                    logger.write_debug(u"验收-部分通过流程")
                    _driver.find_element_by_xpath(
                        '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[7]/div/button/i' % str(i)).click()
                    sleep(2)
                    logger.write_debug(u"抽样出一个任务")
                    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]/input[1]').clear()
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/input[1]', "2", "send_keys")
                    logger.write_debug(u"点击开始验收")
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/button')

                    logger.write_debug(u"获取验收包id")
                    publisher_url = _driver.current_url
                    review_unit_id = common.get_text(publisher_url, 0)
                    logger.write_debug(u"驳回的验收包为：%s" % review_unit_id)

                    logger.write_debug(u"1-获取在验收部分通过前各统计的数据")
                    logger.write_debug(u"1.1-查看【任务池工作量统计】页面在验收部分通过前的验收次数")
                    before_review_number = common.task_pool_statistic(_driver, task_pool_id, "13")

                    logger.write_debug(u"1.2-查看【任务池工作量统计】在验收部分通过前的【验收完成个数】")
                    before_review_completed_number = common.task_pool_statistic(_driver, task_pool_id, "14")

                    logger.write_debug(u"1.3-查看【任务池工作量统计】在验收部分通过前的【验收驳回次数】")
                    before_review_reject_number = common.task_pool_statistic(_driver, task_pool_id, "11")

                    logger.write_debug(u"1.4-查看【从任务池进入多队列工作量统计】在验收部分通过前的【验收个数，unit个数，跳过个数】")
                    before_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "13",
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.5-查看【工作流工作量统计】页面在验收部分通过前的【验收次数】")
                    before_wf_review_number = common.work_flow_statistic(_driver, task_pool_id, "13", work_flow_id)

                    logger.write_debug(u"1.6-查看【工作流工作量统计】页面在验收部分通过前的【验收完成个数】")
                    before_wf_review_completed_number = common.work_flow_statistic(_driver, task_pool_id, "14",
                                                                                   work_flow_id)

                    logger.write_debug(u"1.7-查看【工作流工作量统计】页面在验收部分通过前的【验收驳回次数】")
                    before_wf_review_reject_number = common.work_flow_statistic(_driver, task_pool_id, "11",
                                                                                work_flow_id)

                    logger.write_debug(u"1.8-查看【从工作流进入多队列工作量统计】页面在验收部分通过前的【验收总数，unit个数，跳过个数】")
                    before_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "13", work_flow_id,
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.9-查看【工作量汇总统计】页面在验收部分通过前的【验收次数】")
                    before_review_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '12')

                    logger.write_debug(u"1.10-查看【老的工作量汇总统计】页面在验收部分通过前的【验收驳回次数】")
                    before_review_reject_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL,
                                                                          '10')

                    logger.write_debug(u"1.11-查看【老的工作量汇总统计】页面在验收部分通过前的【验收通过总数】")
                    handles_1 = common.get_window(_driver, config.OLD_STATISTIC_URL)
                    before_review_completed_total_number = common.get_text(_driver.find_element_by_id("info-text").text,
                                                                           7)
                    common.close_window(_driver, handles_1)

                    logger.write_debug(u"1.12-查看【老的用户工作量统计】页面在验收部分通过前的【验收总数，unit个数，提交次数，跳过个数】")
                    before_user_review_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '12', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.13-查看【我的工作量总统计】页面在验收部分通过前的【验收次数】")
                    before_my_review_total_number = common.statistics(_driver, task_name, config.MY_STATISTIC_URL, '12')

                    logger.write_debug(u"1.14-查看【我的工作量汇总统计】页面在验收部分通过前的【验收驳回次数】")
                    before_my_review_refute_total_number = common.statistics(_driver, task_name,
                                                                             config.MY_STATISTIC_URL, '10')

                    logger.write_debug(u"1.15-查看【我的工作量汇总统计】页面在验收部分通过前的【验收通过总数】")
                    handles_2 = common.get_window(_driver, config.MY_STATISTIC_URL)
                    before_my_review_completed_total_number = common.get_text(
                        _driver.find_element_by_id("info-text").text, 7)
                    common.close_window(_driver, handles_2)

                    logger.write_debug(u"1.16-查看【我的工作量处用户工作量统计】页面在验收部分通过前的【验收总数，unit个数，提交次数，跳过个数】")
                    before_my_user_review_number = common.old_user_statistic(_driver, task_name,
                                                                             config.MY_STATISTIC_URL,
                                                                             '12', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.17-查看【任务池进度】页面在验收部分通过前的【待批驳总数】")
                    before_to_refute_number = common.progress_statistics(_driver, task_pool_id, "12")
                    logger.write_debug(u"1.18-查看任务池进度页面在验收部分通过前的检查中总数")
                    before_in_check_number = common.progress_statistics(_driver, task_pool_id, "7")

                    logger.write_debug(u"1.19-查看【任务池进度】页面在验收部分通过前的【完成总数】")
                    before_completed_number = common.progress_statistics(_driver, task_pool_id, "14")

                    if task_name == u"Face - 假脸识别":
                        logger.write_debug(u"显示所有的unit")
                        common.select_all(_driver)

                    logger.write_debug(u"获取unit_id")
                    part_approve_unit_id = _driver.find_element_by_xpath(
                        '//*[@id="image-panel"]/div[1]/div').get_attribute("id")
                    sleep(config.STIME)
                    part_reject_unit_id = _driver.find_element_by_xpath(
                        '//*[@id="image-panel"]/div[2]/div').get_attribute("id")
                    sleep(config.STIME)
                    logger.write_debug(u"正在验收部分通过的通过的unit_id为：%s， 驳回的unit_id为：%s" %
                                       (part_approve_unit_id, part_reject_unit_id))
                    logger.write_debug(u"把驳回的unit %s 标记为哭脸" % part_reject_unit_id)
                    _driver.find_element_by_xpath('//*[@id="%s"]/div[2]/img' % str(part_reject_unit_id)).click()
                    sleep(config.STIME)
                    logger.write_debug(u"点击部分通过按钮")
                    common.find_by_id(_driver, "partapprove")
                    _driver.switch_to_alert().accept()
                    sleep(config.STIME)

                    logger.write_debug(u"2-校验验收部分通过后，未批驳前的验收包信息的正确性")
                    common.check_review_unit(_driver, review_unit_id, task_pool_id, '2', "100%", u"2-1（50.00%）",
                                             u"部分通过(待确认)")

                    logger.write_debug(u"3查看部分通过后批驳前的统计数据")
                    logger.write_debug(u"3.1-查看【任务池工作量统计】页面在验收部分通过后的【验收次数】")
                    after_review_number = common.task_pool_statistic(_driver, task_pool_id, "13")

                    logger.write_debug(u"3.2-查看【从任务池进入多队列工作量统计】在验收部分通过后批驳前的【验收个数，unit个数，跳过个数】")
                    after_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "13",
                                                                           config.USERNAME_VENDOR[0])
                    logger.write_debug(after_tp_user_number)

                    logger.write_debug(u"3.3-查看【工作流工作量统计】页面在验收部分通过后批驳前的【验收次数】")
                    after_wf_review_number = common.work_flow_statistic(_driver, task_pool_id, "13", work_flow_id)

                    logger.write_debug(u"3.4-查看【从工作流进入多队列工作量统计】页面在验收部分通过后批驳前的【验收总数，unit个数，跳过个数】")
                    after_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "13", work_flow_id,
                                                                           config.USERNAME_VENDOR[0])
                    logger.write_debug(after_wf_user_number)

                    logger.write_debug(u"3.5-查看【任务池进度列表】页面在验收部分通过后的待批驳个数")
                    after_to_refute_number = common.progress_statistics(_driver, task_pool_id, "12")

                    logger.write_debug(u"4-校验验收部分通过后的统计数据的正确性")
                    common.check_statistic(u"4.1-验收部分通过", u"任务池", u"验收个数",
                                           before_review_number, after_review_number, 2)
                    common.check_statistic(u"4.2.1-验收部分通过", u"任务池进入的用户工作量统计", u"验收总数",
                                           before_tp_user_number[0], after_tp_user_number[0], 2)
                    # 此方法不适用部分驳回，TODO
                    # common.check_number(_driver, u"4.2.2-验收部分通过", u"任务池进入的用户工作量统计",
                    #                     part_reject_unit_id, u"验收unit", u"验收跳过",
                    #                     before_tp_user_number[1], before_tp_user_number[2],
                    #                     after_tp_user_number[1], after_tp_user_number[2])

                    common.check_statistic(u"4.3-验收部分通过", u"工作量", u"验收个数",
                                           before_wf_review_number, after_wf_review_number, 2)
                    common.check_statistic(u"4.4.1-验收部分通过", u"工作流进入的用户工作量统计", u"验收总数",
                                           before_wf_user_number[0], after_wf_user_number[0], 2)
                    # common.check_number(_driver, u"4.4.2-验收部分通过", u"工作流进入的用户工作量统计",
                    #                     reject_unit_id, u"验收unit", u"验收跳过",
                    #                     before_wf_user_number[1], before_wf_user_number[2],
                    #                     after_wf_user_number[1], after_wf_user_number[2])

                    common.check_statistic(u"4.5-验收部分通过", u"任务池进度列表", u"待批驳",
                                           before_to_refute_number, after_to_refute_number, 2)

                    logger.write_debug(u"关闭浏览器")
                    common.tear_down(_driver)

                    logger.write_debug(u"5-进入小组长批驳过程")
                    refute(review_unit_id, 0, "2", "2 (100)%", "1(1)", u"是", u"同意驳回")

                    _driver2 = common.set_up()
                    common.diff_url_login(_driver2, config.BASE_URL, 0)

                    logger.write_debug(u"6-校验验收部分通过后，同意驳回后的验收包信息的正确性")
                    common.check_review_unit(_driver2, review_unit_id, task_pool_id, '2', "100%", u"2-1（50.00%）",
                                             u"部分通过")

                    logger.write_debug(u"7-校验验收部分通过后的操作评论的正确性")
                    logger.write_debug(u"校验部分通过的操作评论")
                    common.check_comment_after(_driver2, part_approve_unit_id, u"验收",
                                               config.USERNAME_VENDOR[0], u"通过(笑脸)")
                    logger.write_debug(u"校验部分驳回的操作评论")
                    common.check_comment_after(_driver2, part_reject_unit_id, u"验收",
                                               config.USERNAME_VENDOR[0], u"驳回(哭脸)")

                    logger.write_debug(u"8-获取在验收部分通过并同意驳回后各统计的数据")
                    logger.write_debug(u"8.1-查看【任务池工作量统计】在验收部分通过并同意驳回后的【验收驳回次数】")
                    after_review_reject_number = common.task_pool_statistic(_driver2, task_pool_id, "11")
                    logger.write_debug(u"8.2-查看【任务池工作量统计】在验收部分通过后的【验收完成个数】")
                    after_review_completed_number = common.task_pool_statistic(_driver2, task_pool_id, "14")

                    logger.write_debug(u"8.3-查看【工作流工作量统计】页面在验收同意驳回后的【验收驳回次数】")
                    after_wf_review_reject_number = common.work_flow_statistic(_driver2, task_pool_id, "11",
                                                                               work_flow_id)
                    logger.write_debug(u"8.4-查看【工作流工作量统计】页面在验收部分通过后的【验收完成个数】")
                    after_wf_review_completed_number = common.work_flow_statistic(_driver2, task_pool_id, "14",
                                                                                  work_flow_id)

                    logger.write_debug(u"8.5-查看【工作量汇总统计】页面在验收同意驳回后的【验收次数】")
                    after_review_total_number = common.statistics(_driver2, task_name, config.OLD_STATISTIC_URL, '12')

                    logger.write_debug(u"8.6-查看【老的工作量汇总统计】页面在验收部分通过驳回后的【验收驳回次数】")
                    after_review_reject_total_number = common.statistics(_driver2, task_name, config.OLD_STATISTIC_URL,
                                                                         '10')

                    logger.write_debug(u"8.7-查看【老的工作量汇总统计】页面在验收部分通过后的【验收通过总数】")
                    handles_3 = common.get_window(_driver2, config.OLD_STATISTIC_URL)
                    after_review_completed_total_number = common.get_text(_driver2.find_element_by_id("info-text").text,
                                                                          7)
                    common.close_window(_driver2, handles_3)

                    logger.write_debug(u"8.8-查看【老的用户工作量统计】页面在验收同意驳回后的【验收总数，unit个数，提交次数，跳过个数】")
                    after_user_review_total_number = common.old_user_statistic(
                        _driver2, task_name, config.OLD_STATISTIC_URL, '12', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"8.9-查看【我的工作量总统计】页面在验收同意驳回后的【验收次数】")
                    after_my_review_total_number = common.statistics(_driver2, task_name, config.MY_STATISTIC_URL, '12')
                    logger.write_debug(u"8.10-查看【我的工作量汇总统计】页面在验收部分通过前的【验收驳回次数】")
                    after_my_review_refute_total_number = common.statistics(_driver2, task_name,
                                                                            config.MY_STATISTIC_URL, '10')

                    logger.write_debug(u"8.11-查看【我的工作量汇总统计】页面在验收部分通过后的【验收通过总数】")
                    handles_4 = common.get_window(_driver2, config.MY_STATISTIC_URL)
                    after_my_review_completed_total_number = common.get_text(
                        _driver2.find_element_by_id("info-text").text, 7)
                    common.close_window(_driver2, handles_4)

                    logger.write_debug(u"8.12-查看【我的工作量处用户工作量统计】页面在验收同意驳回后的"
                                       u"【验收总数，unit个数，提交次数，跳过个数】")
                    after_my_user_review_number = common.old_user_statistic(_driver2, task_name,
                                                                            config.MY_STATISTIC_URL,
                                                                            '12', config.USERNAME_VENDOR[0])
                    logger.write_debug(u"8.13-查看任务池进度页面在验收同意驳回后的检查中总数")
                    after_in_check_number = common.progress_statistics(_driver2, task_pool_id, "7")

                    logger.write_debug(u"8.14-查看【任务池进度】页面在验收部分通过后的【完成总数】")
                    after_completed_number = common.progress_statistics(_driver2, task_pool_id, "14")

                    logger.write_debug(u"9-校验验收部分通过后的统计数据的正确性")
                    common.check_statistic(u"9.1-验收部分通过", u"任务池", u"验收驳回次数",
                                           before_review_reject_number, after_review_reject_number)
                    common.check_statistic(u"9.2-验收部分通过", u"任务池工作量统计", u"验收完成总数",
                                           before_review_completed_number, after_review_completed_number)
                    common.check_statistic(u"9.3-验收部分通过", u"工作流", u"验收驳回次数",
                                           before_wf_review_reject_number, after_wf_review_reject_number)
                    common.check_statistic(u"9.4-验收部分通过", u"工作流工作量统计", u"验收完成总数",
                                           before_wf_review_completed_number, after_wf_review_completed_number)
                    common.check_statistic(u"9.5-验收部分通过", u"老的工作量统计", u"验收次数",
                                           before_review_total_number, after_review_total_number, 2)
                    common.check_statistic(u"9.6-验收部分通过", u"老的工作量统计", u"验收驳回次数",
                                           before_review_reject_total_number, after_review_reject_total_number)
                    common.check_statistic(u"9.7-验收部分通过", u"老的工作量统计", u"验收完成总数",
                                           before_review_completed_total_number, after_review_completed_total_number)

                    common.check_statistic(u"9.8.1-验收部分通过", u"老的工作量的用户工作量统计", u"验收总数",
                                           before_user_review_total_number[0], after_user_review_total_number[0], 2)
                    common.check_statistic(u"9.8.2-验收部分通过", u"老的工作量的用户工作量统计", u"验收提交总数",
                                           before_user_review_total_number[1], after_user_review_total_number[1], 2)
                    # common.check_number(_driver2, u"8.5.3-验收部分通过", u"老的工作量的用户工作量统计",
                    #                     reject_unit_id, u"验收unit", u"验收跳过",
                    #                     before_user_review_total_number[2], before_user_review_total_number[3],
                    #                     after_user_review_total_number[2], after_user_review_total_number[3])
                    common.check_statistic(u"9.9-验收部分通过", u"我的工作量统计", u"验收次数",
                                           before_my_review_total_number, after_my_review_total_number, 2)

                    common.check_statistic(u"9.10-验收部分通过", u"我的工作量统计", u"验收驳回次数",
                                           before_my_review_refute_total_number, after_my_review_refute_total_number)

                    common.check_statistic(u"9.11-验收部分通过", u"我的的工作量统计", u"验收完成总数",
                                           before_my_review_completed_total_number,
                                           after_my_review_completed_total_number)

                    common.check_statistic(u"9.12.1-验收部分通过", u"我的工作量的用户工作量统计", u"验收总数",
                                           before_my_user_review_number[0], after_my_user_review_number[0], 2)
                    common.check_statistic(u"9.12.2-验收部分通过", u"我的工作量的用户工作量统计", u"验收提交总数",
                                           before_my_user_review_number[1], after_my_user_review_number[1], 2)
                    # common.check_number(_driver2, u"8.8.3-验收部分通过", u"我的工作量的用户工作量统计",
                    #                     reject_unit_id, u"验收unit", u"验收跳过",
                    #                     before_my_user_review_number[2], before_my_user_review_number[3],
                    #                     after_my_user_review_number[2], after_my_user_review_number[3])

                    common.check_statistic(u"9.13-验收部分通过", u"任务池进度", u"检查中个数",
                                           before_in_check_number, after_in_check_number)
                    common.check_statistic(u"9.14-验收部分通过", u"任务池进度", u"验收完成总数",
                                           before_completed_number, after_completed_number)

                    # 校验检查员处是否有驳回的数据（TODO）

                    break

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
    logger.write_debug(u"程序结束执行的时间为：%s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
