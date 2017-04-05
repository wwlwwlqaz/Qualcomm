'''
@author: li,yazhou
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from test_suit_cmcc_devci_contact import *

class test_suit_cmcc_devci_contact_case31(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    def test_case_main(self, case_results):
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases: Contact "
        log_test_framework(self.name, " -Start")
        
        
        """
        cases contnets you need to add
        """
        
        # launch contact     

           
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
            phone.permission_allow()
        if wait_for_fun(lambda:search_text("Contacts", searchFlag=TEXT_CONTAINS), True, 5) or search_text("All contacts") or search_text("ADD NEW ACCOUNT"):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Enter contact successfully")
            sleep(3)
        contact.add_contact_to_phone("y","10086")
        contact.add_contact_to_family_group()             
        if wait_for_fun(lambda:search_text("No people in this group", searchFlag=TEXT_CONTAINS), False, 10):
            log_test_case("concatct31", "case pass")
            case_flag = True                 
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
        sleep(2)
        click_textview_by_text("ALL")
        sleep(2)
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
    
