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
#    check native clock
# precondition:
#    
# steps:
#    launch native clock
#    set alarm
#    wait for alarm
############################################

import sys, string, os, shutil
from threading  import Thread
import commands
import re, subprocess, shlex
import datetime
from test_suit_ui_native_apk import *

class test_suit_ui_native_apk_case05(TestCaseBase):
    '''
    test_suit_ui_native_apk_case05 is a class for check native clock: can it alarm in expect time.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_native_apk_case05'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''        
        case_flag = False
        
        pre_check()
        
        #
        # read what's the time now
        #
        try:
            (hour, minute, a_p, cur_time) = cur_time_in_mobilephone()
        except:
            set_cannot_continue()
            log_test_case(self.tag, "before SET ALARM: time format maybe wrong" + cur_time)
        
        
        #
        # STEP 1: launch alarm
        #
        if can_continue():
            launcher.launch_from_launcher('clock')
                
                
        #
        # STEP 2: set alarm
        #
        if can_continue():
            # new alarm
            click_view_by_container_id('action_bar_container', 'android.widget.ImageView', 0)
            click_button_by_id('fab')  # alarm_add_alarm
            # set the alarm. e.g.:now(12:56AM)set( 1:00AM)
            #                     now(     PM)set(     PM)
            #                     now(11:56AM)set(12:00PM)
            #                     now(     PM)set(     AM)
            #
            # caculate what time should be set
            #
            # minute decide hour
            if (int(minute) + 1 + 5) > 60:boundary = True
            else:boundary = False
            setMinute = (int(minute) + 1 + 5) / 5
            setHour = int(hour) + boundary
            
            if setHour % 12 == 0 and boundary:
                apDict = {'True':'pm', 'False':'am'}
                setAP = apDict[str(a_p == 'AM')]
            else:setAP = a_p.lower()
                
            setMinute = '%02.0f' % (setMinute * 5 % 60)
            setHour = str(setHour)
            log_test_case(self.tag, "SET hour: " + setHour + " minute: " + setMinute + " ap: " + setAP)
            
            # set alarm
            click(CLOCK_PLATE['HOUR'][setHour][0], CLOCK_PLATE['HOUR'][setHour][1])
            click(CLOCK_PLATE['MINUTE'][setMinute][0], CLOCK_PLATE['MINUTE'][setMinute][1])
            # click(CLOCK_PLATE['A_P'][setAP][0],CLOCK_PLATE['A_P'][setAP][1])
            click_textview_by_text(setAP.upper())
    
            #
            # check if alarm is set correctly
            #
            if get_view_text_by_id(VIEW_TEXT_VIEW, 'hours') == setHour \
            and get_view_text_by_id(VIEW_TEXT_VIEW, 'minutes') == setMinute:
            # and get_view_text_by_id(VIEW_TEXT_VIEW,'ampm_label')==setAP
                click_button_by_text('OK')
            else:
                set_cannot_continue()
                log_test_case(self.tag, "SET ALARM: h,m,ap At least one of them is clicked wrong")
            
        #    
        # STEP 3: wait for alarm
        #
        if can_continue():
            send_key(KEY_HOME)
            sleep(2)
            send_key(KEYCODE_POWER)
            sleep(2)
            func = lambda:is_view_enabled_by_id(VIEW_IMAGE_VIEW, 'alarm', isScrollable=0)
            if wait_for_fun(func, True, timeout=300, sleeptime=10):
                a = get_view_text_by_id(VIEW_TEXT_VIEW, 'digital_clock', isScrollable=0)
                if a:case_flag = True
                startX = int(240.0 / 480 * 100)
                startY = int(590.0 / 855 * 100)
                endX = int(400.0 / 480 * 100)
                endY = int(590.0 / 855 * 100)
                drag_by_param(startX, startY, endX, endY, 10)
            

        
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
        
        
