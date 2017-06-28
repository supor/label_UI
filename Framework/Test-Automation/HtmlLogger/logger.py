# coding: utf-8

import os
import constants

from framework import taf_config as config


class Logger:
    def __init__(self):
        pass

    Content = ""
    LogPath = ""

    def load(self, log_path):
        """
        Load the log content from specified log file or log template file
        """
        print "Execution function 'load' with log_path=%s" % log_path

        self.LogPath = log_path
        _title = (os.path.basename(log_path)).split(".")[0]
        _file_to_load = log_path if os.path.exists(log_path) else config.HTML_REPORT_TEMPLATE
        self.Content = self.load_log_content(_file_to_load, "logger.load")
        self.Content = self.Content.replace(constants.TitleFormat, _title)

    def create_test_case_record(self, case_id, case_result, case_duration, case_log):
        """
        Append a new test case record
        """
        print "Executing function 'create_test_case_record' with case_id=%s, case_result=%s, case_duration=%s" % (case_id, case_result, case_duration)

        _tb_id = "tb_%s" % case_id
        _tr_id = "tr_%s" % case_id

        if case_result == "Pass":
            _result = constants.CssPass
        elif case_result == "Skip":
            _result = constants.CssSkip
        elif case_result == "Fail":
            _result = constants.CssFail

        # the test case record
        sb = ""
        sb += "\n" + "<tr>"
        sb += "\n" + "    <td style='font-weight: bold'><a style='margin-left: 44%' href='#' onclick=\"ShowSubLogs('" + _tb_id + "')\">(+)</a> case " + case_id + "</td>"
        sb += "\n" + "    <td style='text-align: center'>" + _result + "</td>"
        sb += "\n" + "    <td style='text-align: center'><a href='javascript:void(0)' onmousedown=\"ShowLogs('" + _tr_id + "')\">Link</a></td>"
        sb += "\n" + "    <td style='text-align: center'>" + case_duration + "</td>"
        sb += "\n" + "</tr>"

        # the test case log
        sb += "\n" + "<tr id='" + _tr_id + "' style='display: none'>"
        sb += "\n" + "    <td colspan='4' style='word-break: break-all'>" + case_log + "</td>"
        sb += "\n" + "</tr>"
        sb += "\n" + constants.SubTaskFormat
        sb += "\n" + constants.TaskFormat

        self.Content = self.Content.replace(constants.SubTaskFormat, "")
        self.Content = self.Content.replace(constants.TaskFormat, sb)
        self.write_log_file(self.LogPath, self.Content, "logger.create_test_case_record")

    def create_task_record(self, case_id, task_id, task_result, task_duration, task_log):
        """
        Append a new task record
        """
        print "Executing function 'create_task_record' with task_id=%s, task_result=%s, task_duration=%s" % (task_id, task_result, task_duration)

        _tb_id = "tb_%s_%s" % (case_id, task_id)
        _tr_id = "tr_%s_%s" % (case_id, task_id)

        if task_result == "Pass":
            _result = constants.CssPass
        elif task_result == "Skip":
            _result = constants.CssSkip
        elif task_result == "Fail":
            _result = constants.CssFail
        elif task_result == "Error":
            _result = constants.CssError

        # the task record
        sb = ""
        sb += "\n" + "<tr id='" + _tb_id + "' style='display: none'>"
        sb += "\n" + "    <td><span style='margin-left: 49%'>task " + task_id + "</span></td>"
        sb += "\n" + "    <td style='text-align: center'>" + _result + "</td>"
        sb += "\n" + "    <td style='text-align: center'><a href='javascript:void(0)' onmousedown=\"ShowLogs('" + _tr_id + "')\">Link</a></td>"
        sb += "\n" + "    <td style='text-align: center'>" + task_duration + "</td>"
        sb += "\n" + "</tr>"

        # the task log
        sb += "\n" + "<tr id='" + _tr_id + "' style='display: none'>"
        sb += "\n" + "    <td colspan='4' style='word-break: break-all'>" + task_log + "</td>"
        sb += "\n" + "</tr>"
        sb += "\n" + constants.SubTaskFormat

        self.Content = self.Content.replace(constants.SubTaskFormat, sb)
        self.write_log_file(self.LogPath, self.Content, "logger.create_task_record")

    def summary(self, total_count, pass_count, skip_count, fail_count, duration):
        """
        Sync the summary of test results
        """
        print "Executing function 'summary' with total_count=%s, pass_count=%s, skip_count=%s, fail_count=%s, " \
              "duration=%s" % (total_count, pass_count, skip_count, fail_count, duration)

        self.Content = self.Content.replace(constants.ExecutedFormat, str(total_count))
        self.Content = self.Content.replace(constants.PassedFormat, str(pass_count))
        self.Content = self.Content.replace(constants.SkippedFormat, str(skip_count))
        self.Content = self.Content.replace(constants.FailedFormat, str(fail_count))
        self.Content = self.Content.replace(constants.DurationFormat, duration)

        #self.Content = self.Content.replace(constants.SummaryFormat, constants.CssDisplay)
        self.Content = self.Content.replace(constants.SummaryFormat, str(total_count))
        self.write_log_file(self.LogPath, self.Content, "logger.summary")

    @staticmethod
    def load_log_content(file_to_load, function_name):
        """
        Load the log content
        """
        _timeout = 10
        _can_load = False
        _log_content = ""
        _error_message = ""
        while _timeout > 0:
            try:
                sr = open(file_to_load)
                try:
                    lines = sr.readlines()
                finally:
                    sr.close()
                for l in lines:
                    if len(l) > 0:
                        _log_content += l
                _can_load = True
                break
            except Exception, e:
                _timeout -= 1
                _error_message = constants.ErrorFomart % (function_name, e.message)
        if not _can_load:
            raise Exception(_error_message)

        return _log_content

    @staticmethod
    def write_log_file(log_path, log_content, function_name):
        """
        Write the log content to the log file
        """
        _timeout = 10
        _can_write = False
        _error_message = ""
        while _timeout > 0:
            try:
                sw = open(log_path, "w")
                sw.writelines(log_content)
                sw.close()
                _can_write = True
                break
            except Exception,ex:
                _timeout -=1
                _error_message = constants.ErrorFomart % (function_name, ex.message)
        if not _can_write:
            raise Exception(_error_message)