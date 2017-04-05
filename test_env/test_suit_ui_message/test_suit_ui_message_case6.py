# -*- coding: utf-8 -*-  
'''
@author: U{huitingn<huitingn@qti.qualcomm.com>}

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log,print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
import re
from test_suit_ui_message import *


class test_suit_ui_message_case6(TestCaseBase):
    '''
    test_suit_ui_message_case05 is a class to forward SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_message_case6'
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
        
        #pre_check()
        local_assert(True, mms.go_home())
        local_assert(True, mms.exist())
        forwardTo = SC.PUBLIC_SLOT1_PHONE_NUMBER
        forwardFrom = SC.PUBLIC_SLOT2_PHONE_NUMBER
            
        if can_continue():
            #log_test_case(self.tag, 'start')
            num1 = message_num_in_thread(thread=forwardTo)[0]
            log_test_case(self.tag, "num1 = "+str(num1))
            if num1==0:
                set_cannot_continue()
                print 'Should followed by noting'
            
        if can_continue():
            #content = forward_sms_in_thread(forwardTo,thread=forwardFrom)
            forward_sms_in_thread(forwardTo,thread=forwardFrom)
            #log_test_case(self.tag, 'content = %s'%content.decode('utf-8'))
            
        if can_continue():
            num2 = message_num_in_thread(thread=forwardTo)[0]
            log_test_case(self.tag, "num2 = "+str(num2))
            
        if can_continue():
            if num2 > num1:
                case_flag = True
        
        
        exit_cur_case(self.tag)
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "Forward sms is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
            
            
