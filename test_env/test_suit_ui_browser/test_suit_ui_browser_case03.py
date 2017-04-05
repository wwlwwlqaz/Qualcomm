# coding=utf-8
'''
@author: huitingn

'''

import fs_wrapper
import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case, save_fail_log, print_report_line
from test_case_base import TestCaseBase
import test_suit_ui_browser
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
from test.test_multiprocessing import get_value




class test_suit_ui_browser_case03(TestCaseBase):
    '''
    test_suit_ui_browser_case03 is a class for back or forward through webpages

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_browser_case03'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False
        
        #
        # STEP 1: open wifi and add email account for sharing by email
        #
        init_and_open_wifi()
        
        #
        # STEP 2: open browser
        #
        open_browser()
            
        #
        # STEP 3: input url and record webpage info
        #
        title_list = ['百度', '新浪', '豌豆荚']
        record_list = []
        browser.clear_cache()
        for title in title_list:
            if can_continue():
                browser.access_browser(URL_TITLE[title][0], title, 5, is_checked=False)
                func = lambda:is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'favicon')
                if wait_for_fun(func, True, 30):
                    click_imageview_by_id('favicon')
                elif is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'stop', isScrollable=0):
                    click_imageview_by_id('stop')
                    click_imageview_by_id('favicon')
                else:
                    log_test_case(self.tag, "cannot get info in page " + URL_TITLE[title][0] + " in 30s")
                    set_cannot_continue()
            if can_continue():
                t = get_view_text_by_index(VIEW_TEXT_VIEW, 1)
                log_test_case(self.tag, "t= " + t)
                record_list.append(t)
                click_button_by_text('OK', isScrollable=0)
        
        #
        # STEP 4: backward and forward between pages
        #
        if can_continue():
            reverse_record_list = record_list[:]
            reverse_record_list.reverse()
            
            count = check_page_forward_or_backward(reverse_record_list, browser.get_value('back'))\
                + check_page_forward_or_backward(record_list, browser.get_value('forward'))
            
            if count == 2:
                case_flag = True
        
       
        exit_browser()
        # exit_cur_case(self.tag)
        send_key(KEY_HOME)
        
        log_test_case(self.tag, "case_flag = " + str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "webpages back or forward is wrong", SEVERITY_HIGH)
            
        # case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
    



'''
def stop_page():
    send_key(KEY_MENU)
    if search_text(browser.get_value('stop')):
        click_textview_by_text(browser.get_value('stop'))
        if search_text(browser.get_value('stop')):
            goback()
    else: goback()
'''
        
def check_page_forward_or_backward(record_list, direction, wait_time=60):
    tag = 'check_page_forward_or_backward'
    flag = False
    count = 0
    for record in record_list:
        click_imageview_by_id('favicon')
        if record != get_view_text_by_index(VIEW_TEXT_VIEW, 1):
        # if not search_text(record,searchFlag=TEXT_CONTAINS):
            log_test_framework(tag, "page " + direction + " is wrong")
        else: count += 1
        click_button_by_text('OK')
        
        if record_list.index(record) == (len(record_list) - 1):
            break
        else:
            # click_menuitem_by_text(direction)
            if direction == browser.get_value('forward'):
                send_key(KEY_MENU)
                click_imageview_by_desc('Forward', isScrollable=0)
            elif direction == browser.get_value('back'):
                goback()
            else:
                set_cannot_continue()
                log_test_framework(tag, "direction '%s' is wrong!" % (direction))
                return False
            
            func = lambda:search_view_by_id('favicon')
            if not wait_for_fun(func, True, wait_time):
                try:click_imageview_by_id('stop',isScrollable=0)
                except:log_test_framework(tag, "page " + direction + " cannot open in %ss" % wait_time)
    
    if count == len(record_list):flag = True
    
    return flag
