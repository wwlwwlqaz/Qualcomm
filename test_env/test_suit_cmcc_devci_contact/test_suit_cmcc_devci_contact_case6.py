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


class test_suit_cmcc_devci_contact_case6(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    def test_case_main(self, case_results):
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases: Contact "
        log_test_framework(TAG, self.name + " -Start")
        
        """
        cases contnets you need to add
        """
        settings.check_after_resetphone()
        start_activity('com.android.settings','.Settings')
        sleep(5)
        settings.set_default_sms(1)
        sleep(1)
        
        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        sleep(10)
        phone.permission_allow()
        mms.send_sms("13916371006", "13916371006")
        click_textview_by_id("text_view_buttom")
        sleep(3)
        click_textview_by_text("Add to Contact")
        sleep(15)
        click_textview_by_text("Create new contact")
        sleep(3)
        click_textview_by_id("menu_save")
        sleep(3)
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(5)
        phone.permission_allow()
        click_textview_by_text("All contacts")
        sleep(3)
        if search_text("13916371006",searchFlag=TEXT_CONTAINS):
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
    
