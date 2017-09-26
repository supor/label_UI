# coding:utf-8
# 任务池管理-新增任务池

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def create_task_pool():
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
    logger.write_debug(u"新增-任务池。。。")
    sleep(config.STIME)

    logger.write_debug(u"点击新增按钮")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/button')
    common.assert_url(_driver, 'spa/manager/task-flow/create?type=4', u"新增任务池页面")

    logger.write_debug(u"选择任务类型...")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/div/select')
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/div/select/option[' + config.TASK_ID + ']')
    logger.write_debug(u"选择任务池类型为：%s" % config.MULT_TASK_NAME)

    logger.write_debug(u"填写任务池标题...")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[3]/div/div/input',
                         u"任务池-%s" % unicode(int(last_id) + 1), "send_keys")
    logger.write_debug(u"填写的任务池标题为：%s" % (u"任务池-%s" % unicode(int(last_id) + 1)))

    logger.write_debug(u"选择任务池管理员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[4]/div/div/div[1]/input',
                         config.CREATE_GROUP_LEADER,
                         '//*[@id="autocomplete-pool_leaders"]/ul/li/a', '//*[@id="3"]', u"任务池管理员")

    logger.write_debug(u"选择验收员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[5]/div/div/div[1]/input', config.CREATE_REVIEWER,
                         '//*[@id="autocomplete-pool_inspectors"]/ul/li/a', '//*[@id="40"]', u"验收员")

    logger.write_debug(u"填写标注时长")
    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[6]/div/div/input').clear()
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[6]/div/div/input', "240", "send_keys")
    _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[7]/div/div/input').clear()
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[7]/div/div/input', "180", "send_keys")

    logger.write_debug(u"填写工作进度收件人")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[9]/div/div/input', config.SCHEDULE_EMAIL,
                         "send_keys")

    logger.write_debug(u"填写工作量统计收件人")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[11]/div/div/input', config.STATISTIC, "send_keys")

    logger.write_debug(u"点击提交按钮")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[14]/button[1]')
    common.assert_url(_driver, "spa/manager/task-flow-pool?type=4", u"新建任务池完成后的")

    logger.write_debug(u"校验新建任务池后的数据正确性...")

    logger.write_debug(u"校验-任务池ID")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[2]', unicode(int(last_id) + 1),
                 u"任务池id")

    logger.write_debug(u"校验-任务池名称")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[3]', u"任务池-%s" %
                 unicode(int(last_id) + 1), u"任务池名称")

    logger.write_debug(u"校验-任务类型")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[4]/span', config.MULT_TASK_NAME,
                 u"任务类型")

    logger.write_debug(u"校验-任务池管理员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[5]', config.CREATE_GROUP_LEADER,
                 u"任务池管理员")

    logger.write_debug(u"校验-验收员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[6]', config.CREATE_REVIEWER,
                 u"验收员")

    logger.write_debug(u"校验-是否不发工作进度邮件")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[7]', u"是", u"是否不发工作进度邮件")

    logger.write_debug(u"校验-是否不发工作量统计邮件")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[8]', u"是", u"是否不发工作量统计邮件")

    logger.write_debug(u"校验-是否冻结")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[9]', u"否", u"是否冻结")

    logger.write_debug(u"关闭浏览器")
    sleep(config.STIME)
    common.tear_down(_driver)



