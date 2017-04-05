'''
@author: wxiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_ui_phone_case7(TestCaseBase):
    '''
    test_suit_ui_contact_case1 is a class for add a new contact

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_phone_case7'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_phone_case7 : case Start')
                
        global case_flag
        case_flag = False
        start_activity('com.android.settings', '.Settings')
        settings.set_default_voice(1)
        
        call_duration = float(SC.PRIVATE_PHONE_CALL_TIME)
        if (is_cdma()):
            phoneNumber = SC.PRIVATE_PHONE_CDMA_CALL_PHONENUMBER
        else:
            phoneNumber = SC.PRIVATE_PHONE_GSM_WCDMA_CALL_PHONENUMBER
        
        start_activity("com.android.dialer", "com.android.dialer.DialtactsActivity")
        phone.go_home()
        click_button_by_id("floating_action_button")
        phone.dial(phoneNumber)
        func = lambda:((is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'elapsedTime')))
        if wait_for_fun(func, True, 10):
            elapsedTime = get_view_text_by_id(VIEW_TEXT_VIEW, 'elapsedTime', isScrollable=0)
            log_test_framework("ui_phone_case7 :", "elapsedTime : "+str(elapsedTime))
            send_key(KEYCODE_POWER)
        else:
            pass
        take_screenshot()
        sleep(call_duration)
        send_key(KEYCODE_POWER)
        take_screenshot()
        func = lambda:((is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'elapsedTime')))
        if wait_for_fun(func, True, 10):
            elapsedTime = get_view_text_by_id(VIEW_TEXT_VIEW, 'elapsedTime', isScrollable=0)
        if search_view_by_id("floating_end_call_action_button") and (cmp(elapsedTime, '00:00')) :
            click_button_by_id("floating_end_call_action_button")
            case_flag=True
        else:
            case_flag=False
            
            
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case7 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case7: case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case7 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case7: case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case7 : \tfail')
            save_fail_log()
