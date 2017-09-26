# coding:utf-8
# 项目管理分配-多队列

from time import sleep

import framework.taf_logging as logger
from Projects.LABEL.UI.common import common, pro_config as config


def multiple_assign():
    logger.write_debug(u"管理员登录")
    _driver = common.set_up()
    common.diff_url_login(_driver, config.BASE_URL, 0)
    sleep(config.STIME)

    logger.write_debug(u'进入管理员页面')
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[1]/div')
    common.assert_url(_driver, "manager/dashboard", u"任务管理")

    logger.write_debug(u"进入项目列表页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[1]/div')
    common.assert_url(_driver, "spa/job/manager/jobs?sorts=&page=1&per_page=10&", u"项目管理")

    logger.write_debug(u"筛选已导入的第一个 %s 项目" % config.MULT_TASK_NAME)
    common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[1]/div/div[1]/div[2]/select/option[' +
                         config.TASK_XPATH_ID + ']')
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select")
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select/option[2]")
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select")
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select/option[2]")
    elements = _driver.find_elements_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr')
    l = len(elements)
    if l == 0:
        raise Exception(u"项目列表无已导入的 %s 的项目，请导入项目" % config.MULT_TASK_NAME)
    else:
        logger.write_debug(u"修改标注流向开始...")
        # 获取job_id
        job_id = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/a').text
        task_mount = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[8]').text
        logger.write_debug(u"正在使用的 %s 项目的job_id 是：%s，该项目的任务总数为：%s" % (config.MULT_TASK_NAME, job_id, task_mount))
        logger.write_debug(u"点击进入项目详情页面")
        common.find_by_xpath(_driver, '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/a')
        common.assert_url(_driver, "manager/job-detail/" + job_id, u"项目详情")
        logger.write_debug(u"修改流向为流式标注")
        common.find_by_id(_driver, "jobstream-edit")
        sleep(config.STIME)
        common.find_by_xpath(_driver, "//*[@id='stream-select-area']/div[1]/select")
        common.find_by_xpath(_driver, "//*[@id='stream-select-area']/div[1]/select/option[3]")
        common.find_by_id(_driver, "change-jobstream-save")
        common.find_by_xpath(_driver, '/html/body/div[2]/div/div/div[3]/button[2]')
        job_label_type = _driver.find_element_by_xpath('//*[@id="stream-areaval"]').text
        if job_label_type != u"多队列":
            raise Exception(u"修改任务流向为多队列失败")
        else:
            logger.write_debug(u"修改任务流向为多队列成功")
            sleep(config.STIME)
            common.scroll(_driver)
            logger.write_debug(u"开始任务池分配。。。")
            logger.write_debug(u"点击任务池分配按钮")
            common.find_by_xpath(_driver, '//*[@id="main"]/div[2]/div[2]/a/button')
            common.get_list(_driver, config.TASK_POOL_ID, '//*[@id="taskPoolModal"]/div/div/div[2]/table/tbody/tr',
                            u"分配任务池", '/td[4]/button', '/td[1]')
            sleep(1)
            common.find_by_xpath(_driver, '//*[@id="addPoolModal"]/div/div/div[3]/button[2]')
            sleep(1)
            logger.write_debug(u"分配任务池完成，任务池id为 %s " % config.TASK_POOL_ID)
            logger.write_debug(u"校验分配任务池后的信息正确性")
            if _driver.find_element_by_xpath('//*[@id="subjob-list"]/table/tbody/tr/td[1]').text == config.TASK_POOL_ID:
                logger.write_debug(u"分配任务池后，任务池信息正确")
            else:
                logger.write_error(u"分配任务池后，任务池信息错误")
            if _driver.find_element_by_xpath('//*[@id="subjob-list"]/table/tbody/tr/td[3]').text == task_mount:
                logger.write_debug(u"分配任务池后，任务数量信息正确")
            else:
                logger.write_error(u"分配任务池后，任务数量信息错误")
    logger.write_debug(u"关闭浏览器")
    sleep(config.STIME)
    common.tear_down(_driver)
