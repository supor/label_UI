# coding: utf-8

import random
import time

import Driver.webserviceDriver as restful
import Projects.LABEL.RestAPI.mysql.mysqlManagments as mysql
import Projects.LABEL.UI.common.pro_config as config
import framework.taf_logging as logger


def send_post_requests(uri, data, headers, status, table_main, sment_no, other_header={}):
    """
    Send post requests
    :param uri:
    :param data:
    :param headers:
    :param other_header:
    :return:
    """
    # 封装请求头 headers 在main.json里定义, other_header 在独立json里定义的头
    headers = dict(headers.items()+other_header.items())
    logger.write_debug(u'请求头: %s' % headers)
    # 拼接请求url
    url = config.base_url+uri
    logger.write_debug(u'请求url: %s' % url)
    logger.write_debug(u'请求方式: POST')
    logger.write_debug(u'请求参数: %s' % data)
    logger.write_debug(u'请求头部: %s' % headers)
    _dict = restful.send_post_requests(url, data=data, headers=headers)
    logger.write_debug('check html return code..')

    # 判断返回结果
    if _dict['code'] != config.code_success:
        logger.write_error('check html code is error!')
        raise Exception(U'html return code is %s not the expected %s' % (_dict['code'], config.code_success))
    logger.write_debug(u'响应数据: %s' % _dict)

    # check return result
    check_result(_dict, url)

    time.sleep(config.TIME)

    # select status,check status
    smet_status_main = mysql.select_smet_status(table_main, sment_no)
    smet_status_total = mysql.select_smet_status(config.TABLE_TOTAL, sment_no)

    if smet_status_main == status and smet_status_total == status:
        logger.write_debug(u'The interface test succeed, the end status is %s' % smet_status_total)
    else:
        logger.write_error(u'The interface test failed')
        raise Exception('The interface test failed,the smet_status_main is %s, the smet_status_total is %s,the expected status is %s' % (smet_status_main, smet_status_total, status))

    time.sleep(config.TIME)


def get_sment_no(sment_no):
    """
    get sment_no
    :return:
    """
    return sment_no


def check_result(result, url):
    """
    Check return code
    :param result:
    :param return_code:
    """
    logger.write_debug(u'check api return code')
    if result.has_key('fault'):
        if result['fault']['returnCode'] != config.RETURN_CODE:
            logger.write_error(u'check api return code error!')
            raise Exception('%s return code is %s , codedesc is %s, not the expected' %
                            (url, result['fault']['returncode'], result['fault']['codeDesc']))
        else:
            logger.write_debug("check api return code secceed" )
    else:
        logger.write_error('check api return code error!')
        raise Exception('%s return code error!' % url)


def get_random_remitxnsn(start, end):
    """
    get random remi txn_sn
    :return:
    """
    random_remitxnsn = random.randint(start, end)
    return str(random_remitxnsn)


def send_remi_pay_requests(transfer_type, txn_status, url_pay, headers, table_main, sment_no, status, other_header):
    """
    send remi payment requests

    """
    remi_id = mysql.split_remi_id(transfer_type, txn_status, sment_no)
    body = {}
    data = {}
    remi_all_id = []
    for i in range(len(remi_id[config.IN])):
        remi_all_id.append(remi_id[config.IN][i])
    for j in range(len(remi_id[config.OUT])):
        remi_all_id.append(remi_id[config.OUT][j])

    for re_id in remi_all_id:

        body[config.REMIID] = re_id
        data[config.BODY] = body
        data[config.HEADER] = config.BODY_HEADER
        logger.write_debug(u'请求头: %s' % headers)
        # 拼接请求url
        url = config.base_url+url_pay
        logger.write_debug(u'对内复核请求url: %s' % url)
        logger.write_debug(u'请求方式: POST')
        logger.write_debug(u'请求参数: %s' % data)
        logger.write_debug(u'请求头部: %s' % headers)
        _dict = restful.send_post_requests(url, data, config.REQUEST_HEADER)
        logger.write_debug('check html return code..')

        # 判断返回结果
        if _dict['code'] != config.code_success:
            logger.write_error('check html code is error!')
            raise Exception(U'html return code is %s not the expected %s' % (_dict['code'], config.code_success))
        logger.write_debug(u'响应数据: %s' % _dict)

        # check return result
        check_result(_dict, url)

        time.sleep(config.TIME)

        # select status, check_two_tables_status
        smet_status_main = mysql.select_smet_status(table_main, sment_no)
        smet_status_total = mysql.select_smet_status(config.TABLE_TOTAL, sment_no)
        if smet_status_main == status and smet_status_total == status:
            logger.write_debug(u'The interface test succeed, the end status is %s' % smet_status_total)
        else:
            logger.write_error(u'The interface test failed')
            raise Exception('The interface test failed,the smet_status_main is %s, the smet_status_total is %s,the '
                            'expected all status is %s' % (smet_status_main, smet_status_total, status))

        time.sleep(config.TIME)

    time.sleep(config.TIME)


def send_recheck_requests(transfer_type, txn_status,  url_in_recheck, headers, table_main, sment_no, other_header, need_txn_sn=True):
    """
    send recheck requests
    """
    remi_all_id = mysql.split_remi_id(transfer_type, txn_status, sment_no)
    body = {}
    data = {}

    # 判断对内复核申请
    for in_id in remi_all_id[config.IN]:

        # 获取银企直联信息
        bank_corp_sn = mysql.select_bank_corp_sn(in_id)
        print bank_corp_sn is None
        if bank_corp_sn is None:
            body[config.REMI_TXN_SN] = get_random_remitxnsn(0, 10000000000)
        else:
            if need_txn_sn is True:
                body[config.REMI_TXN_SN] = get_random_remitxnsn(0, 10000000000)
            else:
                body[config.REMI_TXN_SN] = ""

        body[config.REMIID] = in_id
        data[config.BODY] = body
        data[config.HEADER] = config.BODY_HEADER

        logger.write_debug(u'请求头: %s' % headers)
        url = config.base_url+url_in_recheck
        logger.write_debug(u'对内复核请求url: %s' % url)
        logger.write_debug(u'请求方式: POST')
        logger.write_debug(u'请求参数: %s' % data)
        logger.write_debug(u'请求头部: %s' % headers)
        logger.write_debug('check html return code..')
        _dict = restful.send_post_requests(url, data, config.REQUEST_HEADER)

        time.sleep(config.TIME)

        # 判断返回结果
        if _dict['code'] != config.code_success:
            logger.write_error('check html code is error!')
            raise Exception(U'html return code is %s not the expected %s' % (_dict['code'], config.code_success))
        logger.write_debug(u'响应数据: %s' % _dict)

        # check return result
        check_result(_dict, url)

        time.sleep(config.TIME)

        if remi_all_id[config.OUT] == []:

            if remi_all_id[config.IN].index(in_id) != len(remi_all_id[config.IN])-1:
                wait_time = 0
                while wait_time <= 150:
                    # select two tables status,check status
                    smet_status_main = mysql.select_smet_status(table_main, sment_no)
                    smet_status_total = mysql.select_smet_status(config.TABLE_TOTAL, sment_no)
                    if smet_status_main == "Z06" and smet_status_total == "Z06":
                        logger.write_debug(u'select total time is %s, the interface test succeed,'
                                           u' the remi payrequests status is %s' % (wait_time, smet_status_total))
                        break
                    else:
                        if wait_time > 150:
                            logger.write_error(u'The interface test failed')
                            raise Exception('The interface test failed,the smet_status_main is %s,'
                                            ' the smet_status_total'' is %s,the expected all status is %s'
                                            % (smet_status_main, smet_status_total, "Z06"))
                        else:
                            time.sleep(1)
                            wait_time += 1
            else:
                wait_time = 0
                while wait_time <= 150:
                    # select two tables status,check status
                    smet_status_main = mysql.select_smet_status(table_main, sment_no)
                    smet_status_total = mysql.select_smet_status(config.TABLE_TOTAL, sment_no)
                    if smet_status_main == "Z08" and smet_status_total == "Z08":
                        logger.write_debug(u'select total time is %s, the interface test succeed,'
                                           u' the remi payrequests status is %s' % (wait_time, smet_status_total))
                        break
                    else:
                        if wait_time > 150:
                            logger.write_error(u'The interface test failed')
                            raise Exception('The interface test failed,the smet_status_main is %s,'
                                            ' the smet_status_total'' is %s,the expected all status is %s'
                                            % (smet_status_main, smet_status_total, "Z08"))
                        else:
                            time.sleep(1)
                            wait_time += 1

        if remi_all_id[config.OUT] != []:

            wait_time = 0
            while wait_time <= 150:
                # select two tables status,check status
                smet_status_main = mysql.select_smet_status(table_main, sment_no)
                smet_status_total = mysql.select_smet_status(config.TABLE_TOTAL, sment_no)
                if smet_status_main == "Z06" and smet_status_total == "Z06":
                    logger.write_debug(u'select total time is %s, the interface test succeed, '
                                       u'the remi payrequests status is %s' % (wait_time, smet_status_total))
                    break
                else:
                    if wait_time > 150:
                        logger.write_error(u'The interface test failed')
                        raise Exception('The interface test failed,the smet_status_main is %s,'
                                        ' the smet_status_total'' is %s,the expected all status is %s'
                                        % (smet_status_main, smet_status_total, "Z06"))
                    else:
                        time.sleep(1)
                        wait_time += 1

        time.sleep(config.TIME)

    if remi_all_id[config.OUT] != []:
        # 对外复核
        for out_id in remi_all_id[config.OUT]:

            # 获取银企直联信息
            bank_corp_sn = mysql.select_bank_corp_sn(out_id)
            print bank_corp_sn is None
            if bank_corp_sn is None:
                body[config.REMI_TXN_SN] = get_random_remitxnsn(0, 10000000000)
            else:
                if need_txn_sn is True:
                    body[config.REMI_TXN_SN] = get_random_remitxnsn(0, 10000000000)
                else:
                    body[config.REMI_TXN_SN] = ""

            body[config.REMIID] = out_id
            data[config.BODY] = body
            data[config.HEADER] = config.BODY_HEADER
            logger.write_debug(u'请求头: %s' % headers)
            # 拼接请求url
            url = config.base_url+url_in_recheck
            logger.write_debug(u'对外复核请求url: %s' % url)
            logger.write_debug(u'请求方式: POST')
            logger.write_debug(u'请求参数: %s' % data)
            logger.write_debug(u'请求头部: %s' % headers)
            logger.write_debug('check html return code..')
            _dict = restful.send_post_requests(url, data, config.REQUEST_HEADER)

            if _dict['code'] != config.code_success:
                logger.write_error('check html code is error!')
                raise Exception(U'html return code is %s not the expected %s' % (_dict['code'], config.code_success))
            logger.write_debug(u'响应数据: %s' % _dict)

            # check return result
            check_result(_dict, url)

            time.sleep(config.TIME)

            # select two tables status
            if remi_all_id[config.OUT].index(out_id) != len(remi_all_id[config.OUT])-1:

                wait_time = 0
                while wait_time <= 150:
                    # select two tables status,check status
                    smet_status_main = mysql.select_smet_status(table_main, sment_no)
                    smet_status_total = mysql.select_smet_status(config.TABLE_TOTAL, sment_no)
                    if smet_status_main == "Z06" and smet_status_total == "Z06":
                        logger.write_debug(u'select total time is %s, the interface test succeed,'
                                           u' the remi payrequests status is %s' % (wait_time, smet_status_total))
                        break
                    else:
                        if wait_time > 150:
                            logger.write_error(u'The interface test failed')
                            raise Exception('The interface test failed,the smet_status_main is %s,'
                                            ' the smet_status_total'' is %s,the expected all status is %s'
                                            % (smet_status_main, smet_status_total, "Z06"))
                        else:
                            time.sleep(1)
                            wait_time += 1

            else:
                wait_time = 0
                while wait_time <= 150:
                    # select two tables status,check status
                    smet_status_main = mysql.select_smet_status(table_main, sment_no)
                    smet_status_total = mysql.select_smet_status(config.TABLE_TOTAL, sment_no)
                    if smet_status_main == "Z08" and smet_status_total == "Z08":
                        logger.write_debug(u'select total time is %s, the interface test succeed,'
                                           u' the remi payrequests status is %s' % (wait_time, smet_status_total))
                        break
                    else:
                        if wait_time > 150:
                            logger.write_error(u'The interface test failed')
                            raise Exception('The interface test failed,the smet_status_main is %s,'
                                            ' the smet_status_total'' is %s,the expected all status is %s'
                                            % (smet_status_main, smet_status_total, "Z08"))
                        else:
                            time.sleep(1)
                            wait_time += 1

            time.sleep(config.TIME)

    if remi_all_id[config.OUT] == []:
        logger.write_debug("there is no out recheck")

    time.sleep(config.TIME)










