#coding=utf-8

#需要import的一些模块
from test_case_base import TestCaseBase
from logging_wrapper import *
from qrd_shared.case import *
from fs_wrapper import *
from case_utility import *
from qrd_shared.launcher.Launcher import Launcher

class test_suit_sample_case4(TestCaseBase):
    def test_case_main(self, case_results):
        #launch app which u want
        launcher.launch_from_launcher('gallery')
        #interactive test case
        #弹出一个对话框提示，只有ok选项并且会响铃震动30秒后自动消除。
        interact_with_user_by_single_btn("Title", "This is a test message.",wait_timeout=30)
        #弹出一个对话框提示，有["Very Good", "Good", "Bad"]选项并且会响铃震动30秒后自动消除，默认选择第一个。
        interact_with_user_by_multi_btn("Title", "message.", ["Very Good", "Good", "Bad"], "18918799781", "Come to operate.",wait_timeout=30,default_result=0)
        #弹出一个对话框提示，有["Very Good", "Good", "Bad", "Very Bad"]选项但会响铃震动，30秒后自动消除，默认选择第一个。
        interact_with_user_by_list("Title", "message.", ["Very Good", "Good", "Bad", "Very Bad"], "18918799781", "Come to operate.", enable_ring_shake=False, wait_timeout=30,default_result=0)
        #interval only used on phone .Can't debug.
        #休眠60秒
        goToSleepMode(60)
        qsst_log_case_status(STATUS_SUCCESS, 'interactive test success', SEVERITY_HIGH)
