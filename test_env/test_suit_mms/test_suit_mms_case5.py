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
from logging_wrapper import *
from test_case_base import TestCaseBase

class test_suit_mms_case5(TestCaseBase):
    '''
    test_suit_mms_case5 is a class for mms case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_mms_case5"
    '''@var TAG: tag of test_suit_mms_case5'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        send_key(KEY_MENU)
        mms.delete_all_threads()

        num = SC.PUBLIC_SLOT1_PHONE_NUMBER
        search_num = format_phone_number(SC.PUBLIC_SLOT1_PHONE_NUMBER)
        mms_text = "test message."

        if not mms.send_sms(3, search_num, mms_text):
            qsst_log_case_status(STATUS_FAILED, "send sms case failed.", SEVERITY_HIGH)
        func1 = lambda:search_text(search_num, searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func1, True, 30):
            qsst_log_case_status(STATUS_FAILED, "", SEVERITY_HIGH)

        func1 = lambda:search_text(search_num, searchFlag=TEXT_CONTAINS)
        if not wait_for_fun(func1, True, 30):
            qsst_log_case_status(STATUS_FAILED, "Received sms case failed.", SEVERITY_HIGH)
        click_textview_by_text(search_num, searchFlag=TEXT_CONTAINS)
        if not search_text(mms.get_value("received"), searchFlag=TEXT_CONTAINS):
            mms.click_home_icon()
            qsst_log_case_status(STATUS_FAILED, "Received sms case failed.", SEVERITY_HIGH)
        mms.click_home_icon()
        qsst_log_case_status(STATUS_SUCCESS, "case success.", SEVERITY_HIGH)

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
