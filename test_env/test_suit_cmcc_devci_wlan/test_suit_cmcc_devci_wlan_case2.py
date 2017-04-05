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
from test_suit_cmcc_devci_wlan import *
from urlparse import clear_cache

class test_suit_cmcc_devci_wlan_case2(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    
    def test_case_main(self, case_results):
        global case_flag , TAG
        case_flag = False
        TAG = 'Dev-ci cases: WLAN '
        log_test_framework(TAG, self.name + " -Start")

        start_activity('com.android.settings','com.android.settings.Settings')
        if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
            phone.permission_allow()      
        if search_text('WLAN'):
            click_textview_by_text('WLAN')
            if wait_for_fun(lambda:search_view_by_id("switch_widget"), True, 5):
                click_button_by_id('switch_widget')
            if wait_for_fun(lambda:search_text('Hydra'), True, 30):
                click_textview_by_text('Hydra')
                sleep(3)
                entertext_edittext_by_id('password','K5x48Vz3')
                sleep(5)
                send_key(KEY_BACK)
                sleep(2)
                click_button_by_text("CONNECT")
                if wait_for_fun(lambda:search_text('Connected'), True, 60):
                    log_test_framework("cmcc_devci_browser_case2:", "Connect wlan pass")
                    case_flag = True
        elif search_text("has stopped", isScrollable=0):
            log_test_framework("cmcc_devci_bt_case1:", "Popup has stopped")
            take_screenshot()
            click_textview_by_text('OK')
            sleep(2)        
        else:
            log_test_framework("cmcc_devci_browser_case2:", "Connect wlan fail") 
            take_screenshot()     
        

        click_button_by_id('switch_widget')
        sleep(3)
        send_key(KEY_BACK)
        sleep(1)
        send_key(KEY_BACK)
        sleep(1)
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

    