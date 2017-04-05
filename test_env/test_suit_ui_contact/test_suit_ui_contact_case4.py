'''
@author: wxiang
@version: zhiyangz

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *


class test_suit_ui_contact_case4(TestCaseBase):
    '''
    test_suit_ui_contact_case1 is a class for add a new contact

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_contact_case4  : case Start')
        # enter_app_manual()
        global case_flag
        case_flag = False
        
              
        waitActivity = lambda:get_activity_name().startswith("com.android.contacts")
        if not wait_for_fun(waitActivity, True, 5):
            start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(1)
        contact.go_home()
        
         # click "All contacts" sheet to lock view
        click_textview_by_text(SC.PRIVATE_CONTACT_CONTACTS_OPTION, isScrollable=0)
        
        if search_text(SC.PRIVATE_CONTACT_PHONE) | search_text(SC.PRIVATE_CONTACT_SIM1) | search_text(SC.PRIVATE_CONTACT_SIM2):
            log_test_framework("ui_contact_case4", "found exist phone contact")
            local_assert(True, contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM1, SC.PRIVATE_CONTACT_SIM2))
        else:
            log_test_framework("ui_contact_case4 :", "cannot found phone contact. Add new contact into phone")
        scroll_to_top()
        click_imageview_by_desc('add new contact')
        contact.add_contact_into_phone(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_NUMBER)
        log_test_framework("ui_contact_case4 :", "Start to share it via mms")
        sleep(1)
        
        case_flag = contact.share_contact_mms(SC.PRIVATE_CONTACT_PHONE)
        goback()
               
#         sleep(1)
#         log_test_framework("ui_contact_case4 : ", "finally delete all contacts")
#         start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
#         sleep(1)
#         contact.clear_contact()
        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "", SEVERITY_HIGH)
            
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        
            

    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case4  : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case4  : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case4  : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case4  : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case4  : \tfail')
            save_fail_log()
