# coding=utf-8
'''
@author: huitingn

'''

import fs_wrapper
import settings.common as SC
from case_utility import *  # ,click_menuitem_by_text
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from test_suit_ui_browser import *

############################################
# author:
#    huitingn@qti.qualcomm.com
# function:
#    Add and navigate several webpages in multiple windows
# precondition:
#    Available network, wifi
#    browser is closed
# steps:
#    step 1: open wifi
#    step 2: open browser
#    step 3: add and input url to goto new webpages
#    step 4: check webtitle
#    step 5: exit
############################################
from test_suit_ui_browser import *


class test_suit_ui_browser_case01(TestCaseBase):
    '''
    test_suit_ui_browser_case01 is a class for adding and navigating several webpages in multiple windows

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_browser_case01'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False
        #
        # STEP 1: open wifi
        #
        init_and_open_wifi()
        
        #
        # STEP 2: open browser
        #
        open_browser()
                    
        #
        # STEP 3: add and input url to goto new webpages
        #
        title_list = ['百度', '新浪', '豌豆荚']
        count = 0
        for title in title_list:
            
            log_test_framework(self.tag, 'begin go %s' % title)
            
            # entertext_edittext_by_id('url', URL_TITLE[title][0])    #this func cannot work
            click_textview_by_id('url')  # this can
            send_key(KEY_DEL)
            entertext_edittext_by_index(0, URL_TITLE[title][0])
            send_key(KEY_ENTER)
            
            func = lambda:((not is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'stop', isScrollable=0)) and is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'favicon', isScrollable=0))
            if not wait_for_fun(func, True, 60):
                click_imageview_by_id('stop',isScrollable=0)
            
            func = lambda:(search_text('Page info', isScrollable=0) or click_imageview_by_id('favicon', isScrollable=0))
            if wait_for_fun(func, True, 10):
                if search_text(title, searchFlag=TEXT_CONTAINS):
                    log_test_case(self.tag, "goto " + title.decode('utf-8') + " sucessfully")
                    count += 1
                click_button_by_text('OK')
            
            send_key(KEY_MENU)
            click_imageview_by_desc('New tab')
            stop_page()
        
        
        if count == len(title_list):
            case_flag = True
        
        
        exit_browser()
        # exit_cur_case(self.tag)
        log_test_case(self.tag, "case_flag = " + str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "add and navigate several webpages in multiple windows is wrong", SEVERITY_HIGH)
            
        # case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
            
       
            
    
