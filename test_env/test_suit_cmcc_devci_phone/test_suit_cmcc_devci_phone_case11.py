'''
@author: wei,xiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from qrd_shared.mms.Mms import *



class test_suit_cmcc_devci_phone_case11(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''

    
    
    def test_case_main(self, case_results):
        
        
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases: Phone "
        log_test_framework(TAG, self.name+" -Start")
        
        """
        
        cases contents you need to add
        
        
        """
        wakeUpDevice()
        settings.kill_allpid()
        
        start_activity('com.android.settings','.Settings')
        sleep(1)
        settings.set_default_voice(2)
        

        start_activity("com.android.dialer", "com.android.dialer.DialtactsActivity")
        sleep(10)
        phone.permission_allow()
        if search_view_by_desc("Speed dial"):
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Enter dialer successfully")
      
        
            if search_view_by_desc("dial pad"):
                click_button_by_id("floating_action_button")
                sleep(3)
                if search_view_by_id("deleteButton"):
                    click_imageview_by_id("deleteButton", 1, 0, 0, LONG_CLICK)
                    sleep(5)
                    
                if phone.phone_call("10086", "",slot=1,call_duration=30):
                    case_flag = True
                    
                else:
                    log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], " MO call from SIM2 failed")

                                                     
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
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], "Case fail")
            
        
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
            
