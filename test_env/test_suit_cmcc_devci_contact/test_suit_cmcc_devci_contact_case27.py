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

class test_suit_cmcc_devci_contact_case27(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    def test_case_main(self, case_results):
        global case_flag , TAG, case_flag_phone, case_flag_simcard
        case_flag = False
        TAG = "Dev-ci cases: Contact "
        log_test_framework(self.name, " -Start")
        
        
        """
        cases contnets you need to add
        """
        
        # launch contact     

           
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
#         if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
#             phone.permission_allow() 
        if wait_for_fun(lambda:search_text("Contacts", searchFlag=TEXT_CONTAINS), True, 5):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Enter contact successfully")
            sleep(3)
            
        contact.add_contact_to_phone("case","187")
        sleep(3)
        click_textview_by_text('case')
        if wait_for_fun(lambda:search_view_by_id("menu_star"), True, 10):
            click_textview_by_id('menu_star')
            sleep(2)
        send_key(KEY_BACK)
        if wait_for_fun(lambda:search_text("Favorites"), True, 5):
            click_textview_by_text('Favorites')
        if wait_for_fun(lambda:search_text("fa"), True, 5):
            log_test_framework(self.name, "Add contact to favorite successfully")
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
        
        click_textview_by_text('ALL')
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
    
