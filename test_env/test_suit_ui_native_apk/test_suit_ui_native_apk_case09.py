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
#    check native FM radio : record audio of FM radio
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



class test_suit_ui_native_apk_case09(TestCaseBase):
    '''
    test_suit_ui_native_apk_case09 is a class for check FM radio : record audio of FM radio

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_native_apk_case09'
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
            # STEP 3: before operation, record the audio number
            #
            #strCMD = "adb shell"
            #p2 = subprocess.Popen(shlex.split(strCMD), shell = False, stdout=subprocess.PIPE)
            strCMD = "adb shell \"ls -l '/sdcard/FMRecording' | grep '.3gpp'\""
            #strCMD = "winver"
            p1 = subprocess.Popen(shlex.split(strCMD), shell = False, stdout=subprocess.PIPE)
            (output,erroutput) = p1.communicate()
            p1.stdout.close()
    
            GPP3 = re.compile( "\.3gpp.*\n" )
            num1 = len(GPP3.findall(output))
            log_test_case(self.tag, "num1 = "+str(num1))
            
            #
            # STEP 4: record audio
            #
            #click_textview_by_id('record_msg_tv')   # start
            click_menuitem_by_text('Start Recording',isScrollable=0)
            # deal with the annoying permission dialog ,set 'always''allow'
            while search_text('Permission',1,0):
                click_checkbox_by_id('permission_remember_choice_checkbox')
                click_button_by_id('button1')   #2:deny 1:allow
            sleep(random.randint(1,9))
            #click_textview_by_id('record_msg_tv')   # end
            click_menuitem_by_text('Stop Recording',isScrollable=0)
                
            
            #
            # STEP 5:after operation, record the audio number
            #
            # have to wait for operation completing, about 3 seconds
            sleep(3)
            # caculate the .3gpp number
            strCMD = "adb shell \"ls -l '/sdcard/FMRecording' | grep '.3gpp'\""
            p1 = subprocess.Popen(shlex.split(strCMD), shell = False, stdout=subprocess.PIPE)
            (output,erroutput) = p1.communicate()
            p1.stdout.close()
                
            num2 = len(GPP3.findall(output))
            log_test_case(self.tag, "num2 = "+str(num2))
            #
            # STEP 4: check if number increase
            #
            if num2 == (num1 + 1):
                case_flag = True
            
        else:
            log_test_case(self.tag, "WRONG! no Headset")
        
        #
        # STEP 6: exit
        #
        exit_cur_case(self.tag)
        

        log_test_case(self.tag, "case_flag = "+str(case_flag))  
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "native FM radio is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
        