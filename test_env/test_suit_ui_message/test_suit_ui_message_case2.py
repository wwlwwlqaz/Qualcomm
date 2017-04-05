'''
@author: zhiyangz

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from tarfile import TUREAD


class test_suit_ui_message_case2(TestCaseBase):
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
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], 'ui_message_case2 : case Start')
        # enter_app_manual()

        global case_flag
        case_flag = False
        global case_flag_sms_draft
        case_flag_sms_draft = False
        
        start_activity('com.android.settings','.Settings')
        settings.set_default_sms(1)

        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        # click_imageview_by_id("home")
        local_assert(True, mms.go_home())
        
        # mms.delete_all_threads()
        send_num = SC.PUBLIC_CHINAMOBIE_TESTING_NUMBER
        # receive_num = self.format_phone_number(SC.PUBLIC_SLOT2_PHONE_NUMBER)
        sms_text = "ui automation test send sms"
        sms_text_add_draft = " edit this draft sms"
        
        click_imageview_by_desc('New message')
        click_textview_by_id("recipients_editor")
        ime.IME_input_number(1, send_num, "c")
        
        click_textview_by_text(mms.get_value("type_message"))
        ime.IME_input_english(1, sms_text)
        sleep(1)
        click_imageview_by_desc('Navigate up')
       
        # mms.click_home_icon()
        sleep(2)
        func1 = lambda:search_text('Draft', isScrollable=0, searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func1, True, 10):
            log_test_framework("ui_message_case2 -->", "cannot find Draft field")
            set_cannot_continue()
        else :
            log_test_framework("ui_message_case2 -->", "find Draft field")
        click_textview_by_text('Draft', searchFlag=TEXT_CONTAINS)
        sleep(2)
        
        click_textview_by_id('embedded_text_editor')
        ime.IME_input_english(1, sms_text_add_draft)
        """
        entertext_edittext_by_index(1, sms_text_add_draft)
        """
        # mms.click_home_icon()
        if not cmp(get_view_text_by_id(VIEW_EDIT_TEXT, 'embedded_text_editor'), sms_text):
            log_test_framework("ui_message_case2 -->", "Text in EditText have no changes")
            case_flag = False
        else:
            log_test_framework("ui_message_case2 -->", "Text in EditText have changes")
            case_flag = True
        click_imageview_by_desc('Navigate up')
            
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "", SEVERITY_HIGH)
        
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
               
        

    def test_case_end(self):
        '''
        record the case result

        '''
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case2 : end')
        if can_continue() and case_flag == True:
            # shutdown()
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case2 : case pass')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_message_case2 : \tpass')
        else:
            log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR], ' ui_message_case2 : case fail')
            print_report_line(self.case_config_map[fs_wrapper.CASE_NAME_ATTR] + ' ui_message_case2 : \tfail')
            save_fail_log()

    
