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




class test_suit_ui_browser_case05(TestCaseBase):
    '''
    test_suit_ui_browser_case04 is a class for playing online streaming - video

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_browser_case05'
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
        # STEP 3: input url and play online streaming
        #
        width_rate = float(getDisplayWidth()) / 1080
        height_rate = float(getDisplayHeight()) / 1920
        browser.access_browser(URL_TITLE['优酷'][0], '优酷', 5, is_checked=False)
        take_screenshot()
        # click(POSITION['video'][0],POSITION['video'][1])
        # choose video
        click(540 * width_rate, 1002 * height_rate) 
        sleep(10)
        take_screenshot()
        # click 'play'
        click(541 * width_rate, 765 * height_rate)
        sleep(20)  # wait for loading video
        take_screenshot()
        
        case_flag = True
        
       
        exit_browser()
        # exit_cur_case(self.tag)
        send_key(KEY_HOME)
        log_test_case(self.tag, "case_flag = " + str(case_flag))

        if case_flag:
            log_test_case(self.tag, "need manual check")
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "wifi_flag: " + str(self.tag), SEVERITY_HIGH)
            
        # case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], case_flag))
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
    

