'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from test_suit_cmcc_devci_contact import *

class test_suit_cmcc_devci_contact_case1(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    def test_case_main(self, case_results):
        global case_flag , TAG, case_flag_special_name, case_flag_empty_name
        case_flag = False
        case_flag_special_name = False
        case_flag_empty_name = False
        TAG = "Dev-ci cases: Contact "
        log_test_framework(self.name, " -Start")
        
        
        """
        cases contnets you need to add
        """
        
        settings.check_after_resetphone()
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(5)
        phone.permission_allow()
        contact.add_contact_to_phone("testui@#$%+","18721469139")
        sleep(3)
        if search_text("testui@#$%+", searchFlag=TEXT_CONTAINS):
            log_test_framework(self.name, "Add special name contact with some punctuation success. Find in the phone")
            case_flag_special_name = True
        contact.add_contact_to_phone(" ","19721469139")
        sleep(3)
        if search_text("19721 469 139", searchFlag=TEXT_CONTAINS):
            log_test_framework(self.name, "Add blank name contact success. Find in the phone")
            case_flag_empty_name = True


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
        sleep(3)
        send_key(KEY_BACK)
        sleep(3)
        send_key(KEY_HOME)
        sleep(3)


            
        case_flag = case_flag_special_name and case_flag_empty_name
        
        
        
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
    
