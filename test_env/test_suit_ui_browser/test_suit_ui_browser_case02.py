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
#    Download files in browser
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


class test_suit_ui_browser_case02(TestCaseBase):
    '''
    test_suit_ui_browser_case02 is a class for downloading files in browser.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_browser_case02'
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
        # STEP 3: input url to Download files 
        #
        notificationBar.clear_all()
        sleep(5)
        # send_key(KEY_HOME)
        BROWSER_ADDRESS_URL_DOWNLOAD = 'www.wandoujia.com'
        BROWSER_WEB_TITLE_DOWNLOAD = '豌豆荚'
        browser.access_browser(BROWSER_ADDRESS_URL_DOWNLOAD, BROWSER_WEB_TITLE_DOWNLOAD, 5, is_checked=True)
        
        # width = int(getDisplayWidth())
        # height= int(getDisplayHeight())
        download_button_x = 243
        download_button_y = 534
        
        click(download_button_x, download_button_y)  # click "download" button on website
        
        func = lambda:search_text('Download Settings')
        if wait_for_fun(func, True, 30):
            download_filename = get_view_text_by_id(VIEW_EDIT_TEXT, 'download_filename_edit', isScrollable=0)
            click_button_by_id("download_start")
            sleep(3)
            if search_text(browser.get_value('file_exist'), searchFlag=TEXT_CONTAINS) and search_text('Please input a new filename.', searchFlag=TEXT_CONTAINS):
                click_button_by_text("OK")
                send_key(KEY_DEL)
                download_filename = rand_name(only_letter=True).lower()
                ime.IME_input(1, download_filename)
                click_button_by_id("download_start")  # click "Ok " button to start download in downloader
        else:
            set_cannot_continue()
            log_test_case(self.tag, "cannot download in 30s")
        
        
        
        if can_continue():
            # here can add sth. about Download view check.
            notificationBar.drag_down()
            func = lambda:search_text(download_filename) and search_text('Download complete.')
            if wait_for_fun(func, True, 60):
                case_flag = True
                # notificationBar.clear_all()
            goback()
        
        goback()
        exit_browser()
        
        # exit_cur_case(self.tag)
        send_key(KEY_HOME)
        
        log_test_case(self.tag, "case_flag = " + str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "download files in browser is wrong", SEVERITY_HIGH)
            
        # case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
