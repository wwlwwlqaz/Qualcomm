# -*- coding: utf-8 -*-  
'''
@author: U{huitingn<huitingn@qti.qualcomm.com>}

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
import re
from test_suit_ui_message import *


class test_suit_ui_message_case4(TestCaseBase):
    '''
    test_suit_ui_message_case01 is a class for deleting single SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_message_case4'
    def test_case_main(self, case_results):
        
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        global case_flag
        case_flag = False
        
        start_activity('com.android.settings','.Settings')
        settings.set_default_sms(1)
        
        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        # click_imageview_by_id("home")
        # pre_check()
        local_assert(True, mms.go_home())
        local_assert(True, mms.exist())
        if can_continue():
            mms.clear('draft')
            # mms.clear('error')
            
            mms.go_home()
            (num1, phoneNumber, left) = mms.number()
            log_test_case(self.tag, "num1 = " + str(num1))
            
            mms.go_home()
            click_textview_by_id('from')
            try:scroll_to_top()
            except:pass
            click_textview_by_id('text_view', clickType=LONG_CLICK)
            '''click_textview_by_text('Delete')
            click_button_by_text('Delete')'''
            click_textview_by_desc('Call', isScrollable=0)  # Why delete's description is 'Call'??
            click_button_by_text('OK', isScrollable=0)
            
            mms.go_home()
            num2 = mms.number(thread=phoneNumber)[0]
            log_test_case(self.tag, "num2 = " + str(num2))
            
            if num2 == (num1 - 1):case_flag = True
            
        
        exit_cur_case(self.tag)
        
        log_test_case(self.tag, "case_flag = " + str(case_flag))
        if case_flag:qsst_log_case_status(STATUS_SUCCESS, "success" , SEVERITY_HIGH)
        else:qsst_log_case_status(STATUS_FAILED, "fail", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
    
        
    def test_case_end(self):
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%s: end' % self.tag)
        if can_continue() and case_flag == True:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%s: case pass' % self.tag)
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '%s: \tpass' % self.tag)
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], '%s: case fail' % self.tag)
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + '%s: \tfail' % self.tag)
            save_fail_log()
            
