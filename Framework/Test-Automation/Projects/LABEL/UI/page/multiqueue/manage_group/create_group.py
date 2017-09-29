# coding:utf-8
# 小组管理-新增小组

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def create_group():
    logger.write_debug(u"管理员登录")
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)

    logger.write_debug(u"进入小组管理页面")
    _driver.get(config.BASE_URL_VENDOR + "spa/manager/team/teamList")
    sleep(config.STIME)

    # 获取最后一条小组信息的id
    common.scroll(_driver)
    last_id = common.get_text(
        _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/div/div[1]').text, 2)
    logger.write_debug(u"最后一条小组的id为：%s" % last_id)

    logger.write_debug(u"新增-小组。。。")
    sleep(config.STIME)

    logger.write_debug(u"1-新增小组")
    logger.write_debug(u"1.1-点击新增按钮")
    _driver.refresh()
    sleep(config.STIME)
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/button')
    common.assert_url(_driver, 'spa/manager/team/creation', u"新增小组页面")

    logger.write_debug(u"1.2-输入小组名称...")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div/div/input', u"小组%s"
                         % str(int(last_id) + 1), "send_key")
    logger.write_debug(u"输入的小组名称为：%s" % u"小组%s" % str(int(last_id) + 1))

    logger.write_debug(u"1.3-选择小组长...")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/div/div/div[1]/input',
                         config.CREATE_GROUP_LEADER,
                         '//*[@id="autocomplete-leaders"]/ul/li/a', '//*[@id="3"]', u"小组长")

    logger.write_debug(u"1.4-选择组员-验收员")
    common.select_worker(_driver, '//*[@id="root"]/div[2]/div/div/div[3]/div/div/div[1]/input', config.CREATE_REVIEWER,
                         '//*[@id="autocomplete-members"]/ul/li/a', '//*[@id="40"]', u"小组组员-验收员")

    logger.write_debug(u"1.5-点击提交按钮")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[5]/button[1]')
    _driver.switch_to_alert().accept()
    sleep(config.STIME)
    common.assert_url(_driver, "spa/manager/team/teamList", u"新建小组完成后的")

    logger.write_debug(u"2-校验新建小组后的数据正确性...")

    logger.write_debug(u"定位到新增的小组")
    common.scroll(_driver)
    page = (int(last_id) + 1) / 10 + 1
    page_index = (int(last_id) + 1) % 10
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/div/div[2]/div/ul/li[%s]/a' % str(page + 2))

    logger.write_debug(u"2.1-校验-组名")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[2]' % str(page_index),
                 u"小组%s" % str(int(last_id) + 1), u"组名")

    logger.write_debug(u"2.2-校验-组长")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[3]' % str(page_index),
                 config.CREATE_GROUP_LEADER, u"组长")

    logger.write_debug(u"2.3-校验-组员")
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[4]' % str(page_index),
                 config.CREATE_REVIEWER, u"组员")

    logger.write_debug(u"2.4-校验-小组编号")
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[1]/a' % str(page_index))
    common.check(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td/table/tbody/tr[1]/td[2]'
                 % str(page_index + 1), str(int(last_id) + 1), u"小组编号")

    logger.write_debug(u"关闭浏览器")
    sleep(config.STIME)
    common.tear_down(_driver)




