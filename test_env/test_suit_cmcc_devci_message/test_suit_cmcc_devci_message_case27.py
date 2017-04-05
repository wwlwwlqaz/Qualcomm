'''
@author: wei,xiang

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *



class test_suit_cmcc_devci_message_case27(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    
    def test_case_main(self, case_results):
        global case_flag , TAG,case_flag_sim1,case_flag_sim2
        case_flag = False
        TAG = "Dev-ci cases: Messager "
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR],  self.name +' : case Start')
        log_test_framework(TAG, self.name + " -Start")
        
         
        
        wakeUpDevice()
        settings.kill_allpid()
        
        start_activity('com.android.settings','.Settings')
        sleep(1)
        settings.set_default_sms(2)
        
        

        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        sleep(10)
        phone.permission_allow()
        if search_view_by_id("action_compose_new") or search_view_by_id("create"):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Enter Message successfully")
            sleep(1)
            if search_view_by_id('create'):
                click_button_by_id('create')
                sleep(5)
            if  search_view_by_id('action_compose_new'):
                click_button_by_id('action_compose_new') 
                sleep(5)
            mms.add_recipient('13916371096')
            sleep(3)
            take_screenshot()
            sleep(3)
            mms.add_picture()
            sleep(5)
            if search_view_by_id('send_button_mms'):
                click_imageview_by_id('send_button_mms')
                sleep(120)
                if wait_for_fun(lambda:search_text('Sent'), True, 120):
                    log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Send mms from SIM2 successfully")
                    case_flag=True
                else:
                    log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Send mms from SIM2 failed")
                    take_screenshot()                   
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
    