# coding: utf-8

import httplib
import json
import hashlib


def invoke_web_request(host, port, method, sub_url, headers, body=None):
    http_client = None
    try:
        if body is not None:
            jbody = json.dumps(body)  # 对数据进行JSON格式化编码
        else:
            jbody = None

        http_client = httplib.HTTPConnection(host, port, timeout=60)
        http_client.request(method, sub_url, jbody, headers)

        response = http_client.getresponse()
        print response.read()
        print response.status
        print response.reason
    except Exception, e:
        print "Invoke invoke_web_request failed, error message: %s" % e
    finally:
        if http_client:
            http_client.close()


if __name__ == '__main__':
    print "web..."

