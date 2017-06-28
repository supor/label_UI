# coding: utf-8

import os
import sys
import time

# BASIC
ENCODING = "utf-8"
ROOT_PATH = os.path.split(os.path.dirname(sys.argv[0]))[0]
CURRENT_TIME = time.strftime("%b_%d_%Y_%H_%M_%S")
WEB_REQUEST_TYPE = "http"

# JSON NODE
NOTIFICATION = "notification"
NOTIFY = "notify"
MAIL_LIST = "mailList"
SUBJECT = "subject"
OWNER_NAME = "ownerName"
SUITE_LIST = "suiteList"
SUITE_NAME = "suiteName"
FOLDER_PATH = "folderPath"
EXECUTE_SEQUENCER = "executeSequencer"

# LOG
LOG_ROOT_PATH = "%s/logs" % ROOT_PATH
LOG_DETAIL_PATH = "%s/log-%s.log" % (LOG_ROOT_PATH, CURRENT_TIME)
LOG_RESULT_PATH = "%s/result-%s.log" % (LOG_ROOT_PATH, CURRENT_TIME)

# REPORT
REPORT_TITLE = "Test Report"
HTML_REPORT_TEMPLATE = "%s/HtmlLogger/LoggerTemplate.html" % ROOT_PATH
HTML_REPORT_NAME_FORMAT = "%s-%s.html"

# TEST CASE
TEST_CASE_ROOT_PATH = "%s/Projects/LABEL/testcase" % ROOT_PATH
DEFAULT_TEST_JSON_PATH = "%s/main.json" % TEST_CASE_ROOT_PATH

# JSON
PREREQUISITES_MAIN = {"suiteList": "list"}
PREREQUISITES_SUITE = {"suiteName": "str", "folderPath": "str", "executeSequencer": "list"}
PREREQUISITES_CASE = {"id": None, "name": None, "tasks": "list"}
PREREQUISITES_TASK = {"id": None, "name": None, "moduleName": None, "functionName": None}
PREREQUISITES_NOTIFICATION = {"notify": "bool", "subject": "str", "ownerName": "str", "mailList": "list"}

# MAIL
MAIL_SERVER = "smtp.qq.com"
MAIL_SENDER_ADDR = "930305620@qq.com"
MAIL_ADMIN_USERNAME = "930305620@qq.com"
MAIL_ADMIN_PASSWORD = ""
MAIL_SUMMARY_FORMAT = \
    '''
        Summary for suite '%s':\n
        -- total cases: %s\n
        -- pass  cases: %s\n
        -- skip  cases: %s\n
        -- fail  cases: %s\n
        -- durations: %s\n
    '''
MAIL_BODY_FORMAT = \
    '''
        Hi %s,
        %s
        Please refer to the attachment for details.\n
        Thanks!
    '''
