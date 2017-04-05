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
# author:
#    huitingn@qti.qualcomm.com
# function:
#    check native clock: timer
# precondition:
#    
# steps:
#    launch native clock
#    set timer
#    wait for timer
############################################

import sys, string, os, shutil
from threading  import Thread
import commands
import re, subprocess, shlex
import datetime
from test_suit_ui_native_apk import *
import random


class test_suit_ui_native_apk_case06(TestCaseBase):
    '''
    test_suit_ui_native_apk_case06 is a class for check native clock: can it count down in expect time.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_native_apk_case06'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False
        #
        # STEP 1: launch alarm
        #
        package = 'com.android.deskclock'
        activity = package + '.DeskClock'
        start_activity(package, activity)
        '''
        func = lambda:activity == get_activity_name()
        if not wait_for_fun(func,True,3):
            set_cannot_continue()
            log_test_case(self.tag, "before SET TIMER: cannot start activity" + activity)
        '''
        
        #
        # STEP 2: set count down timer
        #
        if can_continue():
            # click_view_by_container_id('action_bar_container', 'android.widget.ImageView', 2)
            click_imageview_by_desc('Timer')
            # if search_view_by_id('timer_time_text'):    # exist 1 Timer at least
                # click_imageview_by_desc('Add Timer',isScrollable=0)   # click 'add' button to add a new timer 
            MAX_SET_TIME = 30
            set_time = random.randint(1, MAX_SET_TIME)
            # in case the time is too long, so make it no more than 30sec
            # if set_time > 30:set_time %= 30
            
            set_time = '%05.0f' % set_time
            (hour_ones, minute_tens, minute_ones, second_tens, second_ones) = tuple(set_time)
            for i in range(5):
                click_imageview_by_desc('Delete')
            
            
            # hour
            # click_view_by_container_id(TIMER_BUTTON[hour_ones][0],TIMER_BUTTON[hour_ones][1],TIMER_BUTTON[hour_ones][2])
            click_button_by_text(hour_ones)
            
            
            # minute
            # click_view_by_container_id(TIMER_BUTTON[minute_tens][0],TIMER_BUTTON[minute_tens][1],TIMER_BUTTON[minute_tens][2])
            # click_view_by_container_id(TIMER_BUTTON[minute_ones][0],TIMER_BUTTON[minute_ones][1],TIMER_BUTTON[minute_ones][2])
            click_button_by_text(minute_tens)
            click_button_by_text(minute_ones)
            # second
            # click_view_by_container_id(TIMER_BUTTON[second_tens][0],TIMER_BUTTON[second_tens][1],TIMER_BUTTON[second_tens][2])
            # click_view_by_container_id(TIMER_BUTTON[second_ones][0],TIMER_BUTTON[second_ones][1],TIMER_BUTTON[second_ones][2])
            click_button_by_text(second_tens)
            click_button_by_text(second_ones)
            
            sleep(2)
            click_imageview_by_desc('Start', isScrollable=0, waitForView=1)
            
            #
            # STEP 3:  wait for Timer
            #
            # activity = package + '.timer.TimerAlertFullScreen'
            # func = lambda:activity == get_activity_name()
            func = lambda:is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'timer_time') and not is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'right_button')
            if wait_for_fun(func, True, MAX_SET_TIME):  # time_out is 5min+5sec
                #    
                # STEP 4: close timer
                #
                click_imageview_by_id('fab', isScrollable=0)
                # send_key(KEY_HOME)
                case_flag = True

        
        #
        # STEP 5: exit
        #
        exit_cur_case(self.tag)
        

        log_test_case(self.tag, "case_flag = " + str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "native alarm is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
        
