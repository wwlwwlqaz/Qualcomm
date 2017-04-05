# -*- coding: utf-8 -*-  
'''
@author: U{huitingn<huitingn@qti.qualcomm.com>}

'''

import settings.common as SC
from case_utility import *
from logging_wrapper import log_test_case,save_fail_log,print_report_line
from test_case_base import TestCaseBase
from qrd_shared.case import *
from test_suit_ui_customer_issue import *
from test.test_multiprocessing import get_value


class test_suit_ui_customer_issue_case02(TestCaseBase):
    '''
    test_suit_ui_customer_issue_case02 is a class for deleting single SMS

    @see: L{TestCaseBase <TestCaseBase>}
    '''
    tag = 'ui_customer_issue_case02'
    def test_case_main(self, case_results):
        
        '''
        main entry.

        @type case_results: tuple
        @param case_results: record some case result information
        '''
        for i in range(10):
            case_flag = False    
            
            #launcher.launch_from_launcher('download')
            command = r'adb install C:/NHTworkspace/task1_100App/new/test.apk'
            os.system('start '+command)
            print 'install'
            send_key(KEY_HOME)
            send_key(KEYCODE_POWER) # now the LCD is sleep
            
            # wait for sms
            localPhoneNumber = '13301777998'
            command = r'adb shell am start -a android.intent.action.SENDTO -d sms:%s --es sms_body Hello'%localPhoneNumber
            os.system(command)
            print 'write sending msg'
            os.system('adb shell input keyevent 22')
            os.system('adb shell input keyevent 66')
            
            sleep(90)
            
            
            send_key(KEYCODE_POWER)# wake up the LCD
            try:click_textview_by_desc('Apps',isScrollable=0)
            except:case_flag=False
            else:case_flag=True
        

        exit_cur_case(self.tag)
        
        log_test_case(self.tag, "case_flag = "+str(case_flag))
        if case_flag:
            qsst_log_case_status(STATUS_SUCCESS, "" , SEVERITY_HIGH)
        else:
            qsst_log_case_status(STATUS_FAILED, "take photo is failed", SEVERITY_HIGH)
        case_results.append((self.case_config_map[fs_wrapper.CASE_NAME_ATTR], can_continue()))
            
            