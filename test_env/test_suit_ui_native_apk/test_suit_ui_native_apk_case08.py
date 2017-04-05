# coding: utf-8
'''
   check native apk: alarm


   @author: U{huitingn<huitingn@qti.qualcomm.com>}
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
from case_utility import *
from logging_wrapper import log_test_case, take_screenshot
from test_case_base import TestCaseBase
from qrd_shared.case import *

############################################
#author:
#    huitingn@qti.qualcomm.com
#function:
#    check native FM radio : add favorite channel
#precondition:
#    Headset
#steps:
#    launch native FM radio
#    check some setting
#    add new favorite channel
#    confirm if right
#    exit
############################################

import sys, string, os, shutil
from threading  import Thread
import commands
import re,subprocess,shlex
import datetime
import random
from test_suit_ui_native_apk import *



class test_suit_ui_native_apk_case08(TestCaseBase):
    '''
    test_suit_ui_native_apk_case08 is a class for check FM radio : add favorite channel

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_native_apk_case08'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False
        #
        #
        # STEP 1: launch FM radio
        #
        package = 'com.caf.fmradio'
        activity = package + '.FMRadio'
        start_activity(package,activity)
        
        #
        # STEP 2: check
        #
        # check, no Headset no begin
        func = lambda:search_text('Please plug in a Headset to use FM Radio',isScrollable=0)
        if wait_for_fun(func,False,5):
            #
            # check, need place to add new favorite channel
            #
            #a = get_view_text_by_id(VIEW_BUTTON,'presets_button_4')
            while get_view_text_by_id(VIEW_BUTTON,'presets_button_4') != '+':
                click_button_by_id('presets_button_4',clickType=LONG_CLICK)
                click_textview_by_text('Delete')
            
            #
            # STEP 3: add new channel
            #
            # read the channel frequency to be add
            frequency = get_view_text_by_id(VIEW_TEXT_VIEW,'prog_frequency_tv',isScrollable=0)
            frequency = re.findall( '(\d+\.\d)(?=MHz)' , frequency)[0]
            # add
            click_button_by_text('+',clickType=LONG_CLICK,isScrollable=0)
            
            #
            # STEP 4: confirm
            #
            # confirm the frequency has been add correctly
            func = lambda:search_text(str(frequency),searchFlag=TEXT_MATCHES,isScrollable=0)
            if wait_for_fun(func,True,2):
                case_flag = True
            
        else:
            log_test_case(self.tag, "WRONG! no Headset")
        
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
        

        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "native alarm is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
        