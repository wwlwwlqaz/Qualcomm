#coding=utf-8
'''
   enter the address


   @author: U{c_huangl<c_huangl@qti.qualcomm.com>}
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
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log,print_report_line
from test_case_base import TestCaseBase
import test_suit_browser
from qrd_shared.case import *
from test_suit_browser_case1 import enter_app_manual
############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    enter the address
#precondition:
#    N/A
#steps:
#    1. Click on MENU
#    2. Click Browser
#    3. Input Address
############################################

class test_suit_browser_case3(TestCaseBase):
    '''
    test_suit_browser_case3 is a class for browser case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        enter_app_manual()

        #check possible interrupted info
        browser.pre_check()

        browser.access_browser(SC.PRIVATE_BROWSER_ADDRESS_URL, SC.PRIVATE_BROWSER_WEB_TITLE, SC.PRIVATE_BROWSER_WAIT_TIME, False)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
