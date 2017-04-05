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

class test_suit_ui_contact_case2_1(TestCaseBase):
    '''
    test_suit_ui_contact_case2 is a class for add a new contact

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_contact_case2 : case Start')
                
        global case_flag
        case_flag = False
        
        # launch contact
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(1)
        contact.go_home()
        # click "All contacts" sheet to lock view
        click_textview_by_text(SC.PRIVATE_CONTACT_CONTACTS_OPTION, isScrollable=0)
        
        if search_text(SC.PRIVATE_CONTACT_NO_CONTACTS_1, isScrollable=0) :
            log_test_framework("ui_contact_case1 :", "No Contacts in it")
            pass
        else:
            log_test_framework("ui_contact_case1 :", "firstly delete exist contacts")
            #local_assert(True, contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM1, SC.PRIVATE_CONTACT_SIM2))
        """
        if search_text(SC.PRIVATE_CONTACT_PHONE) | search_text(SC.PRIVATE_CONTACT_SIM):
            log_test_framework("ui_contact_case2 :", "firstly delete exist contacts")
            local_assert(True, contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM))
        else:
            log_test_framework("ui_contact_case2 :", "cannot find contacts")
        """
        log_test_framework("ui_contact_case2 : ", "Now add new contact into sim1 ")
        case_flag = contact.add_contact_into_sim(SC.PRIVATE_CONTACT_SIM2, SC.PRIVATE_CONTACT_NUMBER,2)
               
        
#         sleep(2) 
#         log_test_framework("ui_contact_case2 : ", "finally delete all contacts")
#         start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
#         sleep(1)
#         contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM)
        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "add contact into sim1 failed ", SEVERITY_HIGH)
            
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
            

    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case2 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case2: case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case2 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case2: case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case2 : \tfail')
            save_fail_log()
