'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *


class test_suit_ui_dev_ci_case1(TestCaseBase):
    '''
    test_suit_ui_message_case1 is a class for browser website by wifi

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    

    def test_case_main(self, case_results):
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases "
        call_result = []
        
        if call("test_suit_ui_browser", "test_suit_ui_browser_case01"):
            call_result.append(1)
        else:call_result.append(0)
            
        if call("test_suit_ui_phone", "test_suit_ui_phone_case8"): 
            call_result.append(1)
        else:call_result.append(0)
        
        if call("test_suit_ui_contact", "test_suit_ui_contact_case6"):
            call_result.append(1)
        else:call_result.append(0)
        
        if call("test_suit_ui_contact", "test_suit_ui_contact_case5"):
            call_result.append(1)
        else:call_result.append(0)
    
        if call("test_suit_ui_contact", "test_suit_ui_contact_case4"):
            call_result.append(1)
        else:call_result.append(0)
        
        if call("test_suit_ui_message", "test_suit_ui_message_case4"):
            call_result.append(1)
        else:call_result.append(0)
    
        if call("test_suit_ui_message", "test_suit_ui_message_case3"):
            call_result.append(1)
        else:call_result.append(0)
        
        if call("test_suit_ui_message", "test_suit_ui_message_case6"):
            call_result.append(1)
        else:call_result.append(0)
        
        
        
        # get the whole cases result
        for j in call_result:
            log_test_framework(TAG, 'search call result array :' + str(j))
            if j == 0:
                case_flag =False
                #break
                continue
            else:
                pass
        
    """
    def test_case_end(self):
        '''
        record the case result

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
    """