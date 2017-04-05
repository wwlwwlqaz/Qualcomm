'''
@author: wxiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_ui_phone_case2(TestCaseBase):
    '''
    test_suit_ui_contact_case1 is a class for add a new contact

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_phone_case2'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_phone_case2 : case Start')
                
        global case_flag
        case_flag = True
        call_result = []
        start_activity('com.android.settings', '.Settings')
        settings.set_default_voice(2)
        
        call_repeat_times = int(SC.PRIVATE_PHONE_CALL_REPEAT_TIMES)
        call_duration = float(SC.PRIVATE_PHONE_CALL_TIME)
        if (is_cdma()):
            phoneNumber = SC.PRIVATE_PHONE_CDMA_CALL_PHONENUMBER
        else:
            phoneNumber = SC.PRIVATE_PHONE_GSM_WCDMA_CALL_PHONENUMBER
        
        for i in range(0, call_repeat_times):
            sleep(3)
            try:
                log_test_framework(self.tag, 'Start to dial time :' + str(i+1))
                #start_activity("com.google.android.dialer", "com.android.dialer.DialtactsActivity")
                start_activity("com.android.dialer", "com.android.dialer.DialtactsActivity")
                phone.go_home()
                click_button_by_id("floating_action_button")
                phoneOn=phone.phone_call(phoneNumber, "", 2, call_duration)
                if phoneOn:call_result.append(1)
                else:call_result.append(0)
            except Exception as e:
                print e
                take_screenshot()
                set_cannot_continue()
        
        for j in call_result:
            log_test_framework(self.tag, 'search call result array :' + str(j))
            if j == 0:
                case_flag =False
                break
            else:
                pass
            
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case2 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case2: case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case2 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case2: case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case2 : \tfail')
            save_fail_log()
