# coding: utf-8

import os
import sys
import json


def create_json_file(file_path, data):
    """
    Generate json file
    """
    _json_content = json.dumps(data, indent=4, ensure_ascii=False)
    _root_path = os.path.split(os.path.dirname(sys.argv[0]))[0]
    _file_path = "%s/%s" % (_root_path, file_path)
    with open(_file_path, 'w') as f:
        f.write(_json_content.encode('utf-8'))
