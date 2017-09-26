# coding: utf-8

import Driver.mysqlDriver as mysql
import Projects.LABEL.UI.common.pro_config as config
import framework.taf_logging as logger


def select_distprofit_id(sment_no):
    select_distprofit_id = config.SELECT_DISTPROFIT % sment_no
    conn = mysql.get_conn()
    cur = mysql.get_cur(conn)
    mysql.execute_sql(cur, select_distprofit_id)
    result = cur.fetchall()
    result_id = []
    for i in range(len(result)):
        result_id.append(result[i][0])
        type(result[i][0])
    return result_id


def delete_distprofit_info(sment_no):
    result_id = select_distprofit_id(sment_no)
    conn = mysql.get_conn()
    cur = mysql.get_cur(conn)
    logger.write_debug(u'删除结算单%s关联表数据' % sment_no)
    if len(result_id) != 0:
        for i in range(len(result_id)):
            logger.write_debug(u'删除remittance表结算单%s提交信息，remittance id 为%s' % (sment_no, result_id[i]))
            delete_remittance_id = config.DELETE_REMITTANCE_ID % result_id[i]
            mysql.execute_sql(cur, delete_remittance_id)

        logger.write_debug(u'删除distprofit表结算单%s分润信息' % sment_no)
        delete_distprofit_id = config.DELETE_DISTPROFIT_ID % sment_no
        mysql.execute_sql(cur, delete_distprofit_id)
        mysql.commit_sql(conn)
        mysql.close_conn(conn, cur)
    else:
        logger.write_debug(u'结算单%s关联表无数据，不用清除' % sment_no)


def update_smet_status(table, total_table, status, smet_no):
    """

    :param smet_no:
    :return:
    """
    # 修改结算单状态为Y00
    sment_main_status = select_smet_status(table, smet_no)
    sment_total_status = select_smet_status(total_table, smet_no)
    sql_total = config.UPDATE_SMET_INFO_STATUS % (table, status, smet_no)
    sql_main = config.UPDATE_SMET_LOAN_STATUS % (total_table, status, smet_no)
    conn = mysql.get_conn()
    cur = mysql.get_cur(conn)
    logger.write_debug(u'修改结算单%s的状态为Y00' % smet_no)
    if sment_main_status != "Y00":
        mysql.execute_sql(cur, sql_total)
    if sment_total_status != "Y00":
        mysql.execute_sql(cur, sql_main)

    mysql.commit_sql(conn)
    mysql.close_conn(conn, cur)

    # 清除关联表信息
    delete_distprofit_info(smet_no)


def select_remi_id(transfer_type, txn_status):
    select_remi = config.SELECT_REMI % (transfer_type, txn_status)
    conn = mysql.get_conn()
    cur = mysql.get_cur(conn)
    mysql.execute_sql(cur, select_remi)
    mysql.commit_sql(conn)
    result = cur.fetchall()
    return result


def split_remi_id(transfer_type, txn_status, sment_no):
    result = select_remi_id(transfer_type, txn_status)
    conn = mysql.get_conn()
    cur = mysql.get_cur(conn)
    remi_all_id = {}
    remi_in_id = []
    remi_out_id = []
    result_id = select_distprofit_id(sment_no)

    for i in range(len(result)):
        if str(result[i][0]) in result_id:
            print type(result[i][0])
            if result[i][26] == "01":
                print result[i][0]
                remi_in_id.append(result[i][0])
                print remi_in_id
            elif result[i][26] == "02":
                remi_out_id.append(result[i][0])
                print 'out: %s' % result[i][0]
                print remi_out_id

    remi_all_id[config.IN] = remi_in_id
    remi_all_id[config.OUT] = remi_out_id
    mysql.close_conn(conn, cur)
    return remi_all_id


def select_bank_corp_sn(remi_id):
    # result = select_remi_id(txn_status, transfer_type)
    select_bank_corp_sn = config.SELECT_BANK_CORP_SN % remi_id
    conn = mysql.get_conn()
    cur = mysql.get_cur(conn)
    mysql.execute_sql(cur, select_bank_corp_sn)
    bank_corp_sn = cur.fetchall()
    return bank_corp_sn


def select_smet_status(table, sment_no):
    select_smet_status = config.SELECT_SMET_STATUS % (table, sment_no)
    conn = mysql.get_conn()
    cur = mysql.get_cur(conn)
    mysql.execute_sql(cur, select_smet_status)
    mysql.commit_sql(conn)
    result = cur.fetchall()
    sment_status = result[0][0]
    mysql.close_conn(conn, cur)
    return sment_status
