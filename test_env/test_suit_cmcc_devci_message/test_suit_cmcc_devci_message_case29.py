'''
@author: wei,xiang

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *



class test_suit_cmcc_devci_message_case29(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    
    def test_case_main(self, case_results):
        global case_flag , TAG,case_flag_sim1,case_flag_sim2
        case_flag = False
        TAG = "Dev-ci cases: Messager "
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR],  self.name +' : case Start')
        log_test_framework(TAG, self.name + " -Start")
        
         

        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
#         if wait_for_fun(lambda:search_text("NEXT", searchFlag=TEXT_CONTAINS), True, 5) or wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
#             phone.permission_allow()
        if wait_for_fun(lambda:search_view_by_id("action_compose_new"), True, 5) or wait_for_fun(lambda:search_view_by_id("create"), True, 5):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Enter Message successfully")
            sleep(1)
        click_textview_by_text('139 1637 1096')
        sleep(5)
        click_imageview_by_desc('More options')
        if wait_for_fun(lambda:search_text("Delete thread"), True, 5):
            click_textview_by_text('Delete thread')
            sleep(3)
        click_button_by_id('button1')
        sleep(5)
        if search_text('139 1637 1096')==False:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Delete a thread successfully")
            case_flag=True                  
        elif search_text("Unfortunately"):
            if search_text("OK"):
                click_button_by_text("OK")
            take_screenshot()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs Crash")
            
        elif search_text("isn't responding"):
            if search_text("OK"):
                click_button_by_text("OK")
            take_screenshot()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs ANR")
            
        else:
            take_screenshot()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "case fail")
                        
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
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ': case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], TAG + ' : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + TAG + ' : \tfail')
            save_fail_log()
    