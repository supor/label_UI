# coding: utf-8

import MySQLdb

import Projects.LABEL.UI.common.pro_config as config
import framework.taf_logging as logger


def get_conn():
    """
    Get conn
    :return:
    """
    conn = MySQLdb.connect(host=config.MYSQL_HOST,
                           port=config.MYSQL_PORT,
                           user=config.MYSQL_USER,
                           passwd=config.MYSQL_PASSWD,
                           db=config.MYSQL_DATABASE
                           )
    return conn


def get_cur(conn):
    """
    Get cur
    :param conn:
    :return:
    """
    cur = conn.cursor()
    return cur


def execute_sql(cur, sql):
    """
    Execute sql
    :param cur:
    :return:
    """
    result = cur.execute(sql)
    logger.write_debug(u'受影响行数%s' % result)
    if result > 0:
        logger.write_debug(u"执行sql语句 ' %s' 成功! " % sql)
    else:
        logger.write_warn(u"执行sql语句 ' %s' 失败! " % sql)
        logger.write_warn(u'受影响数据行数为0,请确认sql: %s 的正确性,或者数据状态已在之前被更新..')


def commit_sql(conn):
    """

    :param cur:
    :return:
    """
    conn.commit()


def close_conn(conn, cur):
    """
    Close conn
    :param conn:
    :param cur:
    :return:
    """
    conn.close()
    cur.close()


