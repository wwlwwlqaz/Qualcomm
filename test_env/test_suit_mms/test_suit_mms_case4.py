'''
   send a mms from slot2 to slot1.


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

class test_suit_mms_case4(TestCaseBase):
    '''
    test_suit_mms_case4 is a class for mms case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_mms_case4"
    '''@var TAG: tag of test_suit_mms_case4'''
    wait_time = 2 * 60
    '''@var wait_time: wait time for receive message'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        send_key(KEY_MENU)
        delete_all_threads = mms.get_value("delete_all_threads")
        if search_text(delete_all_threads):
            click_textview_by_text(delete_all_threads)
            click_button_by_index(1)
            wait_for_fun(lambda:search_text(mms.get_value("no_conversations")), True, 5)
        else:
            goback()
        num = SC.PUBLIC_SLOT1_PHONE_NUMBER
        search_num = format_phone_number(SC.PUBLIC_SLOT2_PHONE_NUMBER)
        mms_text = "g to c"
        click_imageview_by_id('action_compose_new')
        #entertext_edittext_by_index(0, num)
        click_textview_by_id("recipients_editor")
        ime.IME_input_number(1, num, "c")
        click_textview_by_desc(mms.get_value("attach"))
        click_textview_by_text(mms.get_value("capture_picture"))
        camera.get_picture_by_camera()
        #entertext_edittext_by_index(1, mms_text + str(i))
        #click_textview_by_id("embedded_text_editor")
        click_textview_by_text(mms.get_value("type_message"))
        ime.IME_input_english(1, mms_text)
        #click_textview_by_text("MMS1")
        click_textview_by_text(mms.get_value('mms'))
        click_button_by_index(1)
        func = lambda:search_text(mms.get_value("sent"), searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func, True, self.wait_time):
            mms.click_home_icon()
            set_cannot_continue()
            log_test_case(self.TAG, "Sent MMS on slot2 failed.")
        mms.click_home_icon()
        func1 = lambda:search_text(search_num, searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func1, True, self.wait_time):
            set_cannot_continue()
        click_textview_by_text(search_num, searchFlag=TEXT_CONTAINS)
        click_button_by_id("btn_download_msg")
        click_button_by_index(1)
        func2 = lambda:search_text(mms.get_value("received"), searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func2, True, self.wait_time):
            mms.click_home_icon()
            set_cannot_continue()
            log_test_case(self.TAG, "Recived MMS on slot2 failed.")
        click_textview_by_text(mms.get_value("received"))
        func3 = lambda:search_text(mms.get_value("message_size"), searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func3, True, 10):
            mms.click_home_icon()
            set_cannot_continue()
            log_test_case(self.TAG, "Recived MMS on slot2 failed.")
        mms.click_home_icon()
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

def format_phone_number(num):
    '''
    format phone number,for example:format "12345678901" to "123 4567 8901"

    @type num: string
    @param num: phone number that need format
    @return: a phone number which have formated
    '''
    s = insert(num, ' ', 3)
    return insert(s, ' ', 8)

def insert(original, new, pos):
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
