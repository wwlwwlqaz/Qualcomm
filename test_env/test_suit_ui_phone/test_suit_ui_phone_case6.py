'''
@author: wxiang
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *

class test_suit_ui_phone_case6(TestCaseBase):
    '''
    test_suit_ui_contact_case1 is a class for add a new contact

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_phone_case6'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_phone_case6 : case Start')
                
        global case_flag
        case_flag = False
        case_flag_add_speed_dail=False
        case_flag_dail_speed_dail=False

        start_activity('com.android.settings', '.Settings')
        settings.set_default_voice(1)
        
        want_to_add_speed_dail_number = "2"
        phoneNumber = SC.PUBLIC_CHINAMOBIE_TESTING_NUMBER
    
        start_activity("com.android.dialer", "com.android.dialer.DialtactsActivity")
        phone.go_home()
        case_flag_add_speed_dail=phone.speed_dial(phoneNumber,want_to_add_speed_dail_number)
        #start_activity("com.android.dialer", "com.android.dialer.DialtactsActivity")
        phone.go_home()
        click_button_by_id("floating_action_button")
        click_textview_by_text(want_to_add_speed_dail_number, isScrollable=0, searchFlag=TEXT_MATCHES,clickType=LONG_CLICK)
        sleep(float(SC.PRIVATE_PHONE_CALL_TIME))
        take_screenshot()
        func = lambda:((is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'elapsedTime')))
        if wait_for_fun(func, True, 10):
            elapsedTime = get_view_text_by_id(VIEW_TEXT_VIEW, 'elapsedTime', isScrollable=0)
        if search_view_by_id("floating_end_call_action_button") and (cmp(elapsedTime, '00:00')) :
            click_button_by_id("floating_end_call_action_button")
            case_flag_dail_speed_dail=True
        else:
            case_flag_dail_speed_dail=False
            
        case_flag= case_flag_dail_speed_dail & case_flag_add_speed_dail
            
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case6 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case6: case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case6 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_phone_case6: case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_phone_case6 : \tfail')
            save_fail_log()
