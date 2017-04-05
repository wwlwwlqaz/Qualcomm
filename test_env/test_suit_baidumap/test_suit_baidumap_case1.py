#coding=utf-8
'''
    This case provide some operation for baidumap.

    1.Skip guidepage.
    2.Search Zhangjiang in baidumap.


   @author: U{c_chuanc<c_chuanc@qti.qualcomm.com>}
   @version: version 1.0.0
   @requires:python 2.7+
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

count = 2
success = 0

class test_suit_baidumap_case1(TestCaseBase):
    '''
    test_suit_settings_case1 is a class for baidumap case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    TAG = "test_suit_baidumap_case1"
    '''@var TAG: tag of test_suit_baidumap_case1'''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        if search_text(u'接受'):
            click_button_by_text(u'接受')
            self.operate_guidepage()

        func = lambda:get_activity_name() == "com.baidu.BaiduMap.map.mainmap.MainMapActivity"
        if not wait_for_fun(func, True, 15):
            set_cannot_continue()
            return

        register_update_watcher("com.android.BaiduMap", VIEW_BUTTON, ID_TYPE_ID, "button2", ACTION_CLICK)
        # wating for the activity display
        sleep(5)
        func1 = lambda:search_text(u"再次点击进入罗盘模式")
        if wait_for_fun(func1, True, 10):
            goback()

        func2 = lambda:search_view_by_id("searchBox")
        if wait_for_fun(func2, True, 10):
            click_button_by_id("searchBox")
            #entertext_edittext_by_id("EditText_poi_search", "zhangjiang")
            click_textview_by_id("EditText_poi_search")
            ime.IME_input_english(1, "zhangjiang")
            click_textview_by_text(u"上海市浦东新区")
            sleep(20)
        else:
            log_test_case(self.TAG, "Can't find searchBox.")
            set_cannot_continue()

        unregister_update_watcher("com.android.BaiduMap")
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))

    def operate_guidepage(self):
        '''
        operation guidepage.
        '''
        if get_activity_name() == 'com.baidu.BaiduMap.common.guide.GuidePage':
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            drag_by_param(90,50,10,50,10)
            if search_view_by_id('start_map'):
                click_imageview_by_id('start_map')