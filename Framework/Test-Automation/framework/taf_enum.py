"""
Created on Jul 20, 2015

@author: Hanchen Lin
"""


class Enum:
    def __init__(self, dic):
        for key, value in dic.items():
            setattr(self, key, value)


# TEST_RESULT = Enum({"PASS":"PASS","FAILED":"FAILED","PENDING":"PENDING","SKIPPED":"SKIPPED","READY":"READY"})

class TestResult:
    PASS = "Pass"
    FAIL = "Fail"
    PENDING = "Pending"
    SKIP = "Skip"
    READY = "Ready"
    ERROR = "Error"

TEST_RESULT = TestResult()
