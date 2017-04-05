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
from test_suit_ui_customer_issue import *
from test.test_multiprocessing import get_value


class test_suit_ui_customer_issue_case01(TestCaseBase):
    '''
    test_suit_ui_customer_issue_case01 is a class for deleting single SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_customer_issue_case01'
    def test_case_main(self, case_results):
        
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False

        
        for i in range(10):
            print ' i = '+str(i)
            launcher.launch_from_launcher('mms')
            pre_check()
            
                
            if can_continue():
                #log_test_case(self.tag, 'start')
                
                mms.click_home_icon()
                click_textview_by_desc('New message',isScrollable=0)
                
                write_mms('send','13312345678')
                
                launcher.back_to_launcher()
        
        case_flag = True

        exit_cur_case(self.tag)
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "take photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
            
            