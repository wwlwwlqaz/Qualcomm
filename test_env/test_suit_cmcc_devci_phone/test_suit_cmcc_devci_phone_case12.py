'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from qrd_shared.mms.Mms import *



class test_suit_cmcc_devci_phone_case12(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''

    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases: Phone "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """

        start_activity("com.android.dialer", "com.android.dialer.DialtactsActivity")
#         if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
#             phone.permission_allow()
        if wait_for_fun(lambda:search_view_by_desc("Speed dial"), True, 5):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Enter dialer successfully")
            if wait_for_fun(lambda:search_view_by_id('dialtacts_options_menu_button'), True, 3):
                click_button_by_id('dialtacts_options_menu_button')
                if wait_for_fun(lambda:search_text('Call History'), True, 5):
                    click_textview_by_text('Call History')
                    sleep(3)
                    click_imageview_by_desc("More options")
                    sleep(3)
                    click_textview_by_text('Clear call history')
                    sleep(3)
                    if search_view_by_id("selection_menu"):
                        click_button_by_id("selection_menu")
                        sleep(3)
                        click_textview_by_text("Select all")
                        sleep(5)
                        click_textview_by_text("CLEAR")
                        sleep(3)
                        click_button_by_text('OK')
                        sleep(5)
                    click_imageview_by_desc("More options")
                    sleep(3)
                    if search_text("Clear call history")==False:
                        case_flag = True
                    #if search_text('Your call log is empty') or search_text("Make a call") or search_view_by_id("emptyListViewMessage"):
                        #case_flag = True
                                                     
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
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Case fail")
            
        
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
            
