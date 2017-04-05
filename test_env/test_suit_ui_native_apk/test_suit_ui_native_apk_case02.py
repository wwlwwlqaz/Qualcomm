# -*- coding: utf-8 -*-  

'''
   check native apk: caculator


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
#from qrd_shared.ui_apk_cmcc.Ui_apk_cmcc import *

############################################
#author:
#    huitingn@qti.qualcomm.com
#function:
#    check native caculator
#precondition:
#    
#steps:
#    launch native caculator
#    run monkey
#    
############################################

import sys, string, os, shutil
from threading  import Thread
import commands,shlex
from test_suit_ui_native_apk import *
import re,subprocess,shlex

class test_suit_ui_native_apk_case02(TestCaseBase):
    '''
    test_suit_ui_native_apk_case02 is a class for check native caculator.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_native_apk_case02'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        case_flag = False
        #
        # STEP 1: run monkey
        #
        package = 'com.android.calculator2'
        monkey_num = '500'
        internal = '5000'
        strCMD = "adb shell monkey -p %s %s --throttle %s --monitor-native-crashes --kill-process-after-error"%(package,monkey_num,internal)
        try:
            p1 = subprocess.Popen(shlex.split(strCMD), shell = False, stdout=subprocess.PIPE)
            (result,erroutput) = p1.communicate()
            p1.stdout.close()
        except:
            set_cannot_continue()
            log_test_case(self.tag, "cannot start monkey")
        if can_continue():
            #
            # STEP 2: check
            #
            log_test_case(self.tag,"monkey result: " + result)  
            
            if (re.findall("Events injected: "+monkey_num,result)):
                case_flag = True
            else:take_screenshot()
        
        #
        # STEP 3: exit
        #
        exit_cur_case(self.tag)
        
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "native caculator is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))