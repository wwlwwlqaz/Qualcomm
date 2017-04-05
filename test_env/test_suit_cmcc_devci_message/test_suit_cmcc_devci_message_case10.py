'''
@author: wei,xiang
modified by c_yazli
'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *



class test_suit_cmcc_devci_message_case10(TestCaseBase):
    '''

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    
    
    def test_case_main(self, case_results):
        
        global case_flag , TAG
        case_flag = False
        TAG = "Dev-ci cases: Messager "
        log_test_case(self.case_config_map[fs_wrapper.CASE_NAME_ATTR],  self.name +' : case Start')
        log_test_framework(TAG, self.name + " -Start")
        
        
        settings.kill_allpid()
        start_activity('com.android.settings','.Settings')
        settings.set_default_sms(1)
        start_activity("com.android.mms", "com.android.mms.ui.ConversationList")
        sleep(1)
        
        mms.go_home()
        mms.check_default_mms_app()
        mms.go_home()
        mms.delete_all_threads()
        sleep(1)
        '''
        @attention: change to PUBLIC_SLOT2_PHONE_NUMBER
        '''
        send_num = SC.PUBLIC_SLOT2_PHONE_NUMBER
        sms_text = "ui automation test send"
        
        click_textview_by_desc('New message')
        click_textview_by_id("recipients_editor")
        ime.IME_input_number(1, send_num, "c")
        click_textview_by_text(mms.get_value("type_message"))
        entertext_edittext_on_focused(sms_text)
        #ime.IME_input_english(1, sms_text)
        sleep(1)
        
        mms.attach_capture_video(1)
        sleep(1)
        attach_size1=get_view_text_by_id(VIEW_TEXT_VIEW, "mms_size_indicator")
        if search_text("^\d\dK/300K$", searchFlag=TEXT_MATCHES_REGEX):
            log_test_case("test_suit_cmcc_devci_message_case10", "attach first attachment successfully")
            take_screenshot()
        else:
            take_screenshot()
            log_test_case("test_suit_cmcc_devci_message_case10", "Fail to attach first attachment")
            set_cannot_continue()
        sleep(3)
        #click_button_by_id("replace_image_button")
        click_button_by_text(mms.get_value("replace"),searchFlag=TEXT_CONTAINS)
        
        mms.attach_capture_video(2)
        sleep(1)
        func_size = lambda:search_view_by_id("mms_size_indicator")
        if not wait_for_fun(func_size, True, 10):
            log_test_case("test_suit_cmcc_devci_message_case10", "can not found the size of video")
        attach_size2=get_view_text_by_id(VIEW_TEXT_VIEW, "mms_size_indicator")
        if search_text("^\d\d+K/300K$", searchFlag=TEXT_MATCHES_REGEX)and(not attach_size1==attach_size2):
            log_test_case("test_suit_cmcc_devci_message_case10", "Replace attachment successfully")
            take_screenshot()
        else:
            take_screenshot()
            log_test_case("test_suit_cmcc_devci_message_case10", "Fail to replace first attachment")
            set_cannot_continue()
        
        func2 = lambda:search_text('MMS', isScrollable=1, searchFlag=TEXT_CONTAINS) 
        if not wait_for_fun(func2, True, 10):
            set_cannot_continue()
            log_test_framework("cmcc_devci_message_case10:", "send button not found")
        else:
            click_imageview_by_id('send_button_mms')
        
        func3 = lambda:search_text(mms.get_value("sent"), searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func3, True, 120):
            log_test_framework("cmcc_devci_message_case10:", "Sent mms failed")
        else:
            log_test_framework("cmcc_devci_message_case10:", "Sent mms successful")
            case_flag = True
        
        
    
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
