'''
@author: zhiyangz
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *


class test_suit_ui_message_case1(TestCaseBase):
    '''
    test_suit_ui_message_case1 is a class for browser website by wifi

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    def format_phone_number(self, num):
        '''
        format phone number,for example:format "12345678901" to "123 4567 8901"

        @type num: string
        @param num: phone number that need format
        @return: a phone number which have formated
        '''
        s = self.insert(num, ' ', 3)
        return self.insert(s, ' ', 8)

    def insert(self, original, new, pos):
        '''
       insert a new string into a tuple.

        @type original: string
        @param original: original string
        @type new: string
        @param new: a string that need insert.
        @type pos: number
        @param pos: position that need insert.
        @return: a new string.
        '''
        return original[:pos] + new + original[pos:]

    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_message_case1 : case Start')
       
        global case_flag
        case_flag = False
        global case_flag_sms_send
        case_flag_sms_send = False
        global case_flag_sms_receive
        case_flag_sms_receive = False
        
        start_activity('com.android.settings','.Settings')
        settings.set_default_sms(1)
        
        # lunch Message
        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        # click_imageview_by_id("home")
        local_assert(True, mms.go_home())
        
        click_textview_by_text('All')
        sleep(1)
        click_textview_by_text('All')
        
        mms.delete_all_threads()
        
        send_num = SC.PUBLIC_SLOT2_PHONE_NUMBER
        receive_num = self.format_phone_number(SC.PUBLIC_SLOT1_PHONE_NUMBER)
        sms_text = "ui automation test send sms"
        
        click_imageview_by_desc('New message')
        click_textview_by_id("recipients_editor")
        ime.IME_input_number(1, send_num, "c")
        
        click_textview_by_text(mms.get_value("type_message"))
        ime.IME_input_english(1, sms_text)
        
        if search_view_by_id('send_button_sms'):
            click_imageview_by_id('send_button_sms')
        else:
            log_test_framework("ui_message_case1 :", "Please check sim state")
        
        func = lambda:search_text(mms.get_value("sent"), searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func, True, 10):
            case_flag_sms_send = False
            # mms.click_home_icon()
            set_cannot_continue()
            log_test_framework("ui_message_case1 :", "send SMS  failed")
        else:
            case_flag_sms_send = True
        # mms.click_home_icon()
        sleep(1)
        mms.go_home()
        
        func1 = lambda:search_text(receive_num, searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func1, True, 10):
            set_cannot_continue()
        
        click_textview_by_text(receive_num, searchFlag=TEXT_CONTAINS)
        if not search_text(mms.get_value("received"), searchFlag=TEXT_CONTAINS):
            case_flag_sms_receive = False
            # mms.click_home_icon()
            set_cannot_continue()
            log_test_framework("ui_message_case1 :", "Receive SMS failed")
        else:
            case_flag_sms_receive = True
       
        # mms.click_home_icon()
        case_flag = case_flag_sms_send & case_flag_sms_receive
        goback()
        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "case_flag_sms_receive: " + str(case_flag_sms_receive) + ", case_flag_sms_send: " + str(case_flag_sms_send), SEVERITY_HIGH)
            
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        
    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case1 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case1 : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_message_case1 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case1 : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_message_case1 : \tfail')
            save_fail_log()

    
