'''
   operate renren,doubanfm,weibo,gmail,email,reren share,weibo share.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{TestCaseBase <TestCaseBase>}
   @note:
   @attention:
   @bug:
   @warning:



'''
import fs_wrapper
from qrd_shared.case import *
from case_utility import *
from utility_wrapper import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase

class test_suit_scenario1_case2(TestCaseBase):
    '''
    test_suit_scenario1_case2 is a class for scenario1 case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        success = 0
        if call("test_suit_renren", "test_suit_renren_case1"):
            success += 1
        if call("test_suit_doubanfm", "test_suit_doubanfm_case1"):
            success += 1
        if call("test_suit_weibo", "test_suit_weibo_case1"):
            success += 1
        if call("test_suit_gmail", "test_suit_gmail_case3"):
            success += 1
        if call("test_suit_email", "test_suit_email_case5"):
            success += 1
        if call("test_suit_camera", "test_suit_camera_case7"):
            success += 1
        if call("test_suit_camera", "test_suit_camera_case8"):
            success += 1
        goback()
        sleep(1)
        notificationBar.clear_all()
        if success < 7:
            set_cannot_continue()
        sleep(1)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

