# coding: utf-8
# #
# #
# # import MySQLdb
# # import time
# # import Projects.LABEL.pro_config as config
# #
# #
# #
# #
# # conn = MySQLdb.connect(host="172.16.11.6",port=3306,user="root",passwd="123456",db="cfms")
# #
# # cur = conn.cursor()
# # # select_result = cur.execute("select remittance_id from t_cfms_notional_distprofit where sment_no = '56401'")
# # # result = cur.fetchall()
# # # result_id = []
# # #
# # # for i in range(len(result)):
# # #     print result[i]
# # #     result_id.append(result[i][0])
# # #
# # #     print type(result[i])
# # #     print type(result_id[0])
# # # #     cur.execute("delete from t_cfms_remittance where id='%s'" % result_id[i])
# # # #     cur.execute("delete from t_cfms_notional_distprofit where sment_no = '56401'")
# # # # conn.commit()
# # # # conn.close()
# # # cur.close()
# #
# #
# #
# #
# #
# #
# # s=cur.execute('select * from t_cfms_remittance where transfer_type="06"and txn_status="01"')
# #
# # result = cur.fetchall()
# #
# # remi_all_id = {}
# # remi_in_id = []
# # remi_out_id = []
# #
# # for i in range(len(result)):
# #     # if result[i][0] in result_id:
# #     if result[i][26] == "01":
# #         remi_in_id.append(result[i][0])
# #         print result[i][0], type(str(result[i][0]))
# #     else:
# #         print result[i][0]
# #         remi_out_id.append(result[i][0])
# #
# # remi_all_id["in"] = remi_in_id
# # remi_all_id['out'] = remi_out_id
# #
# # r =[]
# # for i in remi_all_id['in']:
# #     r.append(repr(i))
# #     print i
# # for j in remi_all_id['out']:
# #     r.append(repr(j))
# #     print j
# #
# # print ','.join(r)
# #
# #
#
# import requests
# import time
# import random
# import hashlib
#
#
# tim = str(time.time())[:-3]
# key = "fenqi_union"
# password = "af88b8d59f46e6af1899056e41c5e9c48994a662"
# mer_id = "heziqiche"
# uid = "Useao9IkW1xaU"
# buz_id = str(random.randint(0, 10000000000000000000))
# description = "盒子汽车"
# request_time = tim
# expire = "600"
# amt = "1000"
# credit_flag = "true"
# callback_url = "https://www.demo.com/api/callback/pay"  # 暂时未知，非必选
# redirect_url = "https://www.demo.com/api/callback/pay"  # 暂时未知，非必选
#
# dic = {"mer_id": mer_id, "uid": uid, "buz_id": buz_id, "description": description, "request_time": request_time,
#        "expire": expire, "amt": amt}
#
# param_str = sorted(dic.iteritems(), key=lambda d: d[0], reverse=False)
#
# print(param_str)
# splice = key+"|"+tim+"|"+password+"|"
# for i in range(len(param_str)):
#     splice += param_str[i][1]
#     print splice
#
# md = hashlib.md5(splice)
#
# url = 'http://pay.t.bbtfax.com/api/cashier/order/apply'
# data = {
#     "key": key,
#     "time": tim,
#     "m": md.hexdigest(),
#     "mer_id": mer_id,
#     "uid": uid,
#     "buz_id": buz_id,
#     "description": description,
#     "request_time": request_time,
#     "expire": expire,
#     "amt": amt
# }
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }
#
# result = requests.post(url=url, data=data, headers=headers)
#
# print result.text


# #
def login():
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome("D:\chromedriver")
    driver.get("http://vendor.zzcrowd.com/login")
    sleep(1)
    driver.find_element_by_id("username").send_keys("r")
    sleep(0.5)
    driver.find_element_by_id("password").send_keys("vendor")
    sleep(0.5)
    driver.find_element_by_id("submit").click()
    sleep(1)
    return driver
# driver.get('http://vendor.zzcrowd.com/spa/review/task-flow-jobs?page=1&per_page=10&continuable=1#1')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/ul/li[2]/a').click()
# sleep(5)
# div_id = driver.find_element_by_xpath('//*[@id="image-panel"]/div[1]/div').get_attribute("id")
# total_text = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[3]').text



# for handle in handles:
#     if driver.current_window_handle != handle:
#         print handle
#         print driver.current_window_handle
#         print u"不是本窗口"
#         driver.switch_to.window(handle)
#
#     else:
#         print handle
#         print driver.current_window_handle
#         print u"是本窗口"

# def statistics(new_window_url):
#     js = 'window.open("%s");' % new_window_url
#     driver.execute_script(js)
#     handles = driver.window_handles
#     driver.switch_to.window(handles[-1])
#     number_text = driver.find_element_by_xpath('//*[@id="salary-list"]/table/tbody/tr[1]/td[4]/a').text
#     print number_text
#     driver.close()
#     driver.switch_to.window(handles[0])
#     driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div[1]/div').click()
#     return number_text
#
# statistics("http://vendor.zzcrowd.com/statistics/flow/task-pool?start_date=2017-08-25&end_date=2017-08-25&user_match=&user_type_id=0&task_type_id=0&job_id=0&user_ids=[]&action_type_id=0&task_pool_id=12")


# def test():
#     driver.get("http://vendor.zzcrowd.com/statistics/flow/task-pools")
#     print "1:" + driver.current_window_handle
#     js = 'window.open("%s");' % (
#     "%sstatistics/flow/task-pool?start_date=2017-08-25&end_date=2017-08-25&user_match=&user_type_id=0&task_type_id=0&job_id=0&user_ids=[]&action_type_id=0&task_pool_id=12" % (
#     'http://vendor.zzcrowd.com/'))
#     driver.execute_script(js)
#     handles = driver.window_handles
#     print "2" + driver.current_window_handle
#     print handles
#
#     # driver.switch_to.window(handles[1])
#     sleep(1)
#     driver.find_element_by_xpath('//*[@id="salary-list"]/table/tbody/tr[1]/td[4]/a').click()


def t(c):
    a = 0
    if c == 1:
        a = "1"
    return a


# def get_text():
#     driver = login()
#     driver.get("http://vendor.zzcrowd.com/manager/statistic/task-type")
#     total_text = driver.find_element_by_xpath('//*[@id="info-text"]').text[43:45]
#     print total_text
#
# get_text()

def get_review_unit_id(publisher_url, publisher_type=u"验收"):
    if publisher_type == u"验收":
        review_unit_id = publisher_url.replace("http://vendor.zzcrowd.com/publisher/stream-reviewing/", "").replace("?from=taskflow&fromPage=flow", "")
    else:
        review_unit_id = publisher_url.replace("http://vendor.zzcrowd.com/extra_bp/sample/sampling/", "").replace("?from=taskflow", "")
    return review_unit_id


def get_id():
    l = get_review_unit_id("http://vendor.zzcrowd.com/publisher/stream-reviewing/178?from=taskflow&fromPage=flow")
    print l


def t_for():
    for i in range(0, 10):
        if i != 5:
            print "i:" + str(i)
            continue
        else:
            for j in range(10,15):
                if j != 13:
                    print "j:" + str(j)
                    continue
                else:
                    break
            break


def run_edit():
    from time import sleep
    driver = login()
    driver.get('http://vendor.zzcrowd.com/editor/flow-editing/37')
    sleep(1)

    for i in range(0, 500):
        unit_id = driver.find_element_by_id('unit_id').text
        if unit_id == "19103":
            break
        else:
            driver.find_element_by_id('skip').click()
            sleep(0.5)
            driver.find_element_by_xpath('//*[@id="reason-dialog"]/div/div[2]/button').click()
            sleep(1.5)

run_edit()
