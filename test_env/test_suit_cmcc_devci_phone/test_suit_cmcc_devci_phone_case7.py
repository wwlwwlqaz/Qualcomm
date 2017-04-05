'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
import re



class test_suit_cmcc_devci_phone_case7(TestCaseBase):  
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    def test_case_main(self, case_results):       
        global case_flag ,case_flag_slot1,case_flag_slot2, TAG
        case_flag_slot1=False
        case_flag_slot2=False
        case_flag = False
        TAG = "Dev-ci cases: Phone "
        log_test_framework(TAG, self.name + " -Start")
        
        
        """
        
        cases contnets you need to add
        
        
        """
        settings.check_after_resetphone()
        start_activity('com.android.settings','.Settings')
        settings.set_default_voice(1)
        sleep(1)
        send_key(KEY_HOME)
        
        start_activity("com.android.phone", "com.android.phone.EmergencyDialer")
        sleep(3)
        phone.dial("911")
        sleep(3)
        if search_text('Emergency', searchFlag=TEXT_CONTAINS):
            case_flag_slot1=True 
            log_test_framework(TAG, "Dial emergency call from card 1 successfully ")
            click_button_by_id("floating_end_call_action_button")
            sleep(2)
         
        start_activity('com.android.settings','.Settings')
        settings.set_default_voice(2)
        sleep(1)
        send_key(KEY_HOME)
        
        start_activity("com.android.phone", "com.android.phone.EmergencyDialer")  
        sleep(3)  
        phone.dial('911')
        sleep(3)
        if search_text('Emergency', searchFlag=TEXT_CONTAINS):
            case_flag_slot2=True 
            log_test_framework(TAG, "Dial emergency call from card 2 successfully ")
            click_button_by_id("floating_end_call_action_button")
            sleep(2)
    
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
        
        case_flag=case_flag_slot1 and case_flag_slot2
        
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
            
            
       # self.exe_command(self.adb_pipe,'kill -2 %s\n'%self.dog)
        #time.sleep(3)
       # os.system('adb pull /storage/sdcard0/Record.mp4 C:/1/1.mp4')
        #self.adb_pipe.kill()
