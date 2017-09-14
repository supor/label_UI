# coding:utf-8
# 任务池管理

from time import sleep
from Projects.LABEL import pro_config as config
import framework.taf_logging as logger
from Projects.LABEL.UI.common import common


# 新增任务池
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


# 修改任务池
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


# 新增工作流
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


# 修改工作流
def update_work_flow():
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

    logger.write_debug(u"修改第一条工作流")
    logger.write_debug(u"点击修改按钮进入修改工作流页面")
    # 获取第一条工作流的id
    last_work_flow_id = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[1]').text
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[9]/div/button')
    common.assert_url(_driver, 'spa/manager/task-flow-pool-user/edit/%s?type=4' % last_work_flow_id, u"修改工作流页面")

    logger.write_debug(u"修改工作流名称...")
    _driver.find_element_by_xpath('//*[@id="title"]').clear()
    common.find_by_xpath(_driver, '//*[@id="title"]', u"修改任务池-%s-工作流-%s" % (last_id, last_work_flow_id), "send_keys")
    logger.write_debug(u"填写的工作流名称为：%s" % (u"修改任务池-%s-工作流-%s" % (last_id, last_work_flow_id)))

    logger.write_debug(u"修改工作流-标注员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[3]/div/div/div[1]/input',
                         config.USERNAME_VENDOR[5],
                         '//*[@id="autocomplete-pool_editors"]/ul/li/a', '//*[@id="8"]', u"工作流-标注员")

    logger.write_debug(u"修改工作流-检查员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[4]/div/div/div[1]/input',
                         config.USERNAME_VENDOR[0],
                         '//*[@id="autocomplete-pool_checkers"]/ul/li/a', '//*[@id="1"]', u"工作流-检查员")

    logger.write_debug(u"选择工作流-抽查员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[5]/div/div/div[1]/input',
                         config.USERNAME_VENDOR[0],
                         '//*[@id="autocomplete-pool_samplers"]/ul/li/a', '//*[@id="1"]', u"工作流-抽查员")

    logger.write_debug(u"修改工作量收件人")
    _driver.find_element_by_xpath('//*[@id="email_list"]').clear()
    common.find_by_xpath(_driver, '//*[@id="email_list"]', config.UPDATE_TASK_FLOW_EMAIL, "send_keys")

    logger.write_debug(u"修改是否不发邮件")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[7]/div/select')
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[7]/div/select/option[1]')

    logger.write_debug(u"修改是否禁用")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[8]/div/select', '')
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[8]/div/select/option[2]')

    logger.write_debug(u"点击提交按钮")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[10]/button[1]')
    common.assert_url(_driver, "spa/manager/task-flow-pool-user/%s" % last_id, u"修改工作流完成后的")

    logger.write_debug(u"校验新建工作流后的数据正确性...")

    logger.write_debug(u"校验-工作流名称")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[2]',
                 u"修改任务池-%s-工作流-%s"
                 % (last_id, last_work_flow_id), u"工作流名称")

    logger.write_debug(u"校验-工作流-标注员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[3]',
                 config.USERNAME_VENDOR[1] + ',' + config.USERNAME_VENDOR[5], u"工作流标注员")

    logger.write_debug(u"校验-工作流-检查员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[4]',
                 config.USERNAME_VENDOR[2] + ',' + config.USERNAME_VENDOR[0], u"工作流检查员")

    logger.write_debug(u"校验-工作流-抽查员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[5]',
                 config.USERNAME_VENDOR[3] + ',' + config.USERNAME_VENDOR[0], u"工作流抽查员")

    logger.write_debug(u"校验-工作流-收件人")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[6]',
                 config.UPDATE_TASK_FLOW_EMAIL, u"收件人")

    logger.write_debug(u"校验-是否不发工作流邮件")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[7]', u"否", u"是否不发邮件")

    logger.write_debug(u"校验-是否禁用")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[8]', u"是", u"是否禁用")

    logger.write_debug(u"关闭浏览器")
    sleep(config.STIME)
    common.tear_down(_driver)
