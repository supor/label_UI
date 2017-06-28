# coding: utf-8

import os
import logging
import taf_utility
import taf_enum as enum
import taf_config as config

from HtmlLogger import logger

__msg_flag = "NULL"

logging.basicConfig(level=logging.DEBUG,
                    format='"%(asctime)s","%(levelname)s",%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=config.LOG_DETAIL_PATH,
                    filemode='w'
                    )

__result_logger = logging.getLogger("result")
if len(__result_logger.handlers) == 0:
    _handler = logging.FileHandler(config.LOG_RESULT_PATH)
    _handler._name = __msg_flag
    _handler.setLevel(logging.INFO)
    __formatter = logging.Formatter(fmt='%(message)s')
    _handler.setFormatter(__formatter)
    __result_logger.addHandler(_handler)
else:
    _handler = (__result_logger.handlers)[0]
    __msg_flag = _handler._name


def change_message_flag(_msg_flag):
    _handler = (__result_logger.handlers)[0]
    _handler._name = _msg_flag


def write_result(status, duration, suite_name='NULL', case_id='NULL', task_id='NULL'):
    """
    Output test result of the test suite/case/task
    """
    _format_info = '"%s","%s","%s","%s","%s"' % (suite_name, case_id, task_id, status, duration)
    __result_logger.info(_format_info)


def write_debug(msg):
    if "\"" in msg:
        msg.replace("\"", "\"\"")

    _format_info = '"%s","%s"' % (__msg_flag, msg)
    print "[DEBUG]%s" % _format_info
    logging.debug(_format_info)


def write_warn(msg):
    if "\"" in msg:
        msg.replace("\"", "\"\"")

    _format_info = '"%s","%s"' % (__msg_flag, msg)
    print "[WARNING]%s[31;2m%s%s[0m" % (chr(27), _format_info, chr(27))  # 31: fore color, red
    logging.warning(_format_info)


def write_error(msg):
    if "\"" in msg:
        msg.replace("\"", "\"\"")

    _format_info = '"%s","%s"' % (__msg_flag, msg)
    print "[ERROR]%s[31;2m%s%s[0m" % (chr(27), _format_info, chr(27))  # 31: fore color, red
    logging.error(_format_info)


def load_result_log(result_log_path):
    _suite_dict = {}
    _result_log = taf_utility.load_csv(result_log_path)
    for _result in _result_log:
        _suite_name = _result[0]
        _case_id = _result[1]
        _case_record = _result[2:]
        if _suite_dict.has_key(_suite_name):
            _case_dict = _suite_dict[_suite_name]
            if _case_dict.has_key(_case_id):
                _case_dict[_case_id].append(_case_record)
            else:
                _case_dict[_case_id] = [_case_record]
        else:
            _suite_dict[_suite_name] = {_case_id: [_case_record]}
    return _suite_dict


def generate_html_report_file(suite_name, suite_case, detail_log_path):
    _report_key = suite_name if suite_name != "NULL" else "report"
    _report_name = config.HTML_REPORT_NAME_FORMAT % (_report_key, config.CURRENT_TIME)
    _report_path = "%s/%s" % (config.LOG_ROOT_PATH, _report_name)

    if os.path.exists(_report_path):
        os.remove(_report_path)

    _logger = logger.Logger()
    _logger.load(_report_path)
    _detail_log = taf_utility.load_csv(detail_log_path)

    _case_status_list = []
    _case_durations = 0
    for _case_id, _case_result in suite_case.items():
        # append test case record
        _case_record = [res for res in _case_result if res[0] == "NULL"]  # eg.['NULL', 'Pass', '10.937']
        if len(_case_record) > 0:
            _case_record = _case_record[0]
            _case_status = _case_record[1]
            _case_duration = _case_record[2]
        else:
            _case_status = enum.TEST_RESULT.FAIL
            _case_duration = "0"
        _case_log_flag = "%s-%s" % (suite_name, _case_id)
        _case_log_list = [", log, ".join(log) for log in _detail_log if len(log) > 2 and log[2] == _case_log_flag]
        _logger.create_test_case_record(case_id=_case_id, case_result=_case_status, case_duration=_case_duration, case_log="<br/>".join(_case_log_list))
        _case_status_list.append(_case_status)
        _case_durations += float(_case_duration)

        # append task record
        _task_records = [res for res in _case_result if res[0] != "NULL"]  # eg.['1', 'Pass', '5.262']
        for _record in _task_records:
            _task_id = _record[0]
            _task_log_flag = "%s-%s-%s" % (suite_name, _case_id, _task_id)
            # _task_log_list = [", ".join(log) for log in _detail_log if len(log) > 2 and log[2] == _task_log_flag]
            _task_log_list = []
            for _log in _detail_log:
                if len(_log) > 2 and _log[2] == _task_log_flag:
                    if _log[1] == "ERROR":
                        _task_log_list.append("<span style='color: #c00000'>%s</span>" % ", ".join(_log))
                    elif _log[1] == "WARN":
                        _task_log_list.append("<span style='color: #c55911'>%s</span>" % ", ".join(_log))
                    else:
                        _task_log_list.append(", ".join(_log))
            _logger.create_task_record(case_id=_case_id, task_id=_task_id, task_result=_record[1], task_duration=_record[2], task_log="<br/>".join(_task_log_list))

    # append summary
    _total_count = len(_case_status_list)
    _pass_count = _case_status_list.count(enum.TEST_RESULT.PASS)
    _skip_count = _case_status_list.count(enum.TEST_RESULT.SKIP)
    _fail_count = _case_status_list.count(enum.TEST_RESULT.FAIL)
    _total_durations = str(round(_case_durations, 3))
    _logger.summary(total_count=_total_count, pass_count=_pass_count, skip_count=_skip_count, fail_count=_fail_count, duration=_total_durations)
    _suite_result = {"total_cases": _total_count, "pass_cases": _pass_count, "skip_cases": _skip_count, "fail_cases": _fail_count,
                     "durations": _total_durations, "report_path": _report_path}
    return {_report_key: _suite_result}


def generate_html_report(result_log_path, detail_log_path):
    _results = []
    _suite_dict = load_result_log(result_log_path)
    if len(_suite_dict.keys()) == 1:
        _suite_name = (_suite_dict.keys())[0]
        _suite_case = _suite_dict[_suite_name]
        _suite_result = generate_html_report_file(_suite_name, _suite_case, detail_log_path)
        _results.append(_suite_result)
    elif len(_suite_dict.keys()) > 1:
        for _key, _value in _suite_dict.items():
            _suite_result1 = generate_html_report_file(_key, _value, detail_log_path)
            _results.append(_suite_result1)
    return _results
