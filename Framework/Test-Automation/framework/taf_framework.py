# coding: utf-8

import re
import os
import sys
import json
import types
import inspect
import threading
from datetime import datetime

import taf_mail
import taf_utility
import taf_reflection
import taf_enum as enum
import taf_config as config
import taf_logging as logging


__test_case_set = {}


def get_case(case_id):
    print "Executing function 'get_test_case' with case_id = %s" % case_id

    _test_case = (__test_case_set.has_key(case_id) and [__test_case_set[case_id]] or [None])[0]
    execute_prerequisites(_test_case, config.PREREQUISITES_CASE)
    return _test_case


def get_task(case_id, task_id):
    print "Executing function 'get_test_task' with case_id=%s, task_id=%s" % (case_id, task_id)

    _test_case = get_case(case_id)
    if _test_case is None:
        return None

    for task in _test_case["tasks"]:
        execute_prerequisites(task, config.PREREQUISITES_TASK)
        if repr(task["id"]) == repr(task_id):
            return task


def wakeup_pending_test(test_result, id):
    print "Executing function 'wakeup_pending_test' with test_result=%s, id=%s" % (test_result, id)

    test_result[id] = enum.TEST_RESULT.READY


def execute_prerequisites(json_dict={}, name_type_dict={}):
    """
    Check prerequisites
    """
    print "Executing function 'execute_prerequisites' with json_dict=%s, name_type_dict=%s" % (json_dict, name_type_dict)

    _missing_params = []
    _wrong_type_message = ""
    for _name, _type in name_type_dict.items():
        if not json_dict.has_key(_name):
            _missing_params.append(_name)

        _actual_type = type(json_dict[_name]).__name__
        if _type is not None and _actual_type != _type:
            _wrong_type_message += "The param %s should be %s, but actually is %s \n" % (_name, _type, _actual_type)

    if len(_missing_params) != 0:
        raise KeyError("You are missing the mandatory params %s in the json file." % _missing_params)

    if _wrong_type_message != "":
        raise ValueError(_wrong_type_message)


def register_status(test_result, id, status=enum.TEST_RESULT.READY):
    """
    Set test case/task status
    """
    print "Executing function 'register_test_status' with test_result=%s, id=%s, status=%s" % (test_result, id, status)

    test_result[repr(id)] = status


def check_result(test_result, id):
    """
    Check if the test case/task is passed
    """
    print "Executing function 'check_test_result' with test_result=%s, id=%s" % (test_result, id)

    if type(id) is not types.ListType:
        id = [id]

    for i in id:
        if not test_result.has_key(repr(i)):
            logging.write_debug("The test case '%s' have not registered yet" % i)
            return False
        else:
            _test_result = test_result[repr(i)]
            logging.write_debug("The test case '%s' is %s" % (id, _test_result))
            if _test_result != enum.TEST_RESULT.PASS:
                return False
    return True


def apply_dynamic_value(common_variable, missing_return_value, target_object):
    """
    Get the dynamic value of the target object
    """
    print "Executing function 'apply_dynamic_value' with common_variable=%s, target_object=%s" % (common_variable, target_object)

    if type(target_object) is types.ListType:
        for _obj in target_object:
            if type(_obj) is types.DictionaryType or type(_obj) is types.ListType:
                apply_dynamic_value(common_variable, missing_return_value, _obj)

    elif type(target_object) is types.DictionaryType:
        for _k, _v in target_object.items():
            if type(_v) is types.DictionaryType or type(_v) is types.ListType:
                apply_dynamic_value(common_variable, missing_return_value, _v)
                continue

            if type(_v) is types.UnicodeType:
                while True:
                    match = re.search(r'(?<=&\()[a-zA-Z0-9._]+(\[(\"|\')[0-9A-Za-z_]+(\"|\')\])?(?=\))', target_object[_k])  # ?

                    if match is None:
                        break

                    obj_str = match.group()
                    has_key = False
                    if obj_str.count('[') == 1:
                        obj_str = re.search(r'[0-9a-zA-Z._]+(?=\[)', obj_str).group()
                        has_key = True

                    if common_variable.has_key(obj_str):
                        _get_value = common_variable[obj_str]
                        if has_key:
                            __key = re.search(r'(?<=\[(\"|\'))[0-9a-zA-Z_]+(?=(\"|\')\])', match.group()).group()
                            _get_value = _get_value[__key]

                        if len(_v) == len(match.group()) + 3:
                            target_object[_k] = _get_value
                            break
                        else:
                            target_object[_k] = target_object[_k].replace(r'&(%s)' % (match.group()), _get_value)
                            break
                    else:
                        missing_return_value.append(obj_str)
                        break

    else:
        _error_message = "The param 'target_object' should be a list or dictionary, but it's a %s" % (type(target_object))
        raise ValueError(_error_message)


def execute_task(tasks_result, global_variable, local_variable, suite_name, case_id, task):
    """
    Execute test task
    """
    print "Executing function 'execute_test_task' with suite_name=%s, case_id=%s, task=%s" % (suite_name, case_id, task)

    try:
        _start_time = datetime.now()
        execute_prerequisites(task, config.PREREQUISITES_TASK)  # check parameters: id, name, moduleName, functionName
        _task_id = task["id"]
        _task_name = task["name"]
        _task_module_name = task["moduleName"]
        _task_function_name = task["functionName"]

        logging.__msg_flag = "%s-%s-%s" % (suite_name, case_id, _task_id)  # set log flag
        logging.change_message_flag("%s-%s-%s" % (suite_name, case_id, _task_id))
        logging.write_debug("Start to execute task: %s - %s" % (_task_id, _task_name))

        # check if need to run
        if task.has_key("run") and task["run"] == 0:
            logging.write_debug("Current task is not run because the param 'run' is 0")
            logging.write_debug("End executing current task")
            _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
            logging.write_result(enum.TEST_RESULT.SKIP, _duration, suite_name, case_id, _task_id)
            register_status(tasks_result, _task_id, enum.TEST_RESULT.SKIP)
            return

        # check the depended task
        if task.has_key("dependsOn") and not check_result(tasks_result, task["dependsOn"]):
            logging.write_debug("Current task is skipped because its depended task '%s' is not 'Pass'" % task["dependsOn"])
            logging.write_debug("End executing current task")
            _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
            logging.write_result(enum.TEST_RESULT.SKIP, _duration, suite_name, case_id, _task_id)
            register_status(tasks_result, _task_id, enum.TEST_RESULT.SKIP)
            return

        # check if need to run immediately
        if task.has_key("realtime") and task["realtime"] == 0:
            logging.write_debug("Current task will not be run immediately because the param 'realtime' is 0")
            register_status(tasks_result, _task_id, enum.TEST_RESULT.PENDING)
        else:
            register_status(tasks_result, _task_id, enum.TEST_RESULT.READY)

        _task_class_name = ((task.has_key("className") and task["className"] != "") and [task["className"]] or [None])[0]
        _task_params = ((task.has_key("params") and len(task["params"]) > 0) and [task["params"]] or [{}])[0]
        _task_exception = ((task.has_key("expectedError") and task["expectedError"] != "") and [task["expectedError"]] or [None])[0]
        _task_global_return_value = ((task.has_key("globalReturnedValue") and task["globalReturnedValue"] == 1) and [1] or [0])[0]

        for _key, _value in global_variable.items():
            if local_variable.has_key(_key):
                continue
            local_variable[_key] = _value

        for _key, _value in local_variable.items():
            if _task_params is not None and _task_params.has_key(_key):
                continue
            _task_params[_key] = _value

        if _task_params is not None:
            _missing_list = []
            apply_dynamic_value(local_variable, _missing_list, _task_params)  # get the dynamic value of the task parameters
            for _miss_id in _missing_list:
                if "." in _miss_id:
                    logging.write_error("The global variable '%s' can not be found" % _miss_id)
                    logging.write_debug("End executing current task")
                    _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                    logging.write_result(enum.TEST_RESULT.ERROR, _duration, suite_name, case_id, _task_id)
                    register_status(tasks_result, _task_id, enum.TEST_RESULT.ERROR)
                    return
                else:
                    pattern = re.compile(r'^[0-9]+$')
                    match = pattern.search(_miss_id)
                    if match is None:
                        logging.write_error("Its referred variable '%s' is not existed" % _miss_id)
                        logging.write_debug("End executing current task")
                        _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                        logging.write_result(enum.TEST_RESULT.ERROR, _duration, suite_name, case_id, _task_id)
                        register_status(tasks_result, _task_id, enum.TEST_RESULT.ERROR)
                        return

                    if tasks_result.has_key(_miss_id):
                        if tasks_result[_miss_id] == enum.TEST_RESULT.PENDING:
                            _realtime_task = get_task(case_id, _miss_id)
                            wakeup_pending_test(tasks_result, _miss_id)
                            execute_task(tasks_result, global_variable, local_variable, suite_name, case_id, _realtime_task)
                            apply_dynamic_value(local_variable, _missing_list, _task_params)
                        elif tasks_result[_miss_id] == enum.TEST_RESULT.READY:
                            logging.write_debug("Its referred task '%s' has not been executed yet. So it can not " \
                                         "provide the return value to task '%s'" % (_miss_id, _task_id))
                            logging.write_debug("End executing current task")
                            _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                            logging.write_result(enum.TEST_RESULT.SKIP, _duration, suite_name, case_id, _task_id)
                            register_status(tasks_result, _task_id, enum.TEST_RESULT.SKIP)
                            return
                        elif tasks_result[_miss_id] == enum.TEST_RESULT.PASS:
                            logging.write_error("Its referred task '%s' has already been executed successfully, but its " \
                                        "return value is not added to local variable list by weird issue" % _miss_id)
                            logging.write_debug("End executing current task")
                            _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                            logging.write_result(enum.TEST_RESULT.ERROR, _duration, suite_name, case_id, _task_id)
                            register_status(tasks_result, _task_id, enum.TEST_RESULT.ERROR)
                            return
                        else:
                            logging.write_debug("Its referred task '%s' is %s" % (_miss_id, tasks_result[_miss_id]))
                            logging.write_debug("End executing current task")
                            _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                            logging.write_result(enum.TEST_RESULT.SKIP, _duration, suite_name, case_id, _task_id)
                            register_status(tasks_result, _task_id, enum.TEST_RESULT.SKIP)
                            return
                    else:
                        logging.write_error("The local variable '%s' can not be found, you need to register it firstly." % _miss_id)
                        logging.write_debug("End executing current task")
                        _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                        logging.write_result(enum.TEST_RESULT.ERROR, _duration, suite_name, case_id, _task_id)
                        register_status(tasks_result, _task_id, enum.TEST_RESULT.ERROR)
                        return
        try:
            # execute task function
            logging.write_debug("Start to execute function '%s'" % _task_function_name)
            _result = taf_reflection.execute_function(_task_module_name, _task_class_name, _task_function_name, _task_params)

            if _task_exception is not None:
                _error_msg = "the expected error likes '%s' but actually there is no error thrown" % _task_exception
                logging.write_error("Current task executes failed, error message: %s" % _error_msg)
                logging.write_debug("End executing current task")
                _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                logging.write_result(enum.TEST_RESULT.FAIL, _duration, suite_name, case_id, _task_id)
                register_status(tasks_result, _task_id, enum.TEST_RESULT.FAIL)
            else:
                if _task_global_return_value != 0:
                    _key = "%s.%s" % (case_id, _task_id)
                    global_variable[_key] = _result
                    if local_variable.has_key(_key):
                        local_variable[_key] = _result  # replace with new value
                else:
                    local_variable[repr(_task_id)] = _result

                logging.write_debug("End executing current task")
                _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                logging.write_result(enum.TEST_RESULT.PASS, _duration, suite_name, case_id, _task_id)
                register_status(tasks_result, _task_id, enum.TEST_RESULT.PASS)
        except:
            _error_type, _error_msg, _traceback = sys.exc_info()
            if _task_exception is not None and _task_exception in unicode(_error_msg):
                logging.write_debug("Current task is a negative test, the expected error is '%s' and actual error is '%s'"
                                   % (_task_exception, unicode(_error_msg)))
                logging.write_debug("End executing current task")
                _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                logging.write_result(enum.TEST_RESULT.PASS, _duration, suite_name, case_id, _task_id)
                register_status(tasks_result, _task_id, enum.TEST_RESULT.PASS)
            else:
                logging.write_error("Current task executes failed, error message: %s" % unicode(_error_msg))
                logging.write_debug("End executing current task")
                _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
                logging.write_result(enum.TEST_RESULT.FAIL, _duration, suite_name, case_id, _task_id)
                register_status(tasks_result, _task_id, enum.TEST_RESULT.FAIL)
    except:
        _error_type, _error_msg, _traceback = sys.exc_info()
        logging.write_error("Current task executes failed by error: %s" % unicode(_error_msg))
        logging.write_debug("End executing current task")
        _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
        logging.write_result(enum.TEST_RESULT.ERROR, _duration, suite_name, case_id, _task_id)
        register_status(tasks_result, _task_id, enum.TEST_RESULT.ERROR)


def execute_case(file_path, global_variable, global_test_result, suite_name='NULL'):
    """
    Execute test case
    """
    print "Executing function 'execute_test_case' with file_path=%s, global_test_result=%s" \
          % (file_path, global_test_result)

    try:
        _start_time = datetime.now()

        _testFile = file(file_path)
        _testJson = json.load(_testFile, config.ENCODING)
        execute_prerequisites(_testJson, config.PREREQUISITES_CASE)  # check parameters: id, name, tasks
        _case_id = _testJson["id"]
        _case_name = _testJson["name"]
        _case_tasks = _testJson["tasks"]

        # get "notification" info
        _notify = False
        _generateReport = False
        parent = inspect.stack()[1][3]  # get current function name
        if parent == "<module>":  # ?
            _generateReport = True
            if _testJson.has_key(config.NOTIFICATION):
                _notification = _testJson[config.NOTIFICATION]
                execute_prerequisites(_notification, config.PREREQUISITES_NOTIFICATION)  # check parameters under "notification": notify, subject, ownerName, mailList
                _notify = _notification[config.NOTIFY]
                _subject = _notification[config.SUBJECT]
                _ownerName = _notification[config.OWNER_NAME]
                _mailList = _notification[config.MAIL_LIST]

        logging.__msg_flag = "%s-%s" % (suite_name, _case_id)  # set log flag
        logging.change_message_flag("%s-%s" % (suite_name, _case_id))
        logging.write_debug("Start to execute test case: %s - %s" % (_case_id, _case_name))
        register_status(global_test_result, _case_id)  # set test case status to "Ready"

        if _testJson.has_key("dependsOn") and not check_result(global_test_result, _testJson["dependsOn"]):
            logging.write_warn("Skip to execute current test case because its depended test case '%s' is not 'Pass'" % _testJson["dependsOn"])
            _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
            logging.write_result(enum.TEST_RESULT.SKIP, _duration, suite_name, _case_id)
            register_status(global_test_result, _case_id, enum.TEST_RESULT.SKIP)  # set test case status to "Skip"
            return

        _task_result = {}
        _local_variable = ((_testJson.has_key("params") and len(_testJson["params"]) > 0) and [_testJson["params"]] or [{}])[0]  # get the parameters under "params"

        # execute the tasks in current test case
        for _task in _case_tasks:
            execute_task(_task_result, global_variable, _local_variable, suite_name, _case_id, _task)

        # collect the task results
        _tasks_total = len(_case_tasks)
        _tasks_pass, _tasks_skip, _tasks_fail, _tasks_error = 0, 0, 0, 0
        for _key, _value in _task_result.items():
            if _value == enum.TEST_RESULT.PASS:
                _tasks_pass += 1
            elif _value == enum.TEST_RESULT.SKIP:
                _tasks_skip += 1
            elif _value == enum.TEST_RESULT.FAIL:
                _tasks_fail += 1
            elif _value == enum.TEST_RESULT.ERROR:
                _tasks_error += 1

        # output the test case result
        _duration = str(round((datetime.now() - _start_time).total_seconds(), 3))
        if _tasks_fail + _tasks_error > 0:
            logging.write_result(enum.TEST_RESULT.FAIL, _duration, suite_name, _case_id)
            register_status(global_test_result, _case_id, enum.TEST_RESULT.FAIL)
        elif _tasks_skip == _tasks_total:
            logging.write_result(enum.TEST_RESULT.SKIP, _duration, suite_name, _case_id)
            register_status(global_test_result, _case_id, enum.TEST_RESULT.SKIP)
        else:
            logging.write_result(enum.TEST_RESULT.PASS, _duration, suite_name, _case_id)
            register_status(global_test_result, _case_id, enum.TEST_RESULT.PASS)

        logging.__msg_flag = "%s-%s" % (suite_name, _case_id)  # set log flag
        logging.change_message_flag("%s-%s" % (suite_name, _case_id))
        logging.write_debug("End executing test case: %s - %s" % (_case_id, _case_name))
    except:
        _error_type, _error_msg, _traceback = sys.exc_info()
        logging.write_error("Current test case executes failed, error message: %s" % _error_msg)
    finally:
        if file is not None:
            _testFile.close()

        # generate report
        if _generateReport:
            _report_path = logging.generate_html_report(result_log_path=config.LOG_RESULT_PATH, detail_log_path=config.LOG_DETAIL_PATH)

            # send email
            if _notify:
                _body = config.MAIL_BODY_FORMAT % _ownerName
                taf_mail.send_mail(send_to=_mailList, subject=_subject, body=_body, attachments=_report_path)


def execute_suite(suite, global_variable, test_case_root_path):
    """
    Execute suite
    """
    print "Executing function 'execute_suite' with _suite = %s, test_case_root_path=%s" % (suite, test_case_root_path)

    try:
        _suite_result = {}
        _suite_name = suite[config.SUITE_NAME]
        _folder_path = suite[config.FOLDER_PATH]
        _execute_sequencer = suite[config.EXECUTE_SEQUENCER]

        logging.__msg_flag = _suite_name  # set log flag
        logging.change_message_flag(_suite_name)
        if suite.has_key("run") and suite["run"] == 0:
            logging.write_debug("Test suite '%s' do not run because the param 'run' is 0" % _suite_name)
            return

        _dir_path = test_case_root_path + _folder_path
        if not os.path.isdir(_dir_path):
            logging.write_error("Test suite '%s' cannot be run because the folder path '%s' is a invalid directory." % (_suite_name, _dir_path))
            return

        logging.write_debug("Start to execute suite: %s" % _suite_name)
        for _test_file in _execute_sequencer:
            _test_file_path = "%s/%s" % (test_case_root_path, _test_file)
            if not os.path.exists(_test_file_path):
                _test_file_path = "%s/%s" % (_dir_path, _test_file)
            if os.path.exists(_test_file_path):
                execute_case(_test_file_path, global_variable, _suite_result, _suite_name)
            else:
                logging.write_error("Test case path '%s' is invalid" % _test_file_path)
        logging.__msg_flag = _suite_name  # set log flag
        logging.change_message_flag(_suite_name)
        logging.write_debug("End executing suite: %s" % _suite_name)
    except:
        _error_type, _error_msg, _traceback = sys.exc_info()
        logging.write_error(_error_msg)


def execute_main_file(file_path):
    """
    Execute main json
    """
    
    print "Executing function 'execute_main_file' with filePath = %s" % file_path

    _mainFile = file(file_path)
    _mainJson = json.load(_mainFile, config.ENCODING)
    execute_prerequisites(_mainJson, config.PREREQUISITES_MAIN)

    # get "notification" info
    _notify = False
    if _mainJson.has_key(config.NOTIFICATION):
        _notification = _mainJson[config.NOTIFICATION]
        execute_prerequisites(_notification, config.PREREQUISITES_NOTIFICATION)  # check parameters under "notification": notify, subject, ownerName, mailList
        _notify = _notification[config.NOTIFY]
        _mailList = _notification[config.MAIL_LIST]
        _subject = _notification[config.SUBJECT]
        _ownerName = _notification[config.OWNER_NAME]

    try:
        _main_params = ((_mainJson.has_key("params") and len(_mainJson["params"]) > 0) and [_mainJson["params"]] or [{}])[0]
        _suite_list = _mainJson[config.SUITE_LIST]
        if len(_suite_list) == 0:
            logging.write_debug("No suite to execute")
            return
        elif len(_suite_list) == 1:
            _suite = _suite_list[0]
            execute_prerequisites(_suite, config.PREREQUISITES_SUITE)
            execute_suite(_suite, _main_params, config.TEST_CASE_ROOT_PATH)
        else:
            _execute_type = "parallel" if (_mainJson.has_key("params") and _mainJson["params"] == "parallel") else "serial"
            if _execute_type == "serial":  # serial
                for _suite in _suite_list:
                    execute_prerequisites(_suite, config.PREREQUISITES_SUITE)
                    execute_suite(_suite, _main_params, config.TEST_CASE_ROOT_PATH)
            else:  # parallel
                _threads = []
                for _suite in _suite_list:
                    execute_prerequisites(_suite, config.PREREQUISITES_SUITE)
                    _suite_name = _suite[config.SUITE_NAME]
                    _t = threading.Thread(target=execute_suite, args=(_suite, _main_params, config.TEST_CASE_ROOT_PATH), name=_suite_name)
                    # _t.SetDaemon(True)  # True, thread will be closed once the main thread is closed.
                    _threads.append(_t)

                # start threads
                for _s in _threads:
                    _s.start()

                # wait for threads to exit
                for _s in _threads:
                    _s.join()
    except:
        _error_type, _error_msg, _traceback = sys.exc_info()
        logging.write_error("Invoke function 'execute_main_file' failed, error message: %s" % _error_msg)
    finally:
        if file is not None:
            _mainFile.close()

        # generate report
        _results = logging.generate_html_report(result_log_path=config.LOG_RESULT_PATH, detail_log_path=config.LOG_DETAIL_PATH)
        _report_paths = []
        _summary = ""
        for _res in _results:
            for _key, _value in _res.items():
                _report_paths.append(_value["report_path"])
                _summary += "\n" + config.MAIL_SUMMARY_FORMAT % (_key, _value["total_cases"], _value["pass_cases"],
                                                          _value["skip_cases"], _value["fail_cases"], _value["durations"])
        # send email
        if _notify:
            _body = config.MAIL_BODY_FORMAT % (_ownerName, _summary)
            taf_mail.send_mail(send_to=_mailList, subject=_subject, body=_body, attachments=_report_paths)


if __name__ == '__main__':
    _test_json_path = ""
    _test_case_variable = {}
    _test_case_result = {}
    if len(sys.argv) > 1:
        _test_json_path = sys.argv[1]
    else:
        _test_json_path = config.DEFAULT_TEST_JSON_PATH

    print "The json path is %s" % _test_json_path
    if os.path.exists(_test_json_path):
        if os.path.isdir(_test_json_path):
            print "The json path is a directory"
            if taf_utility.have_file(_test_json_path, "main.json"):
                execute_main_file(_test_json_path + "/main.json")  # execute main json
            else:
                for _file in taf_utility.get_files(_test_json_path):
                    execute_case(_file, _test_case_variable, _test_case_result)  # execute test json
        else:
            _file_path, _file_name = os.path.split(_test_json_path)
            _name, _ext = os.path.splitext(_file_name)
            if _ext.lower() == ".json":
                print "The json path is a json file"
                if _name.lower() == "main":
                    execute_main_file(_test_json_path)  # execute main json
                else:
                    execute_case(_test_json_path, _test_case_variable, _test_case_result)  # execute test json
            else:
                raise Exception("The json path should be as a json file or directory")
    else:
        raise Exception("The json path does not exist!")
