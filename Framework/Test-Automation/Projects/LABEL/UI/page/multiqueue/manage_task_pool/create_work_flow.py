# coding:utf-8
# 任务池管理-新增工作流

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def create_work_flow():
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

    logger.write_debug(u"点击按钮进入工作流列表页面")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[10]/div/button[2]')
    common.assert_url(_driver, 'spa/manager/task-flow-pool-user/%s?type=4' % last_id, u"工作流列表页面")

    logger.write_debug(u"新增一条工作流")
    logger.write_debug(u"点击新增按钮进入新增工作流页面")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/button')
    common.assert_url(_driver, 'spa/manager/task-flow-pool-user/create/%s?type=4' % last_id, u"新建工作流页面")

    logger.write_debug(u"填写工作流名称...")
    common.find_by_xpath(_driver, '//*[@id="title"]',
                         u"任务池-%s-工作流" % last_id, "send_keys")
    logger.write_debug(u"填写的工作流名称为：%s" % (u"任务池-%s-工作流" % last_id))

    logger.write_debug(u"选择工作流-标注员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[3]/div/div/div[1]/input',
                         config.USERNAME_VENDOR[1],
                         '//*[@id="autocomplete-pool_editors"]/ul/li/a', '//*[@id="38"]', u"工作流-标注员")

    logger.write_debug(u"选择工作流-检查员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[4]/div/div/div[1]/input',
                         config.USERNAME_VENDOR[2],
                         '//*[@id="autocomplete-pool_checkers"]/ul/li/a', '//*[@id="39"]', u"工作流-检查员")

    logger.write_debug(u"选择工作流-抽查员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[5]/div/div/div[1]/input',
                         config.USERNAME_VENDOR[3],
                         '//*[@id="autocomplete-pool_samplers"]/ul/li/a', '//*[@id="40"]', u"工作流-抽查员")

    logger.write_debug(u"填写工作量收件人")
    common.find_by_xpath(_driver, '//*[@id="email_list"]', config.TASK_FLOW_EMAIL, "send_keys")

    logger.write_debug(u"点击提交按钮")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[10]/button[1]')
    common.assert_url(_driver, "spa/manager/task-flow-pool-user/%s" % last_id, u"新建工作流完成后的")

    logger.write_debug(u"校验新建工作流后的数据正确性...")

    logger.write_debug(u"校验-工作流名称")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[2]', u"任务池-%s-工作流" % last_id,
                 u"工作流名称")

    logger.write_debug(u"校验-工作流-标注员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[3]', config.USERNAME_VENDOR[1],
                 u"工作流标注员")

    logger.write_debug(u"校验-工作流-检查员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[4]', config.USERNAME_VENDOR[2],
                 u"工作流检查员")

    logger.write_debug(u"校验-工作流-抽查员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[5]', config.USERNAME_VENDOR[3],
                 u"工作流抽查员")

    logger.write_debug(u"校验-工作流-收件人")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[6]', config.TASK_FLOW_EMAIL, u"收件人")

    logger.write_debug(u"校验-是否不发工作流邮件")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[7]', u"是", u"是否不发邮件")

    logger.write_debug(u"校验-是否禁用")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[8]', u"否", u"是否禁用")

    logger.write_debug(u"关闭浏览器")
    sleep(config.STIME)
    common.tear_down(_driver)
