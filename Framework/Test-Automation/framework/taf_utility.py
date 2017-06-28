# coding: utf-8

import os
import codecs


def load_csv(file_path):
    _csv_list = []
    _file = codecs.open(file_path)

    try:
        _data = _file.read()
        if _data[:3] == codecs.BOM_UTF8:
            _data = _data[3:]
        _lines = _data.splitlines()
        _merge_line = ""
        _line_index = 0
        for i in range(len(_lines)):
            _merge_line += _lines[i] + "\n"
            if _merge_line.count('"') % 2 == 0:
                _column_list = []
                _columns = _merge_line.strip("\n").split(",")
                _merge_column = ""
                for _col in _columns:
                    _merge_column += _col + ","
                    if _merge_column.count('"') % 2 == 0:
                        _column_list.append(_merge_column.strip(",").strip('"'))
                        _merge_column = ""
                _csv_list.append(_column_list)
                # _csv_list[_line_index].append()
                _merge_line = ""
                _line_index += 1
        return _csv_list

    finally:
        if _file is not None:
            _file.close()


def get_files(directory, extension=".json"):
    """
    Get files from the directory
    :param directory: the directory
    :param extension: the file extension
    :return: the files
    """
    if not os.path.isdir(directory):
        raise Exception("The param 'directory' should be a directory")

    _file_list = []
    for _item in os.listdir(directory):
        _item_full_path = os.path.join(directory, _item)
        if os.path.isdir(_item_full_path):
            for _file in get_files(os.path.join(directory, _item), extension):
                _file_list.append(_file)
        else:
            _name, _extension = os.path.splitext(_item_full_path)
            if _extension.lower() == extension.lower():
                _file_list.append(_item_full_path)

    return _file_list


def have_file(directory, file_name, extension=".json"):
    """
    Check if the directory contains specified file
    :param directory: the directory
    :param file_name: the file name
    :param extension: the file extension
    :return: True or False
    """
    for _file in get_files(directory, extension):
        if os.path.split(_file)[1].lower() == file_name.lower():
            return True

    return False
