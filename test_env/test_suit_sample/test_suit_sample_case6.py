#coding=utf-8

#需要import的一些模块
from test_case_base import TestCaseBase
from logging_wrapper import *
from qrd_shared.case import *
from fs_wrapper import *
from case_utility import *
from qrd_shared.launcher.Launcher import Launcher

#本条case是多平台复用case的实例。
class test_suit_sample_case6(TestCaseBase):
    def test_case_main(self, case_results):
        #通用的code部分
        #launch app which u want
        launcher.launch_from_launcher('gallery')
        click_textview_by_desc(sample.get_value("switch_camera"),waitForView=1)
        #The new usage about the API get_value. You must add platform on values/string. You must write the phone software version or null
        print sample.get_value("choose_camera")
        #差异性code的部分
        #If you want to replace some code ,you can call the api to adapt the code on different version
        #调用下面api实现差异性替换，差异的文件在platform中，需要设定个默认的default。
        InvokeFuncByCurRunTarget(self,"test_suit_sample","test_suit_sample_adaptive","sample_code")