#coding=utf-8

#需要import的一些模块
from test_case_base import TestCaseBase
from logging_wrapper import *
from qrd_shared.case import *
from fs_wrapper import *
from case_utility import *
from qrd_shared.launcher.Launcher import Launcher

#本条case是测试从gallery里面打开camera并拍照。主要是给大家看个一般case编写的模版。
class test_suit_sample_case1(TestCaseBase):
    def test_case_main(self, case_results):
        #launch app which u want
        #这里的gallery需要在qrd_shared/launcher中的res中添加需要打开的app name，这样才能利用下个方法调用。
        launcher.launch_from_launcher('gallery')
        #Open camera
        click_textview_by_desc(sample.get_value("switch_camera"),waitForView=1)
        sleep(1)
        #Choose camera
        if search_text(sample.get_value("choose_camera")):
            click_textview_by_text(sample.get_value("choose_camera"), waitForView=1)
            sleep(1)
            click_textview_by_text(sample.get_value("just_once"), waitForView=1)
            sleep(1)
        else:
            sleep(1)
        #take photo
        click_imageview_by_desc(sample.get_value("Shutter_button"), waitForView=1)
        #tell us case success
        #最后建议大家加上下面一句log，会在report中显示这条case正常跑完。如果想得到case失败的提示可以将下面的第一个参数STATUS_SUCCESS改为STATUS_FAILED。
        qsst_log_case_status(STATUS_SUCCESS, 'gallery test success',SEVERITY_HIGH)
