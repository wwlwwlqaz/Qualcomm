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


class test_suit_ui_message_case5(TestCaseBase):
    '''
    test_suit_ui_message_case03 is a class for replying SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_message_case5'
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
        func = lambda:is_view_enabled_by_id(VIEW_TEXT_VIEW, 'unread_conv_count', isScrollable=0)
        if wait_for_fun(func,True,60,5) is True:
            unread_origianl = get_view_text_by_id(VIEW_TEXT_VIEW, 'unread_conv_count', isScrollable=0)
            log_test_case(self.tag, 'unread message count = '+unread_origianl)
        else:
            unread_origianl=0
            log_test_case(self.tag, 'unread message count = '+unread_origianl)
        
        (num1,phoneNumber1,left1) = message_num_in_thread(SC.PUBLIC_SLOT1_PHONE_NUMBER)
        log_test_case(self.tag, "num1 = "+str(num1))
          
        if can_continue():
            #log_test_case(self.tag, 'start')
            #mms.click_home_icon()
            #mms.go_home()
            (num2,phoneNumber2,left2) = message_num_in_thread(SC.PUBLIC_SLOT2_PHONE_NUMBER)
            log_test_case(self.tag, "num2 = "+str(num2))
            
            click_textview_by_text(left2)
            reply_sms()
            #mms.click_home_icon()
            mms.go_home()
            
            num2_now = message_num_in_thread(thread=phoneNumber2)[0]
            log_test_case(self.tag, "num2_now = "+str(num2_now))
                        
            if num2_now>num2 is False :
                log_test_case(self.tag, 'send msg is failed!')
                set_cannot_continue()
            else:
                log_test_case(self.tag, 'send msg is passed!')
        
        
        if can_continue():
            func = lambda:is_view_enabled_by_id(VIEW_TEXT_VIEW, 'unread_conv_count', isScrollable=0)
            if wait_for_fun(func,True,60,5) is True:
                unread_now = get_view_text_by_id(VIEW_TEXT_VIEW, 'unread_conv_count', isScrollable=0)
                log_test_case(self.tag, 'unread message count = '+unread_now)
                num1_now = message_num_in_thread(thread=phoneNumber1)[0]
                log_test_case(self.tag, "num1_now = "+str(num1_now))
                if (num1_now>num1) & (unread_now>=unread_origianl) is False :
                    log_test_case(self.tag, 'reply msg is failed!')
                    case_flag = False
                    set_cannot_continue()
                else:
                    log_test_case(self.tag, 'reply msg is passed!')
                    case_flag = True
            else:
                log_test_case(self.tag, "cannot receive the reply Msg")
                case_flag = False
            
            """
            unread = get_unread_number() 
            func = lambda:get_unread_number()==unread+1
            if wait_for_fun(func,True,60,5) is False:
                log_test_case(self.tag, 'receive msg is failed!') 
            else:
                case_flag = True
            """
        exit_cur_case(self.tag)
        
        log_test_case(self.tag, "case_flag = " + str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "take photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
            
            
