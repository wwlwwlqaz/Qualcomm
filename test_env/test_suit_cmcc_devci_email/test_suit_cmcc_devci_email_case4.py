'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from qrd_shared.gmail.Gmail import *



class test_suit_cmcc_devci_email_case4(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    '''
    "Procedure:
    Step1:Launch camera
    Step2:Check camera
    Verification: 
    ER1:phone number would display as URI
    ER2:DUT would go into Dialer"
    
    '''
    
    
    def test_case_main(self, case_results):
        
        global case_flag , TAG , i , case_flag_people , case_flag_subject
        case_flag_people = False
        case_flag_subject = False
        case_flag = False
        TAG = "Dev-ci cases: Email "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """           
        start_activity('com.android.email', 'com.android.email.activity.Welcome')
#         if wait_for_fun(lambda:search_view_by_id('permission_allow_button'), True, 5):
#             phone.permission_allow()
        if wait_for_fun(lambda:search_text('Inbox'), True, 5):
            log_test_framework("cmcc_devci_email_case4:", "Launch email account pass")
        click_textview_by_id('search')
        sleep(3)
        entertext_edittext_by_id("search_actionbar_query_text","cmcc")
        send_key(KEY_ENTER)
        if wait_for_fun(lambda:search_view_by_id("empty_text"), False, 120):
            log_test_framework("cmcc_devci_email_case4:", "Search email people pass")
            case_flag_people = True
        send_key(KEY_BACK)
        sleep(2)
        click_textview_by_id("search")
        sleep(2)
        entertext_edittext_by_id("search_actionbar_query_text", "hi")
        send_key(KEY_ENTER)               
        if wait_for_fun(lambda:search_view_by_id("empty_text"), False, 120):
            log_test_framework("cmcc_devci_email_case4:", "Search email subject pass")
            case_flag_subject = True
        case_flag=case_flag_people and case_flag_subject                
        if search_text('has stopped'):
            log_test_framework("cmcc_devci_email_case4:", "Popup has stopped")
            take_screenshot()
            click_textview_by_text('OK')
            sleep(2) 
        elif search_text("isn't responding"):
            if search_text("OK"):
                click_button_by_text("OK")
                take_screenshot()
                log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Occurs ANR")    
        else:
            log_test_framework("cmcc_devci_email_case4:", "Search email fail")
            take_screenshot()
        send_key(KEY_BACK)
        sleep(2)
        send_key(KEY_BACK)
        sleep(2)
        send_key(KEY_HOME)
        sleep(3) 
        
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
            
