# coding=utf-8
'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from test_suit_cmcc_devci_browser import *
from urlparse import clear_cache

class test_suit_cmcc_devci_browser_case3(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    
    def test_case_main(self, case_results):
        global case_flag , TAG
        case_flag = False
        TAG = 'Dev-ci cases: Browser '
        log_test_framework(TAG, self.name + " -Start")



        start_activity("com.android.browser", "org.chromium.chrome.browser.ChromeTabbedActivity")
        if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 15):
            phone.permission_allow()
        if wait_for_fun(lambda:search_view_by_id('terms_accept'), True, 15):            
            click_button_by_id('terms_accept')
            if wait_for_fun(lambda:search_view_by_id('next_button'), True, 5):
                click_button_by_id('next_button')
                if wait_for_fun(lambda:search_view_by_id('next_button'), True, 5):
                    click_button_by_id('next_button')
                    if wait_for_fun(lambda:search_view_by_id('next_button'), True, 5):
                        click_button_by_id('next_button')                           
        if wait_for_fun(lambda:search_view_by_id('more_browser_settings'), True, 5) or search_view_by_id('menu_button'):
            log_test_framework("cmcc_devci_browser_case3:", "Launch browser pass")
            if search_view_by_id('url'):
                click_textview_by_id('url')
                sleep(3)
                send_key(KEY_DEL)
                entertext_edittext_by_id('url','http://www.baidu.com')
                sleep(5)
                send_key(KEY_ENTER)
                sleep(3)
                if wait_for_fun(lambda:search_text("百度"), True, 180):
                    log_test_framework("cmcc_devci_browser_case3:", "OPen baidu pass")
                    case_flag = True
            else:
                click_textview_by_id('url_bar')
                sleep(3)
                send_key(KEY_DEL)
                entertext_edittext_by_id('url_bar','http://www.baidu.com')
                sleep(5)
                send_key(KEY_ENTER)
                sleep(3)
                if wait_for_fun(lambda:search_text("百度"), True, 180):
                    log_test_framework("cmcc_devci_browser_case3:", "OPen baidu pass")
                    case_flag = True
        elif search_text('has stopped'):
            log_test_framework("cmcc_devci_browser_case3:", "Popup has stopped")
            take_screenshot()
            click_textview_by_text('OK')
            sleep(2)
        else:
            log_test_framework("cmcc_devci_browser_case3:", "OPen baidu fail")
            take_screenshot()       
        
        send_key(KEY_BACK)
        sleep(1)
        send_key(KEY_BACK)
        sleep(1)
        if search_text('QUIT'):
            click_textview_by_text('QUIT')
            sleep(2)
        send_key(KEY_HOME)
        sleep(1) 
          
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "", SEVERITY_HIGH)
        
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))            
    
    def test_case_end(self):
        '''
        record the case result
        '''
        '''
        @attention: modify by min.sheng
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ': case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tfail')
            save_fail_log()
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case1 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case1: case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case1 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case1: case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case1 : \tfail')
            save_fail_log()
        '''

    