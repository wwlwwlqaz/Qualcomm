'''
   send a sms from slot1 to slot2.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires: python 2.7+
   @license:

   @see: L{TestCaseBase <TestCaseBase>}
   @note:
   @attention:
   @bug:
   @warning:



'''
import fs_wrapper
import settings.common as SC
from qrd_shared.case import *
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase

class test_suit_test_ime_case1(TestCaseBase):
    '''
    test_suit_test_ime_case1 is a class for test_ime case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_test_ime_case1"
    '''@var TAG: tag of test_suit_test_ime_case1'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        self.test_ime(3, "qwertyuiopasdfghjklZXCVBNM .")
        self.test_ime(2, "1234567890")

    def test_ime(self, type, str):
        click_imageview_by_id('action_compose_new')
        click_textview_by_text(mms.get_value("type_message"))
        if type == 1:
            ime.IME_input(1, str, lanauage='c', input_type='p')
        elif type == 2:
            ime.IME_input_number(1, str, keyboard_type='c', input_type='p')
        elif type == 3:
            ime.IME_input_english(1, str, input_type='p')
        goback()
        result = interact_with_user_by_multi_btn("Title", 'The input should be "' + str + '", Is this input right?', ["No", "Yes"])
        mms.click_home_icon()
        click_button_by_index(1)
        return True if result==1 else False