# coding:utf-8
# 验收员验收流程-验收驳回

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config
from Projects.LABEL.UI.page.multiqueue.review.refute import refute


def review_reject(work_flow_id, task_pool_id=config.TASK_POOL_ID, task_name=config.MULT_TASK_NAME):
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)
    _driver.get(config.BASE_URL + "spa/review/task-flow-jobs?sorts=&page=1&per_page=10&continuable=1#1")
    sleep(config.STIME + 1)

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
                if int(text_2) < 1:
                    raise Exception(u"任务池 %s 可验收的任务量不够，请确认数据" % task_pool_id)
                else:
                    logger.write_debug(u"验收-驳回流程")
                    common.find_by_xpath(
                        _driver, '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[7]/div/button/i' % str(i))
                    logger.write_debug(u"抽样出一个任务")
                    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]/input[1]').clear()
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/input[1]', "1", "send_keys")
                    logger.write_debug(u"点击开始验收")
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/button')

                    logger.write_debug(u"获取验收包id")
                    publisher_url = _driver.current_url
                    review_unit_id = common.get_text(publisher_url, 0)
                    logger.write_debug(u"驳回的验收包为：%s" % review_unit_id)

                    logger.write_debug(u"校验创建验收包后，未操作验收前的验收包信息正确性")
                    common.check_review_unit(_driver, review_unit_id, task_pool_id, '1', "100%", u"1-1（100.00%）",
                                             u"验收中")

                    if task_name == u"Face - 假脸识别":
                        logger.write_debug(u"显示所有的unit")
                        common.select_all(_driver)
                    logger.write_debug(u"获取unit_id")
                    reject_unit_id = _driver.find_element_by_xpath(
                        '//*[@id="image-panel"]/div[1]/div').get_attribute("id")
                    sleep(config.STIME + 1)
                    logger.write_debug(u"正在验收驳回的unit_id为：%s" % reject_unit_id)

                    logger.write_debug(u"1-获取在验收驳回前各统计的数据")
                    logger.write_debug(u"1.1-查看【任务池工作量统计】页面在验收驳回前的验收次数")
                    before_review_number = common.task_pool_statistic(_driver, task_pool_id, "13")

                    logger.write_debug(u"1.2-查看【任务池工作量统计】在验收驳回前的【验收驳回次数】")
                    before_review_reject_number = common.task_pool_statistic(_driver, task_pool_id, "11")

                    logger.write_debug(u"1.3-查看【从任务池进入多队列工作量统计】在验收驳回前的【验收个数，unit个数，跳过个数】")
                    before_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "13",
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.4-查看【工作流工作量统计】页面在验收驳回前的【验收次数】")
                    before_wf_review_number = common.work_flow_statistic(_driver, task_pool_id, "13", work_flow_id)

                    logger.write_debug(u"1.5-查看【工作流工作量统计】页面在验收驳回前的【验收驳回次数】")
                    before_wf_review_reject_number = common.work_flow_statistic(_driver, task_pool_id, "11",
                                                                                work_flow_id)

                    logger.write_debug(u"1.6-查看【从工作流进入多队列工作量统计】页面在验收驳回前的【验收总数，unit个数，跳过个数】")
                    before_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "13", work_flow_id,
                                                                            config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.7-查看【工作量汇总统计】页面在验收驳回前的【验收次数】")
                    before_review_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL, '12')

                    logger.write_debug(u"1.8-查看【老的工作量汇总统计】页面在验收驳回前的【验收驳回次数】")
                    before_review_reject_total_number = common.statistics(_driver, task_name, config.OLD_STATISTIC_URL,
                                                                          '10')

                    logger.write_debug(u"1.9-查看【老的用户工作量统计】页面在验收驳回前的【验收总数，unit个数，提交次数，跳过个数】")
                    before_user_review_total_number = common.old_user_statistic(
                        _driver, task_name, config.OLD_STATISTIC_URL, '12', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.10-查看【我的工作量总统计】页面在验收驳回前的【验收次数】")
                    before_my_review_total_number = common.statistics(_driver, task_name, config.MY_STATISTIC_URL, '12')
                    logger.write_debug(u"1.11-查看【我的工作量汇总统计】页面在验收驳回前的【验收驳回次数】")
                    before_my_review_refute_total_number = common.statistics(_driver, task_name,
                                                                             config.MY_STATISTIC_URL, '10')

                    logger.write_debug(u"1.12-查看【我的工作量处用户工作量统计】页面在验收驳回前的【验收总数，unit个数，提交次数，跳过个数】")
                    before_my_user_review_number = common.old_user_statistic(_driver, task_name,
                                                                             config.MY_STATISTIC_URL,
                                                                             '12', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"1.13-查看【任务池进度】页面在验收驳回前的【待批驳总数】")
                    before_to_refute_number = common.progress_statistics(_driver, task_pool_id, "12")
                    logger.write_debug(u"1.14-查看任务池进度页面在验收驳回前的检查中总数")
                    before_in_check_number = common.progress_statistics(_driver, task_pool_id, "7")

                    logger.write_debug(u"点击驳回按钮")
                    common.find_by_id(_driver, "reject")
                    common.find_by_id(_driver, "reason-btn")
                    sleep(config.STIME)

                    logger.write_debug(u"2-校验驳回后，未批驳前，验收包的信息的正确性")
                    common.check_review_unit(_driver, review_unit_id, task_pool_id, '1', "100%", u"1-1（100.00%）",
                                             u"已驳回(待确认)")
                    logger.write_debug(u"3-查看验收驳回后未批驳前的统计数据")
                    logger.write_debug(u"3.1-查看【任务池工作量统计】页面在验收驳回后的【验收次数】")
                    after_review_number = common.task_pool_statistic(_driver, task_pool_id, "13")
                    logger.write_debug(u"3.2-查看【从任务池进入多队列工作量统计】在验收驳回后批驳前的【验收个数，unit个数，跳过个数】")
                    after_tp_user_number = common.task_pool_user_statistic(_driver, task_pool_id, "13",
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"3.3-查看【工作流工作量统计】页面在验收驳回后批驳前的【验收次数】")
                    after_wf_review_number = common.work_flow_statistic(_driver, task_pool_id, "13", work_flow_id)

                    logger.write_debug(u"3.4-查看【从工作流进入多队列工作量统计】页面在验收驳回后批驳前的【验收总数，unit个数，跳过个数】")
                    after_wf_user_number = common.workflow_user_statistics(_driver, task_pool_id, "13", work_flow_id,
                                                                           config.USERNAME_VENDOR[0])

                    logger.write_debug(u"3.5-查看【任务池进度列表】页面在验收驳回后的待批驳个数")
                    after_to_refute_number = common.progress_statistics(_driver, task_pool_id, "12")

                    logger.write_debug(u"4-校验验收驳回后的统计数据的正确性")
                    common.check_statistic(u"4.1-验收驳回", u"任务池", u"验收个数",
                                           before_review_number, after_review_number)
                    common.check_statistic(u"4.2.1-验收驳回", u"任务池进入的用户工作量统计", u"验收总数",
                                           before_tp_user_number[0], after_tp_user_number[0])
                    common.check_number(_driver, u"4.2.2-验收驳回", u"任务池进入的用户工作量统计",
                                        reject_unit_id, u"验收unit", u"验收跳过",
                                        before_tp_user_number[1], before_tp_user_number[2],
                                        after_tp_user_number[1], after_tp_user_number[2])

                    common.check_statistic(u"4.3-验收驳回", u"工作量", u"验收个数",
                                           before_wf_review_number, after_wf_review_number)
                    common.check_statistic(u"4.4.1-验收驳回", u"工作流进入的用户工作量统计", u"验收总数",
                                           before_wf_user_number[0], after_wf_user_number[0])
                    common.check_number(_driver, u"4.4.2-验收驳回", u"工作流进入的用户工作量统计",
                                        reject_unit_id, u"验收unit", u"验收跳过",
                                        before_wf_user_number[1], before_wf_user_number[2],
                                        after_wf_user_number[1], after_wf_user_number[2])

                    common.check_statistic(u"4.5-验收驳回", u"任务池进度列表", u"待批驳",
                                           before_to_refute_number, after_to_refute_number)

                    logger.write_debug(u"关闭浏览器")
                    common.tear_down(_driver)

                    logger.write_debug(u"5-进入小组长批驳过程")
                    refute(review_unit_id, 0, "1", "1 (100)%", "1(0)", u"否", u"同意驳回")

                    _driver2 = common.set_up()
                    common.diff_url_login(_driver2, config.BASE_URL, 0)

                    logger.write_debug(u"6-校验驳回批驳后，验收包的信息正确性")
                    common.check_review_unit(_driver2, review_unit_id, task_pool_id, '1', "100%", u"1-1（100.00%）",
                                             u"已驳回")

                    logger.write_debug(u"7-获取在验收驳回并同意驳回后各统计的数据")
                    logger.write_debug(u"7.1-查看【任务池工作量统计】在验收驳回并同意驳回后的【验收驳回次数】")
                    after_review_reject_number = common.task_pool_statistic(_driver2, task_pool_id, "11")

                    logger.write_debug(u"7.2-查看【工作流工作量统计】页面在验收同意驳回后的【验收驳回次数】")
                    after_wf_review_reject_number = common.work_flow_statistic(_driver2, task_pool_id, "11",
                                                                               work_flow_id)

                    logger.write_debug(u"7.3-查看【工作量汇总统计】页面在验收同意驳回后的【验收次数】")
                    after_review_total_number = common.statistics(_driver2, task_name, config.OLD_STATISTIC_URL, '12')

                    logger.write_debug(u"7.4-查看【老的工作量汇总统计】页面在验收通过驳回后的【验收驳回次数】")
                    after_review_reject_total_number = common.statistics(_driver2, task_name, config.OLD_STATISTIC_URL,
                                                                         '10')

                    logger.write_debug(u"7.5-查看【老的用户工作量统计】页面在验收同意驳回后的【验收总数，unit个数，提交次数，跳过个数】")
                    after_user_review_total_number = common.old_user_statistic(
                        _driver2, task_name, config.OLD_STATISTIC_URL, '12', config.USERNAME_VENDOR[0])

                    logger.write_debug(u"7.6-查看【我的工作量总统计】页面在验收同意驳回后的【验收次数】")
                    after_my_review_total_number = common.statistics(_driver2, task_name, config.MY_STATISTIC_URL, '12')
                    logger.write_debug(u"7.7-查看【我的工作量汇总统计】页面在验收驳回前的【验收驳回次数】")
                    after_my_review_refute_total_number = common.statistics(_driver2, task_name,
                                                                            config.MY_STATISTIC_URL, '10')

                    logger.write_debug(u"7.8-查看【我的工作量处用户工作量统计】页面在验收同意驳回后的"
                                       u"【验收总数，unit个数，提交次数，跳过个数】")
                    after_my_user_review_number = common.old_user_statistic(_driver2, task_name,
                                                                            config.MY_STATISTIC_URL,
                                                                            '12', config.USERNAME_VENDOR[0])
                    logger.write_debug(u"7.9-查看任务池进度页面在验收同意驳回后的检查中总数")
                    after_in_check_number = common.progress_statistics(_driver2, task_pool_id, "7")

                    logger.write_debug(u"8-校验验收驳回后的统计数据的正确性")
                    common.check_statistic(u"8.1-验收驳回", u"任务池", u"验收驳回次数",
                                           before_review_reject_number, after_review_reject_number)
                    common.check_statistic(u"8.2-验收驳回", u"工作流", u"验收驳回次数",
                                           before_wf_review_reject_number, after_wf_review_reject_number)
                    common.check_statistic(u"8.3-验收驳回", u"老的工作量统计", u"验收次数",
                                           before_review_total_number, after_review_total_number)
                    common.check_statistic(u"8.4-验收驳回", u"老的工作量统计", u"验收驳回次数",
                                           before_review_reject_total_number, after_review_reject_total_number)

                    common.check_statistic(u"8.5.1-验收驳回", u"老的工作量的用户工作量统计", u"验收总数",
                                           before_user_review_total_number[0], after_user_review_total_number[0])
                    common.check_statistic(u"8.5.2-验收驳回", u"老的工作量的用户工作量统计", u"验收提交总数",
                                           before_user_review_total_number[1], after_user_review_total_number[1])
                    common.check_number(_driver2, u"8.5.3-验收驳回", u"老的工作量的用户工作量统计",
                                        reject_unit_id, u"验收unit", u"验收跳过",
                                        before_user_review_total_number[2], before_user_review_total_number[3],
                                        after_user_review_total_number[2], after_user_review_total_number[3])
                    common.check_statistic(u"8.6-验收驳回", u"我的工作量统计", u"验收次数",
                                           before_my_review_total_number, after_my_review_total_number)

                    common.check_statistic(u"8.7-验收驳回", u"我的工作量统计", u"验收驳回次数",
                                           before_my_review_refute_total_number, after_my_review_refute_total_number)
                    common.check_statistic(u"8.8.1-验收驳回", u"我的工作量的用户工作量统计", u"验收总数",
                                           before_my_user_review_number[0], after_my_user_review_number[0])
                    common.check_statistic(u"8.8.2-验收驳回", u"我的工作量的用户工作量统计", u"验收提交总数",
                                           before_my_user_review_number[1], after_my_user_review_number[1])
                    common.check_number(_driver2, u"8.8.3-验收驳回", u"我的工作量的用户工作量统计",
                                        reject_unit_id, u"验收unit", u"验收跳过",
                                        before_my_user_review_number[2], before_my_user_review_number[3],
                                        after_my_user_review_number[2], after_my_user_review_number[3])

                    common.check_statistic(u"8.9-验收驳回", u"任务池进度", u"检查中个数",
                                           before_in_check_number, after_in_check_number)

                    logger.write_debug(u"9-校验驳回后的unit操作评论")
                    common.check_comment_after(_driver2, reject_unit_id, u"验收",
                                               config.USERNAME_VENDOR[0], u"驳回(笑脸)")
                    # 校验检查员处是否有驳回的数据（TODO）
                    break

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
