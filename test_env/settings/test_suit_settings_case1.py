'''
   This Class provide some presettings operation.

   1.Close lockscreen.
   2.Set default IME as google pinyin.
   3.Set default SMS as always ask.


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
import time
from qrd_shared.case import *
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
import os

class test_suit_settings_case1(TestCaseBase):
    '''
    test_suit_settings_case1 is a class for presettings case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.according to params of config.xml,make the following settings:
       1.Close lockscreen.
       2.Set default IME as google pinyin.
       3.Set default SMS as always ask.
        '''
        #if SC.PUBLIC_CLOSE_LOCKSCREEN: # removed by Liu Jiehui's advice
        #    settings.close_lockscreen()
#         wakeUpDevice()
        send_key(KEYCODE_POWER)
        sleep(1)
        drag_by_param(50, 90, 50, 0, 10)
        sleep(1)
        os.system("adb shell input keyevent 26")
        settings.check_after_resetphone()
        os.system("adb shell input keyevent 26")
        start_activity('com.android.settings','.Settings')
        if SC.PUBLIC_CLOSE_LOCKSCREEN: # removed by Liu Jiehui's advice
            settings.close_lockscreen()
        

        time.sleep(1)

        #set default ime -- google pinyin
        #if SC.PUBLIC_GOOGLE_PINYIN:
        #   ime.set_default_input_method(ime.get_value("google_pinyin"))
        #   start_activity('com.android.browser','.BrowserActivity')
        #   browser.pre_check()
        #   ime.close_auto_capitalization_google_pinyin()
        #   ime.set_google_pinyin_default_input_en()

        if SC.PUBLIC_SET_DEFAULT_SMS_ALWAYS_ASK:
            settings.set_default_sms(0)

        if SC.PRIVATE_TRACKING_TRACKING_PATH:
            settings.access_to_my_location(True)

        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
