# -*- coding: utf-8 -*-  

'''
   App install


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
#    install App
#precondition:
#    There is an apk in directory
#steps:
#    File exploer -> FOLDER -> Pnone storage -> Download
#    QQLite or other apk
#    Next Install -> App installed
############################################

import sys, string, os, shutil
from threading  import Thread
import commands
from test_suit_ui_apk_cmcc import *
import copy

class test_suit_ui_apk_cmcc_case13(TestCaseBase):
    '''
    test_suit_ui_apk_cmcc_case13 is a class for App install case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_apk_cmcc_case13'
    category = 'MUSIC'
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        #deal_with_install_block()
        (apk_list,apk_library_dir,apk_source_dir,sep) = get_files_in_dir(self.category)

        PATTERN1 = 'PackageManager'
        PATTERN2 = 'Running dexopt on'
        pmPattern = re.compile( "%s.+%s.+\n" %(PATTERN1,PATTERN2) )
        
        case_flag = True
        count = 0
        count_fail = 0
        fail_apk_list = []
          
        for apk in apk_list:
            os.popen('adb logcat -c')
            count += 1
            log_test_framework(self.tag, "now the apk is No." + str(count))
            if (count%5 == 0):    sleep(30)
            
            #
            # STEP 1: install
            #
            # WindowsError: [Error 183] Cannot create a file when that file already exists
            try:   os.remove(apk_source_dir+'new.apk')       #pull one apk in newDIR and rename it as new.apk, push it to device and install new.apk
            except WindowsError:     pass
            
            shutil.copy(apk_library_dir+apk,apk_source_dir)
            log_test_framework(self.tag, "now the apk is " + apk)
            os.rename(apk_source_dir+apk , apk_source_dir+'new.apk')
            os.system('adb push ' +'"'+ apk_source_dir + 'new.apk' +'"'+ " /sdcard/Download/")

            sleep(5)

            
            goto_dir('/Phone storage/Download',go_from_home_screen=True)
            #sleep(3)
            
            try:        # cannot find some apks, skip them
                click_textview_by_text('new.apk')
            except AssertFailedException:
                log_test_case(self.tag, 'cannot find '+apk)
                case_flag = False
                count_fail += 1
                fail_apk_list.append(apk)
                continue
                
            sleep(2)
            while search_text('Next',1,0):  # 0:disable scroll
                click_button_by_text('Next')
            click_button_by_text('Install')

            sleep(3)
            # add for Android L
            if is_view_enabled_by_text(VIEW_TEXT_VIEW,'Preferred install location',isScrollable=0):
                click_textview_by_text('Let the system decide')
            
            while not search_text('Done',1,0):pass
            click_button_by_id('done_button')
            
            log = get_logcat_string(raw_cmd='-v time')
            #while not search_text('Folder'):pass    # wait for back
            

            
            #
            # STEP 2: run monkey test
            #
            #open log
            log_test_framework('look',"look at me!!!\n"+log+"\nlook at me!!!\n")
            line = pmPattern.findall(log)[-1]
            log_test_framework(self.tag, "before monkey: "+line)
            package = re.findall("\w+(?:\.\w+){1,6}",line)[0]
            log_test_framework(self.tag, "before monkey: "+package)
            
            #run monkey
            send_key(KEY_HOME)
            monkey_num = '1000'
            result = os.popen("adb shell monkey -p " + package + " "+monkey_num+" --throttle 500 --monitor-native-crashes --kill-process-after-error")
            result = copy.copy(result.read())
            log_test_framework(self.tag, "after monkey:\n"+result)
        
            if not (re.findall("Events injected: "+monkey_num,result)):
                case_flag = False
                take_screenshot()
                log_test_case(self.tag,"%s failed in monkey"%apk)
                count_fail += 1
                fail_apk_list.append(apk)

            
            #
            # STEP 3: exit
            #
            sleep(2)
            send_key(KEY_HOME)
            sleep(2)
            
            #
            # STEP 4: uninstall
            #
            os.system("adb uninstall " + package)
            sleep(5)
            os.system("adb shell rm -r /sdcard/Download/" + 'new.apk')
            sleep(5) 
            

            goback()
            send_key(KEY_HOME)
            goback()
        
        
        
        log_test_case(self.tag,"%s apks to check; %s apks have checked"%(str(len(apk_list)),count))     
        exit_cur_case(self.tag) 
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "some apps are failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
        