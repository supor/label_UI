# coding: utf-8

import requests


def send_post_requests(uri, data, headers):
    """
    :param uri:
    :param data:
    :param headers:
    :return:
    """

    r = requests.post(url=uri, json=data, headers=headers)
    _status = r.status_code
    _dict = r.json()
    _dict['code'] = _status
    return _dict


def send_get_requests(uri, params, headers):
    """

    :param uri:
    :param params:
    :param headers:
    :return:
    """

    r = requests.get(url=uri, params=params, headers=headers)
    _status = r.status_code
    _dict = r.json()
    _dict['code'] = _status
    return _dict


def send_put_requests(uri, data, headers):
    """
    :param uri:
    :param data:
    :param headers:
    :return:
    """

    r = requests.put(url=uri, json=data, headers=headers)
    _status = r.status_code
    _dict = r.json()
    _dict['code'] = _status
    return _dict


def send_delete_requests(uri, data, headers):
    """
    :param uri:
    :param data:
    :param headers:
    :return:
    """

    r = requests.delete(url=uri, json=data, headers=headers)
    _status = r.status_code
    _dict = r.json()
    _dict['code'] = _status
    return _dict