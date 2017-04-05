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

class test_suit_ui_apk_cmcc_case100(TestCaseBase):
    '''
    test_suit_nhtApp_case1 is a class for App install case.

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    def test_case_main(self, case_results):
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        osInfo = get_platform_info()
        #currLocation = os.getcwd()
        if(osInfo == 'Linux-Phone' or osInfo == 'Linux-PC'):
            DIR = 'C:/Dropbox/QSST/200apk/'
        elif(osInfo == 'Windows'):
            #DIR = 'C:\\Dropbox\\QSST\\200apk\\'
            DIR = 'C:\\New folder\\'
        files = os.listdir( DIR )
        #log_test_framework("before for : ", "get all files")
        TYPE = 'apk'
        rr = re.compile( "\.%s$" %TYPE , re.I )
        apk_list = []
        for f in files:
            if rr.search(f):
                apk_list.append("%s"%f) 
        #log_test_framework("before for : ", "get all apks")
        
        
        newDIR = os.path.join(DIR,'new')
        if not os.path.isdir(newDIR):
            os.makedirs(newDIR)
        if(osInfo == 'Linux-Phone' or osInfo == 'Linux-PC'):
            newDIR += '/'
        elif(osInfo == 'Windows'):
            newDIR += '\\'


        case_flag = True  
        for apk in apk_list:
            
            #
            # STEP 1: install
            #
            try:
                os.remove(newDIR+'new.apk')       #pull one apk in newDIR and rename it as new.apk, push it to device and install new.apk
            except WindowsError:
                pass
            os.rename(DIR+apk , newDIR+'new.apk')
            log_test_framework("in for : ", "now the apk is " + apk)
            os.system('adb push ' +'"'+ newDIR + 'new.apk' +'"'+ " /sdcard/Download/")
            #os.system("am start " + package_name + "/" + activity_name)
            #log_test_framework("in for : ", "push one apk")
            sleep(5)
            os.rename(newDIR+'new.apk' , DIR+apk)
            #os.system("adb logcat -c")
            #clear_adb_log()
            #log_test_framework("in for : ", "clear log")
            #log = apk[0:-4] + ".log"
            #os.system("adb logcat > " + DIR + log) # to record the apk package
            #pid = start_capture_adblog("adb logcat > " + '"' + DIR + log + '"')
            #log_test_framework("where : ", "adb logcat > " + DIR + log)
            #log_test_framework("in for : ", "record "+log)
            # os.system("adb install " + )
            #Define the function to get logcat info into queue.
            

            '''
            try:
                pid = os.fork()
                if pid == 0: #子进程 
                    print "this is child process."        #在子进程中source自减1
                    sleep(3)
                else: #父进程
                    print "this is parent process."
            except OSError, e:
                pass
            '''
            
                   
            #launcher.launch_from_launcher('apps')

            goto_dir('/Phone storage/Download')


            sleep(3)
            try:        # cannot find some apks, skip them
                click_textview_by_text('new.apk')
            except AssertFailedException:
                log_test_framework("nht : ", 'cannot find '+apk)
                continue
                
            sleep(2)
            while search_text('Next',1,0):  # 0:disable scroll
                click_button_by_text('Next')
            click_button_by_text('Install')

            sleep(3)
            while not search_text('Done',1,0):pass
            click_button_by_id('done_button')
            
            log = get_logcat_string(raw_cmd='-v time')
            #while not search_text('Folder'):pass    # wait for back
            
            '''        
            #for GODesk
            send_key(KEY_HOME)
            sleep(3)            
            try:
                if search_text('Select a home app'):
                    #click_textview_by_text('Launcher')
                    click_button_by_id('button_always')
            except ValueError:pass
            '''
            
            #
            # STEP 2: run monkey test
            #
            #open log
            #log = get_logcat_string(raw_cmd='-v time')
            #log_test_framework("nht : ", "%s"%(type(log)))
            PATTERN1 = 'PackageManager'
            PATTERN2 = 'Running dexopt on'
            rr = re.compile( "%s.+%s.+\n" %(PATTERN1,PATTERN2) )
            line = rr.findall(log)[0]
            log_test_framework("before monkey : ", line)
            package = re.findall("\w+(?:\.\w+){1,5}",line)[0]
            log_test_framework("before monkey : ", package)
            
            #run monkey
            monkey_num = 500
            result = os.popen("adb shell monkey -p " + package + " "+monkey_num+" --throttle 50 --monitor-native-crashes --kill-process-after-error")
            log_test_framework("after monkey : ", result.read())
        
            if not (re.findall("Events injected: "+monkey_num,result.read())):
                case_flag = False

            
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
                
            
          
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "some apps are failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
        
        
        
        


import getopt


if __name__ == '__main__':
    workDir = r'.'
    outFile = 'out.txt'
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:d", ["help", "output="])
    except getopt.GetoptError:
        pass# print help information and exit:
    
    for o,a in opts:
        if o in ('-h','--help'):
            pass# print help information and exit:
        if o in ('-o','--output'):
            outFile = a
        if o in ('-d'):
            workDir = a
        else:
            print 'unknown command option'
            pass# print help information and exit:
    
    
            
    outHandler = open(workDir+os.path.sep+outFile, 'w')
    sys.stdout = outHandler
    
    
    for i in os.walk(workDir):
        dirpath, dirnames, filenames = i
        print '%s\n%s\n%s\n\n\n'%(dirpath,dirnames,filenames)
    outHandler.close()
    sys.stdout = sys.__stdout__
    sys.stdout = _console
    
    print 'sys.__stdout__ is '+str(sys.__stdout__)
    print '_console is '+str(_console)
