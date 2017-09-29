# coding:utf-8
# 验收员验收流程-验收放弃

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def review_giveup(task_pool_id):
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

    if l != 0:
        for i in range(1, l + 1):
            # 任务池id定位文本值
            text_1 = _driver.find_element_by_xpath(
                '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[1]' % str(i)).text
            # 待验收数量文本值
            text_2 = _driver.find_element_by_xpath(
                '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[5]' % str(i)).text

            # 匹配选择的工作流的操作按钮xpath
            if text_1 == task_pool_id:
                if int(text_2) >= 1:
                    _driver.find_element_by_xpath(
                        '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[7]/div/button/i' % str(i)).click()
                    sleep(2)
                    # total_text = common.get_text(
                    #     _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]').text, 0)
                    # sleep(config.STIME)
                    # if total_text == text_2:
                    #     logger.write_debug(u"共筛选出的验收任务个数正确，个数为：%s" % total_text)
                    # else:
                    #     logger.write_error(u"共筛选出的验收任务个数错误，显示为：%s, 应该是：%s" % (total_text, text_2))
                    logger.write_debug(u"验收-放弃流程")
                    logger.write_debug(u"抽样出一个任务")
                    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]/input[1]').clear()
                    sleep(config.STIME)
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/input[1]', "1", "send_keys")

                    logger.write_debug(u"点击开始验收")
                    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div[3]/button')

                    logger.write_debug(u"获取验收包id")
                    publisher_url = _driver.current_url
                    review_unit_id = common.get_text(publisher_url, 0)
                    logger.write_debug(u"放弃的验收包为：%s" % review_unit_id)

                    sleep(1)
                    logger.write_debug(u"点击放弃")
                    common.find_by_id(_driver, "giveup")
                    _driver.switch_to_alert().accept()
                    sleep(config.STIME)

                    # _driver.get(config.BASE_URL + "spa/review/task-flow-jobs?sorts=&page=1&per_page=10&continuable=1#1")
                    # logger.write_debug(u"获取待验收总数")
                    # text_4 = _driver.find_element_by_xpath(
                    #     '//*[@id="beginReview"]/div/div[2]/table/tbody/tr[%s]/td[5]' % str(i)).text
                    # sleep(config.STIME)
                    # if text_4 == text_2:
                    #     logger.write_debug(u"验收放弃成功")
                    # else:
                    #     logger.write_error(u"放弃后的任务数没有被释放，放弃失败, 放弃前的待验收总数为：%s, 放弃后为：%s"
                    #                        % (text_2, text_4))

                    # 校验验收包
                    common.check_review_unit(_driver, review_unit_id, task_pool_id, "1", "100%", u"1-1（100.00%）",
                                             u"已放弃")

                    sleep(3)
                    break
                else:
                    raise Exception(u"任务池 %s 可验收的任务量不够，请验收数据" % task_pool_id)
            else:
                if i != l:
                    continue
                else:
                    raise Exception(u"任务池 %s 无待验收的数据，执行停止，请验收数据" % task_pool_id)
    else:
        raise Exception(u"无待验收的数据，执行停止,请验收数据")

    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)



