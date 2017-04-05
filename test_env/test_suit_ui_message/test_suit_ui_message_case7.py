# -*- coding: utf-8 -*-  
'''
@author: U{huitingn<huitingn@qti.qualcomm.com>}

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
import re
from test_suit_ui_message import *


class test_suit_ui_message_case7(TestCaseBase):
    '''
    test_suit_ui_message_case05 is a class to forward SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_message_case7 :'
    
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
        global case_flag, case_flag_mms_send, case_flag_mms_receive
        case_flag = False
        case_flag_mms_send = False
        case_flag_mms_receive = False
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], self.tag + ': case Start')
        
        start_activity('com.android.settings', '.Settings')
        settings.set_default_data(1)
        
        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        mms.go_home()
        
        # mms.delete_all_threads()
        receive_num = SC.PUBLIC_SLOT2_PHONE_NUMBER
        send_num = self.format_phone_number(SC.PUBLIC_SLOT1_PHONE_NUMBER)
        sms_text = "ui automation test send MMS Capture Picture"     
        click_imageview_by_desc('New message')
        click_textview_by_id("recipients_editor")
        ime.IME_input_number(1, receive_num, "c")
        click_textview_by_text(mms.get_value("type_message"))
        ime.IME_input_english(1, sms_text)
        
        # Add attachment
        click_imageview_by_desc(mms.get_value("attach"))
        click_textview_by_text(mms.get_value("capture_picture"))
        local_assert(True, camera.get_picture_by_camera())
        sleep(3)
        
        if search_view_by_id('send_button_mms'):
            click_imageview_by_id('send_button_mms')
        else:
            log_test_framework(self.tag, "Please check sim state")
        
        func = lambda:search_text(mms.get_value("sent"), searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func, True, 30):
            case_flag_mms_send = False
            set_cannot_continue()
            log_test_framework(self.tag , "Sent MMS with Capture Picture Failed.")
        else: 
            case_flag_mms_send = True
            log_test_framework(self.tag, "Sent MMS with Capture Picture Passed.")
            
        mms.go_home()
        
        func1 = lambda:search_text(send_num, searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func1, True, 20):
            set_cannot_continue()
        
        click_textview_by_text(send_num, searchFlag=TEXT_CONTAINS)
        if not search_text(mms.get_value("received"), searchFlag=TEXT_CONTAINS):
            case_flag_mms_receive = False
            set_cannot_continue()
            log_test_framework(self.tag , "Receive SMS failed")
        else:
            case_flag_mms_receive = True

       
        case_flag = case_flag_mms_send & case_flag_mms_receive
        
        log_test_case(self.tag, "case_flag = " + str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "Forward sms is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
            
    
    def test_case_end(self):
        '''
        record the case result
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], self.tag + ': end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], self.tag + ' : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + self.tag + ' : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], self.tag + ' : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + self.tag + ' : \tfail')
            save_fail_log()            
