# -*- coding:utf-8 -*-
# 公共方法

import re
from time import sleep

from selenium import webdriver
from Projects.LABEL.UI.common import pro_config as config
from framework import taf_logging as logger


def set_up():
    driver = webdriver.Chrome('D:\chromedriver')
    driver.maximize_window()
    return driver


def tear_down(driver):
    driver.quit()


# 判断元素是否存在
def is_element_exist(driver, find_type, css):
    elements = []
    if find_type == "xpath":
        elements = driver.find_elements_by_xpath(css)
    elif find_type == "id":
        elements = driver.find_elements_by_id(css)

    if len(elements) == 0:
        logger.write_debug(u"未找到元素： %s" % css)
        return False
    elif len(elements) == 1:
        return True
    else:
        logger.write_debug(u"找到%s 个元素：%s" % (len(elements), css))
        return False


# xpath定位
def find_by_xpath(driver, xpath, send_keys_text="", handle_type="click"):
    if is_element_exist(driver, "xpath", xpath):
        if handle_type is "click":
            driver.find_element_by_xpath(xpath).click()
            sleep(config.STIME)
        else:
            driver.find_element_by_xpath(xpath).send_keys(send_keys_text)
            sleep(config.STIME)


# id定位
def find_by_id(driver, id_xpath, send_keys_text="", handle_type="click"):
    if is_element_exist(driver, "id", id_xpath):
        if handle_type is "click":
            driver.find_element_by_id(id_xpath).click()
            sleep(config.STIME)
        else:
            driver.find_element_by_id(id_xpath).send_keys(send_keys_text)
            sleep(config.STIME)


# 校验跳转的页面（url）正确性
def assert_url(driver, url, assert_text):
    if driver.current_url == config.BASE_URL + url:
        logger.write_debug(u"%s 页面跳转正确" % assert_text)
    else:
        logger.write_debug(u"%s 页面跳转不正确" % assert_text)


# 登录
def login(driver, username, passwd):
    # 登录
    driver.get(config.BASE_URL)
    logger.write_debug(u"启动chrome浏览器...")
    sleep(config.STIME)
    logger.write_debug(u"点击主页的登录按钮")
    driver.find_element_by_xpath("//*[@id='navbar-collapse-1']/ul/li[5]/a").click()
    logger.write_debug(u"输入用户名")
    find_by_id(driver, 'username', username, "send_keys")
    logger.write_debug(u"输入密码")
    find_by_id(driver, 'password', passwd, "send_keys")
    logger.write_debug(u"点击登录按钮")
    find_by_id(driver, 'submit')
    sleep(config.STIME)

    assert_url(driver, "distribution", u"登录成功")


# 拖动滚动条到最底部
def scroll(driver):
    js = "var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    sleep(config.STIME)


# 不同的环境登录的用户名及密码
def diff_url_login(driver, base_url, list_index):
    if base_url == config.BASE_URL_VENDOR:
        login(driver, config.USERNAME_VENDOR[list_index], config.PWD_VENDOR)
    if base_url == config.BASE_URL_DEV:
        login(driver, config.USERNAME_DEV[list_index], config.PWD_DEV)


# 获取普通列表（流式标注、项目管理及任务池管理）
def get_list(driver, task_name, list_xpath, page_name, button_xpath_right, right_xpath=""):
    elements = driver.find_elements_by_xpath(list_xpath)
    l = len(elements)
    logger.write_debug(u"%s 列表总共 %s 条数据" % (page_name, l))
    if l != 0:
        for i in range(1, l + 1):
            # //*[@id="subjob-list-body"]/table/tbody/tr[1]
            # 任务类型定位文本值

            text = driver.find_element_by_xpath("%s[%s]%s" % (list_xpath, str(i), right_xpath)).text
            # 匹配选择的任务类型的操作按钮xpath
            if text == task_name:
                driver.find_element_by_xpath("%s[%s]%s" % (list_xpath, str(i), button_xpath_right)).click()
                break
            else:
                if i != l:
                    continue
                else:
                    raise Exception(u"%s 无待 %s 的数据，执行停止，请检查数据" % (task_name, page_name))
    else:
        raise Exception(u"无待%s的数据，执行停止,请检查数据" % page_name)


# 选择人员
def select_worker(driver, url_1, worker_name, url_2, url_3, worker_type):
    find_by_xpath(driver, url_1, worker_name, "send_keys")
    find_by_xpath(driver, url_2)
    name = driver.find_element_by_xpath(url_3).text
    if name == worker_name:
        logger.write_debug(u"选择的%s为：%s" % (worker_type, name))
    else:
        logger.write_error(u"选择的%s不正确，请重新选择" % worker_type)


# 校验添加后的信息的正确性
def check(driver, xpath, before_info, content):
    after_info = driver.find_element_by_xpath(xpath).text
    if after_info == before_info:
        logger.write_debug(u"添加%s正确" % content)
    else:
        logger.write_error(u"添加%s失败，添加后的是：%s, 添加时的是： %s" % (content, after_info, before_info))


def check_comments(driver, unit_id, task_status, username, operate_result, status=""):
    logger.write_debug(u"校验unit %s 当前评论" % unit_id)
    if status == u"跳过":
        unit_status = driver.find_element_by_xpath('//*[@id="alert-msg-wrap"]/strong').text
        if unit_status != u"跳过：":
            logger.write_error(u"unit %s 的状态显示错误，显示的状态为：%s, 应该是：跳过" %
                               (unit_id, unit_status))
        else:
            logger.write_debug(u"unit %s 的状态显示正确" % unit_id)

    logger.write_debug(u"校验%s操作评论..." % task_status)
    logger.write_debug(u"获取%s员用户名" % task_status)
    name = driver.find_element_by_xpath('//*[@id="display-panel"]/ul[1]/li[2]/span[1]').text
    if name != username:
        logger.write_error(u"%s员用户名显示错误，显示的用户名为：%s, 应该是：%s" %
                           (task_status, name, username))

    logger.write_debug(u"获取%s员职位" % task_status)
    position = driver.find_element_by_xpath('//*[@id="display-panel"]/ul[1]/li[2]/span[2]').text
    if position != u"%s员" % task_status:
        logger.write_error(u"%s员职位显示错误，显示的职位为：%s, 应该是：%s员"
                           % (task_status, position, task_status))

    logger.write_debug(u"校验%s操作显示" % task_status)
    operate = driver.find_element_by_xpath('//*[@id="display-panel"]/ul[1]/li[2]/span[3]').text
    if operate != task_status:
        logger.write_error(u"%s员操作显示错误，显示的操作是：%s, 应该是：%s"
                           % (task_status, operate, task_status))

    logger.write_debug(u"校验%s员操作结果" % task_status)
    result = driver.find_element_by_xpath('//*[@id="display-panel"]/ul[1]/li[2]/span[4]').text
    if result != operate_result:
        logger.write_error(u"%s员操作结果显示错误，显示为：%s, 应该是：%s" % (task_status, result, operate_result))
    elif name == username and position == u"%s员" % task_status and operate == task_status and result == operate_result:
        logger.write_debug(u"unit %s 当前评论显示正确，显示为：%s, %s, %s, %s" %
                           (unit_id, name, position, operate, result))


def check_comment_after(driver, unit_id, task_status, username, operate_result):
    driver.get(config.BASE_URL + "manager/inspect-unit/%s" % unit_id)
    sleep(config.STIME + 1)
    check_comments(driver, unit_id, task_status, username, operate_result)


# 校验文本值显示的正确性
def check_text(before_text, after_text, text_name):
    if after_text == before_text:
        logger.write_debug(u"%s显示正确，显示为：%s" % (text_name, after_text))
    else:
        logger.write_error(u"%s显示错误，显示为：%s, 应该为：%s" % (text_name, after_text, before_text))


# 退出
def logout(driver):
    find_by_xpath(driver, '//*[@id="navbar"]/div[2]/div[5]/a')
    find_by_xpath(driver, '//*[@id="navbar"]/div[2]/div[5]/ul/li[5]/a')


# 验收/抽查页面筛选出全部units
def select_all(driver):
    find_by_xpath(driver, '//*[@id="main"]/div[3]/div[1]/div/div[2]/form/div/select')
    find_by_xpath(driver, '//*[@id="main"]/div[3]/div[1]/div/div[2]/form/div/select/option[1]')
    find_by_xpath(driver, '//*[@id="main"]/div[3]/div[1]/div/div[2]/form/button')


# 新打开窗口
def get_window(driver, new_window_url):
    js = 'window.open("%s");' % (config.BASE_URL + new_window_url)
    driver.execute_script(js)
    sleep(config.STIME)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])
    sleep(config.STIME)
    return handles


# 关闭现有窗口并切换窗口
def close_window(driver, handles):
    driver.close()
    driver.switch_to.window(handles[0])
    sleep(config.STIME)


def init_statistics(driver, list_xpath, to_statistic_id, number_xpath_n):
    sleep(config.STIME)
    elements = driver.find_elements_by_xpath(list_xpath)
    l = len(elements)
    number_text = "0"
    if l == 0:
        logger.write_debug(u"无统计数据")
    else:
        for i in range(1, l + 1):
            # 获取任务池id
            text_1 = driver.find_element_by_xpath('%s[%s]/td[1]' % (list_xpath, str(i))).text
            if text_1 != to_statistic_id:
                if i != l:
                    continue
                else:
                    logger.write_debug(u"无%s统计数据" % to_statistic_id)
            else:
                number_text = driver.find_element_by_xpath(
                    '%s[%s]/td[%s]' % (list_xpath, str(i), number_xpath_n)).text

                break
    return number_text


# 任务池工作量统计
def task_pool_statistic(driver, task_pool_id, number_xpath_n):
    handles = get_window(driver, config.TASK_POOL_STATISTIC_URL)
    number_text = init_statistics(driver, config.LIST_XPATH, task_pool_id, number_xpath_n)
    close_window(driver, handles)
    return number_text


# 工作流工作量统计
def work_flow_statistic(driver, task_pool_id, number_xpath_n, work_flow_id):
    handles = get_window(driver, config.TASK_POOL_STATISTIC_URL)
    number_text = "0"
    elements = driver.find_elements_by_xpath(config.LIST_XPATH)
    l = len(elements)
    if l == 0:
        logger.write_debug(u"无统计数据")
    else:
        for i in range(1, l + 1):
            # 获取任务池id
            text_1 = driver.find_element_by_xpath('%s[%s]/td[1]' % (config.LIST_XPATH, str(i))).text
            if text_1 != task_pool_id:
                if i != l:
                    continue
                else:
                    logger.write_debug(u"无任务池%s统计数据" % task_pool_id)
            else:
                find_by_xpath(driver, '%s[%s]/td[1]' % (config.LIST_XPATH, str(i)))
                number_text = init_statistics(driver, config.LIST_XPATH, work_flow_id, number_xpath_n)
                break
    close_window(driver, handles)
    return number_text


# 多队列工作量统计页面
def user_statistic(driver, username):
    users = driver.find_elements_by_xpath('//*[@id="salary-list"]/table/tbody/tr')
    sleep(config.STIME)
    workflow_number_text_list = ["0", "0", "0"]
    if len(users) == 0:
        logger.write_debug(u"工作流统计没有数据")
    else:
        for x in range(1, len(users) + 1):
            workflow_username = driver.find_element_by_xpath(
                '//*[@id="salary-list"]/table/tbody/tr[%s]/td[1]' % str(x)).text
            sleep(config.STIME)
            if workflow_username != username:
                if x != len(users):
                    continue
                else:
                    logger.write_debug(u"无用户%s统计数据" % username)
            else:
                workflow_number_text_list[0] = driver.find_element_by_xpath(
                    '//*[@id="salary-list"]/table/tbody/tr[%s]/td[5]' % str(x)).text
                workflow_number_text_list[1] = driver.find_element_by_xpath(
                    '//*[@id="salary-list"]/table/tbody/tr[%s]/td[6]' % str(x)).text
                workflow_number_text_list[2] = driver.find_element_by_xpath(
                    '//*[@id="salary-list"]/table/tbody/tr[%s]/td[16]' % str(x)).text
                break
    return workflow_number_text_list


# 从工作流进入多队列工作量统计
def workflow_user_statistics(driver, to_statistic_id, number_xpath_n, work_flow_id, username):
    handles = get_window(driver, config.TASK_POOL_STATISTIC_URL)
    elements = driver.find_elements_by_xpath(config.LIST_XPATH)
    sleep(config.STIME)
    l = len(elements)
    workflow_number_text_list = ["0", "0", "0"]
    if l == 0:
        logger.write_debug(u"无统计数据")
    else:
        for i in range(1, l + 1):
            # 获取任务池id
            text_1 = driver.find_element_by_xpath('%s[%s]/td[1]' % (config.LIST_XPATH, str(i))).text
            sleep(config.STIME)
            if text_1 != to_statistic_id:
                if i != l:
                    continue
                else:
                    logger.write_debug(u"无任务池%s统计数据" % to_statistic_id)
            else:
                find_by_xpath(driver, '%s[%s]/td[1]' % (config.LIST_XPATH, str(i)))
                workflow = driver.find_elements_by_xpath(config.LIST_XPATH)
                sleep(config.STIME)
                if len(workflow) == 0:
                    logger.write_error(u"工作流统计没记录，统计错误")
                else:
                    for j in range(1, len(workflow) + 1):
                        workflow_id = driver.find_element_by_xpath('%s[%s]/td[1]' % (config.LIST_XPATH, str(j))).text
                        sleep(config.STIME + 1)
                        if workflow_id != work_flow_id:
                            if j != len(workflow):
                                continue
                            else:
                                logger.write_debug(u"无工作流%s统计数据" % work_flow_id)
                        else:
                            find_by_xpath(driver, '%s[%s]/td[%s]/a' % (config.LIST_XPATH, str(j), number_xpath_n))
                            workflow_number_text_list = user_statistic(driver, username)

                            break
                break

    close_window(driver, handles)
    return workflow_number_text_list


# 从任务池进入多队列工作量统计
def task_pool_user_statistic(driver, to_statistic_id, number_xpath_n, username):
    handles = get_window(driver, config.TASK_POOL_STATISTIC_URL)
    elements = driver.find_elements_by_xpath(config.LIST_XPATH)
    sleep(config.STIME)
    l = len(elements)
    task_pool_number_text_list = ["0", "0", "0"]
    if l == 0:
        logger.write_debug(u"无统计数据")
    else:
        for i in range(1, l + 1):
            # 获取任务池id
            text_1 = driver.find_element_by_xpath('%s[%s]/td[1]' % (config.LIST_XPATH, str(i))).text
            sleep(config.STIME)
            if text_1 != to_statistic_id:
                if i != l:
                    continue
                else:
                    logger.write_debug(u"无任务池%s统计数据" % to_statistic_id)
            else:
                find_by_xpath(driver, '%s[%s]/td[%s]/a' % (config.LIST_XPATH, str(i), number_xpath_n))
                task_pool_number_text_list = user_statistic(driver, username)
                break

    close_window(driver, handles)
    return task_pool_number_text_list


# 老的工作量统计和我的工作量统计
def statistics(driver, task_name, new_window_url, number_xpath_n):
    handles = get_window(driver, new_window_url)
    number_text = init_statistics(driver, config.LIST_XPATH, task_name, number_xpath_n)
    close_window(driver, handles)
    return number_text


# 任务池进度统计
def progress_statistics(driver, task_pool_id, number_xpath_n):
    handles = get_window(driver, config.POOL_PROGRESS_URL)
    driver.find_element_by_id("_id").click()
    sleep(config.STIME)
    number_text = init_statistics(driver, config.PROGRESS_XPATH, task_pool_id, number_xpath_n)
    close_window(driver, handles)
    return number_text


# 老的工作量统计和我的工作量统计-用户工作量统计
def old_user_statistic(driver, task_name, new_window_url, number_xpath_n, username):
    handles = get_window(driver, new_window_url)
    elements = driver.find_elements_by_xpath(config.LIST_XPATH)
    sleep(config.STIME)
    user_number_text_list = ["0", "0", "0", "0"]
    l = len(elements)
    if l == 0:
        logger.write_debug(u"无统计数据")
    else:
        for i in range(1, l + 1):
            # 获取任务名称
            text_1 = driver.find_element_by_xpath('%s[%s]/td[1]' % (config.LIST_XPATH, str(i))).text
            sleep(config.STIME)
            if text_1 != task_name:
                if i != l:
                    continue
                else:
                    logger.write_debug(u"无%s统计数据" % task_name)
            else:
                find_by_xpath(driver, '%s[%s]/td[%s]/a' % (config.LIST_XPATH, str(i), number_xpath_n))
                users = driver.find_elements_by_xpath(config.LIST_XPATH)
                sleep(config.STIME)
                if len(users) == 0:
                    logger.write_debug(u"统计没有数据")
                else:
                    for x in range(1, len(users) + 1):
                        user_username = driver.find_element_by_xpath(
                            '//*[@id="salary-list"]/table/tbody/tr[%s]/td[1]' % str(x)).text
                        sleep(config.STIME)
                        if user_username != username:
                            if x != len(users):
                                continue
                            else:
                                logger.write_debug(u"无用户%s统计数据" % username)
                        else:
                            user_number_text_list[0] = driver.find_element_by_xpath(
                                '//*[@id="salary-list"]/table/tbody/tr[%s]/td[5]' % str(x)).text
                            user_number_text_list[1] = driver.find_element_by_xpath(
                                '//*[@id="salary-list"]/table/tbody/tr[%s]/td[6]' % str(x)).text
                            user_number_text_list[2] = driver.find_element_by_xpath(
                                '//*[@id="salary-list"]/table/tbody/tr[%s]/td[7]' % str(x)).text
                            user_number_text_list[3] = driver.find_element_by_xpath(
                                '//*[@id="salary-list"]/table/tbody/tr[%s]/td[17]' % str(x)).text
                            break
                break

    close_window(driver, handles)
    return user_number_text_list


# 获取项目列表页面的项目进度的数据
def job_progress_statistic(driver, job_id, n):
    handles = get_window(driver, config.JOB_LIST)
    find_by_xpath(driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/input', job_id, "send_keys")
    find_by_xpath(driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/button[1]')
    number = get_text(driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr/td[%s]' % n).text, 0)
    close_window(driver, handles)
    return number


# 校验次数
def check_statistic(check_name, check_page, check_statistic_name, before_number, after_number, increase=1):
    if int(after_number) == int(before_number) + increase:
        logger.write_debug(u"%s后的%s的%s统计正确，为：%s" % (
            check_name, check_page, check_statistic_name, after_number))
    else:
        logger.write_error(u"%s后的%s的%s统计错误，"
                           u"前为：%s, 后为：%s"
                           % (check_name, check_page, check_statistic_name, before_number, after_number))


# 校验个数（不能校验部分驳回的情况）
def check_number(driver, check_name, check_page, unit_id, check_statistic_unit_name, check_statistic_skip_name,
                 before_number_unit, before_number_skip, after_number_unit, after_number_skip):
    # 打开一个标签
    handles = get_window(driver, "manager/inspect-unit/%s" % unit_id)

    if is_element_exist(driver, "id", "alert-msg-wrap"):
        check_statistic(check_name, check_page, check_statistic_skip_name, before_number_skip, after_number_skip)
        if before_number_unit == after_number_unit:
            logger.write_debug(u"跳过的unit验收通过后unit个数不变,为：%s" % after_number_unit)
        else:
            logger.write_error(u"跳过的unit验收通过后unit个数错误，之前为：%s, 之后为：%s" % (before_number_unit, after_number_unit))
    else:
        check_statistic(check_name, check_page, check_statistic_unit_name, before_number_unit, after_number_unit)
        if before_number_skip == after_number_skip:
            logger.write_debug(u"未跳过的unit验收通过后跳过个数不变,为：%s" % after_number_skip)
        else:
            logger.write_error(u"未跳过的unit验收通过后跳过个数错误，之前为：%s, 之后为：%s" % (before_number_skip, after_number_skip))

    close_window(driver, handles)


def check_review_unit(driver, review_unit_id, task_pool_id, review_unit_number,
                      sample_proportion, acceptability, review_unit_status):
    handles = get_window(driver, "spa/review/task-flow-jobs-manage?sorts=&page=1&per_page=10&")

    logger.write_debug(u"搜索框查询出验收包%s" % review_unit_id)
    find_by_xpath(driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/input', review_unit_id, "send_keys")
    find_by_xpath(driver, '//*[@id="root"]/div[2]/div/div/div[1]/div[2]/div/button[1]')

    elements = driver.find_elements_by_xpath('//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr')
    sleep(config.STIME)
    l = len(elements)
    logger.write_debug(u"验收包列表总共 %s 条数据" % l)

    if l != 0:
        for i in range(1, l + 1):
            # 验收包名称（id）
            review_unit_name = driver.find_element_by_xpath(
                '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[1]' % str(i)).text
            text_1 = get_text(review_unit_name, 0)

            if text_1 == review_unit_id:
                # 任务池ID
                text_2 = driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[2]' % str(i)).text

                # 验收包总量
                text_3 = driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[6]' % str(i)).text
                # 抽样（比例）
                text_4 = driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[8]' % str(i)).text
                # 样本数-合格样本数（合格率）
                text_5 = driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[9]' % str(i)).text
                # 当前状态
                text_6 = driver.find_element_by_xpath(
                    '//*[@id="root"]/div[2]/div/div/div[2]/table/tbody/tr[%s]/td[11]' % str(i)).text

                logger.write_debug(u"开始校验验收包%s 的的正确性" % review_unit_id)
                check_text(task_pool_id, text_2, u"任务池id")
                check_text(review_unit_number, text_3, u"验收包总量")
                check_text(sample_proportion, text_4, u"抽样(比例)")
                check_text(acceptability, text_5, u"样本数-合格样本数（合格率）")
                check_text(review_unit_status, text_6, u"验收包状态")
                break
            else:
                if i != l:
                    continue
                else:
                    raise Exception(u"验收包%s不存在，执行停止，请确认数据" % review_unit_id)
    else:
        logger.write_error(u"无验收包数据，执行停止,请确认数据")

    close_window(driver, handles)


def get_text(s, n):
    _text = re.findall(r"\d+", s)[n]
    return _text
