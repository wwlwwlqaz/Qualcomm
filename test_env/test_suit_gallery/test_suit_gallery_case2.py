#coding=utf-8

import settings.common as SC
from test_case_base import TestCaseBase
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *
import fs_wrapper
from case_utility import *
import settings.common as SC
from utility_wrapper import *


class test_suit_gallery_case2(TestCaseBase):
    def test_case_main(self, case_results):
        '''same code'''
        '''The old usage about the API get_value'''
        click_textview_by_desc(gallery.get_value("switch_camera"),waitForView=1)
        '''The new usage about the API getValByCurRunTarget. You must add platform on values/string. You must write the phone software version or null.'''
        print gallery.getValByCurRunTarget("choose_camera")
        '''diff code'''
        ''''sample'''
        '''If you want to replace some code ,you can call the api to adapt the code on different version'''
        InvokeFuncByCurRunTarget(self,"test_suit_gallery","test_suit_gallery_case2_adaptive","diff_code")