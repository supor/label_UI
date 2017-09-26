# coding:utf-8
# 任务池管理-修改任务池

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def update_task_pool():
    logger.write_debug(u"管理员登录")
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)

    logger.write_debug(u"管理员进入任务池管理页面")
    _driver.get(config.BASE_URL_VENDOR + "spa/manager/task-flow-pool?type=4")
    sleep(config.STIME)

    # 获取最后一条任务池的id
    last_id = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]').text

    logger.write_debug(u"最后一条任务池的id为：%s" % last_id)
    logger.write_debug(u"修改-任务池。。。")
    sleep(config.STIME)

    logger.write_debug(u"点击修改按钮")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[10]/div/button[1]')
    common.assert_url(_driver, 'spa/manager/task-flow/update/' + last_id + '?type=4', u"修改任务池页面")

    logger.write_debug(u"修改任务池标题...")
    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[3]/div/div/input').clear()
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[3]/div/div/input',
                         u"修改任务池-%s" % last_id, "send_keys")
    logger.write_debug(u"修改的任务池标题为：%s" % (u"修改任务池-%s" % last_id))

    logger.write_debug(u"修改任务池管理员...")
    logger.write_debug(u"删除已有任务池管理员")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[4]/div/div/div[5]/button/span')
    logger.write_debug(u"新增任务池管理员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[4]/div/div/div[1]/input',
                         config.UPDATE_GROUP_LEADER,
                         '//*[@id="autocomplete-pool_leaders"]/ul/li/a', '//*[@id="1"]', u"任务池管理员")

    logger.write_debug(u"修改验收员...")
    logger.write_debug(u"添加验收员")
    logger.write_debug(u"选择验收员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[5]/div/div/div[1]/input', config.UPDATE_REVIEWER,
                         '//*[@id="autocomplete-pool_inspectors"]/ul/li/a', '//*[@id="1"]', u"验收员")
    # reviewer_text = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[5]/div/div/div[5]').text

    logger.write_debug(u"修改标注时长")
    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[6]/div/div/input').clear()
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[6]/div/div/input', config.UPDATE_EDIT_TIME,
                         "send_keys")
    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[7]/div/div/input').clear()
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[7]/div/div/input', config.UPDATE_CHECK_TIME,
                         "send_keys")

    logger.write_debug(u"修改是否发送工作进度邮件..")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[8]/div/select')
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[8]/div/select/option[1]')

    logger.write_debug(u"修改工作进度收件人...")
    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[9]/div/div/input').clear()
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[9]/div/div/input', config.UPDATE_SCHEDULE_EMAIL,
                         "send_keys")
    # update_schedule_email = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[9]/div/div/input').text

    logger.write_debug(u"修改是否发送工作量统计邮件..")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[10]/div/select')
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[10]/div/select/option[1]')

    logger.write_debug(u"修改工作量统计收件人")
    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[11]/div/div/input').clear()
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[11]/div/div/input', config.UPDATE_STATISTIC_EMAIL,
                         "send_keys")
    # update_statistic_email = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[11]/div/div/input').text

    logger.write_debug(u"点击提交按钮")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[14]/button[1]')
    common.assert_url(_driver, "spa/manager/task-flow-pool?type=4", u"修改任务池完成后的")

    logger.write_debug(u"校验修改任务池后的数据正确性...")

    logger.write_debug(u"校验-任务池ID")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]', last_id,
                 u"任务池id")

    logger.write_debug(u"校验-任务池名称")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[3]', u"修改任务池-%s" % last_id,
                 u"任务池名称")

    logger.write_debug(u"校验-任务池管理员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]', config.UPDATE_GROUP_LEADER,
                 u"任务池管理员")

    logger.write_debug(u"校验-验收员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[6]',
                 config.CREATE_REVIEWER + ',' + config.UPDATE_REVIEWER, u"验收员")

    logger.write_debug(u"校验-是否不发工作进度邮件")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[7]', u"否", u"是否不发工作进度邮件")

    logger.write_debug(u"校验-是否不发工作量统计邮件")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]', u"否", u"是否不发工作量统计邮件")

    logger.write_debug(u"关闭浏览器")
    sleep(config.STIME)
    common.tear_down(_driver)