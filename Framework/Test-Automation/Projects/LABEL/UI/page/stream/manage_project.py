# coding:utf-8
# 项目管理分配

from time import sleep
from Projects.LABEL import pro_config as config
import framework.taf_logging as logger
from Projects.LABEL.UI.common import common


def stream_assign():
    _driver = common.diff_url_login(config.BASE_URL, 0)

    logger.write_debug(u"管理员登录")
    sleep(config.STIME)

    logger.write_debug(u'进入管理员页面')
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div/div/div[1]/div')
    common.assert_url(_driver, "manager/dashboard", u"任务管理")

    logger.write_debug(u"进入项目列表页面")
    common.find_by_xpath(_driver, '//*[@id="main"]/div/div[2]/div/div[1]/div')
    common.assert_url(_driver, "spa/job/manager/jobs?sorts=&page=1&per_page=10&", u"项目管理")

    logger.write_debug(u"筛选已导入的第一个项目")
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select")
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[3]/div[2]/select/option[2]")
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select")
    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[1]/div[1]/div/div[4]/div[2]/select/option[2]")

    logger.write_debug(u"进入第一个项目详情页面")

    job_id = _driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/a').text

    common.find_by_xpath(_driver, "//*[@id='root']/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/a")

    common.assert_url(_driver, "manager/job-detail/" + job_id, u"项目详情")

    logger.write_debug(u"修改流向为流式标注")
    common.find_by_id(_driver, "jobstream-edit")
    sleep(config.STIME)
    common.find_by_xpath(_driver, "//*[@id='stream-select-area']/div[1]/select")
    common.find_by_xpath(_driver, "//*[@id='stream-select-area']/div[1]/select/option[2]")
    common.find_by_id(_driver, "change-jobstream-save")
    common.find_by_xpath(_driver, '/html/body/div[2]/div/div/div[3]/button[2]')

    job_label_type = _driver.find_element_by_xpath('//*[@id="stream-areaval"]').text
    if job_label_type == u"流式标注":
        logger.write_debug(u"修改任务流向为流式标注成功")
    else:
        raise Exception(u"修改任务流向为流式标注失败")
    sleep(config.STIME+2)
    logger.write_debug(u"关闭浏览器")
    common.tear_down(_driver)
