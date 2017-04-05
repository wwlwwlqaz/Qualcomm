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
#    check native sound recorder : record sound
#precondition:
#    
#steps:
#    launch native sound recorder
#    some setting
#    begin record a random time
#    stop and check
############################################

import sys, string, os, shutil
from threading  import Thread
import commands
import re,subprocess,shlex
import datetime
import random
from test_suit_ui_native_apk import *



class test_suit_ui_native_apk_case07(TestCaseBase):
    '''
    test_suit_ui_native_apk_case07 is a class for check sound recorder : recode sound

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_native_apk_case07'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False
        
        FILE_LOCATION_LIST = ('Phone storage',)
        FILE_TYPE_LIST = ('AMR','3GPP','WAV')
        flag = True
        for location in FILE_LOCATION_LIST:
            for filetype in FILE_TYPE_LIST:
                #
                # STEP 1: launch sound recorder
                #
                package = 'com.android.soundrecorder'
                activity = package + '.SoundRecorder'
                #start_activity(package,activity)
                launcher.launch_from_launcher('sound_recorder')
                
                #
                # STEP 2: setting and check before record sound
                #
                # choose the record file type
                click_imageview_by_desc('More options')
                click_textview_by_text('File type')
                click_textview_by_text(filetype)
                # choose the record file location
                click_imageview_by_desc('More options')
                click_textview_by_text('Storage location')
                click_textview_by_text(location)

                #
                # STEP 3: record sound
                #
                click_button_by_id('recordButton')
                func = lambda: search_text('Insert an SD card')
                if wait_for_fun(func,True,2):
                    set_cannot_continue()
                    log_test_case(self.tag, "WRONG! no sdcard in test filetype:"+ filetype + " location:" + location)
                else:
                    sleep(random.randint(1,9))
                    click_button_by_id('stopButton')
                    click_button_by_text('Done')
                    
                    #
                    # STEP 4: check whether sound is record correctly
                    #
                    func = lambda:search_text(filetype.lower()+"\nFile has been saved",searchFlag=TEXT_CONTAINS)
                    if not wait_for_fun(func, True, 5):    #time_out is 5sec
                        flag = False
                        #
                    if search_text('OK'):
                        click_button_by_text('OK')
        
        if flag:
            case_flag = True
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
        
        