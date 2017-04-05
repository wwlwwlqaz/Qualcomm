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
import string


class test_suit_ui_message_case3(TestCaseBase):
    '''
    test_suit_ui_message_case02 is a class for deleting single SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_message_case3'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False
        
        start_activity('com.android.settings','.Settings')
        settings.set_default_sms(1)
        
        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        # pre_check()
        local_assert(True, mms.go_home())
        local_assert(True, mms.exist())
        
            
        if can_continue():
            # log_test_case(self.tag, 'start')
            # mms.click_home_icon()  
            mms.go_home()
            func1 = lambda:search_text('Draft', isScrollable=0, searchFlag=TEXT_CONTAINS)
            if not wait_for_fun(func1, True, 10):
                log_test_framework("ui_message_case2 -->", "cannot find Draft field")
                set_cannot_continue()
            else :
                log_test_framework("ui_message_case2 -->", "find Draft field")
                click_textview_by_text('Draft', searchFlag=TEXT_CONTAINS)
                click_imageview_by_id('send_button_sms')
            """
            click_textview_by_id('from')
            """
            # phoneNumber1 = get_view_text_by_id(VIEW_TEXT_VIEW,'action_bar_title')
            phoneNumber1 = get_view_text_by_index(VIEW_TEXT_VIEW, 0)
            log_test_case(self.tag, "case_flag(number1) = " + str(phoneNumber1))
            take_screenshot()
            click_textview_by_desc('Call', waitForView=1)
            
            # when there are 2 SIM in mobile phone
            if is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'dialButton1', isScrollable=0):
                click_imageview_by_id('dialButton1', waitForView=1)
            
            phoneNumber2 = get_view_text_by_id(VIEW_TEXT_VIEW, 'name')
            log_test_case(self.tag, "case_flag(number2) = " + str(phoneNumber2))
            sleep(2)
            func = lambda:((is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'elapsedTime')))
            if wait_for_fun(func, True, 10):
                elapsedTime = get_view_text_by_id(VIEW_TEXT_VIEW, 'elapsedTime', isScrollable=0)
            sleep(5)
             # this delay(5s) is to make call out successfully
            elapsedTime = get_view_text_by_id(VIEW_TEXT_VIEW, 'elapsedTime', isScrollable=0)
            
            # print 'elapsedTime:' + elapsedTime
            log_test_case(self.tag, "elapsedTime = " + str(elapsedTime))
            take_screenshot()
            click_imageview_by_desc('End')
            
            if (phoneNumber2 == phoneNumber1) and (cmp(elapsedTime, '00:00')):
                case_flag = True
        
        exit_cur_case(self.tag)
        
        log_test_case(self.tag, "case_flag = " + str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "take photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
            
            
