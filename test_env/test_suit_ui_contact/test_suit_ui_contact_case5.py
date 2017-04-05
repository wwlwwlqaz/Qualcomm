'''
@author: wxiang

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *


class test_suit_ui_contact_case5(TestCaseBase):
    '''
    test_suit_ui_contact_case1 is a class for export/import contact

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_contact_case5 : case Start')
        # enter_app_manual()
        notificationBar.clear_all()
        
        global case_flag_export_to_sim 
        case_flag_export_to_sim = False
        global case_flag_export_to_storage
        case_flag_export_to_storage = False
        global case_flag
        case_flag = False
        
        
        d = { 'type1':'import_from_sim', 'type2':'import_from_storage', 'type3':'export_to_sim' , 'type4':'export_to_storage'} 
        
     
        
        # launch contact
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        contact.go_home()
        """
        waitActivity = lambda:get_activity_name().startswith("com.android.contacts")
        if not wait_for_fun(waitActivity, True, 5):
            start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(1)
        contact.go_home()
        """
        sleep(1)
          # click "All contacts" sheet to lock view
        click_textview_by_text(SC.PRIVATE_CONTACT_CONTACTS_OPTION, isScrollable=0)
        
        if search_text(SC.PRIVATE_CONTACT_PHONE) | search_text(SC.PRIVATE_CONTACT_SIM1) | search_text(SC.PRIVATE_CONTACT_SIM2):
            log_test_framework("ui_contact_case5 :", "found phone contact. Delete all")
            local_assert(True, contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM1, SC.PRIVATE_CONTACT_SIM2))
        else:
            log_test_framework("ui_contact_case5 :", "cannot find phone contact, Add new contact into phone")
        sleep(1)
        scroll_to_top()
        click_imageview_by_desc('add new contact')
        local_assert(True, contact.add_contact_into_phone(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_NUMBER))
        log_test_framework("ui_contact_case5 :", "Start to export / import contact operation")
        goback()
        
        sleep(2)
        case_flag_export_to_sim = contact.export_import_contact(d['type3'], SC.PRIVATE_CONTACT_PHONE) 
        
        sleep(2)
        case_flag_export_to_storage = contact.export_import_contact(d['type4'], SC.PRIVATE_CONTACT_PHONE) 
        
        case_flag = case_flag_export_to_sim & case_flag_export_to_storage 
        
        sleep(2)
        log_test_framework("ui_contact_case5 :", "finally delete all contacts")
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        contact.go_home()
        sleep(1)
        contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM1,SC.PRIVATE_CONTACT_SIM2)
        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "export_to_sim: " + str(case_flag_export_to_sim) + ", export_to_storage: " + str(case_flag_export_to_storage), SEVERITY_HIGH)
            
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
    
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case5 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case5 : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case5 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_contact_case5 : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_contact_case5 : \tfail')
            save_fail_log()
