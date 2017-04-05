#coding=utf-8
'''
   Browse the Web by slot 1's data call


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

############################################
#author:
#    c_huangl@qti.qualcomm.com
#function:
#    Browse the Web by slot 1's data call
#precondition:
#    exist slot 1 and slot 1 has signal
#steps:
#    disable wifi
#    switch data call to slot1
#    clear the browser cache
#    addressing config web address
#    make sure whether access successful
############################################

class test_suit_browser_case1(TestCaseBase):
    '''
    test_suit_browser_case1 is a class for browser case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''

        enter_app_manual()

        global case_flag
        case_flag = False

        #check possible interrupted info
        browser.pre_check()

        #turn off the wifi
        if  not test_suit_browser.BOOL_STK_WIFI_CHECK:
            start_activity('com.android.settings','.Settings')
            settings.disable_wifi()
            test_suit_browser.BOOL_STK_WIFI_CHECK = True

        if not is_cdma():
            #switch data call to slot 1
            start_activity('com.android.settings','.Settings')
            settings.set_default_data(1)
            goback()

        start_activity('com.android.browser','.BrowserActivity')

        case_flag = browser.access_browser(SC.PRIVATE_BROWSER_ADDRESS_URL, SC.PRIVATE_BROWSER_WEB_TITLE, SC.PRIVATE_BROWSER_WAIT_TIME)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))

    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'end')
        if can_continue() and case_flag == True:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] +'\tpass')

        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] +'\tfail')
            save_fail_log()

#manual start activity
def enter_app_manual():
    '''
    manual start activity

    '''
    waitActivity = lambda:get_activity_name().startswith("com.android.browser")
    if not wait_for_fun(waitActivity, True, 5):
        start_activity("com.android.browser",".BrowserActivity")
        sleep(3)