'''
   download weixin,baidumap,weibo,renren,douban applications from google play store.


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

class test_suit_playstore_case1(TestCaseBase):
    '''
    test_suit_playstore_case1 is a class for playstore case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    success = 0
    '''@var success: count the number of download successfully.'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        sleep(2)
        register_update_watcher("com.android.vending", VIEW_BUTTON, ID_TYPE_ID, "positive_button", ACTION_CLICK)
        if search_view_by_id("continue_button"):
            click_button_by_id("continue_button")
        if search_view_by_id("positive_button"):
            click_button_by_id("positive_button")
        sleep(10)
        if playstore.download("weixin", "Tencent Technology"):
            success += 1
        if playstore.download("baidu map", "Baidu Inc"):
            success += 1
        if playstore.download("weibo", "Sina.com"):
            success += 1
        if playstore.download("renren", "Renren Inc"):
            success += 1
        if playstore.download("douban", playstore.get_value("douban_fm")):
            success += 1

        if success < 5:
            set_cannot_continue()
        unregister_update_watcher("com.android.vending")
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
