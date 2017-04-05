#coding=utf-8

#需要import的一些package
from test_case_base import TestCaseBase
from logging_wrapper import *
from fs_wrapper import *
from case_utility import *
from qrd_shared.launcher.Launcher import Launcher
#使用call方法必须import下面这个模块
from qrd_shared.case import *

#本条case是像大家介绍call方法的用于调用别的现成的case。
class test_suit_sample_case2(TestCaseBase):
    def test_case_main(self, case_results):
        #call方法第一个参数是你需要调用的case的suit名字，第二个参数是具体的case名字。
        call("test_suit_sample", "test_suit_sample_case1")
        qsst_log_case_status(STATUS_SUCCESS, 'call test success', SEVERITY_HIGH)