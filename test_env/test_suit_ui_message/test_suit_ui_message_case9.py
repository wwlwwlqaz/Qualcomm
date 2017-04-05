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


class test_suit_ui_message_case9(TestCaseBase):
    '''
    test_suit_ui_message_case05 is a class to forward SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_message_case9'
    
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
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_message_case9 : case Start')
       
        global case_flag
        case_flag = False
        global case_flag_sms_send
        case_flag_sms_send = False
        global case_flag_add_contact
        case_flag_add_contact = False
        
        num = SC.PUBLIC_SLOT2_PHONE_NUMBER
        name = "addFromSMS"
        search_num = self.format_phone_number(SC.PUBLIC_SLOT2_PHONE_NUMBER)
        sms_text = "ui automation test send sms"
                
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(1)
        contact.go_home()
        
        log_test_framework("ui_message_case9 :", "firstly delete exist contacts")
        local_assert(True, contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM1, SC.PRIVATE_CONTACT_SIM2))

        sleep(2)
        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        mms.go_home()
        #mms.delete_all_threads()
                   
        click_imageview_by_desc('New message')
        click_textview_by_id("recipients_editor")
        ime.IME_input_number(1, num, "c")
        
        click_textview_by_text(mms.get_value("type_message"))
        ime.IME_input_english(1, sms_text)
        
        if search_view_by_id('send_button_sms'):
            click_imageview_by_id('send_button_sms')
        else:
            log_test_framework("ui_message_case9 :", "Please check sim state")
        
        sleep(2)
        func = lambda:search_text(mms.get_value("sent"), searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func, True, 10):
            case_flag_sms_send = False
            mms.go_home()
            set_cannot_continue()
            log_test_framework("ui_message_case9 :", "send SMS failed")
        else:
            case_flag_sms_send = True
        mms.go_home()
               
        func1 = lambda:search_text(search_num, searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func1, True, 10):
            set_cannot_continue()
        
        click_textview_by_text(search_num, searchFlag=TEXT_CONTAINS)
        send_key(KEY_MENU)
        # ##
        if  search_text('Add to Contacts'):
            click_textview_by_text('Add to Contacts')
            click_textview_by_text('Create new contact')
            case_flag_add_contact = contact.add_contact_into_phone(name, num)
        else:
            case_flag_add_contact = False
            log_test_framework("ui_message_case9 :", "cannot find Add to People option")
              
       
        mms.go_home()
       
        case_flag = case_flag_add_contact & case_flag_sms_send
        
        start_activity("com.android.contacts", "com.android.contacts.activities.PeopleActivity")
        sleep(1)
        
        log_test_framework("ui_message_case9 :", "Delete contacts added")
        local_assert(True, contact.del_all_contact(SC.PRIVATE_CONTACT_PHONE, SC.PRIVATE_CONTACT_SIM1, SC.PRIVATE_CONTACT_SIM2))
        
        
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "case_flag_add_contact: " + str(case_flag_add_contact) + ", case_flag_sms_send: " + str(case_flag_sms_send), SEVERITY_HIGH)
        
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        
        
    def test_case_end(self):
        '''
        record the case result
        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case9 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case9 : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_message_case9 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case9 : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_message_case9 : \tfail')
            save_fail_log()      
            
