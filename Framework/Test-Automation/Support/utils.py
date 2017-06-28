# coding: utf-8

import os
import sys
import time
import locale
import random
import shutil
import zipfile
import subprocess


VALID_STRING = r'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_beebank自动化测试()"",:@!'
INVALID_STRING = r'<>/?'


def generate_random_string(min_len=1, max_len=10, invalid_character=False, excluded_characters='', head_string='', tail_string=''):
    """
    Generate a random string with some specific options for testing.
    :param min_len: the minimal length of the string
    :param max_len: the max length of the string
    :param invalid_character: whether the generated string must have invalid character or not,
        invalid characters are defined by constant INVALID_STRING
    :param excluded_characters: the generated string must have not characters defined here
    :param head_string: the generated string must start with head_string; head_string takes certain length
    :param tail_string: the generated string must end with tail_string; tail_string takes certain length
    :return type: string
    :example1:
        generate_random_string(5,40)
        f98化8kg1RlNBtoZfZVGVk动KsE试
    :example2:
        generate_random_string(1, 20, True, head_string="test_text_", tail_string="-不要删")
        test_text_>0tIMP-不要删
    """

    prefix_length = len(head_string + tail_string)
    if max_len <= prefix_length:
        return (head_string + tail_string)[:max_len]

    max_len -= prefix_length
    min_len -= prefix_length

    if min_len > max_len:
        min_len, max_len = max_len, min_len

    valid_string, invalid_string, random_string = VALID_STRING, INVALID_STRING, ''

    random.seed(int(str(time.time()).split('.')[0]))

    character_pool_tuple = tuple(valid_string)
    if invalid_character:
        character_pool_tuple += tuple(invalid_string)

    while 1:
        for _ in range(random.randint(max(min_len, 0), max_len)):
            random_string += random.choice(character_pool_tuple)
        if not invalid_character:
            break
        else:
            try:
                for invalid in invalid_string:
                    if invalid in random_string:
                        assert 1 != 1
                random_string = ''
            except AssertionError:
                break

    for character_excluded in list(excluded_characters):
        random_string = random_string.replace(character_excluded, '')

    return head_string + random_string + tail_string


def zip_dir(dir_path, zip_file_path):
    """
    Zip directory
    """
    _file_list = []
    if os.path.isfile(dir_path):
        _file_list.append(dir_path)
    else:
        for _root, _dirs, _files in os.walk(dir_path):
            for _name in _files:
                _file_list.append(os.path.join(_root, _name))

    _zip_file = zipfile.ZipFile(zip_file_path, "w", zipfile.zlib.DEFLATED)
    for _tar in _file_list:
        _arc_name = _tar[len(dir_path):]
        _zip_file.write(_tar, _arc_name)
    _zip_file.close()


def unzip_file(zip_file_path, unzip_to_dir):
    """
    Unzip file
    """
    if not os.path.exists(unzip_to_dir):
        os.mkdir(unzip_to_dir, 0777)

    _zip_file = zipfile.ZipFile(zip_file_path)
    for _name in _zip_file.namelist():
        _name = _name.replace('\\','/')
        if _name.endswith('/'):
            p = os.path.join(unzip_to_dir, _name[:-1])
            if os.path.exists(p):
                # 如果文件夹存在，则删除之，避免有新更新无法复制
                shutil.rmtree(p)
            os.mkdir(p)
        else:
            _ext_file = os.path.join(unzip_to_dir, _name)
            _ext_dir = os.path.dirname(_ext_file)
            if not os.path.exists(_ext_dir):
                os.mkdir(_ext_dir, 0777)
            _out_file = open(_ext_file, 'wb')
            _out_file.write(_zip_file.read(_name))
            _out_file.close()


def _ping_windows(target_ip, num=4, length=64, timeout=1000):
    """
    Ping the target and return a list of successful result times in milliseconds
    """
    cmd = "ping %s -n %d -l %d -w %d" % (target_ip, num, length, timeout)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p.wait()

    res = p.stdout.readlines()

    # handle 中文操作系统
    local_language_and_coding = locale.getdefaultlocale()
    if local_language_and_coding[0] == 'zh_CN':
        res = [x for x in res if x.decode(local_language_and_coding[1]).encode('UTF-8').startswith('来自')]
        res = [x.split(' ') for x in res]
        res = [[t for t in x if t.decode(local_language_and_coding[1]).encode('UTF-8').startswith('时间')][0] for x in res]
    else:
        res = [x.split(' ') for x in res if x.startswith('Reply from')]
        res = [[t for t in x if t.startswith('time')][0] for x in res]

    # normalize "<1ms" result to be same as "=1ms"
    res = [x.replace('<','=') for x in res]
    res = [int(x.split('=')[1].replace('ms','')) for x in res]

    return res


def _ping_linux(target_ip, num=4, length=64):
    """
    Ping the target and return a list of successful result times in milliseconds
    """
    cmd = "ping %s -i 0.2 -c %d -s %d -W 5" % (target_ip, num, length)
    p = os.popen(cmd, 'r')

    res = p.readlines()

    # extract time from ping results
    res = [x.split(' ') for x in res if 'bytes from' in x]
    res = [[t for t in x if t.startswith('time')][0] for x in res]

    # normalize "<1ms" result to be same as "=1ms"
    res = [x.replace('<','=') for x in res]
    res = [float(x.split('=')[1].replace('ms','')) for x in res]

    return res


def ping(target_ip, num=4, length=64, timeout=1000):
    """
    Ping destination and return reply time, worked on windows(CN, EN) and linux(EN) systems.
    :param target_ip: the ip address try to ping
    :param num: how many ping packet sent
    :param length: how long is of each packet
    :param timeout: threshold (ms) you can set, those feedback packets bigger than threshold will be think as not reachable
    :return example:
        [1, 1, 2, 1]  # reachable and reply time are 1ms, 1ms, 2ms and 1ms
        []  # not reachable
    """
    if sys.platform == "win32":
        return _ping_windows(target_ip, num, length, timeout)
    else:
        return _ping_linux(target_ip, num, length)
