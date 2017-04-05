'''
@author: wxiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_ui_phone_case8(TestCaseBase):
    '''
    test_suit_ui_contact_case1 is a class for add a new contact

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_phone_case8'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_phone_case8 : case Start')
                
        global case_flag
        case_flag = False
        
        start_activity("com.android.dialer", "com.android.dialer.DialtactsActivity")
        phone.go_home()
        clear_flag=phone.clear_call_log()
        sleep(3)
        if clear_flag and (not search_text('10086')) and (search_text("Your call log is empty")):
            case_flag=True
            
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case8 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case8: case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case8 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case8: case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case8 : \tfail')
            save_fail_log()
