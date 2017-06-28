# coding: utf-8
#
#
# import MySQLdb
# import time
# import Projects.LABEL.pro_config as config
#
#
#
#
# conn = MySQLdb.connect(host="172.16.11.6",port=3306,user="root",passwd="123456",db="cfms")
#
# cur = conn.cursor()
# # select_result = cur.execute("select remittance_id from t_cfms_notional_distprofit where sment_no = '56401'")
# # result = cur.fetchall()
# # result_id = []
# #
# # for i in range(len(result)):
# #     print result[i]
# #     result_id.append(result[i][0])
# #
# #     print type(result[i])
# #     print type(result_id[0])
# # #     cur.execute("delete from t_cfms_remittance where id='%s'" % result_id[i])
# # #     cur.execute("delete from t_cfms_notional_distprofit where sment_no = '56401'")
# # # conn.commit()
# # # conn.close()
# # cur.close()
#
#
#
#
#
#
# s=cur.execute('select * from t_cfms_remittance where transfer_type="06"and txn_status="01"')
#
# result = cur.fetchall()
#
# remi_all_id = {}
# remi_in_id = []
# remi_out_id = []
#
# for i in range(len(result)):
#     # if result[i][0] in result_id:
#     if result[i][26] == "01":
#         remi_in_id.append(result[i][0])
#         print result[i][0], type(str(result[i][0]))
#     else:
#         print result[i][0]
#         remi_out_id.append(result[i][0])
#
# remi_all_id["in"] = remi_in_id
# remi_all_id['out'] = remi_out_id
#
# r =[]
# for i in remi_all_id['in']:
#     r.append(repr(i))
#     print i
# for j in remi_all_id['out']:
#     r.append(repr(j))
#     print j
#
# print ','.join(r)
#
#

import requests
import time
import random
import hashlib


tim = str(time.time())[:-3]
key = "fenqi_union"
password = "af88b8d59f46e6af1899056e41c5e9c48994a662"
mer_id = "heziqiche"
uid = "Useao9IkW1xaU"
buz_id = str(random.randint(0, 10000000000000000000))
description = "盒子汽车"
request_time = tim
expire = "600"
amt = "1000"
credit_flag = "true"
callback_url = "https://www.demo.com/api/callback/pay"  # 暂时未知，非必选
redirect_url = "https://www.demo.com/api/callback/pay"  # 暂时未知，非必选

dic = {"mer_id": mer_id, "uid": uid, "buz_id": buz_id, "description": description, "request_time": request_time,
       "expire": expire, "amt": amt}

param_str = sorted(dic.iteritems(), key=lambda d: d[0], reverse=False)

print(param_str)
splice = key+"|"+tim+"|"+password+"|"
for i in range(len(param_str)):
    splice += param_str[i][1]
    print splice

md = hashlib.md5(splice)

url = 'http://pay.t.bbtfax.com/api/cashier/order/apply'
data = {
    "key": key,
    "time": tim,
    "m": md.hexdigest(),
    "mer_id": mer_id,
    "uid": uid,
    "buz_id": buz_id,
    "description": description,
    "request_time": request_time,
    "expire": expire,
    "amt": amt
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

result = requests.post(url=url, data=data, headers=headers)

print result.text






